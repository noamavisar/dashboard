import { useEffect, useState } from 'react'

type AnalyticsData = {
  sharpe: number
  volatility: number
  tickers: string[]
  correlation: number[][]
}

export default function Analytics() {
  const [data, setData] = useState<AnalyticsData | null>(null)

  useEffect(() => {
    const base = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
    fetch(`${base}/api/analytics`)
      .then((res) => res.json())
      .then(setData)
  }, [])

  if (!data) return <div>Loading...</div>

  return (
    <div>
      <p>Sharpe Ratio: {data.sharpe.toFixed(2)}</p>
      <p>Volatility: {(data.volatility * 100).toFixed(2)}%</p>
      <table className="table-auto border mt-4">
        <thead>
          <tr>
            <th></th>
            {data.tickers.map((t) => (
              <th key={t}>{t}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.tickers.map((row, i) => (
            <tr key={row}>
              <td>{row}</td>
              {data.correlation[i].map((c, j) => (
                <td key={j}>{c.toFixed(2)}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
