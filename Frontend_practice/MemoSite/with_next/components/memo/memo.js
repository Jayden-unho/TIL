import styles from './memo.module.css'

export default function Memo({ memo }) {
  return (
    <div className={styles.container}>
      <p className={styles.title}>{memo.title}</p>
      <p>{memo.content}</p>
    </div>
  )
}