import unittest
import urllib.request

class TestWebsite(unittest.TestCase):
    
    def test_website_loads(self):
        url = "https://atg.world"
        print("Connecting to", url)
        response = urllib.request.urlopen(url)
        status_code = response.getcode()
        print("Response status code:", status_code)
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
