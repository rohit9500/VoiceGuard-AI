"""
==========================================================
VoiceGuard AI
Audio Statistics Module
==========================================================
"""

import librosa
import numpy as np


class AudioStatistics:
    """
    Calculates useful statistics from an audio signal.
    """

    @staticmethod
    def get_statistics(audio, sr):
        """
        Returns a dictionary containing audio statistics.
        """

        # Duration
        duration = librosa.get_duration(y=audio, sr=sr)

        # RMS Energy
        rms = np.mean(librosa.feature.rms(y=audio))

        # Zero Crossing Rate
        zcr = np.mean(librosa.feature.zero_crossing_rate(y=audio))

        # Spectral Centroid
        centroid = np.mean(
            librosa.feature.spectral_centroid(
                y=audio,
                sr=sr
            )
        )

        # Spectral Bandwidth
        bandwidth = np.mean(
            librosa.feature.spectral_bandwidth(
                y=audio,
                sr=sr
            )
        )

        # Spectral Roll-off
        rolloff = np.mean(
            librosa.feature.spectral_rolloff(
                y=audio,
                sr=sr
            )
        )

        # Tempo (Estimated BPM)
        tempo, _ = librosa.beat.beat_track(
            y=audio,
            sr=sr
        )

        # Silence Percentage
        threshold = 0.01

        silence = np.sum(np.abs(audio) < threshold)

        silence_percentage = (silence / len(audio)) * 100

        # Estimated Signal-to-Noise Ratio (SNR)

        signal_power = np.mean(audio ** 2)

        noise = audio - np.mean(audio)

        noise_power = np.mean(noise ** 2)

        if noise_power == 0:
            snr = 100
        else:
            snr = 10 * np.log10(signal_power / noise_power)

        return {

            "Duration (sec)": round(float(duration), 2),

            "Sample Rate (Hz)": sr,

            "RMS Energy": round(float(rms), 5),

            "Zero Crossing Rate": round(float(zcr), 5),

            "Spectral Centroid": round(float(centroid), 2),

            "Spectral Bandwidth": round(float(bandwidth), 2),

            "Spectral Roll-off": round(float(rolloff), 2),

            "Tempo (BPM)": round(float(tempo), 2),

            "Silence (%)": round(float(silence_percentage), 2),

            "Estimated SNR (dB)": round(float(snr), 2)

        }