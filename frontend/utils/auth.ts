import AsyncStorage from '@react-native-async-storage/async-storage';
import api from './api';

export const login = async (username: string, password: string) => {
  try {
    const response = await api.post('/api/auth/login', { username, password });
    const { access_token, username: user } = response.data;
    await AsyncStorage.setItem('auth_token', access_token);
    await AsyncStorage.setItem('username', user);
    return { success: true, user };
  } catch (error: any) {
    return { success: false, error: error.response?.data?.detail || 'Login failed' };
  }
};

export const register = async (username: string, password: string) => {
  try {
    const response = await api.post('/api/auth/register', { username, password });
    const { access_token, username: user } = response.data;
    await AsyncStorage.setItem('auth_token', access_token);
    await AsyncStorage.setItem('username', user);
    return { success: true, user };
  } catch (error: any) {
    return { success: false, error: error.response?.data?.detail || 'Registration failed' };
  }
};

export const logout = async () => {
  await AsyncStorage.removeItem('auth_token');
  await AsyncStorage.removeItem('username');
};

export const isAuthenticated = async () => {
  const token = await AsyncStorage.getItem('auth_token');
  return !!token;
};

export const getUsername = async () => {
  return await AsyncStorage.getItem('username');
};