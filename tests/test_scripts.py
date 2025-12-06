import os
import unittest

from scripts.create_sample_log import create_sample
from scripts.log_monitor import scan_logs
from scripts.health_check import health_check
from scripts.cleanup_resources import cleanup_logs


class TestScripts(unittest.TestCase):
    def test_create_sample_log(self):
        # Run the function
        create_sample()

        # Verify sample.log is created
        sample_log_path = os.path.join("logs", "sample.log")
        self.assertTrue(os.path.exists(sample_log_path), "sample.log was not created")

    def test_log_monitor(self):
        # Assume create_sample() has already created sample.log
        create_sample()
        scan_logs()

        # Verify report file is created
        report_path = os.path.join("logs", "log_report.txt")
        self.assertTrue(os.path.exists(report_path), "log_report.txt was not created")

    def test_health_check(self):
        # Just verify it runs without raising exceptions
        try:
            health_check()
        except Exception as e:
            self.fail(f"health_check() raised an exception: {e}")

    def test_cleanup_resources(self):
        # Create fake temp files
        os.makedirs("logs", exist_ok=True)
        temp1 = "logs/temp1.txt"
        temp2 = "logs/temp2.txt"

        for path in (temp1, temp2):
            with open(path, "w") as f:
                f.write("temp")

        # Run cleanup
        cleanup_logs()

        # Files should be deleted
        self.assertFalse(os.path.exists(temp1), "temp1.txt was not deleted")
        self.assertFalse(os.path.exists(temp2), "temp2.txt was not deleted")


if __name__ == "__main__":
    unittest.main()
