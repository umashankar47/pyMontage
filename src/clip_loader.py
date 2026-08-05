import random
from pathlib import Path
from typing import List, Optional
from moviepy import VideoFileClip
from tqdm import tqdm

class ClipLoader:
    SUPPORTED_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv", ".webm"}

    def __init__(self, config):
        self.config = config
        self._loaded_clips: List[VideoFileClip] = []

    def find_video_files(self) -> List[Path]:
        files = []
        input_path = Path(self.config.input_folder)

        if not input_path.exists():
            raise FileNotFoundError(
                f"Input folder does not exist: '{input_path.resolve()}'"
            )

    
        for ext in self.SUPPORTED_EXTENSIONS:
            files.extend(input_path.glob(f"*{ext}"))

        if not files:
            raise FileNotFoundError(
                f"No videos found in '{input_path.resolve()}' "
                f"with supported extensions: {self.SUPPORTED_EXTENSIONS} ")

        intro, outro, middle = self._split_intro_outro(files)

        middle = sorted(middle)
        if self.config.random_order:
            random.shuffle(middle)

        ordered = []
        if intro:
            ordered.append(intro)
        ordered.extend(middle)
        if outro:
            ordered.append(outro)

        return ordered

    def _split_intro_outro(self, files: List[Path]):
        intro: Optional[Path] = None
        outro: Optional[Path] = None
        middle = []

        for f in files:
            name = f.stem.lower()
            if name == "intro":
                if intro is not None:
                    raise ValueError(f"Multiple intro files found: '{intro.name}' and '{f.name}'")
                intro = f
            elif name == "outro":
                if outro is not None:
                    raise ValueError(f"Multiple outro files found: '{outro.name}' and '{f.name}'")
                outro = f
            else:
                middle.append(f)

        if intro:
            print(f"Intro detected: {intro.name}")
        if outro:
            print(f"Outro detected: {outro.name}")

        return intro, outro, middle

    def load_clips(self) -> List[VideoFileClip]:
        files = self.find_video_files()
        print(f"Found {len(files)} clips")

        clips = []

        try:
            for file in tqdm(files):
                clip = VideoFileClip(str(file))
                if self.config.remove_audio:
                    clip = clip.without_audio()
                clips.append(clip)
        except Exception as e:
            for clip in clips:
                clip.close()
            raise e

        
        return self._normalize_sizes(clips)

    def _normalize_sizes(self, clips):

        if not clips:
            return []
        
        target_size = self.config.target_resolution or clips[0].size
        return [
            c if c.size == target_size else c.resized(target_size)
            for c in clips
        ]

    
    def close_all(self):
        for clip in self._loaded_clips:
            clip.close()
        self._loaded_clips.clear()