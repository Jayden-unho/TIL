import Login from '../containers/login/login'
import styles from '../styles/Home.module.css'

export default function Home({ identification, changeIdentification }) {
  return (
    <main className={styles.main}>
      <Login identification={identification} changeIdentification={changeIdentification}>
      </Login>
    </main>
  )
}
