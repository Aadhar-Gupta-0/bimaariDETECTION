import unittest
from guidance import SYMPTOMS, evaluate_symptoms, questions_for_clinician


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

    def test_clinician_questions_are_general_and_opt_in(self):
        self.assertEqual(questions_for_clinician([]), [])
        questions = questions_for_clinician(["Headache"])
        self.assertGreaterEqual(len(questions), 3)
        self.assertTrue(all("diagnosis:" not in q.lower() for q in questions))

    def test_unknown_question_selection_rejected(self):
        with self.assertRaises(ValueError):
            questions_for_clinician(["not a supported symptom"])


if __name__ == "__main__":
    unittest.main()
