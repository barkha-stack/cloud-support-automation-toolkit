import os
import unittest

from utils.logger import log_message


class TestLogger(unittest.TestCase):
    def test_log_message_creates_file_and_writes(self):
        # Use a separate log file for tests so we don't pollute app.log
        test_log_name = "test_unit.log"
        logs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")
        test_log_path = os.path.join(logs_dir, test_log_name)

        # Clean up any old test log
        if os.path.exists(test_log_path):
            os.remove(test_log_path)

        # Call the logger
        log_message("Unit test message", log_file=test_log_name)

        # Assert file was created
        self.assertTrue(os.path.exists(test_log_path), "Test log file was not created")

        # Assert content contains our message
        with open(test_log_path, "r") as f:
            content = f.read()

        self.assertIn("Unit test message", content)


if __name__ == "__main__":
    unittest.main()
