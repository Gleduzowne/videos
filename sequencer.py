import os
import wave

def get_audio_length(file_path):
    with wave.open(file_path, 'rb') as wav:
        frames = wav.getnframes()
        rate = wav.getframerate()
        return frames / float(rate)

class Sequencer:
    def __init__(self, scenes, voiceover_text):
        self.scenes = scenes
        self.voiceover_text = voiceover_text
        self.audio_files = []
        self.audio_lengths = []

    def generate_audio_segments(self):
        segment_start = 0
        for i, scene in enumerate(self.scenes):
            next_idx = self.voiceover_text.find(scene.content, segment_start)
            if next_idx == -1:
                segment = self.voiceover_text[segment_start:]
            else:
                segment = self.voiceover_text[segment_start:next_idx]
                segment_start = next_idx
            audio_file = f"scene_{i}.wav"
            command = f'echo "{segment}" | flite -o {audio_file}'
            os.system(command)
            self.audio_files.append(audio_file)
            audio_length = get_audio_length(audio_file)
            self.audio_lengths.append(audio_length)

    def sequence(self, manim_self):
        for i, scene in enumerate(self.scenes):
            if i < len(self.audio_files):
                manim_self.add_sound(self.audio_files[i], time_offset=manim_self.renderer.time)
            duration = max(scene.duration, self.audio_lengths[i])
            manim_self.wait(duration)
