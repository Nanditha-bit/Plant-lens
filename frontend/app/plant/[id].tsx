import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  ActivityIndicator,
  Alert,
  Image,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useLocalSearchParams, Stack } from 'expo-router';
import api from '../../utils/api';

interface PlantDetails {
  _id: string;
  name: string;
  scientific_name: string;
  family: string;
  description: string;
  characteristics: string[];
  medicinal_properties: string[];
  uses: string[];
  parts_used: string[];
  images_base64: string[];
}

export default function PlantDetailsScreen() {
  const { id } = useLocalSearchParams();
  const [plant, setPlant] = useState<PlantDetails | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (id) {
      fetchPlantDetails();
    }
  }, [id]);

  const fetchPlantDetails = async () => {
    try {
      setLoading(true);
      const response = await api.get(`/api/plants/${id}`);
      setPlant(response.data);
    } catch (error: any) {
      Alert.alert('Error', 'Failed to load plant details');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <SafeAreaView style={styles.container}>
        <Stack.Screen options={{ title: 'Loading...' }} />
        <View style={styles.centerContainer}>
          <ActivityIndicator size="large" color="#4CAF50" />
        </View>
      </SafeAreaView>
    );
  }

  if (!plant) {
    return (
      <SafeAreaView style={styles.container}>
        <Stack.Screen options={{ title: 'Not Found' }} />
        <View style={styles.centerContainer}>
          <Text style={styles.errorText}>Plant not found</Text>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container} edges={['bottom']}>
      <Stack.Screen 
        options={{ 
          title: plant.name,
          headerStyle: { backgroundColor: '#4CAF50' },
          headerTintColor: '#fff',
        }} 
      />
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {plant.images_base64 && plant.images_base64.length > 0 ? (
          <ScrollView
            horizontal
            pagingEnabled
            showsHorizontalScrollIndicator
            style={styles.imageScroll}
          >
            {plant.images_base64.map((image, index) => (
              <Image
                key={index}
                source={{ uri: `data:image/jpeg;base64,${image}` }}
                style={styles.plantImage}
              />
            ))}
          </ScrollView>
        ) : (
          <View style={[styles.plantImage, styles.placeholderImage]}>
            <Text style={styles.placeholderText}>🌿</Text>
          </View>
        )}

        <View style={styles.content}>
          <Text style={styles.plantName}>{plant.name}</Text>
          <Text style={styles.scientificName}>{plant.scientific_name}</Text>
          <Text style={styles.family}>Family: {plant.family}</Text>

          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Description</Text>
            <Text style={styles.text}>{plant.description}</Text>
          </View>

          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Characteristics</Text>
            {plant.characteristics.map((item, index) => (
              <Text key={index} style={styles.bulletPoint}>
                • {item}
              </Text>
            ))}
          </View>

          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Medicinal Properties</Text>
            {plant.medicinal_properties.map((item, index) => (
              <Text key={index} style={styles.bulletPoint}>
                • {item}
              </Text>
            ))}
          </View>

          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Uses</Text>
            {plant.uses.map((item, index) => (
              <Text key={index} style={styles.bulletPoint}>
                • {item}
              </Text>
            ))}
          </View>

          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Parts Used</Text>
            <Text style={styles.text}>{plant.parts_used.join(', ')}</Text>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  errorText: {
    fontSize: 18,
    color: '#999',
  },
  scrollContent: {
    paddingBottom: 24,
  },
  imageScroll: {
    height: 300,
  },
  plantImage: {
    width: undefined,
    aspectRatio: 1.5,
    height: 300,
    backgroundColor: '#e8f5e9',
  },
  placeholderImage: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  placeholderText: {
    fontSize: 80,
  },
  content: {
    padding: 16,
  },
  plantName: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#2E7D32',
    marginBottom: 8,
  },
  scientificName: {
    fontSize: 20,
    fontStyle: 'italic',
    color: '#666',
    marginBottom: 4,
  },
  family: {
    fontSize: 16,
    color: '#999',
    marginBottom: 24,
  },
  section: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 12,
  },
  text: {
    fontSize: 16,
    color: '#666',
    lineHeight: 24,
  },
  bulletPoint: {
    fontSize: 16,
    color: '#666',
    marginBottom: 8,
    marginLeft: 8,
    lineHeight: 24,
  },
});