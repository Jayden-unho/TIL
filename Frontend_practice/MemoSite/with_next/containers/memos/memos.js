import Memo from '../../components/memo/memo'

import styles from './memos.module.css'

export default function Memos({ memos }) {
  let items = memos.map((memo, idx) => {
    return (
      <Memo memo={memo} key={idx}/>
    )
  })

  return (
    <>
      {items}
    </>
  )
}