"""
voice.py

Handles speech recognition.
"""

import os
import sys
import speech_recognition as sr
from contextlib import contextmanager


@contextmanager
def suppress_stderr():
    """
    Temporarily hides ALSA/JACK warnings.
    """

    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)

    try:
        os.dup2(devnull, 2)
        yield
    finally:
        os.dup2(old_stderr, 2)
        os.close(old_stderr)
        os.close(devnull)


class VoiceRecognizer:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):

        with suppress_stderr():

            with sr.Microphone() as source:

                print("\nListening...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5,
                )

                audio = self.recognizer.listen(source)

        try:

            text = self.recognizer.recognize_google(audio)

            print(f"You: {text}")

            return text

        except sr.UnknownValueError:
            return ""

        except Exception as e:
            print(e)
            return ""


voice = VoiceRecognizer()