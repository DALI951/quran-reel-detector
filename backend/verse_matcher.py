import json
import os
from typing import Optional
from difflib import SequenceMatcher


class VerseMatcher:
    def __init__(self, quran_data_dir: str = "quran_data"):
        self.quran_data_dir = quran_data_dir
        self.surahs = {}
        self._load_quran_data()

    def _load_quran_data(self):
        print("Loading Quran data...")
        data_path = os.path.join(self.quran_data_dir, "quran.json")
        if os.path.exists(data_path):
            with open(data_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for surah in data:
                    self.surahs[surah["number"]] = surah
        else:
            self._create_default_data()
        print(f"Loaded {len(self.surahs)} surahs")

    def _create_default_data(self):
        os.makedirs(self.quran_data_dir, exist_ok=True)
        default_surahs = [
            {
                "number": 1,
                "name": "الفاتحة",
                "english_name": "Al-Fatiha",
                "verses": [
                    {"number": 1, "text": "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ"},
                    {"number": 2, "text": "ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَـٰلَمِينَ"},
                    {"number": 3, "text": "ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ"},
                    {"number": 4, "text": "مَـٰلِكِ يَوْمِ ٱلدِّينِ"},
                    {"number": 5, "text": "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"},
                    {"number": 6, "text": "ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ"},
                    {"number": 7, "text": "صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ"}
                ]
            },
            {
                "number": 36,
                "name": "يس",
                "english_name": "Ya-Sin",
                "verses": [
                    {"number": 1, "text": "يسٓ"},
                    {"number": 2, "text": "وَٱلْقُرْءَانِ ٱلْحَكِيمِ"},
                    {"number": 3, "text": "إِنَّكَ لَمِنَ ٱلْمُرْسَلِينَ"},
                    {"number": 4, "text": "عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ"},
                    {"number": 5, "text": "تَنزِيلَ ٱلْعَزِيزِ ٱلرَّحِيمِ"}
                ]
            },
            {
                "number": 55,
                "name": "الرحمن",
                "english_name": "Ar-Rahman",
                "verses": [
                    {"number": 1, "text": "ٱلرَّحْمَـٰنُ"},
                    {"number": 2, "text": "عَلَّمَ ٱلْقُرْءَانَ"},
                    {"number": 3, "text": "خَلَقَ ٱلْإِنسَـٰنَ"},
                    {"number": 4, "text": "عَلَّمَهُ ٱلْبَيَانَ"},
                    {"number": 5, "text": "ٱلشَّمْسُ وَٱلْقَمَرُ بِحُسْبَانٍ"}
                ]
            },
            {
                "number": 67,
                "name": "الملك",
                "english_name": "Al-Mulk",
                "verses": [
                    {"number": 1, "text": "تَبَـٰرَكَ ٱلَّذِى بِيَدِهِ ٱلْمُلْكُ وَهُوَ عَلَىٰ كُلِّ شَىْءٍ قَدِيرٌ"},
                    {"number": 2, "text": "ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًا"}
                ]
            },
            {
                "number": 112,
                "name": "الإخلاص",
                "english_name": "Al-Ikhlas",
                "verses": [
                    {"number": 1, "text": "قُلْ هُوَ ٱللَّهُ أَحَدٌ"},
                    {"number": 2, "text": "ٱللَّهُ ٱلصَّمَدُ"},
                    {"number": 3, "text": "لَمْ يَلِدْ وَلَمْ يُولَدْ"},
                    {"number": 4, "text": "وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ"}
                ]
            },
            {
                "number": 113,
                "name": "الفلق",
                "english_name": "Al-Falaq",
                "verses": [
                    {"number": 1, "text": "قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ"},
                    {"number": 2, "text": "مِن شَرِّ مَا خَلَقَ"},
                    {"number": 3, "text": "وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ"},
                    {"number": 4, "text": "وَمِن شَرِّ ٱلنَّفَّـٰثَـٰتِ فِى ٱلْعُقَدِ"},
                    {"number": 5, "text": "وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ"}
                ]
            },
            {
                "number": 114,
                "name": "الناس",
                "english_name": "An-Nas",
                "verses": [
                    {"number": 1, "text": "قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ"},
                    {"number": 2, "text": "مَلِكِ ٱلنَّاسِ"},
                    {"number": 3, "text": "إِلَـٰهِ ٱلنَّاسِ"},
                    {"number": 4, "text": "مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ"},
                    {"number": 5, "text": "ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ"},
                    {"number": 6, "text": "مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ"}
                ]
            }
        ]

        data_path = os.path.join(self.quran_data_dir, "quran.json")
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(default_surahs, f, ensure_ascii=False, indent=2)

        for surah in default_surahs:
            self.surahs[surah["number"]] = surah

    def _normalize_text(self, text: str) -> str:
        import re
        text = re.sub(r'[\u0610-\u061A]', '', text)
        text = re.sub(r'[\u06D6-\u06DC]', '', text)
        text = re.sub(r'[\u06DF-\u06E4]', '', text)
        text = re.sub(r'[\u06E7-\u06E8]', '', text)
        text = re.sub(r'[\u06EA-\u06ED]', '', text)
        text = re.sub(r'[\u0670]', '', text)
        text = re.sub(r'[\u064B-\u065F]', '', text)
        text = re.sub(r'[\u0617-\u061A]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def _calculate_similarity(self, text1: str, text2: str) -> float:
        norm1 = self._normalize_text(text1)
        norm2 = self._normalize_text(text2)
        return SequenceMatcher(None, norm1, norm2).ratio()

    def find_best_match(self, transcribed_text: str, threshold: float = 0.5) -> Optional[dict]:
        best_match = None
        best_score = 0

        for surah_num, surah in self.surahs.items():
            for verse in surah.get("verses", []):
                score = self._calculate_similarity(transcribed_text, verse["text"])
                if score > best_score and score >= threshold:
                    best_score = score
                    best_match = {
                        "surah_number": surah["number"],
                        "surah_name": surah["name"],
                        "surah_english_name": surah["english_name"],
                        "verse_number": verse["number"],
                        "verse_text": verse["text"],
                        "confidence": round(score, 3)
                    }

        return best_match

    def find_matches(self, transcribed_text: str, top_n: int = 3, threshold: float = 0.3) -> list:
        matches = []

        for surah_num, surah in self.surahs.items():
            for verse in surah.get("verses", []):
                score = self._calculate_similarity(transcribed_text, verse["text"])
                if score >= threshold:
                    matches.append({
                        "surah_number": surah["number"],
                        "surah_name": surah["name"],
                        "surah_english_name": surah["english_name"],
                        "verse_number": verse["number"],
                        "verse_text": verse["text"],
                        "confidence": round(score, 3)
                    })

        matches.sort(key=lambda x: x["confidence"], reverse=True)
        return matches[:top_n]
