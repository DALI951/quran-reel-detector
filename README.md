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

### Backend (Render) - Auto Deploy on Push

1. Go to [render.com](https://render.com) and create an account
2. Click "New +" → "Web Service"
3. Connect your GitHub repo: `DALI951/quran-reel-detector`
4. Render will auto-detect the `render.yaml` config
5. Set these environment variables in Render dashboard:
   - `PYTHON_VERSION` = `3.11`
6. Deploy! It will auto-deploy on every push to `master`

**Alternatively**, set up GitHub Actions secrets for programmatic deploys:
- Go to repo → Settings → Secrets → Actions
- Add `RENDER_SERVICE_ID` and `RENDER_API_KEY` from Render dashboard

### Mobile (EAS) - Auto Build on Push

1. Create an [Expo](https://expo.dev) account
2. Get your token from expo.dev → Account Settings → Access Tokens
3. Go to repo → Settings → Secrets → Actions
4. Add secret: `EXPO_TOKEN` = your Expo access token
5. Push to `master` and the build will trigger automatically

**Manual build:**
```bash
cd mobile
npm install
npm install -g eas-cli
eas login
eas build --platform android --profile production
eas build --platform ios --profile production
```

### GitHub Actions Workflows

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| `deploy-backend.yml` | Push to `backend/**` | Deploys API to Render |
| `build-mobile.yml` | Push to `mobile/**` | Builds Android & iOS apps via EAS |

## Tech Stack

- **Backend**: Python, FastAPI, yt-dlp, Whisper
- **Mobile**: React Native, Expo
- **AI Model**: tarteel-ai/whisper-base-ar-quran
- **CI/CD**: GitHub Actions, Render, EAS Build

## License

MIT
