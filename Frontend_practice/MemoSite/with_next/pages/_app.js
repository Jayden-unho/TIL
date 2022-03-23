import { useState } from 'react'
import Head from 'next/head'
import Layout from '../components/layout'
import '../styles/globals.css'

function MyApp({ Component, pageProps }) {
  const [status, setStatus] = useState({identification: { id: '', password: '' }})

  const changeIdentification = (event) => {
    setStatus({
      ...status,
      identification: {
        ...status.identification,
        [event.target.dataset.type]: event.target.value
      },
    })
  }

  return (
    <Layout>
      <Head>
        <title>메모 사이트</title>
      </Head>
      <Component
        {...pageProps}
        {...status}
        changeIdentification={changeIdentification}
      />
    </Layout>
  )
}

export default MyApp
