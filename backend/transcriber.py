import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import numpy as np
import soundfile as sf


class QuranTranscriber:
    def __init__(self, model_name: str = "tarteel-ai/whisper-base-ar-quran"):
        self.model_name = model_name
        self.processor = None
        self.model = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self._load_model()

    def _load_model(self):
        print(f"Loading model {self.model_name}...")
        self.processor = WhisperProcessor.from_pretrained(self.model_name)
        self.model = WhisperForConditionalGeneration.from_pretrained(self.model_name)
        self.model = self.model.to(self.device)
        print(f"Model loaded on {self.device}")

    def transcribe(self, audio_path: str) -> dict:
        audio, sample_rate = sf.read(audio_path)

        if len(audio.shape) > 1:
            audio = audio.mean(axis=1)

        if sample_rate != 16000:
            from pydub import AudioSegment
            import tempfile
            temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            audio_segment = AudioSegment(
                audio.tobytes(),
                frame_rate=sample_rate,
                sample_width=audio.dtype.itemsize,
                channels=1
            )
            audio_segment = audio_segment.set_frame_rate(16000)
            audio_segment.export(temp_wav.name, format="wav")
            audio, sample_rate = sf.read(temp_wav.name)
            import os
            os.unlink(temp_wav.name)

        input_features = self.processor(
            audio,
            sampling_rate=16000,
            return_tensors="pt"
        ).input_features.to(self.device)

        with torch.no_grad():
            predicted_ids = self.model.generate(input_features)

        transcription = self.processor.batch_decode(
            predicted_ids,
            skip_special_tokens=True
        )[0]

        return {
            "text": transcription.strip(),
            "language": "ar"
        }

    def transcribe_segments(self, audio_path: str, segment_duration: float = 30.0) -> list:
        from pydub import AudioSegment

        audio = AudioSegment.from_wav(audio_path)
        duration_ms = len(audio)
        segment_ms = int(segment_duration * 1000)

        segments = []
        for start in range(0, duration_ms, segment_ms):
            end = min(start + segment_ms, duration_ms)
            segment = audio[start:end]

            segment_path = f"temp/segment_{start}.wav"
            segment.export(segment_path, format="wav")

            result = self.transcribe(segment_path)
            result["start_time"] = start / 1000.0
            result["end_time"] = end / 1000.0
            segments.append(result)

            import os
            os.remove(segment_path)

        return segments
