// frontend/src/components/EquityChart.tsx
import React, { useEffect, useRef, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export default function EquityChart() {
  const [data, setData] = useState<{ equity: number }[]>([]);
  const ws = useRef<WebSocket | null>(null);

  useEffect(() => {
    ws.current = new WebSocket('ws://localhost:8000/ws/metrics');
    ws.current.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      setData(prev => [...prev.slice(-99), { equity: msg.equity }]);
    };
    return () => ws.current?.close();
  }, []);

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-lg font-semibold mb-2">Live Equity Curve</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <XAxis dataKey="index" tick={false} hide />
          <YAxis domain={['auto', 'auto']} />
          <Tooltip />
          <Line type="monotone" dataKey="equity" stroke="#2563eb" dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
} 