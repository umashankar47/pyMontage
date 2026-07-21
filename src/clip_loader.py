import random
from pathlib import Path
from typing import List
from moviepy import VideoFileClip
from tqdm import tqdm

class ClipLoader:
    SUPPORTED_EXTENSIONS = ("*.mp4", "*.mov", "*.avi", "*.mkv", "*.webm")

    def __init__(self, config):
        self.config = config

    def find_video_files(self) -> List[Path]:
        files = []
        for ext in self.SUPPORTED_EXTENSIONS:
            files.extend(Path(self.config.input_folder).glob(ext))
        files = sorted(files)

        if self.config.random_order:
            random.shuffle(files)

        if not files:
            raise FileNotFoundError(f"No videos found in '{self.config.input_folder}'")

        return files

    def load_clips(self) -> List[VideoFileClip]:
        files = self.find_video_files()
        print(f"Found {len(files)} clips")

        clips = []
        for file in tqdm(files):
            clip = VideoFileClip(str(file))
            if self.config.remove_audio:
                clip = clip.without_audio()
            clips.append(clip)

        return self._normalize_sizes(clips)

    def _normalize_sizes(self, clips):
        target_size = self.config.target_resolution or clips[0].size
        return [
            c if c.size == target_size else c.resized(target_size)
            for c in clips
        ]