import whisper
import pyaudio
import wave
import os
from datetime import datetime

# --- CONFIG ---
RECORD_SECONDS = 120       # 2 minutes; change as needed
SAMPLE_RATE = 16000
CHUNK = 1024
CHANNELS = 1
FORMAT = pyaudio.paInt16
OUTPUT_DIR = "transcripts"

def record_audio(filename, duration):
    """Records audio from microphone and saves as .wav"""
    p = pyaudio.PyAudio()
    
    print(f"\n🎙️  Recording for {duration} seconds... Speak now!\n")
    
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK
    )
    
    frames = []
    for i in range(0, int(SAMPLE_RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)
        # Show a simple countdown every 10 seconds
        elapsed = int(i * CHUNK / SAMPLE_RATE)
        if elapsed % 10 == 0 and i > 0:
            print(f"  ... {elapsed}s elapsed")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(b''.join(frames))
    
    print(f"\n✅ Recording saved: {filename}")

def transcribe_audio(filename):
    """Transcribes audio using Whisper base model (runs locally)"""
    print("\n🔄 Transcribing... (first run will download the Whisper model ~150MB)\n")
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result["text"]

def save_transcript(text):
    """Saves transcript to a timestamped .txt file"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(OUTPUT_DIR, f"nurse_note_{timestamp}.txt")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Nurse Note — {datetime.now().strftime('%d %B %Y, %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        f.write(text.strip())
        f.write("\n")
    
    return filepath

def main():
    print("=" * 60)
    print("   🏥 Nurse Voice Transcriber — Local & Private")
    print("=" * 60)
    
    # Ask for custom duration
    try:
        duration = int(input(f"\nHow many seconds to record? (default {RECORD_SECONDS}): ").strip() or RECORD_SECONDS)
    except ValueError:
        duration = RECORD_SECONDS
    
    audio_file = "temp_recording.wav"
    
    # Record
    record_audio(audio_file, duration)
    
    # Transcribe
    transcript = transcribe_audio(audio_file)
    
    # Print to screen
    print("\n📝 TRANSCRIPT:")
    print("-" * 60)
    print(transcript.strip())
    print("-" * 60)
    
    # Save to file
    saved_path = save_transcript(transcript)
    print(f"\n💾 Saved to: {saved_path}")
    
    # Clean up temp audio
    os.remove(audio_file)
    print("\n✅ Done!\n")

if __name__ == "__main__":
    main()