import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

class SpectrogramGenerator:

    @staticmethod
    def waveform(audio):

        fig, ax = plt.subplots(figsize=(10,3))

        librosa.display.waveshow(audio, ax=ax)

        ax.set_title("Waveform")

        return fig


    @staticmethod
    def mel(audio, sr):

        mel = librosa.feature.melspectrogram(
            y=audio,
            sr=sr
        )

        db = librosa.power_to_db(
            mel,
            ref=np.max
        )

        fig, ax = plt.subplots(figsize=(10,4))

        librosa.display.specshow(
            db,
            sr=sr,
            x_axis="time",
            y_axis="mel",
            ax=ax
        )

        ax.set_title("Mel Spectrogram")

        return fig