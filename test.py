import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_predict_endpoint(self):
        input_data = {
            'feature1': 7.8,
            'feature2': 0.88,
            'feature3': 0.96,
            'feature4': 0.02,
            'feature5': 1.8,
            'feature6': 86.0,
            'feature7': 3.45,
            'feature8': 1.25,
            'feature9': 0.5,
            'feature10': 5.5,
            'feature11': 1.1,
            'feature12': 3.0,
            'feature13': 1050.0
        }

        response = self.app.post('/predict', json=input_data)
        data = response.get_json()

        print("Response status code:", response.status_code)
        print("Response data:", data)

        self.assertIn('prediction', data)
        self.assertTrue(data['prediction'] in [
                        'Class 0', 'Class 1', 'Class 2'])


if __name__ == '__main__':
    unittest.main()