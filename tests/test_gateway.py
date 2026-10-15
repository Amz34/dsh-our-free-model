import unittest
from dsh_plugin.gateway import validate_request

class TestGateway(unittest.TestCase):
    def test_valid_model(self):
        self.assertTrue(validate_request({"model": "DeepSeek-V4.1-Flash"}))

    def test_invalid_model(self):
        self.assertFalse(validate_request({"model": "Invalid-Model"}))

if __name__ == '__main__':
    unittest.main()
