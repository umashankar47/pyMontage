from moviepy import CompositeVideoClip
from .clip_loader import ClipLoader
from .transition_engine import TransitionEngine
from .output_manager import OutputManager

class MontageBuilder:
    def __init__(self, config):
        self.config = config
        self.loader = ClipLoader(config)
        self.transitions = TransitionEngine(config.transition)
        self.output = OutputManager(config)

    def build(self):
        try:
            clips = self.loader.load_clips()
            timeline, duration = self.transitions.build_timeline(clips)

            target_size = self.config.target_resolution or clips[0].size
            final = CompositeVideoClip(timeline, size=target_size)
            final = final.with_duration(duration)

            output_path = self.output.get_unique_path()
            print(f"Output will be saved to: {output_path}")

            final.write_videofile(
                str(output_path),
                codec=self.config.codec,
                audio_codec=self.config.audio_codec,
                fps=self.config.fps,
                threads=self.config.threads,
                preset=self.config.preset
            )

            print(f"\nDone! Saved to {output_path}")
        finally:
            self.loader.close_all()
            
        return output_path