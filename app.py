from flask import Flask, jsonify, request, render_template
import requests
import json
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
from io import BytesIO
import base64


app_start = Flask(__name__)

def calculate_variance(data):
    """
    Calculate the variance of a list of integers.

    Parameters:
    - data (list): List of integers.

    Returns:
    - variance (float): Variance of the input data.
    """
    if len(data) < 2:
        raise ValueError("Variance requires at least two data points.")

    # Calculate the mean
    mean = sum(data) / len(data)

    # Calculate the sum of squared differences from the mean
    squared_diff = sum((x - mean) ** 2 for x in data)

    # Calculate the variance
    variance = squared_diff / (len(data) - 1)

    return variance

def calculate_median(data):
    """
    Calculate the median of a list of integers.

    Parameters:
    - data (list): List of integers.

    Returns:
    - median (float or int): Median of the input data.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        # If the number of elements is even, average the middle two
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # If the number of elements is odd, take the middle element
        median = sorted_data[n // 2]

    return median

def calculate_mean(data):
    """
    Calculate the mean of a list of integers.

    Parameters:
    - data (list): List of integers.

    Returns:
    - mean (float): Mean of the input data.
    """
    if len(data) == 0:
        raise ValueError("Cannot calculate mean of an empty list.")

    # Calculate the mean
    mean = sum(data) / len(data)

    return mean

def create_histogram(data):
    growth_set = set(data)
    graph_bin = len(growth_set) + 1
    plt.style.use('fivethirtyeight')
    plt.hist(growth_set, bins = graph_bin, edgecolor='black')
    plt.title('Growth Data')
    plt.xlabel('Growth values')
    plt.xlabel('Count Growth values')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Encode the image as base64
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')

    # Create HTML code to embed the image
    html_code = f'<img src="data:image/png;base64,{encoded_img}" alt="Matplotlib Histogram">'

    return html_code
    

@app_start.route('/')
def index():
    return "Hello Berry fan!"

@app_start.route('/allBerryStats')
def all_berry_stats():
    result = requests.get('https://pokeapi.co/api/v2/berry')
    request_data =  json.loads(result.text)
    berries_data = request_data['results']
    berries_url = [elem['url'] for elem in berries_data]
    berries_name_growth = {}
    for elem in berries_url:
        request_berry_data = requests.get(elem)
        berry_data = json.loads(request_berry_data.text)
        berries_name_growth.update({berry_data['name']: berry_data['growth_time']})
    all_growth_time = [i for i in berries_name_growth.values()]
    all_growth_time = sorted(all_growth_time)
    print(all_growth_time)
    names_list = berries_name_growth.keys()
    names_list = list(names_list)
    plot_html = create_histogram(all_growth_time)
    dict_result = { 
                    "Berries names": names_list,
                    "Min growth time": min(all_growth_time),
                    "Median growth time":  calculate_median(all_growth_time),
                    "Max growth time": max(all_growth_time),
                    "Variance growth time": calculate_variance(all_growth_time),
                    "Mean growth time": calculate_mean(all_growth_time)}
    return render_template('plot_show.html', plot_html=plot_html, berry_data=dict_result)
    


if __name__ == '__main__':
    app_start.run(debug=True)
