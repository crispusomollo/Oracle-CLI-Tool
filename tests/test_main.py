# tests/test_main.py

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

if __name__ == '__main__':
    unittest.main()
