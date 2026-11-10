# bimaariDETECTION

An **educational Tkinter symptom explorer**, modernized from an early student Python project.

## Changes in this edition
- Replaced unsafe symptom-to-disease guesses with conservative, general educational guidance.
- Provides an urgent-care warning for reported chest pain or difficulty breathing.
- Removed hardcoded real-looking doctor's contact information and unverified recommendations.
- No patient CSV records are published, generated, or stored.
- Added a simplified welcome screen, clearer interface, and unit tests.
- Added explicit disclaimers: **this application is not a medical device and cannot diagnose any disease.**

## Run

Python 3.10+ with Tkinter (usually included with Python desktop distributions):

```bash
python Login.py
```

Or skip the welcome screen with `python Detection.py`.

## Tests

```bash
python -m unittest discover -s tests -v
python -m compileall -q Login.py Detection.py guidance.py
```

## Privacy and limitations
The original source contained patient records and phone numbers. These **are intentionally not copied** into this public edition. All user-selected information stays in memory and is lost when the application closes. In a real medical situation, consult a licensed professional, and seek urgent care for possible emergency symptoms.

Based on [ishaands12/Disease-Detection-Project](https://github.com/ishaands12/Disease-Detection-Project), independently maintained as `Aadhar-Gupta-0/bimaariDETECTION`.
