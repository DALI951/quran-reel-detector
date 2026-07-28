import os
from pydub import AudioSegment


class AudioProcessor:
    def __init__(self, output_dir: str = "temp"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def convert_to_wav(self, input_path: str, output_path: str = None) -> str:
        if output_path is None:
            base = os.path.splitext(os.path.basename(input_path))[0]
            output_path = os.path.join(self.output_dir, f"{base}.wav")

        audio = AudioSegment.from_file(input_path)
        audio = audio.set_frame_rate(16000)
        audio = audio.set_channels(1)
        audio.export(output_path, format="wav")
        return output_path

    def extract_audio_segment(self, input_path: str, start_ms: int = 0, end_ms: int = None) -> str:
        audio = AudioSegment.from_file(input_path)
        if end_ms is None:
            end_ms = len(audio)
        segment = audio[start_ms:end_ms]
        output_path = os.path.join(self.output_dir, "segment.wav")
        segment = segment.set_frame_rate(16000)
        segment = segment.set_channels(1)
        segment.export(output_path, format="wav")
        return output_path

    def get_audio_duration(self, file_path: str) -> float:
        audio = AudioSegment.from_file(file_path)
        return len(audio) / 1000.0

    def normalize_audio(self, input_path: str) -> str:
        audio = AudioSegment.from_file(input_path)
        target_dBFS = -20.0
        change_in_dBFS = target_dBFS - audio.dBFS
        normalized = audio.apply_gain(change_in_dBFS)
        output_path = os.path.join(self.output_dir, "normalized.wav")
        normalized = normalized.set_frame_rate(16000)
        normalized = normalized.set_channels(1)
        normalized.export(output_path, format="wav")
        return output_path

    def process(self, input_path: str) -> str:
        wav_path = self.convert_to_wav(input_path)
        normalized_path = self.normalize_audio(wav_path)
        return normalized_path
