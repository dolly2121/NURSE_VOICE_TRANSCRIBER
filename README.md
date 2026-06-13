# Nurse Voice Transcriber

A privacy-focused voice transcription tool built for aged care nurses to quickly convert spoken patient notes into text.

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
