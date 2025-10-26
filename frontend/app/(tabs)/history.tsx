import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
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

interface Scan {
  _id: string;
  identified_plant_name: string;
  confidence: string;
  timestamp: string;
  scanned_image_base64: string;
}

export default function HistoryScreen() {
  const router = useRouter();
  const [scans, setScans] = useState<Scan[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      setLoading(true);
      const response = await api.get('/api/scans/history');
      setScans(response.data.scans);
    } catch (error: any) {
      Alert.alert('Error', 'Failed to load scan history');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const handleRefresh = () => {
    setRefreshing(true);
    fetchHistory();
  };

  const formatDate = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
  };

  const renderScanItem = ({ item }: { item: Scan }) => (
    <View style={styles.scanCard}>
      <Image
        source={{ uri: `data:image/jpeg;base64,${item.scanned_image_base64}` }}
        style={styles.scanImage}
      />
      <View style={styles.scanInfo}>
        <Text style={styles.plantName}>{item.identified_plant_name}</Text>
        <View style={styles.confidenceBadge}>
          <Text style={styles.confidenceText}>Confidence: {item.confidence}</Text>
        </View>
        <Text style={styles.timestamp}>
          {item.timestamp ? formatDate(item.timestamp) : 'Recently scanned'}
        </Text>
      </View>
    </View>
  );

  return (
    <SafeAreaView style={styles.container} edges={['bottom']}>
      {loading ? (
        <View style={styles.centerContainer}>
          <ActivityIndicator size="large" color="#4CAF50" />
        </View>
      ) : scans.length === 0 ? (
        <View style={styles.centerContainer}>
          <Text style={styles.emptyIcon}>📜</Text>
          <Text style={styles.emptyText}>No scan history yet</Text>
          <Text style={styles.emptySubtext}>
            Start identifying plants to see your history here
          </Text>
          <TouchableOpacity
            style={styles.scanButton}
            onPress={() => router.push('/(tabs)/scan')}
          >
            <Text style={styles.scanButtonText}>Scan a Plant</Text>
          </TouchableOpacity>
        </View>
      ) : (
        <FlatList
          data={scans}
          renderItem={renderScanItem}
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
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  emptyIcon: {
    fontSize: 64,
    marginBottom: 16,
  },
  emptyText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 8,
  },
  emptySubtext: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
    marginBottom: 24,
  },
  scanButton: {
    backgroundColor: '#4CAF50',
    borderRadius: 12,
    paddingVertical: 12,
    paddingHorizontal: 24,
  },
  scanButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  listContent: {
    padding: 16,
  },
  scanCard: {
    backgroundColor: '#fff',
    borderRadius: 12,
    marginBottom: 16,
    flexDirection: 'row',
    overflow: 'hidden',
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  scanImage: {
    width: 120,
    height: 120,
    backgroundColor: '#e8f5e9',
  },
  scanInfo: {
    flex: 1,
    padding: 12,
    justifyContent: 'space-between',
  },
  plantName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#2E7D32',
    marginBottom: 8,
  },
  confidenceBadge: {
    backgroundColor: '#e8f5e9',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 12,
    alignSelf: 'flex-start',
    marginBottom: 4,
  },
  confidenceText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#2E7D32',
  },
  timestamp: {
    fontSize: 12,
    color: '#999',
  },
});