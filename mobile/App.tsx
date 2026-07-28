import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  ScrollView,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { detectQuran, DetectionResult } from './services/api';

export default function App() {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<DetectionResult | null>(null);

  const handleDetect = async () => {
    if (!url.trim()) {
      Alert.alert('Error', 'Please enter a reel URL');
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const detectionResult = await detectQuran(url);
      setResult(detectionResult);
    } catch (error) {
      Alert.alert('Error', error instanceof Error ? error.message : 'Failed to detect Quran');
    } finally {
      setLoading(false);
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.header}>
          <Text style={styles.title}>Quran Reel Detector</Text>
          <Text style={styles.subtitle}>Detect Quran from Instagram, TikTok, or YouTube reels</Text>
        </View>

        <View style={styles.inputContainer}>
          <TextInput
            style={styles.input}
            placeholder="Paste reel URL here..."
            placeholderTextColor="#888"
            value={url}
            onChangeText={setUrl}
            autoCapitalize="none"
            autoCorrect={false}
          />
          <TouchableOpacity
            style={[styles.button, loading && styles.buttonDisabled]}
            onPress={handleDetect}
            disabled={loading}
          >
            {loading ? (
              <ActivityIndicator color="#fff" />
            ) : (
              <Text style={styles.buttonText}>Detect</Text>
            )}
          </TouchableOpacity>
        </View>

        {result && (
          <View style={styles.resultCard}>
            <View style={styles.resultHeader}>
              <Text style={styles.surahName}>{result.surah_name}</Text>
              <Text style={styles.surahEnglish}>{result.surah_english_name}</Text>
              <Text style={styles.verseNumber}>Verse {result.verse_number}</Text>
            </View>

            <View style={styles.verseContainer}>
              <Text style={styles.verseText}>{result.verse_text}</Text>
            </View>

            <View style={styles.infoContainer}>
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>Confidence:</Text>
                <Text style={styles.infoValue}>{(result.confidence * 100).toFixed(1)}%</Text>
              </View>
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>Surah Number:</Text>
                <Text style={styles.infoValue}>{result.surah_number}</Text>
              </View>
            </View>

            <View style={styles.transcriptionContainer}>
              <Text style={styles.transcriptionLabel}>Transcription:</Text>
              <Text style={styles.transcriptionText}>{result.transcription}</Text>
            </View>
          </View>
        )}

        <View style={styles.footer}>
          <Text style={styles.footerText}>
            Supports Instagram, TikTok, and YouTube reels
          </Text>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1a1a2e',
  },
  scrollContent: {
    flexGrow: 1,
    padding: 20,
  },
  header: {
    alignItems: 'center',
    marginTop: 60,
    marginBottom: 40,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 14,
    color: '#888',
    textAlign: 'center',
  },
  inputContainer: {
    marginBottom: 30,
  },
  input: {
    backgroundColor: '#16213e',
    borderRadius: 12,
    padding: 16,
    fontSize: 16,
    color: '#fff',
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#0f3460',
  },
  button: {
    backgroundColor: '#e94560',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
  },
  buttonDisabled: {
    backgroundColor: '#888',
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '600',
  },
  resultCard: {
    backgroundColor: '#16213e',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
  },
  resultHeader: {
    alignItems: 'center',
    marginBottom: 20,
  },
  surahName: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 4,
  },
  surahEnglish: {
    fontSize: 16,
    color: '#888',
    marginBottom: 8,
  },
  verseNumber: {
    fontSize: 14,
    color: '#e94560',
    fontWeight: '600',
  },
  verseContainer: {
    backgroundColor: '#1a1a2e',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
  },
  verseText: {
    fontSize: 20,
    color: '#fff',
    textAlign: 'right',
    lineHeight: 36,
  },
  infoContainer: {
    marginBottom: 16,
  },
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  infoLabel: {
    fontSize: 14,
    color: '#888',
  },
  infoValue: {
    fontSize: 14,
    color: '#fff',
    fontWeight: '600',
  },
  transcriptionContainer: {
    backgroundColor: '#1a1a2e',
    borderRadius: 8,
    padding: 12,
  },
  transcriptionLabel: {
    fontSize: 12,
    color: '#888',
    marginBottom: 4,
  },
  transcriptionText: {
    fontSize: 14,
    color: '#ccc',
  },
  footer: {
    alignItems: 'center',
    marginTop: 20,
    paddingBottom: 40,
  },
  footerText: {
    fontSize: 12,
    color: '#666',
  },
});
