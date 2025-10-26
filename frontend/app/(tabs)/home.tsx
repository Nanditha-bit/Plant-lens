import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  ActivityIndicator,
  Alert,
  Image,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import api from '../../utils/api';

interface Plant {
  _id: string;
  name: string;
  scientific_name: string;
  family: string;
  description: string;
  thumbnail?: string;
}

export default function HomeScreen() {
  const router = useRouter();
  const [plants, setPlants] = useState<Plant[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    fetchPlants();
  }, []);

  const fetchPlants = async (search?: string) => {
    try {
      setLoading(true);
      const params = search ? { search, limit: 50 } : { limit: 50 };
      const response = await api.get('/api/plants', { params });
      setPlants(response.data.plants);
    } catch (error: any) {
      Alert.alert('Error', 'Failed to load plants');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const handleSearch = () => {
    if (searchQuery.trim()) {
      fetchPlants(searchQuery);
    } else {
      fetchPlants();
    }
  };

  const handleRefresh = () => {
    setRefreshing(true);
    setSearchQuery('');
    fetchPlants();
  };

  const renderPlantItem = ({ item }: { item: Plant }) => (
    <TouchableOpacity
      style={styles.plantCard}
      onPress={() => router.push(`/plant/${item._id}`)}
    >
      {item.thumbnail ? (
        <Image
          source={{ uri: `data:image/jpeg;base64,${item.thumbnail}` }}
          style={styles.plantImage}
        />
      ) : (
        <View style={[styles.plantImage, styles.placeholderImage]}>
          <Text style={styles.placeholderText}>🌿</Text>
        </View>
      )}
      <View style={styles.plantInfo}>
        <Text style={styles.plantName}>{item.name}</Text>
        <Text style={styles.scientificName}>{item.scientific_name}</Text>
        <Text style={styles.family}>{item.family}</Text>
        <Text style={styles.description} numberOfLines={2}>
          {item.description}
        </Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <SafeAreaView style={styles.container} edges={['bottom']}>
      <View style={styles.searchContainer}>
        <TextInput
          style={styles.searchInput}
          placeholder="Search plants..."
          value={searchQuery}
          onChangeText={setSearchQuery}
          onSubmitEditing={handleSearch}
          returnKeyType="search"
        />
        <TouchableOpacity style={styles.searchButton} onPress={handleSearch}>
          <Text style={styles.searchButtonText}>🔍</Text>
        </TouchableOpacity>
      </View>

      {loading ? (
        <View style={styles.centerContainer}>
          <ActivityIndicator size="large" color="#4CAF50" />
        </View>
      ) : plants.length === 0 ? (
        <View style={styles.centerContainer}>
          <Text style={styles.emptyText}>No plants found</Text>
          {searchQuery && (
            <TouchableOpacity style={styles.clearButton} onPress={handleRefresh}>
              <Text style={styles.clearButtonText}>Clear Search</Text>
            </TouchableOpacity>
          )}
        </View>
      ) : (
        <FlatList
          data={plants}
          renderItem={renderPlantItem}
          keyExtractor={(item) => item._id}
          contentContainerStyle={styles.listContent}
          refreshing={refreshing}
          onRefresh={handleRefresh}
        />
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  searchContainer: {
    flexDirection: 'row',
    padding: 16,
    backgroundColor: '#fff',
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
  },
  searchInput: {
    flex: 1,
    backgroundColor: '#f5f5f5',
    borderRadius: 12,
    padding: 12,
    fontSize: 16,
    marginRight: 8,
  },
  searchButton: {
    backgroundColor: '#4CAF50',
    borderRadius: 12,
    width: 48,
    justifyContent: 'center',
    alignItems: 'center',
  },
  searchButtonText: {
    fontSize: 20,
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  emptyText: {
    fontSize: 18,
    color: '#999',
  },
  clearButton: {
    marginTop: 16,
    padding: 12,
    backgroundColor: '#4CAF50',
    borderRadius: 8,
  },
  clearButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  listContent: {
    padding: 16,
  },
  plantCard: {
    backgroundColor: '#fff',
    borderRadius: 12,
    marginBottom: 16,
    overflow: 'hidden',
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  plantImage: {
    width: '100%',
    height: 200,
    backgroundColor: '#e8f5e9',
  },
  placeholderImage: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  placeholderText: {
    fontSize: 64,
  },
  plantInfo: {
    padding: 16,
  },
  plantName: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#2E7D32',
    marginBottom: 4,
  },
  scientificName: {
    fontSize: 16,
    fontStyle: 'italic',
    color: '#666',
    marginBottom: 4,
  },
  family: {
    fontSize: 14,
    color: '#999',
    marginBottom: 8,
  },
  description: {
    fontSize: 14,
    color: '#333',
    lineHeight: 20,
  },
});