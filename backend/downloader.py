import os
import re
import yt_dlp
import httpx
from typing import Optional
from urllib.parse import urlparse


class VideoDownloader:
    def __init__(self, download_dir: str = "downloads"):
        self.download_dir = download_dir
        os.makedirs(download_dir, exist_ok=True)

    def detect_platform(self, url: str) -> str:
        domain = urlparse(url).netloc.lower()
        if "instagram.com" in domain:
            return "instagram"
        elif "tiktok.com" in domain or "vm.tiktok.com" in domain:
            return "tiktok"
        elif "youtube.com" in domain or "youtu.be" in domain or "youtube.com/shorts" in domain:
            return "youtube"
        return "unknown"

    async def download_instagram(self, url: str) -> Optional[str]:
        try:
            shortcode = self._extract_instagram_shortcode(url)
            if not shortcode:
                return None

            api_url = f"https://api.instagram.com/media/{shortcode}/?__a=1&__d=dis"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }

            async with httpx.AsyncClient() as client:
                response = await client.get(api_url, headers=headers, follow_redirects=True)
                if response.status_code == 200:
                    data = response.json()
                    video_url = data.get("graphql", {}).get("shortcode_media", {}).get("video_url")
                    if video_url:
                        return await self._download_file(video_url, f"{shortcode}.mp4")

            return await self._download_with_ytdlp(url)
        except Exception as e:
            print(f"Instagram download error: {e}")
            return await self._download_with_ytdlp(url)

    def _extract_instagram_shortcode(self, url: str) -> Optional[str]:
        patterns = [
            r"instagram\.com/reel/([A-Za-z0-9_-]+)",
            r"instagram\.com/p/([A-Za-z0-9_-]+)",
            r"instagram\.com/tv/([A-Za-z0-9_-]+)",
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None

    async def download_tiktok(self, url: str) -> Optional[str]:
        return await self._download_with_ytdlp(url)

    async def download_youtube(self, url: str) -> Optional[str]:
        return await self._download_with_ytdlp(url)

    async def _download_with_ytdlp(self, url: str) -> Optional[str]:
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(self.download_dir, '%(id)s.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                base, _ = os.path.splitext(filename)
                return base + ".mp3"
        except Exception as e:
            print(f"yt-dlp download error: {e}")
            return None

    async def _download_file(self, url: str, filename: str) -> str:
        filepath = os.path.join(self.download_dir, filename)
        async with httpx.AsyncClient() as client:
            response = await client.get(url, follow_redirects=True)
            with open(filepath, "wb") as f:
                f.write(response.content)
        return filepath

    async def download(self, url: str) -> Optional[str]:
        platform = self.detect_platform(url)
        print(f"Detected platform: {platform}")

        if platform == "instagram":
            return await self.download_instagram(url)
        elif platform == "tiktok":
            return await self.download_tiktok(url)
        elif platform == "youtube":
            return await self.download_youtube(url)
        else:
            return await self._download_with_ytdlp(url)
