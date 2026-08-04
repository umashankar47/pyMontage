from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class MontageConfig:
    input_folder: str = "pyMontage/clips"
    output_folder: str = "pyMontage/output_clips"
    #intro_outro_folder: str = "clips/intro_outro"  
    output_name: str = "CallOfDutyMobile.mp4"
    transition: float = 0.4
    fps: int = 60
    random_order: bool = False
    remove_audio: bool = False
    target_resolution: Optional[Tuple[int, int]] = None
    codec: str = "libx264"
    audio_codec: str = "aac"
    threads: int = 8
    preset: str = "medium"


    def __post_init__(self):
        pass