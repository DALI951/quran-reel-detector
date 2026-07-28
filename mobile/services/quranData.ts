export interface Verse {
  number: number;
  text: string;
}

export interface Surah {
  number: number;
  name: string;
  englishName: string;
  verses: Verse[];
}

export const quranData: Surah[] = [
  {
    number: 1,
    name: "الفاتحة",
    englishName: "Al-Fatiha",
    verses: [
      { number: 1, text: "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ" },
      { number: 2, text: "ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَـٰلَمِينَ" },
      { number: 3, text: "ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ" },
      { number: 4, text: "مَـٰلِكِ يَوْمِ ٱلدِّينِ" },
      { number: 5, text: "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ" },
      { number: 6, text: "ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ" },
      { number: 7, text: "صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ" }
    ]
  },
  {
    number: 36,
    name: "يس",
    englishName: "Ya-Sin",
    verses: [
      { number: 1, text: "يسٓ" },
      { number: 2, text: "وَٱلْقُرْءَانِ ٱلْحَكِيمِ" },
      { number: 3, text: "إِنَّكَ لَمِنَ ٱلْمُرْسَلِينَ" },
      { number: 4, text: "عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ" },
      { number: 5, text: "تَنزِيلَ ٱلْعَزِيزِ ٱلرَّحِيمِ" }
    ]
  },
  {
    number: 55,
    name: "الرحمن",
    englishName: "Ar-Rahman",
    verses: [
      { number: 1, text: "ٱلرَّحْمَـٰنُ" },
      { number: 2, text: "عَلَّمَ ٱلْقُرْءَانَ" },
      { number: 3, text: "خَلَقَ ٱلْإِنسَـٰنَ" },
      { number: 4, text: "عَلَّمَهُ ٱلْبَيَانَ" },
      { number: 5, text: "ٱلشَّمْسُ وَٱلْقَمَرُ بِحُسْبَانٍ" }
    ]
  },
  {
    number: 67,
    name: "الملك",
    englishName: "Al-Mulk",
    verses: [
      { number: 1, text: "تَبَـٰرَكَ ٱلَّذِى بِيَدِهِ ٱلْمُلْكُ وَهُوَ عَلَىٰ كُلِّ شَىْءٍ قَدِيرٌ" },
      { number: 2, text: "ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًا" }
    ]
  },
  {
    number: 112,
    name: "الإخلاص",
    englishName: "Al-Ikhlas",
    verses: [
      { number: 1, text: "قُلْ هُوَ ٱللَّهُ أَحَدٌ" },
      { number: 2, text: "ٱللَّهُ ٱلصَّمَدُ" },
      { number: 3, text: "لَمْ يَلِدْ وَلَمْ يُولَدْ" },
      { number: 4, text: "وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ" }
    ]
  },
  {
    number: 113,
    name: "الفلق",
    englishName: "Al-Falaq",
    verses: [
      { number: 1, text: "قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ" },
      { number: 2, text: "مِن شَرِّ مَا خَلَقَ" },
      { number: 3, text: "وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ" },
      { number: 4, text: "وَمِن شَرِّ ٱلنَّفَّـٰثَـٰتِ فِى ٱلْعُقَدِ" },
      { number: 5, text: "وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ" }
    ]
  },
  {
    number: 114,
    name: "الناس",
    englishName: "An-Nas",
    verses: [
      { number: 1, text: "قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ" },
      { number: 2, text: "مَلِكِ ٱلنَّاسِ" },
      { number: 3, text: "إِلَـٰهِ ٱلنَّاسِ" },
      { number: 4, text: "مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ" },
      { number: 5, text: "ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ" },
      { number: 6, text: "مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ" }
    ]
  }
];

const normalizeText = (text: string): string => {
  return text
    .replace(/[\u0610-\u061A]/g, '')
    .replace(/[\u06D6-\u06DC]/g, '')
    .replace(/[\u06DF-\u06E4]/g, '')
    .replace(/[\u06E7-\u06E8]/g, '')
    .replace(/[\u06EA-\u06ED]/g, '')
    .replace(/[\u0670]/g, '')
    .replace(/[\u064B-\u065F]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
};

const calculateSimilarity = (text1: string, text2: string): number => {
  const norm1 = normalizeText(text1);
  const norm2 = normalizeText(text2);

  if (norm1 === norm2) return 1;

  const longer = norm1.length > norm2.length ? norm1 : norm2;
  const shorter = norm1.length > norm2.length ? norm2 : norm1;

  if (longer.length === 0) return 1;

  const editDistance = levenshteinDistance(longer, shorter);
  return (longer.length - editDistance) / longer.length;
};

const levenshteinDistance = (s1: string, s2: string): number => {
  const m = s1.length;
  const n = s2.length;
  const dp: number[][] = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));

  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        dp[i][j] = Math.min(
          dp[i - 1][j] + 1,
          dp[i][j - 1] + 1,
          dp[i - 1][j - 1] + 1
        );
      }
    }
  }

  return dp[m][n];
};

export const findBestMatch = (transcribedText: string, threshold: number = 0.5) => {
  let bestMatch = null;
  let bestScore = 0;

  for (const surah of quranData) {
    for (const verse of surah.verses) {
      const score = calculateSimilarity(transcribedText, verse.text);
      if (score > bestScore && score >= threshold) {
        bestScore = score;
        bestMatch = {
          surahNumber: surah.number,
          surahName: surah.name,
          surahEnglishName: surah.englishName,
          verseNumber: verse.number,
          verseText: verse.text,
          confidence: Math.round(score * 1000) / 1000,
        };
      }
    }
  }

  return bestMatch;
};
