import dynamic from 'next/dynamic'
import { useEffect, useState } from 'react'

const Plot = dynamic(() => import('react-plotly.js'), { ssr: false })

type Point = { risk: number; return: number }

export default function OptimizationChart() {
  const [points, setPoints] = useState<Point[]>([])

  useEffect(() => {
    const base = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
    fetch(`${base}/api/optimization`)
      .then((res) => res.json())
      .then(setPoints)
  }, [])

  if (!points.length) return <div>Loading...</div>

  return (
    <Plot
      data={[
        {
          x: points.map((p) => p.risk),
          y: points.map((p) => p.return),
          mode: 'lines+markers',
          name: 'Efficient Frontier',
        },
      ]}
      layout={{ title: 'Efficient Frontier', xaxis: { title: 'Risk' }, yaxis: { title: 'Return' } }}
    />
  )
}
