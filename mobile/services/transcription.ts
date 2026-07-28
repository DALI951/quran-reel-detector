import axios from 'axios';

const HUGGINGFACE_API_URL = 'https://api-inference.huggingface.co/models/tarteel-ai/whisper-base-ar-quran';
const HUGGINGFACE_API_KEY = ''; // Add your free key from huggingface.co/settings/tokens

export const transcribeAudio = async (audioBlob: Blob): Promise<string> => {
  try {
    const response = await axios.post(HUGGINGFACE_API_URL, audioBlob, {
      headers: {
        'Authorization': `Bearer ${HUGGINGFACE_API_KEY}`,
        'Content-Type': 'audio/wav',
      },
      timeout: 60000,
    });

    return response.data.text || '';
  } catch (error) {
    console.error('Transcription error:', error);
    throw new Error('Failed to transcribe audio');
  }
};
