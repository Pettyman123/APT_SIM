import unittest
from scripts.lateral_movement import simulate_lateral_movement

class TestLateralMovement(unittest.TestCase):

    def test_pass_the_hash(self):
        techniques = ["Pass-the-Hash"]
        simulate_lateral_movement(techniques)
        # Assert conditions or use mock to check if the technique was executed

    def test_remote_services(self):
        techniques = ["Remote Services"]
        simulate_lateral_movement(techniques)
        # Assert conditions or use mock to check if the technique was executed

if __name__ == '__main__':
    unittest.main()

