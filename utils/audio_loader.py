import librosa
import numpy as np


class AudioLoader:
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate

    def load_audio(self, file_path):
        """
        Load audio file.

        Returns:
            audio : numpy array
            sample_rate : int
        """

        audio, sr = librosa.load(
            file_path,
            sr=self.sample_rate,
            mono=True
        )

        return audio, sr