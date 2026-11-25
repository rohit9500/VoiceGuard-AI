import librosa
import numpy as np


class FeatureExtractor:

    @staticmethod
    def extract_features(audio, sr):

        mfcc = librosa.feature.mfcc(
            y=audio,
            sr=sr,
            n_mfcc=40
        )

        chroma = librosa.feature.chroma_stft(
            y=audio,
            sr=sr
        )

        mel = librosa.feature.melspectrogram(
            y=audio,
            sr=sr
        )

        contrast = librosa.feature.spectral_contrast(
            y=audio,
            sr=sr
        )

        zcr = librosa.feature.zero_crossing_rate(audio)

        rms = librosa.feature.rms(y=audio)

        centroid = librosa.feature.spectral_centroid(
            y=audio,
            sr=sr
        )

        bandwidth = librosa.feature.spectral_bandwidth(
            y=audio,
            sr=sr
        )

        rolloff = librosa.feature.spectral_rolloff(
            y=audio,
            sr=sr
        )

        features = np.hstack([

            np.mean(mfcc, axis=1),

            np.mean(chroma, axis=1),

            np.mean(mel, axis=1),

            np.mean(contrast, axis=1),

            np.mean(zcr),

            np.mean(rms),

            np.mean(centroid),

            np.mean(bandwidth),

            np.mean(rolloff)

        ])

        return features