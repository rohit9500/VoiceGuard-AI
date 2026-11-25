import librosa
import numpy as np
import noisereduce as nr


class AudioPreprocessor:

    @staticmethod
    def normalize(audio):
        return librosa.util.normalize(audio)

    @staticmethod
    def remove_noise(audio, sr):
        return nr.reduce_noise(
            y=audio,
            sr=sr
        )

    @staticmethod
    def trim_silence(audio):
        trimmed, _ = librosa.effects.trim(
            audio,
            top_db=20
        )
        return trimmed

    @staticmethod
    def preprocess(audio, sr):

        audio = AudioPreprocessor.remove_noise(audio, sr)

        audio = AudioPreprocessor.trim_silence(audio)

        audio = AudioPreprocessor.normalize(audio)

        return audio