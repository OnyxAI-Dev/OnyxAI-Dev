import unittest
from onyxai.ai_engine import AIEngine

class TestAIEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AIEngine()

    def test_process_data(self):
        input_data = {"key": "value"}
        result = self.engine.process_data(input_data)
        self.assertEqual(result["key"], "processed_value")

    def test_predict(self):
        prediction = self.engine.predict("test input")
        self.assertIn(prediction["prediction"], ["positive", "negative", "neutral"])

if __name__ == "__main__":
    unittest.main()
