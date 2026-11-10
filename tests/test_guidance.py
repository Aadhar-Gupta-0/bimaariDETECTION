import unittest
from guidance import SYMPTOMS, evaluate_symptoms


class GuidanceTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(evaluate_symptoms([])["level"], "none")

    def test_ordinary_symptoms_are_not_diagnoses(self):
        result = evaluate_symptoms(["Headache", "Cough"])
        self.assertEqual(result["level"], "general")
        self.assertIn("cannot determine a diagnosis", result["headline"])
        self.assertEqual(len(result["guidance"]), 2)

    def test_emergency_chest_pain(self):
        self.assertEqual(evaluate_symptoms(["Chest pain"])["level"], "emergency")

    def test_emergency_breathing(self):
        self.assertEqual(evaluate_symptoms(["Difficulty breathing", "Fever"])["level"], "emergency")

    def test_unknown_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_symptoms(["made-up symptom"])

    def test_all_options_have_guidance(self):
        for symptom in SYMPTOMS:
            self.assertTrue(evaluate_symptoms([symptom])["guidance"])


if __name__ == "__main__":
    unittest.main()
