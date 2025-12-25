import React, { useState, useEffect } from 'react';
import { Toaster } from 'react-hot-toast';
import { Page, User } from './types';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import CropPrediction from './pages/CropPrediction';
import SoilAnalysis from './pages/SoilAnalysis';
import WeatherForecast from './pages/WeatherForecast';
import PriceForecast from './pages/PriceForecast';
import Optimization from './pages/Optimization';
import History from './pages/History';

const App: React.FC = () => {
  const [currentPage, setCurrentPage] = useState<Page>(Page.LOGIN);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // Initialize user from localStorage
  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      try {
        setUser(JSON.parse(storedUser));
        setCurrentPage(Page.DASHBOARD);
      } catch (e) {
        console.error("Failed to parse user from local storage", e);
        localStorage.removeItem('user');
      }
    }
    setIsLoading(false);
  }, []);

  // Dark mode state initialized from localStorage or system preference
  const [isDarkMode, setIsDarkMode] = useState(() => {
    if (typeof window !== 'undefined') {
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme) {
        return savedTheme === 'dark';
      }
      return window.matchMedia('(prefers-color-scheme: dark)').matches;
    }
    return false;
  });

  // Apply dark class to html element
  useEffect(() => {
    if (isDarkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }, [isDarkMode]);

  const toggleTheme = () => setIsDarkMode(!isDarkMode);

  const handleLogout = () => {
    localStorage.removeItem('user');
    setUser(null);
    setCurrentPage(Page.LOGIN);
  };

  if (isLoading) {
    return (
      <div className="flex h-screen items-center justify-center bg-gray-50 dark:bg-gray-900">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (currentPage === Page.LOGIN) {
    return <Login setPage={setCurrentPage} setUser={setUser} />;
  }

  const renderPage = () => {
    switch (currentPage) {
      case Page.DASHBOARD: return <Dashboard />;
      case Page.CROP_PREDICTION: return <CropPrediction />;
      case Page.SOIL_ANALYSIS: return <SoilAnalysis />;
      case Page.WEATHER: return <WeatherForecast />;
      case Page.PRICE_FORECAST: return <PriceForecast />;
      case Page.OPTIMIZATION: return <Optimization />;
      case Page.HISTORY: return <History />;
      default: return <Dashboard />;
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-200">
      <Header
        toggleSidebar={() => setSidebarOpen(!sidebarOpen)}
        isDarkMode={isDarkMode}
        toggleTheme={toggleTheme}
        onLogout={handleLogout}
        user={user}
      />

      <Toaster
        position="top-right"
        toastOptions={{
          duration: 4000,
          style: {
            background: isDarkMode ? '#1f2937' : '#fff',
            color: isDarkMode ? '#fff' : '#1f2937',
            border: isDarkMode ? '1px solid #374151' : '1px solid #e5e7eb',
          },
          success: {
            iconTheme: {
              primary: '#10b981',
              secondary: 'white',
            },
          },
          error: {
            iconTheme: {
              primary: '#ef4444',
              secondary: 'white',
            },
          },
        }}
      />

      <div className="flex flex-1 overflow-hidden relative">
        <Sidebar
          currentPage={currentPage}
          setPage={setCurrentPage}
          isOpen={sidebarOpen}
          toggleSidebar={() => setSidebarOpen(!sidebarOpen)}
          user={user}
          onLogout={handleLogout}
        />

        {/* Overlay for mobile when sidebar is open */}
        {sidebarOpen && (
          <div
            className="fixed inset-0 bg-black/50 z-30 lg:hidden glass-panel"
            onClick={() => setSidebarOpen(false)}
          ></div>
        )}

        <main className="flex-1 overflow-y-auto p-4 lg:p-8 text-gray-900 dark:text-white scroll-smooth">
          <div className="max-w-7xl mx-auto">
            {renderPage()}
          </div>
        </main>
      </div>
    </div>
  );
};

export default App;