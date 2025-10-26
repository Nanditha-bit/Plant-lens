import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  ActivityIndicator,
  Alert,
  Image,
  ScrollView,
  Platform,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import * as ImagePicker from 'expo-image-picker';
import { useRouter } from 'expo-router';
import api from '../../utils/api';

export default function ScanScreen() {
  const router = useRouter();
  const [image, setImage] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [hasPermission, setHasPermission] = useState(false);

  useEffect(() => {
    requestPermissions();
  }, []);

  const requestPermissions = async () => {
    try {
      const { status: cameraStatus } =
        await ImagePicker.requestCameraPermissionsAsync();
      const { status: galleryStatus } =
        await ImagePicker.requestMediaLibraryPermissionsAsync();

      if (cameraStatus === 'granted' && galleryStatus === 'granted') {
        setHasPermission(true);
      } else {
        Alert.alert(
          'Permission Required',
          'Camera and gallery access is needed to identify plants. Please enable permissions in your device settings.',
          [
            { text: 'Cancel', style: 'cancel' },
            { text: 'Open Settings', onPress: () => requestPermissions() }
          ]
        );
      }
    } catch (error) {
      console.error('Permission error:', error);
    }
  };

  const pickImageFromGallery = async () => {
    const hasPermission = await requestPermissions();
    if (!hasPermission) return;

    try {
      const result = await ImagePicker.launchImageLibraryAsync({
        mediaTypes: ImagePicker.MediaTypeOptions.Images,
        allowsEditing: true,
        aspect: [4, 3],
        quality: 0.8,
        base64: true,
      });

      if (!result.canceled && result.assets[0].base64) {
        setImage(result.assets[0].base64);
        setResult(null);
      }
    } catch (error) {
      Alert.alert('Error', 'Failed to pick image');
    }
  };

  const takePhoto = async () => {
    const hasPermission = await requestPermissions();
    if (!hasPermission) return;

    try {
      const result = await ImagePicker.launchCameraAsync({
        allowsEditing: true,
        aspect: [4, 3],
        quality: 0.8,
        base64: true,
      });

      if (!result.canceled && result.assets[0].base64) {
        setImage(result.assets[0].base64);
        setResult(null);
      }
    } catch (error) {
      Alert.alert('Error', 'Failed to take photo');
    }
  };

  const identifyPlant = async () => {
    if (!image) {
      Alert.alert('Error', 'Please select an image first');
      return;
    }

    try {
      setLoading(true);
      const response = await api.post('/api/plants/identify', {
        image_base64: image,
      });
      setResult(response.data);
    } catch (error: any) {
      Alert.alert(
        'Error',
        error.response?.data?.detail || 'Failed to identify plant'
      );
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setImage(null);
    setResult(null);
  };

  return (
    <SafeAreaView style={styles.container} edges={['bottom']}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {!image ? (
          <View style={styles.emptyState}>
            <Text style={styles.emptyIcon}>📸</Text>
            <Text style={styles.emptyTitle}>Identify a Plant</Text>
            <Text style={styles.emptyText}>
              Take a photo or select from gallery to identify the plant
            </Text>

            <TouchableOpacity style={styles.button} onPress={takePhoto}>
              <Text style={styles.buttonText}>📷 Take Photo</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[styles.button, styles.secondaryButton]}
              onPress={pickImageFromGallery}
            >
              <Text style={styles.buttonText}>🖼️ Choose from Gallery</Text>
            </TouchableOpacity>
          </View>
        ) : (
          <View style={styles.content}>
            <Image
              source={{ uri: `data:image/jpeg;base64,${image}` }}
              style={styles.previewImage}
            />

            {!result ? (
              <View style={styles.actions}>
                <TouchableOpacity
                  style={[styles.button, loading && styles.buttonDisabled]}
                  onPress={identifyPlant}
                  disabled={loading}
                >
                  {loading ? (
                    <ActivityIndicator color="#fff" />
                  ) : (
                    <Text style={styles.buttonText}>Identify Plant</Text>
                  )}
                </TouchableOpacity>

                <TouchableOpacity
                  style={[styles.button, styles.secondaryButton]}
                  onPress={reset}
                >
                  <Text style={styles.buttonText}>Choose Another Image</Text>
                </TouchableOpacity>
              </View>
            ) : (
              <View style={styles.resultContainer}>
                <View style={styles.resultHeader}>
                  <Text style={styles.resultTitle}>{result.plant_name}</Text>
                  {result.scientific_name && (
                    <Text style={styles.scientificName}>
                      {result.scientific_name}
                    </Text>
                  )}
                  <View style={styles.confidenceBadge}>
                    <Text style={styles.confidenceText}>
                      Confidence: {result.confidence}
                    </Text>
                  </View>
                </View>

                {result.full_description && (
                  <View style={styles.section}>
                    <Text style={styles.sectionTitle}>Description</Text>
                    <Text style={styles.sectionText}>
                      {result.full_description}
                    </Text>
                  </View>
                )}

                {result.characteristics && result.characteristics.length > 0 && (
                  <View style={styles.section}>
                    <Text style={styles.sectionTitle}>Characteristics</Text>
                    {result.characteristics.map((item: string, index: number) => (
                      <Text key={index} style={styles.bulletPoint}>
                        • {item}
                      </Text>
                    ))}
                  </View>
                )}

                {result.medicinal_properties &&
                  result.medicinal_properties.length > 0 && (
                    <View style={styles.section}>
                      <Text style={styles.sectionTitle}>Medicinal Properties</Text>
                      {result.medicinal_properties.map(
                        (item: string, index: number) => (
                          <Text key={index} style={styles.bulletPoint}>
                            • {item}
                          </Text>
                        )
                      )}
                    </View>
                  )}

                {result.uses && result.uses.length > 0 && (
                  <View style={styles.section}>
                    <Text style={styles.sectionTitle}>Uses</Text>
                    {result.uses.map((item: string, index: number) => (
                      <Text key={index} style={styles.bulletPoint}>
                        • {item}
                      </Text>
                    ))}
                  </View>
                )}

                {result.matches_database && result.database_plant_id && (
                  <TouchableOpacity
                    style={styles.viewDetailsButton}
                    onPress={() =>
                      router.push(`/plant/${result.database_plant_id}`)
                    }
                  >
                    <Text style={styles.viewDetailsText}>
                      View Full Details in Database
                    </Text>
                  </TouchableOpacity>
                )}

                <TouchableOpacity
                  style={[styles.button, styles.secondaryButton]}
                  onPress={reset}
                >
                  <Text style={styles.buttonText}>Scan Another Plant</Text>
                </TouchableOpacity>
              </View>
            )}
          </View>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  scrollContent: {
    flexGrow: 1,
  },
  emptyState: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  emptyIcon: {
    fontSize: 64,
    marginBottom: 16,
  },
  emptyTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#2E7D32',
    marginBottom: 8,
  },
  emptyText: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
    marginBottom: 32,
  },
  content: {
    padding: 16,
  },
  previewImage: {
    width: '100%',
    height: 300,
    borderRadius: 12,
    marginBottom: 16,
  },
  actions: {
    marginBottom: 16,
  },
  button: {
    backgroundColor: '#4CAF50',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
    marginBottom: 12,
    minHeight: 56,
    justifyContent: 'center',
  },
  secondaryButton: {
    backgroundColor: '#666',
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  resultContainer: {
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 16,
  },
  resultHeader: {
    marginBottom: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
    paddingBottom: 16,
  },
  resultTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#2E7D32',
    marginBottom: 8,
  },
  scientificName: {
    fontSize: 18,
    fontStyle: 'italic',
    color: '#666',
    marginBottom: 8,
  },
  confidenceBadge: {
    backgroundColor: '#e8f5e9',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
    alignSelf: 'flex-start',
  },
  confidenceText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#2E7D32',
  },
  section: {
    marginBottom: 16,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 8,
  },
  sectionText: {
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
  bulletPoint: {
    fontSize: 14,
    color: '#666',
    marginBottom: 4,
    marginLeft: 8,
  },
  viewDetailsButton: {
    backgroundColor: '#2196F3',
    borderRadius: 8,
    padding: 12,
    alignItems: 'center',
    marginVertical: 16,
  },
  viewDetailsText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});