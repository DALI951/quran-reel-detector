# Quran Reel Detector

Detect Quran surah, verse, and reciter from Instagram, TikTok, and YouTube reels.

## Features

- Instagram Reels support (no login required)
- TikTok videos support
- YouTube Shorts support
- Arabic speech recognition using Whisper model
- Quran verse matching with fuzzy search
- REST API for mobile app integration

## Backend

### Setup

```bash
cd backend
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

- `GET /` - API info
- `GET /health` - Health check
- `POST /detect` - Detect Quran from reel URL

### Example Request

```bash
curl -X POST "http://localhost:8000/detect" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/reel/ABC123/"}'
```

### Example Response

```json
{
  "surah_number": 1,
  "surah_name": "الفاتحة",
  "surah_english_name": "Al-Fatiha",
  "verse_number": 1,
  "verse_text": "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ",
  "confidence": 0.95,
  "transcription": "بسم الله الرحمن الرحيم"
}
```

## Mobile App

### Setup

```bash
cd mobile
npm install
```

### Run

```bash
npx expo start
```

## Deployment

### Backend (Render)

1. Push to GitHub
2. Connect repo to Render
3. Deploy as Python service

### Mobile (EAS)

```bash
npm install -g eas-cli
eas build
```

## Tech Stack

- **Backend**: Python, FastAPI, yt-dlp, Whisper
- **Mobile**: React Native, Expo
- **AI Model**: tarteel-ai/whisper-base-ar-quran

## License

MIT
