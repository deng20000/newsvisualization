import unittest
import requests,json

class MyTestCase(unittest.TestCase):

    def test_api_finish(self):
        # Create a URL to query the News API
        url = "https://newsapi.org/v2/everything?q=科技&from=2023-10-27&to=2023-10-29&sortBy=popularity&language=zh&apiKey=b4f080f0c1834adfa203e577d141be21"
        # Make a request to the News API
        responese = requests.get(url)
        # Assert that the response code is 200 (OK)
        self.assertEqual(responese.status_code, 200)

    def test_api_data(self):
        # Create a URL to query the News API
        url = "https://newsapi.org/v2/everything?q=科技&from=2023-10-27&to=2023-10-29&sortBy=popularity&language=zh&apiKey=b4f080f0c1834adfa203e577d141be21"
        # Make a request to the News API
        responese = requests.get(url)





if __name__ == '__main__':
    unittest.main()
