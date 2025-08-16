import Head from 'next/head'
import Tabs from '../components/Tabs'

export default function Home() {
  return (
    <>
      <Head>
        <title>Portfolio Dashboard</title>
      </Head>
      <main className="p-4">
        <h1 className="text-2xl font-bold mb-4">Portfolio Dashboard</h1>
        <Tabs />
      </main>
    </>
  )
}
