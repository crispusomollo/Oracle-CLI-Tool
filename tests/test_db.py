# tests/test_db.py

import unittest
from unittest.mock import patch, MagicMock
from db import run_query

# Ensure project root is in import path
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestDB(unittest.TestCase):
    
    @patch('db.get_connection')
    def test_run_query_returns_data_and_headers(self, mock_get_connection):
        # Mock the cursor and connection
        mock_cursor = MagicMock()
        mock_cursor.description = [('ID',), ('NAME',)]
        mock_cursor.fetchall.return_value = [(1, 'Alice'), (2, 'Bob')]

        mock_conn = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_get_connection.return_value.__enter__.return_value = mock_conn

        # Run
        sql = "SELECT * FROM users"
        rows, headers = run_query(sql)

        # Assertions
        self.assertEqual(rows, [(1, 'Alice'), (2, 'Bob')])
        self.assertEqual(headers, ['ID', 'NAME'])

if __name__ == '__main__':
    unittest.main()
