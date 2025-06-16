// frontend/src/components/SentimentGauge.tsx
import React, { useEffect, useState } from 'react';
import { RadialBarChart, RadialBar, PolarAngleAxis } from 'recharts';

export default function SentimentGauge() {
  const [score, setScore] = useState(0);

  // Simulate fetching latest sentiment
  useEffect(() => {
    const interval = setInterval(() => {
      setScore(Math.round((Math.random() * 2 - 1) * 100) / 100);
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  const data = [{ name: 'Sentiment', value: (score + 1) * 50, fill: score > 0 ? '#22c55e' : '#ef4444' }];

  return (
    <div className="bg-white p-4 rounded shadow flex flex-col items-center">
      <h2 className="text-lg font-semibold mb-2">Sentiment Score</h2>
      <RadialBarChart width={200} height={200} cx={100} cy={100} innerRadius={60} outerRadius={90} barSize={18} data={data} startAngle={180} endAngle={0}>
        <PolarAngleAxis type="number" domain={[0, 100]} tick={false} />
        <RadialBar minAngle={15} background clockWise dataKey="value" />
      </RadialBarChart>
      <div className={`mt-4 text-2xl font-bold ${score > 0 ? 'text-green-600' : 'text-red-600'}`}>{score}</div>
    </div>
  );
} 