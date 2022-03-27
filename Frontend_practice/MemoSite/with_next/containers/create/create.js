import BaseInput from '../../components/inputs/baseInput'
import Button from '../../components/buttons/button'
import styles from './create.module.css'

export default function Create({ memo, onChange, saveMemo }) {
  return (
    <>
      <div className={styles.input__container}>
        <label>제목</label>
        <BaseInput title value={memo.title} onChange={onChange}></BaseInput>
      </div>
      <div className={styles.input__container}>
        <label>내용</label>
        <BaseInput content value={memo.content} onChange={onChange}></BaseInput>
      </div>
      <Button create text="작성하기" onClick={saveMemo}></Button>
    </>
  )
}