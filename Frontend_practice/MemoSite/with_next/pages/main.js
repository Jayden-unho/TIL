import { useState, useEffect } from 'react'

import Create from '../containers/create/create'
import { getStorage, setStorage } from '../lib/storage'
import styles from '../styles/main.module.css'

export default function Main({ identification }) {
  const [memos, setMemos] = useState([])
  const [memo, setMemo] = useState({ title: '', content: '' })

  const username = identification.id

  const memoChange = event => {
    setMemo({
      ...memo,
      [event.target.dataset.type]: event.target.value
    })
  }

  const saveMemo = event => {
    if (!memo.title) {
      alert('메모 제목을 입력하세요')
    } else {
      setStorage(username, [...memos, memo])
      setMemos(getStorage(username))
    }
  }

  useEffect(() => {
    let value = getStorage(username)
    if (value === null) {
      value = []
    }
    setMemos(value)
  }, [])
  
  return (
    <main className={styles.main}>
      <header>
        {username}
      </header>
      <section className={styles.create__container}>
        <Create memo={memo} onChange={memoChange} saveMemo={saveMemo}/>
      </section>
      <section>
        <p>메모 조회하는 곳</p>
      </section>
    </main>
  )
}