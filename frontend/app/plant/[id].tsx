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
          {plant.sanskrit_name && (
            <Text style={styles.sanskritName}>{plant.sanskrit_name}</Text>
          )}
          <Text style={styles.scientificName}>{plant.scientific_name}</Text>
          <Text style={styles.family}>Family: {plant.family}</Text>

          {/* Vernacular Names */}
          {plant.vernacular_names && Object.keys(plant.vernacular_names).length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>📍 Vernacular Names</Text>
              {Object.entries(plant.vernacular_names).map(([lang, name], index) => (
                <Text key={index} style={styles.text}>
                  <Text style={styles.bold}>{lang}:</Text> {name as string}
                </Text>
              ))}
            </View>
          )}

          {/* Synonyms */}
          {plant.synonyms && plant.synonyms.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🏷️ Sanskrit Synonyms</Text>
              {plant.synonyms.map((syn: any, index: number) => (
                <View key={index} style={styles.synonymItem}>
                  <Text style={styles.boldText}>{syn.name}</Text>
                  <Text style={styles.text}>{syn.reason}</Text>
                </View>
              ))}
            </View>
          )}

          {/* Gana Classification */}
          {plant.gana && plant.gana.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>📚 Classification (Gana)</Text>
              {plant.gana.map((g: any, index: number) => (
                <Text key={index} style={styles.bulletPoint}>
                  • <Text style={styles.bold}>{g.author}:</Text> {g.gana}
                </Text>
              ))}
            </View>
          )}

          {/* Types */}
          {plant.types && plant.types.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🌿 Types/Varieties</Text>
              {plant.types.map((type: string, index: number) => (
                <Text key={index} style={styles.bulletPoint}>
                  • {type}
                </Text>
              ))}
            </View>
          )}

          {/* Morphology */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>🔬 Morphology</Text>
            {plant.habit && <Text style={styles.text}><Text style={styles.bold}>Habit:</Text> {plant.habit}</Text>}
            {plant.habitat && <Text style={styles.text}><Text style={styles.bold}>Habitat:</Text> {plant.habitat}</Text>}
            {plant.morphology && plant.morphology.root && (
              <Text style={styles.text}><Text style={styles.bold}>Root:</Text> {plant.morphology.root}</Text>
            )}
            {plant.morphology && plant.morphology.stem && (
              <Text style={styles.text}><Text style={styles.bold}>Stem:</Text> {plant.morphology.stem}</Text>
            )}
            {plant.morphology && plant.morphology.leaf && (
              <Text style={styles.text}><Text style={styles.bold}>Leaf:</Text> {plant.morphology.leaf}</Text>
            )}
            {plant.morphology && plant.morphology.flower && (
              <Text style={styles.text}><Text style={styles.bold}>Flower:</Text> {plant.morphology.flower}</Text>
            )}
            {plant.morphology && plant.morphology.inflorescence && (
              <Text style={styles.text}><Text style={styles.bold}>Inflorescence:</Text> {plant.morphology.inflorescence}</Text>
            )}
            {plant.morphology && plant.morphology.fruit && (
              <Text style={styles.text}><Text style={styles.bold}>Fruit:</Text> {plant.morphology.fruit}</Text>
            )}
            {plant.morphology && plant.morphology.seeds && (
              <Text style={styles.text}><Text style={styles.bold}>Seeds:</Text> {plant.morphology.seeds}</Text>
            )}
          </View>

          <View style={styles.section}>
            <Text style={styles.sectionTitle}>📖 Description</Text>
            <Text style={styles.text}>{plant.description}</Text>
          </View>

          {/* Rasapanchaka - Ayurvedic Properties */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>⚗️ Rasapanchaka (Ayurvedic Properties)</Text>
            {plant.rasa && plant.rasa.length > 0 && (
              <Text style={styles.text}><Text style={styles.bold}>Rasa (Taste):</Text> {plant.rasa.join(', ')}</Text>
            )}
            {plant.guna && plant.guna.length > 0 && (
              <Text style={styles.text}><Text style={styles.bold}>Guna (Quality):</Text> {plant.guna.join(', ')}</Text>
            )}
            {plant.virya && (
              <Text style={styles.text}><Text style={styles.bold}>Virya (Potency):</Text> {plant.virya}</Text>
            )}
            {plant.vipaka && (
              <Text style={styles.text}><Text style={styles.bold}>Vipaka (Post-digestive):</Text> {plant.vipaka}</Text>
            )}
            {plant.prabhava && (
              <Text style={styles.text}><Text style={styles.bold}>Prabhava (Special action):</Text> {plant.prabhava}</Text>
            )}
          </View>

          {/* Dosha Karma */}
          {plant.dosha_karma && Object.keys(plant.dosha_karma).length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>⚖️ Dosha Karma (Effect on Doshas)</Text>
              {Object.entries(plant.dosha_karma).map(([dosha, effect], index) => (
                <Text key={index} style={styles.bulletPoint}>
                  • <Text style={styles.bold}>{dosha}:</Text> {effect as string}
                </Text>
              ))}
            </View>
          )}

          {/* Karma (Actions) */}
          {plant.karma && plant.karma.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>💊 Karma (Pharmacological Actions)</Text>
              <Text style={styles.text}>{plant.karma.join(', ')}</Text>
            </View>
          )}

          {/* Indications */}
          {plant.indication && plant.indication.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🎯 Indications</Text>
              {plant.indication.map((ind: string, index: number) => (
                <Text key={index} style={styles.bulletPoint}>
                  • {ind}
                </Text>
              ))}
            </View>
          )}

          {/* Medicinal Properties */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>💚 Medicinal Properties</Text>
            {plant.medicinal_properties.map((item: string, index: number) => (
              <Text key={index} style={styles.bulletPoint}>
                • {item}
              </Text>
            ))}
          </View>

          {/* Therapeutic Uses */}
          {plant.therapeutic_uses && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🏥 Therapeutic Uses</Text>
              {plant.therapeutic_uses.internal && plant.therapeutic_uses.internal.length > 0 && (
                <View>
                  <Text style={styles.subTitle}>Internal:</Text>
                  {plant.therapeutic_uses.internal.map((use: string, index: number) => (
                    <Text key={index} style={styles.bulletPoint}>
                      • {use}
                    </Text>
                  ))}
                </View>
              )}
              {plant.therapeutic_uses.external && plant.therapeutic_uses.external.length > 0 && (
                <View style={{marginTop: 8}}>
                  <Text style={styles.subTitle}>External:</Text>
                  {plant.therapeutic_uses.external.map((use: string, index: number) => (
                    <Text key={index} style={styles.bulletPoint}>
                      • {use}
                    </Text>
                  ))}
                </View>
              )}
            </View>
          )}

          {/* Parts Used & Dosage */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>📏 Parts Used & Dosage</Text>
            <Text style={styles.text}><Text style={styles.bold}>Parts:</Text> {plant.parts_used.join(', ')}</Text>
            {plant.dosage && Object.keys(plant.dosage).length > 0 && (
              <View style={{marginTop: 8}}>
                <Text style={styles.bold}>Dosage:</Text>
                {Object.entries(plant.dosage).map(([form, dose], index) => (
                  <Text key={index} style={styles.text}>
                    • {form}: {dose as string}
                  </Text>
                ))}
              </View>
            )}
          </View>

          {/* Chemical Constituents */}
          {plant.chemical_constituents && plant.chemical_constituents.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🧪 Chemical Constituents</Text>
              {plant.chemical_constituents.map((chem: string, index: number) => (
                <Text key={index} style={styles.bulletPoint}>
                  • {chem}
                </Text>
              ))}
            </View>
          )}

          {/* Modern Pharmacology */}
          {plant.modern_pharmacology && plant.modern_pharmacology.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🔬 Modern Pharmacology</Text>
              {plant.modern_pharmacology.map((pharm: string, index: number) => (
                <Text key={index} style={styles.bulletPoint}>
                  • {pharm}
                </Text>
              ))}
            </View>
          )}

          {/* Formulations */}
          {plant.formulations && plant.formulations.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>💊 Formulations</Text>
              <Text style={styles.text}>{plant.formulations.join(', ')}</Text>
            </View>
          )}

          {/* Shodana */}
          {plant.shodana && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>⚗️ Shodana (Purification)</Text>
              <Text style={styles.text}>{plant.shodana}</Text>
            </View>
          )}

          {/* Research Updates */}
          {plant.research_updates && plant.research_updates.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🔍 Research Updates</Text>
              {plant.research_updates.map((research: string, index: number) => (
                <Text key={index} style={styles.bulletPoint}>
                  • {research}
                </Text>
              ))}
            </View>
          )}

          {/* Contraindications */}
          {plant.contraindications && plant.contraindications.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>⚠️ Contraindications</Text>
              {plant.contraindications.map((contra: string, index: number) => (
                <Text key={index} style={styles.bulletPoint}>
                  • {contra}
                </Text>
              ))}
            </View>
          )}

          {/* Adulterants */}
          {plant.adulterants && plant.adulterants.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>❌ Adulterants</Text>
              {plant.adulterants.map((adult: string, index: number) => (
                <Text key={index} style={styles.bulletPoint}>
                  • {adult}
                </Text>
              ))}
            </View>
          )}

          {/* References */}
          {plant.references && plant.references.length > 0 && (
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>📚 References</Text>
              {plant.references.map((ref: any, index: number) => (
                <View key={index} style={styles.referenceItem}>
                  <Text style={styles.verse}>{ref.verse}</Text>
                  <Text style={styles.text}>{ref.text}</Text>
                  <Text style={styles.refSource}>- {ref.source}</Text>
                </View>
              ))}
            </View>
          )}
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
    marginBottom: 4,
  },
  sanskritName: {
    fontSize: 20,
    fontStyle: 'italic',
    color: '#FF6F00',
    marginBottom: 8,
  },
  scientificName: {
    fontSize: 18,
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
    backgroundColor: '#f9f9f9',
    padding: 16,
    borderRadius: 12,
    borderLeftWidth: 4,
    borderLeftColor: '#4CAF50',
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#2E7D32',
    marginBottom: 12,
  },
  subTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
    marginBottom: 8,
    marginTop: 4,
  },
  text: {
    fontSize: 15,
    color: '#444',
    lineHeight: 24,
    marginBottom: 6,
  },
  bold: {
    fontWeight: '600',
    color: '#2E7D32',
  },
  boldText: {
    fontSize: 15,
    fontWeight: 'bold',
    color: '#2E7D32',
    marginBottom: 4,
  },
  bulletPoint: {
    fontSize: 15,
    color: '#444',
    marginBottom: 8,
    marginLeft: 8,
    lineHeight: 24,
  },
  synonymItem: {
    marginBottom: 12,
    paddingBottom: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  referenceItem: {
    marginBottom: 16,
    padding: 12,
    backgroundColor: '#fff',
    borderRadius: 8,
  },
  verse: {
    fontSize: 15,
    fontStyle: 'italic',
    color: '#FF6F00',
    marginBottom: 8,
    lineHeight: 22,
  },
  refSource: {
    fontSize: 14,
    fontWeight: '600',
    color: '#666',
    marginTop: 4,
  },
});