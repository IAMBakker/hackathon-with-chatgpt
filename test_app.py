import os
import unittest
import requests

class TestUploadEndpoint(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:5050/upload'
        self.test_image_dir = 'test_images'
        os.makedirs(self.test_image_dir, exist_ok=True)

    def tearDown(self):
        # Remove the test images
        for filename in os.listdir(self.test_image_dir):
            os.remove(os.path.join(self.test_image_dir, filename))
        os.rmdir(self.test_image_dir)

    def test_upload_smarty(self):
        # Upload a Smarty image
        with open('test_images/Candy_04_Smarties.jpg', 'rb') as f:
            response = requests.post(self.url, files={'image': f})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['candy'], 'smarty')

    def test_upload_skittles(self):
        # Upload a Skittles image
        with open('test_images/Candy_02_Skittle.jpg', 'rb') as f:
            response = requests.post(self.url, files={'image': f})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['candy'], 'skittle')

    def test_upload_mnm(self):
        # Upload an M&M image
        with open('test_images/Candy_01_MM.jpg', 'rb') as f:
            response = requests.post(self.url, files={'image': f})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['candy'], 'm&m')

    def test_upload_mnm_crispy(self):
        # Upload an M&M image
        with open('test_images/Candy_03_MMcrispy.jpg', 'rb') as f:
            response = requests.post(self.url, files={'image': f})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['candy'], 'm&m_crispy')

if __name__ == '__main__':
    unittest.main()
