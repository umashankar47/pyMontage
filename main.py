from src.config import MontageConfig
from src.montage_builder import MontageBuilder

def main():
    config = MontageConfig(
        input_folder="clips",
        output_folder="output_clips",
        output_name="sniper_montage.mp4",
        transition=0.4,
        fps=60,
        random_order=False,
        remove_audio=False,
    )

    builder = MontageBuilder(config)
    builder.build()

if __name__ == "__main__":
    main()