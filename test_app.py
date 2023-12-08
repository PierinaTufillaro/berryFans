import unittest
from unittest.mock import MagicMock, patch

from app import app_start, calculate_median, calculate_mean, calculate_variance

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app_start.test_client()
        self.app.testing = True
        self.list_of_berry_growth = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 8, 12]

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello Berry fan!")

    @patch('app.render_template')
    def test_all_berry_stats(self, mock_render):
        mock_render.return_value = ""
        response = self.app.get('/allBerryStats')
        self.assertEqual(response.status_code, 200)
        
    def test_calculate_mean(self):
        result = calculate_mean(self.list_of_berry_growth)
        self.assertEqual(result, 4.1)
        
    def test_calculate_variance(self):
        result = calculate_variance(self.list_of_berry_growth)
        self.assertEqual(result, 5.778947368421053)
        
    def test_calculate_median(self):
        result = calculate_median(self.list_of_berry_growth)
        self.assertEqual(result, 3.5)
        
             
if __name__ == '__main__':
    unittest.main()