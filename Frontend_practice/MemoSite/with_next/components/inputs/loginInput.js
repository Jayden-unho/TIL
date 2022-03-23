import { useRef } from 'react'
import styles from '../../styles/loginInput.module.css'

export default function LoginInput({ id, password, onChange }) {
  return (
    <>
      <input
        className={styles.item}
        type={id ? 'text' : password ? 'password' : ''}
        placeholder={id ? "아이디를 입력하세요" : password ? "비밀번호를 입력하세요." : ''}
        onChange={onChange}
        data-type={id ? 'id' : password ? 'password' : ''}
      ></input>
    </>
  )
}