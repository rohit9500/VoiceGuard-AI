"""
===========================================
VoiceGuard AI
Video Processor
===========================================
"""

import os
import subprocess


class VideoProcessor:

    @staticmethod
    def is_video(filename):

        extensions = (
            ".mp4",
            ".avi",
            ".mov",
            ".mkv",
            ".flv",
            ".wmv"
        )

        return filename.lower().endswith(extensions)

    @staticmethod
    def extract_audio(video_path):

        output_audio = os.path.splitext(video_path)[0] + ".wav"

        command = [

            "ffmpeg",

            "-y",

            "-i",

            video_path,

            "-ac",

            "1",

            "-ar",

            "16000",

            output_audio

        ]

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return output_audio