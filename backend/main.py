import os
import tempfile
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from downloader import VideoDownloader
from audio_processor import AudioProcessor
from transcriber import QuranTranscriber
from verse_matcher import VerseMatcher

app = FastAPI(
    title="Quran Reel Detector",
    description="Detect Quran surah, verse, and reciter from Instagram/TikTok/YouTube reels",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

downloader = VideoDownloader()
audio_processor = AudioProcessor()
transcriber = QuranTranscriber()
verse_matcher = VerseMatcher()


class URLRequest(BaseModel):
    url: str


class DetectionResult(BaseModel):
    surah_number: int
    surah_name: str
    surah_english_name: str
    verse_number: int
    verse_text: str
    confidence: float
    transcription: str


class ErrorResponse(BaseModel):
    error: str
    detail: str = None


@app.get("/")
async def root():
    return {
        "message": "Quran Reel Detector API",
        "version": "1.0.0",
        "endpoints": {
            "detect": "POST /detect",
            "health": "GET /health"
        }
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/detect", response_model=DetectionResult)
async def detect_quran(request: URLRequest):
    try:
        print(f"Processing URL: {request.url}")

        video_path = await downloader.download(request.url)
        if not video_path:
            raise HTTPException(status_code=400, detail="Failed to download video")

        print(f"Downloaded to: {video_path}")

        audio_path = audio_processor.process(video_path)
        print(f"Audio processed: {audio_path}")

        transcription_result = transcriber.transcribe(audio_path)
        transcribed_text = transcription_result["text"]
        print(f"Transcribed: {transcribed_text}")

        match = verse_matcher.find_best_match(transcribed_text)
        if not match:
            raise HTTPException(
                status_code=404,
                detail="Could not match transcription to any Quran verse"
            )

        _cleanup_files(video_path, audio_path)

        return DetectionResult(
            surah_number=match["surah_number"],
            surah_name=match["surah_name"],
            surah_english_name=match["surah_english_name"],
            verse_number=match["verse_number"],
            verse_text=match["verse_text"],
            confidence=match["confidence"],
            transcription=transcribed_text
        )

    except HTTPException:
        raise
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


def _cleanup_files(*files):
    for file_path in files:
        try:
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
        except Exception:
            pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
