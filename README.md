# Inspiration
Nurse while talking to the patient or older adult seems distracted bcz they feel taking notes is necessary which result in loss of empathy while talking to the patient or older adult. This tool was made so that nurse can engage with full attantion while talking and AI will do it's work of taking notes

# Nurse Voice Transcriber

A privacy-focused voice transcription tool built for aged care nurses to quickly convert spoken patient notes into text and download the file at the end of the day.

## Features

- Voice-to-text transcription using OpenAI Whisper
- Runs entirely locally, no patient data leaves your device
- Patient slot management for organizing notes
- Waveform visualization during recording
- Inline editing of transcribed text
- Export to Excel

## Versions

### 1. Python (Local)
Run `transcriber.py` for a local Whisper-based transcriber.

```bash
pip install -r requirements.txt
python transcriber.py
```

### 2. Browser-based (Whisper.js)
Open `index.html` in a modern browser. Runs entirely client-side using Whisper.js, no installation needed.

## Privacy

All processing happens locally on your device. No audio or transcribed data is sent to external servers.

## Sample Data

`Patient_Notes.xlsx` contains dummy data for demonstration purposes only.
