from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class MontageConfig:
    input_folder: str = "clips"
    output_folder: str = "output_clips"
    output_name: str = "sniper_montage.mp4"
    transition: float = 0.4
    fps: int = 60
    random_order: bool = False
    remove_audio: bool = False
    target_resolution: Optional[Tuple[int, int]] = None
    codec: str = "libx264"
    audio_codec: str = "aac"
    threads: int = 8
    preset: str = "medium"