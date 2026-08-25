import os
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VOICE_DIR = Path(os.getenv("PIPER_VOICE_DIR", Path.home() / "piper"))
MODEL = Path(os.getenv("PIPER_MODEL_PATH", VOICE_DIR / "en_US-ryan-high.onnx"))

custom_piper = os.getenv("PIPER_BIN")
if custom_piper:
    PIPER = Path(custom_piper)
else:
    PIPER = REPO_ROOT / ".venv" / "bin" / "piper"
    fallback_piper = Path.home() / "Projects" / "Jarvis" / ".venv" / "bin" / "piper"
    if not PIPER.exists() and fallback_piper.exists():
        PIPER = fallback_piper

TEMP_WAV = os.getenv("JARVIS_TEMP_WAV", "/tmp/jarvis.wav")


def speak(text: str):
    if not PIPER.exists():
        print(f"[WARNING] TTS engine not found at {PIPER}. Skipping audio output.")
        return

    if not MODEL.exists():
        print(f"[WARNING] Voice model not found at {MODEL}. Skipping audio output.")
        return

    try:
        subprocess.run(
            [
                str(PIPER),
                "--model",
                str(MODEL),
                "--output_file",
                TEMP_WAV,
            ],
            input=text,
            text=True,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"[WARNING] Unable to generate speech: {exc}")
        return

    try:
        subprocess.run(["aplay", TEMP_WAV], check=True)
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"[WARNING] Unable to play audio: {exc}")
