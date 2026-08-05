from dataclasses import dataclass
from typing import Optional, Tuple
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


@dataclass
class MontageConfig:
    input_folder: str = str(PROJECT_ROOT / "clips")
    output_folder: str = str(PROJECT_ROOT / "output_clips")
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


def __post_init__(self) -> None:
        if self.transition < 0:
            raise ValueError("transition must be greater than or equal to 0")

        if self.fps <= 0:
            raise ValueError("fps must be greater than 0")

        if self.threads <= 0:
            raise ValueError("threads must be greater than 0")

        if self.target_resolution is not None:
            width, height = self.target_resolution

            if width <= 0 or height <= 0:
                raise ValueError(
                    "target_resolution width and height must be positive integers"
                )
