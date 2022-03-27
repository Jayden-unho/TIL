import styles from './button.module.css'

export default function Button({ login, create, text, onClick }) {
  return (
    <>
      {
        login
        ? <button className={styles.login} onClick={onClick}>{text}</button>
        : create
        ? <button className={styles.create} onClick={onClick}>{text}</button>
        : <button>{text}</button>
      }
    </>
  )
}