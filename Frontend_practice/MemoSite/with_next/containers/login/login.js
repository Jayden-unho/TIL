import { useState } from 'react'
import { useRouter } from 'next/router'
import LoginInput from '../../components/inputs/loginInput'
import Button from '../../components/buttons/button'
import { setStorage, getStorage } from '../../lib/storage'
import styles from '../../styles/login.module.css'

export default function Login({ identification, changeIdentification }) {
  const router = useRouter()

  const localLogin = () => {
    const value = getStorage(identification.id + identification.password)

    if (value === null) {
      setStorage(identification.id + identification.password, '')
    }

    router.push({ pathname: '/main' })
  }

  const googleLogin = () => {
    console.info('clicked google')
  }

  return (
    <div className={styles.container}>
      <LoginInput id onChange={changeIdentification}></LoginInput>
      <LoginInput password onChange={changeIdentification}></LoginInput>
      <Button
        login
        text="로컬 로그인"
        onClick={localLogin}
      />
      <Button
        login
        text="구글 로그인"
        onClick={googleLogin}
      />
    </div>
  )
}