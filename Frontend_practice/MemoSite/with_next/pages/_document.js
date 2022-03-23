import { Html, Head, NextScript, Main } from 'next/document'

export default function Document() {
  console.log('docu')
  return (
    <Html>
      <Head>
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}