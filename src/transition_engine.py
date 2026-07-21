from moviepy.video.fx.CrossFadeIn import CrossFadeIn
from moviepy.audio.fx.AudioFadeIn import AudioFadeIn

class TransitionEngine:
    def __init__(self, transition_duration: float):
        self.transition_duration = transition_duration

    def build_timeline(self, clips):
        timeline = []
        current_time = 0

        for i, clip in enumerate(clips):
            if i == 0:
                clip = clip.with_start(0)
                current_time = clip.duration
            else:
                clip = clip.with_start(current_time - self.transition_duration)
                current_time += clip.duration - self.transition_duration
                clip = self._apply_fade(clip)

            timeline.append(clip)

        return timeline, current_time

    def _apply_fade(self, clip):
        clip = clip.with_effects([CrossFadeIn(self.transition_duration)])
        if clip.audio is not None:
            clip = clip.with_audio(
                clip.audio.with_effects([AudioFadeIn(self.transition_duration)])
            )
        return clip