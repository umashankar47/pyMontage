from email import parser

from src.config import MontageConfig
from src.montage_builder import MontageBuilder
import argparse


def parse_resolution(value : str) -> tuple[int, int]:
    try:
        width, height = value.lower().split("x")
        return int(width), int(height)
    except Exception:
        raise argparse.ArgumentTypeError(f"Invalid resolution format: {value}. Expected WIDTHxHEIGHT")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Build a video montage")

    parser.add_argument("--input", default="clips", help="Input folder containing video clips")
    parser.add_argument("--output", default="output_clips", help="Output folder for the final video")
    parser.add_argument("--opfile", default="sniper_montage.mp4", help="Name of the output video file")
    parser.add_argument("--transition", type=float, default=0.4, help="Duration of the transition between clips")
    parser.add_argument("--fps", type=int, default=60, help="Frames per second for the output video")
    parser.add_argument("--random", action="store_true", help="Shuffle the order of clips")
    parser.add_argument("--remove-audio", action="store_true", help="Remove audio from the final video")
    parser.add_argument("--resolution", type=parse_resolution, default=None, help="Target resolution for the output video (e.g., 1920x1080)")
    parser.add_argument("--codec", default="libx264", help="Video codec for the output video")
    parser.add_argument("--audio-codec", default="aac", help="Audio codec for the output video")
    parser.add_argument("--threads", type=int, default=8, help="Number of threads   for video processing")
    parser.add_argument("--preset", default="medium", choices=["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"],help="Encoding speed/quality tradeoff (default: medium)")

    return parser.parse_args()

def main():
    args = parse_arguments()

    overrides = { k: v for k, v in vars(args).items() if v is not None }
    config = MontageConfig( 
        **{

            "input_folder": overrides.get("input"),
            "output_folder": overrides.get("output"),
            "output_name": overrides.get("opfile"),
            "transition": overrides.get("transition"),
            "fps": overrides.get("fps"),
            "random_order": overrides.get("random"),
            "remove_audio": overrides.get("remove_audio"),
            "target_resolution": overrides.get("resolution"),
            "video_codec": overrides.get("codec"),
            "audio_codec": overrides.get("audio_codec"),
            "threads": overrides.get("threads"),
            "preset": overrides.get("preset")

        }
                           
        
    )

    builder = MontageBuilder(config)
    builder.build()

if __name__ == "__main__":
    main()