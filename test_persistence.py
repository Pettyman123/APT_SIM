import unittest
from scripts.persistence import simulate_persistence

class TestPersistence(unittest.TestCase):

    def test_registry_run_keys(self):
        techniques = ["Registry Run Keys"]
        simulate_persistence(techniques)
        # Assert conditions or use mock to check if the technique was executed

    def test_startup_folder(self):
        techniques = ["Startup Folder"]
        simulate_persistence(techniques)
        # Assert conditions or use mock to check if the technique was executed

if __name__ == '__main__':
    unittest.main()
