
from src.config import MontageConfig
from src.montage_builder import MontageBuilder
import argparse

ARG_TO_CONFIG = {
    "input": "input_folder",
    "output": "output_folder",
    "opfile": "output_name",
    "transition": "transition",
    "fps": "fps",
    "random": "random_order",
    "remove_audio": "remove_audio",
    "resolution": "target_resolution",
    "codec": "codec",
    "audio_codec": "audio_codec",
    "threads": "threads",
    "preset": "preset",
}



def parse_resolution(value : str) -> tuple[int, int]:
    try:
        width, height = value.lower().split("x")
        return int(width), int(height)
    except Exception:
        raise argparse.ArgumentTypeError(f"Invalid resolution format: {value}. Expected WIDTHxHEIGHT")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Build a video montage")

    parser.add_argument("--input", default=None, help="Input folder containing video clips")
    parser.add_argument("--output", default=None, help="Output folder for the final video")
    parser.add_argument("--opfile", default=None, help="Name of the output video file")
    parser.add_argument("--transition", type=float, default=None, help="Duration of the transition between clips")
    parser.add_argument("--fps", type=int, default=None, help="Frames per second for the output video")
    parser.add_argument("--random", action="store_true", help="Shuffle the order of clips")
    parser.add_argument("--remove-audio", action="store_true", help="Remove audio from the final video")
    parser.add_argument("--resolution", type=parse_resolution, default=None, 
                        help="Target resolution for the output video (e.g., 1920x1080)")
    
    parser.add_argument("--codec", default=None, help="Video codec for the output video")
    parser.add_argument("--audio-codec", default=None, help="Audio codec for the output video")
    parser.add_argument("--threads", type=int, default=None, help="Number of threads   for video processing")
    parser.add_argument("--preset", default=None, 
                        choices=["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"],
                        help="Encoding speed/quality tradeoff (default: medium)")

    return parser.parse_args()

def build_config(args) -> MontageConfig:
    """
    Convert CLI arguments into MontageConfig.

    Only arguments explicitly provided on the command line override
    the defaults defined in MontageConfig.
    """
    kwargs = {}

    for arg, config_attr in ARG_TO_CONFIG.items():
        value = getattr(args, arg)
        if value is not None:
            kwargs[config_attr] = value

    return MontageConfig(**kwargs)


    

def main():
    args = parse_arguments()

    config = build_config(args)

    builder = MontageBuilder(config)
    builder.build()



if __name__ == "__main__":
    main()


    