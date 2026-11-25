import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


class AudioVisualizer:

    @staticmethod
    def load_audio(file_path, sample_rate=16000):
        """
        Load an audio file.

        Returns
        -------
        audio : np.ndarray
        sr : int
        """

        audio, sr = librosa.load(
            file_path,
            sr=sample_rate,
            mono=True
        )

        return audio, sr

    @staticmethod
    def plot_waveform(audio, sr):
        """
        Generate waveform figure.
        """

        fig, ax = plt.subplots(
            figsize=(12, 3)
        )

        librosa.display.waveshow(
            audio,
            sr=sr,
            ax=ax
        )

        ax.set_title("Waveform")

        ax.set_xlabel("Time")

        ax.set_ylabel("Amplitude")

        ax.grid(alpha=0.3)

        plt.tight_layout()

        return fig

    @staticmethod
    def plot_mel_spectrogram(audio, sr):
        """
        Generate Mel Spectrogram.
        """

        mel = librosa.feature.melspectrogram(
            y=audio,
            sr=sr,
            n_mels=128
        )

        mel_db = librosa.power_to_db(
            mel,
            ref=np.max
        )

        fig, ax = plt.subplots(
            figsize=(12, 4)
        )

        img = librosa.display.specshow(
            mel_db,
            x_axis="time",
            y_axis="mel",
            sr=sr,
            cmap="magma",
            ax=ax
        )

        fig.colorbar(
            img,
            ax=ax,
            format="%+2.0f dB"
        )

        ax.set_title("Mel Spectrogram")

        plt.tight_layout()

        return fig

    @staticmethod
    def plot_mfcc(audio, sr):
        """
        Plot MFCC Heatmap.
        """

        mfcc = librosa.feature.mfcc(
            y=audio,
            sr=sr,
            n_mfcc=40
        )

        fig, ax = plt.subplots(
            figsize=(12, 4)
        )

        img = librosa.display.specshow(
            mfcc,
            x_axis="time",
            sr=sr,
            cmap="viridis",
            ax=ax
        )

        fig.colorbar(img)

        ax.set_title("MFCC")

        plt.tight_layout()

        return fig

    @staticmethod
    def plot_chroma(audio, sr):
        """
        Plot Chroma Feature.
        """

        chroma = librosa.feature.chroma_stft(
            y=audio,
            sr=sr
        )

        fig, ax = plt.subplots(
            figsize=(12, 4)
        )

        img = librosa.display.specshow(
            chroma,
            x_axis="time",
            y_axis="chroma",
            sr=sr,
            cmap="coolwarm",
            ax=ax
        )

        fig.colorbar(img)

        ax.set_title("Chroma Features")

        plt.tight_layout()

        return fig

    @staticmethod
    def plot_pitch(audio, sr):
        """
        Plot estimated pitch contour.
        """

        pitches, magnitudes = librosa.piptrack(
            y=audio,
            sr=sr
        )

        pitch = []

        for i in range(pitches.shape[1]):

            index = magnitudes[:, i].argmax()

            pitch.append(pitches[index, i])

        fig, ax = plt.subplots(
            figsize=(12, 3)
        )

        ax.plot(
            pitch,
            linewidth=1
        )

        ax.set_title("Estimated Pitch")

        ax.set_xlabel("Frame")

        ax.set_ylabel("Frequency (Hz)")

        ax.grid(alpha=0.3)

        plt.tight_layout()

        return fig