// frontend/src/App.tsx
import React, { useState } from 'react';
import EquityChart from './components/EquityChart';
import SentimentGauge from './components/SentimentGauge';

const TABS = ['Dashboard', 'Sentiment Feed', 'Trades'];

export default function App() {
  const [tab, setTab] = useState('Dashboard');
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="p-4 bg-white shadow flex items-center justify-between">
        <h1 className="text-2xl font-bold text-blue-700">FinSight Alpha-Lite</h1>
        <nav className="space-x-4">
          {TABS.map(t => (
            <button
              key={t}
              className={`px-3 py-1 rounded ${tab === t ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700'}`}
              onClick={() => setTab(t)}
            >
              {t}
            </button>
          ))}
        </nav>
      </header>
      <main className="p-6">
        {tab === 'Dashboard' && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <EquityChart />
            <SentimentGauge />
          </div>
        )}
        {tab === 'Sentiment Feed' && (
          <div className="bg-white p-4 rounded shadow">Sentiment Feed coming soon...</div>
        )}
        {tab === 'Trades' && (
          <div className="bg-white p-4 rounded shadow">Trades log coming soon...</div>
        )}
      </main>
    </div>
  );
} 