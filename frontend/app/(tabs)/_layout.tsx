import { Tabs } from 'expo-router';
import React from 'react';
import { Platform } from 'react-native';

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: '#4CAF50',
        tabBarInactiveTintColor: '#999',
        headerShown: true,
        headerStyle: {
          backgroundColor: '#4CAF50',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
        tabBarStyle: {
          height: Platform.OS === 'ios' ? 88 : 64,
          paddingBottom: Platform.OS === 'ios' ? 24 : 8,
          paddingTop: 8,
        },
      }}
    >
      <Tabs.Screen
        name="home"
        options={{
          title: 'Plants',
          tabBarLabel: 'Plants',
          tabBarIcon: ({ color, size }) => (
            <Text style={{ fontSize: 24, color }}>🌿</Text>
          ),
        }}
      />
      <Tabs.Screen
        name="scan"
        options={{
          title: 'Identify Plant',
          tabBarLabel: 'Scan',
          tabBarIcon: ({ color, size }) => (
            <Text style={{ fontSize: 24, color }}>📷</Text>
          ),
        }}
      />
      <Tabs.Screen
        name="history"
        options={{
          title: 'Scan History',
          tabBarLabel: 'History',
          tabBarIcon: ({ color, size }) => (
            <Text style={{ fontSize: 24, color }}>📜</Text>
          ),
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          title: 'Profile',
          tabBarLabel: 'Profile',
          tabBarIcon: ({ color, size }) => (
            <Text style={{ fontSize: 24, color }}>👤</Text>
          ),
        }}
      />
    </Tabs>
  );
}