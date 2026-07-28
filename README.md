# Quran Reel Detector

Detect Quran surah, verse, and reciter from Instagram, TikTok, and YouTube reels.

## Features

- No server required - runs entirely on your device
- Instagram Reels support
- TikTok videos support
- YouTube Shorts support
- Arabic speech recognition using Whisper model
- Quran verse matching with fuzzy search
- Free to use

## How It Works

1. Paste a reel URL
2. App downloads and transcribes the audio
3. Matches transcription to Quran verses
4. Shows surah name, verse number, and Arabic text

## Build from Source

### Prerequisites

- Node.js 20+
- npm or yarn
- Expo CLI (`npm install -g expo-cli`)
- EAS CLI (`npm install -g eas-cli`)

### Setup

```bash
git clone https://github.com/DALI951/quran-reel-detector.git
cd quran-reel-detector/mobile
npm install
```

### Run Locally

```bash
npx expo start
```

### Build APK

```bash
eas login
eas build --platform android --profile production
```

## API Keys (Optional)

For better transcription accuracy, add your HuggingFace API key:

1. Get free key at https://huggingface.co/settings/tokens
2. Add to `mobile/services/transcription.ts`

## Tech Stack

- **Mobile**: React Native, Expo
- **Transcription**: HuggingFace Whisper API
- **Quran Data**: Local fuzzy matching

## Download

Download the latest APK from [Releases](https://github.com/DALI951/quran-reel-detector/releases)

## License

MIT
