import subprocess
from pathlib import Path

VOICE_DIR = Path.home() / "piper"

MODEL = VOICE_DIR / "en_US-ryan-high.onnx"

PIPER = (
    Path.home()
    / "Projects"
    / "Jarvis"
    / ".venv"
    / "bin"
    / "piper"
)

TEMP_WAV = "/tmp/jarvis.wav"


def speak(text: str):
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

    subprocess.run(["aplay", TEMP_WAV], check=True)
