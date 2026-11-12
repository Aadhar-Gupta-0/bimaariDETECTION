"""Educational symptom guidance. NOT a diagnosis or a medical decision system.

This module intentionally avoids inferring named diseases from a handful of symptoms.
"""
from typing import Iterable

SYMPTOMS = (
    "Headache",
    "Cough",
    "High blood pressure",
    "Dizziness",
    "Fever",
    "Chest pain",
    "Difficulty breathing",
)

EMERGENCY_SYMPTOMS = frozenset({"Chest pain", "Difficulty breathing"})

GENERAL_ADVICE = {
    "Headache": "Headaches have many possible causes. Discuss severe, new or persistent symptoms with a qualified clinician.",
    "Cough": "Coughs have many possible causes. Seek medical attention if symptoms persist or worsen.",
    "High blood pressure": "A blood pressure concern requires a properly measured reading and professional medical review.",
    "Dizziness": "Dizziness has many causes. Seek prompt help if it is severe, recurrent, or accompanied by other concerning symptoms.",
    "Fever": "A fever can occur with many conditions. Seek clinical care for persistent, high or concerning fever.",
    "Chest pain": "Chest pain can be an emergency.",
    "Difficulty breathing": "Breathing difficulty can be an emergency.",
}


def evaluate_symptoms(symptoms: Iterable[str]) -> dict:
    """Return generic, conservative guidance without generating a diagnosis."""
    selected = set(symptoms)
    if not selected:
        return {
            "level": "none",
            "headline": "Select at least one symptom.",
            "guidance": [],
        }

    unknown = selected - set(SYMPTOMS)
    if unknown:
        raise ValueError("Unknown symptom selection")

    if selected & EMERGENCY_SYMPTOMS:
        return {
            "level": "emergency",
            "headline": "Potential emergency: seek urgent medical help now.",
            "guidance": [
                "If you have chest pain or difficulty breathing, contact local emergency services or seek emergency care immediately.",
                "Do not use this demonstration to decide whether to delay medical attention.",
            ],
        }

    return {
        "level": "general",
        "headline": "These symptoms cannot determine a diagnosis.",
        "guidance": [GENERAL_ADVICE[name] for name in SYMPTOMS if name in selected],
    }


def questions_for_clinician(symptoms: Iterable[str]) -> list[str]:
    """General appointment-preparation questions, not medical instructions."""
    selected = set(symptoms)
    if selected - set(SYMPTOMS):
        raise ValueError("Unknown symptom selection")
    if not selected:
        return []
    return [
        "When did these symptoms begin, and have they changed?",
        "What should I tell you about symptom frequency, triggers, and severity?",
        "Are any existing medicines or health conditions relevant?",
        "What warning signs should prompt urgent medical attention?",
    ]
