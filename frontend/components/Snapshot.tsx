import { useEffect, useState } from 'react'

type Holding = {
  symbol: string
  quantity: number
  cost_basis: number
  price: number
}

type EnrichedHolding = Holding & {
  value: number
  pnl: number
}

export default function Snapshot() {
  const [holdings, setHoldings] = useState<EnrichedHolding[]>([])

  useEffect(() => {
    const base = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
    fetch(`${base}/api/holdings`)
      .then((res) => res.json())
      .then((data: Holding[]) => {
        const enriched = data.map((h) => ({
          ...h,
          value: h.price * h.quantity,
          pnl: (h.price - h.cost_basis) * h.quantity,
        }))
        setHoldings(enriched)
      })
  }, [])

  if (!holdings.length) return <div>Loading...</div>

  const totalValue = holdings.reduce((sum, h) => sum + h.value, 0)
  const totalPnl = holdings.reduce((sum, h) => sum + h.pnl, 0)

  return (
    <div>
      <p className="mb-2">Portfolio Value: ${totalValue.toFixed(2)}</p>
      <p className="mb-4">Total P&L: ${totalPnl.toFixed(2)}</p>
      <table className="table-auto border">
        <thead>
          <tr>
            <th className="px-2">Symbol</th>
            <th className="px-2">Qty</th>
            <th className="px-2">Cost Basis</th>
            <th className="px-2">Price</th>
            <th className="px-2">Value</th>
            <th className="px-2">P&amp;L</th>
          </tr>
        </thead>
        <tbody>
          {holdings.map((h) => (
            <tr key={h.symbol}>
              <td className="px-2">{h.symbol}</td>
              <td className="px-2">{h.quantity}</td>
              <td className="px-2">${h.cost_basis.toFixed(2)}</td>
              <td className="px-2">${h.price.toFixed(2)}</td>
              <td className="px-2">${h.value.toFixed(2)}</td>
              <td className="px-2">${h.pnl.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
