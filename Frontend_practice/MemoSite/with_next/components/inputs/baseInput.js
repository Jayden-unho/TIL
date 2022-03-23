import styles from '../../styles/baseInput.module.css'

export default function BaseInput({ title, content, search, onChange }) {
  return (
    <>
      {
        title
        ? <input
            onChange={onChange}
            data-type='title'
            className={styles.input}
            type='text'
            placeholder='제목을 입력하세요'
          />
        : content
        ? <textarea
            onChange={onChange}
            data-type='content'
            className={styles.input}
            placeholder='내용을 입력하세요'
          />
        : search
        ? <input
            onChange={onChange}
            data-type='search'
            className={styles.input}
            type='text'
            placeholder='검색어를 입력하세요'
          />
        : <></>
      }
    </>
  )
}