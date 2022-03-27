import { useState } from 'react'
import { useRouter } from 'next/router'
import LoginInput from '../../components/inputs/loginInput'
import Button from '../../components/buttons/button'

import { setStorage, getStorage } from '../../modules/storage'
import styles from './login.module.css'

export default function Login({ identification, changeIdentification }) {
  const router = useRouter()

  const localLogin = () => {
    const value = getStorage(identification.id)

    if (value === null) {
      setStorage(identification.id, '')
    }

    router.push({ pathname: '/main' })
  }

  const googleLogin = () => {
    console.info('clicked google')
  }

  return (
    <div className={styles.container}>
      <LoginInput id onChange={changeIdentification}></LoginInput>
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