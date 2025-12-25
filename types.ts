export enum Page {
  DASHBOARD = 'dashboard',
  CROP_PREDICTION = 'crop_prediction',
  SOIL_ANALYSIS = 'soil_analysis',
  WEATHER = 'weather',
  PRICE_FORECAST = 'price_forecast',
  OPTIMIZATION = 'optimization',
  HISTORY = 'history',
  LOGIN = 'login'
}

export interface User {
  id: number;
  name: string;
  email: string;
}

export interface WeatherData {
  temperature: number;
  humidity: number;
  description: string;
  lat: number;
  lon: number;
}

export interface PredictionLog {
  id: string;
  date: string;
  type: 'Yield' | 'Soil' | 'Price' | 'Optimization';
  details: string;
  result: string;
}

export interface SoilAnalysisResult {
  recommendedCrops: string[];
  soilHealth: string;
  actionPlan: string[];
}

export interface CropOptimizationResult {
  cropPlan: { crop: string; acres: number; estimatedProfit: number }[];
  totalProfit: number;
  waterUsage: number;
  rationale: string;
}

declare global {
  interface Window {
    google: any;
  }
}
