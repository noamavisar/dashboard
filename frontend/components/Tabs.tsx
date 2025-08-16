import { useState } from 'react'
import Analytics from './Analytics'
import OptimizationChart from './OptimizationChart'

const tabs = ['Current Snapshot', 'Data Analysis & Insights', 'Portfolio Optimization']

export default function Tabs() {
  const [active, setActive] = useState(0)
  return (
    <div>
      <div className="flex space-x-4 border-b mb-4">
        {tabs.map((t, idx) => (
          <button
            key={t}
            className={`pb-2 ${active === idx ? 'border-b-2 border-blue-500' : ''}`}
            onClick={() => setActive(idx)}
          >
            {t}
          </button>
        ))}
      </div>
      <div>
        {active === 0 && <div>Real-time snapshot goes here.</div>}
        {active === 1 && <Analytics />}
        {active === 2 && <OptimizationChart />}
      </div>
    </div>
  )
}
