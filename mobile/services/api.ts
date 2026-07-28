import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface DetectionResult {
  surah_number: number;
  surah_name: string;
  surah_english_name: string;
  verse_number: number;
  verse_text: string;
  confidence: number;
  transcription: string;
}

export const detectQuran = async (url: string): Promise<DetectionResult> => {
  try {
    const response = await api.post<DetectionResult>('/detect', { url });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.response?.status === 404) {
        throw new Error('Could not match transcription to any Quran verse');
      }
      throw new Error(error.response?.data?.detail || 'Failed to detect Quran');
    }
    throw error;
  }
};

export const checkHealth = async (): Promise<boolean> => {
  try {
    const response = await api.get('/health');
    return response.data.status === 'healthy';
  } catch {
    return false;
  }
};

export default api;
