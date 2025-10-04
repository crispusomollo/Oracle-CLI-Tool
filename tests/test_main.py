# tests/test_main.py

from main import load_sql_file

import unittest
import os
from main import save_to_csv

class TestMain(unittest.TestCase):

    def test_save_to_csv_creates_file_with_headers_and_data(self):
        data = [(1, 'Alice'), (2, 'Bob')]
        headers = ['ID', 'Name']
        filename = 'test_output.csv'
        path = os.path.join("output", filename)

        # Ensure output dir exists
        os.makedirs("output", exist_ok=True)

        # Run function
        save_to_csv(data, headers, filename)

        # Assert file was created
        self.assertTrue(os.path.exists(path))

        # Optionally check contents
        with open(path, 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0].strip(), 'ID,Name')
        self.assertEqual(lines[1].strip(), '1,Alice')
        self.assertEqual(lines[2].strip(), '2,Bob')

        # Cleanup
        os.remove(path)

    def test_load_sql_file_success(self):
        test_sql_name = "test_query"
        test_sql_path = f"sql/{test_sql_name}.sql"

        os.makedirs("sql", exist_ok=True)
        with open(test_sql_path, "w") as f:
            f.write("SELECT * FROM users")

        sql_content = load_sql_file(test_sql_name)
        self.assertIn("SELECT * FROM users", sql_content)

        # Cleanup
        os.remove(test_sql_path)

    def test_load_sql_file_missing(self):
        with self.assertRaises(FileNotFoundError):
            load_sql_file("non_existent_query")


if __name__ == '__main__':
    unittest.main()
