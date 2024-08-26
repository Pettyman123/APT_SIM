import unittest
from scripts.data_exfiltration import simulate_data_exfiltration

class TestDataExfiltration(unittest.TestCase):

    def test_https_exfiltration(self):
        methods = ["HTTPS"]
        simulate_data_exfiltration(methods)
        # Assert conditions or use mock to check if the method was executed

    def test_ftp_exfiltration(self):
        methods = ["FTP"]
        simulate_data_exfiltration(methods)
        # Assert conditions or use mock to check if the method was executed

if __name__ == '__main__':
    unittest.main()
