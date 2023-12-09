# Berry Fans :blueberries:
   API is created to get berries statistics from https://pokeapi.co/docs/v2#berries. 
   
## :blueberries: Requirements

1. Python 3.10
2. Docker

## :blueberries: How to run the API locally

1. Open a terminal.
2. Clone the repository.
3. Build the Docker image with the sentence `docker build -t berry-api`
4. Run `docker run -it -p 8000:8000 berry-api` to create a container and run the app in the port 8000
5. Enjoy it :wink:!

## :blueberries: How to open deployed version
   Access to http://pierinatp.pythonanywhere.com/ to check the deployed version.

## :blueberries: Endpoints 
   - **GET /** Is the main page of the application. It only has a welcome message
   - **GET /allBerryStats** Contains the information of the current berries.
     Names,
     Min Growth Time,
     Median Growth Time,
     Max Growth Time,
     Variance Growth Time and
     Mean Growth Time.

   
## :blueberries: How to run the tests

1. Open a terminal
2. Go to the API directory
3. Run `pytest`
4. Check it :ok_hand:!
