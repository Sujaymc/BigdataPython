import unittest
from flask import json
from unittest.mock import patch
import pandas as pd
from api2 import app, engine  # Import from api2.py

class FlaskAppTestCase(unittest.TestCase):

    @patch('api2.pd.read_sql')  # Mock the pandas read_sql function
    def test_get_data_success(self, mock_read_sql):
        # Mock data
        mock_data = pd.DataFrame([
            {"age": 59,"balance": 2343,"campaign": 1,"contact": "unknown", "day": 5,"default": "no","deposit": "yes","duration": 1042,"education": "secondary", "housing": "yes","id": 1,"job": "admin.","loan": "no","marital": "married","month": "may","pdays": -1,"poutcome": "unknown","previous": 0},
            {"age": 12,"balance": 2133,"campaign": 1,"contact": "unknown", "day": 5,"default": "no","deposit": "yes","duration": 1042,"education": "secondary", "housing": "yes","id": 1,"job": "admin.","loan": "Yes","marital": "married","month": "may","pdays": 0,"poutcome": "unknown","previous": 0}
     
        ])
        mock_read_sql.return_value = mock_data

        # Create a test client
        tester = app.test_client()
        
        # Send a GET request to the /data endpoint
        response = tester.get('/data')
        
        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        
        # Assert the response data
        expected_data = mock_data.to_dict(orient='records')
        self.assertEqual(json.loads(response.data), expected_data)

    @patch('api2.pd.read_sql')  # Mock the pandas read_sql function
    def test_get_data_failure(self, mock_read_sql):
        # Simulate a database read failure
        mock_read_sql.side_effect = Exception("Database error")
        
        # Create a test client
        tester = app.test_client()
        
        # Send a GET request to the /data endpoint
        response = tester.get('/data')
        
        # Assert the response status code
        self.assertEqual(response.status_code, 500)
        
        # Assert the error message
        self.assertEqual(json.loads(response.data), {"error": "Unable to fetch data from database"})

if __name__ == '__main__':
    unittest.main()
