# [Next.js] 페이지 나누기

Next.js 를 이용한 개발에서 가장 기초적이며 필수적인 요소로 페이지 라우팅 입니다.\
해당 포스트는 Next.js 에서 페이지 구성하는 방법과 진행한 프로젝트에서 어떠한 방식으로 라우팅을 이용하였는지에 대해 다루었습니다.

&nbsp;

---

## 📘 React 페이지 구성과 라우팅

React 를 이용할때는 페이지를 구분하고 이동시키기 위하여 라우터 기능이 있는 [`react-router`](https://reactrouter.com) 라이브러리를 이용해야 합니다.\
해당 라이브러리를 이용하기 위해서는 react-router 에 대한 추가적인 학습이 필요하고, \<Routes\> 와 \<Route\> 등을 이용하여 라우팅 구성이 필요합니다.

이러한 점이 React 에서 페이지를 구성하는것에 어려움을 가져다줍니다.

&nbsp;

---

## 📗 Next.js 페이지 구성과 라우팅

Next.js 는 라우팅 기능을 내장하고 있어 손쉽게 페이지를 구성할 수 있습니다.

```text
npx create-next-app@latest
# or
yarn create next-app
# or
pnpm create next-app
```

위의 방법을 이용하여 프로젝트를 구성하는 경우, 자동으로 최상위 폴더에 `pages` 폴더가 생성됩니다.\
`pages` 폴더에 자바스크립트 파일 또는 폴더를 생성하여 해당 파일/폴더의 이름으로 자동으로 구성됩니다.

### 라우트 구성 3가지

기본적인 라우트, 중첩, 동적 라우트로 3가지로 구성 할 수 있습니다.

1. 일반적인 라우트

    **pages/index.js** -> **/**

    **pages/book.js** -> **/book**

    **pages/book/index.js** -> **/book**

1. 중첩 라우트

    **pages/book/novel.js** -> **/book/novel**

    **pages/book/essay/index.js** -> **/book/essay**

    **pages/book/novel/like.js** -> **/book/novel/like**

1. 동적 라우트

    **pages/book/[id].js** -> **/book/:id**

    **pages/book/[genre]/index.js** -> **/book/:genre**

    **pages/book/[...id].js** -> **/book/\***  (book/1/like/10)

    **pages/book/[genre]/all.js** -> **/book/:genre/all**

위의 방식들을 이용하여 라우트를 구성할 수 있습니다.

&nbsp;

### 페이지 이동

#### <a href="https://nextjs.org/docs/api-reference/next/link" target="_blank">JSX</a>

```javascript
import Link from 'next/link'

function App() {
    const [bookNumber, setBookNumber] = useState(1)

    return (
        <>
            <Link href="/"><a>Index</a></Link>
            <Link href={`/book/${bookNumber}`}><a>Book</a></Link>
            <Link href={{
                pathname: '/book/novel',
                query: {title: 'XXXX'}
            }}><a>Novel</a></Link>
        </>
    )
}
```

위의 코드와 같이 JSX 내에서 Link Element 를 이용하여 다른 페이지로 라우팅 할 수 있습니다.

### <a href="https://nextjs.org/docs/api-reference/next/router" target="_blank">JavaScript</a>

```javascript
import {useRouter} from 'next/router'

function App() {
    const router = useRouter()

    const buttonClicked = () => {
        router.push('/')
        // router.push({ pathname: '/', query: {title: '***'}})
    }

    return (
        <>
            <button onClick={buttonClicked}>Go Index</button>
        </>
    )
}
```

useRouter 를 이용하여 JavaScript 코드 내에서 페이지 라우팅을 할 수 있습니다.

&nbsp;

## 💻 프로젝트에서 사용하기

### 동적 라우팅

사용자가 테스트를 진행하면 테스트 고유의 ID 값이 생성되었습니다.\
테스트별 고유 ID 값을 URL 주소 뒤에 포함하여 동적 라우팅을 이용하였습니다.

pages 폴더를 아래와 같은 구조로 구성하였습니다.

```text
pages/share/[shareId]/index.js
pages/customize/[...customizeId]/index.js
```

위의 형태로 구성하여 /share/30 또는 /customize/gangwon/3 과 같은 형태의 동적 주소로 라우팅 시 해당 페이지로 이동되도록 하였습니다.

&nbsp;

### 에러 페이지 라우팅

사용자가 옳지 않은 방식으로 다른 페이지에 접속하거나 백엔드 서버의 오류와 같은 상황이 발생하여 오류가 발생하는 경우에 404 페이지로 라우팅하였습니다.\
라우팅 시 쿼리 값으로 에러 코드를 추가하여 상황에 맞는 에러 메시지를 404 페이지에서 표시하도록 하였습니다.

```javascript
// pages/result.js
useEffect(() => {
    // 상태값이 비어있는 경우
    // 사용자가 인위적으로 주소를 입력하여 테스트 중간부터 참여를 시도하는 경우
    if (staticState.caseId === -1 || staticState.sentences.length === 0) {
        // 404 페이지로 라우팅 (쿼리로 에러코드도 함께 라우팅)
        router.push({ pathname: '/404', query: { code: '0001' } })
    }
}, [])

// 404.js
// 사용자에게 에러 상황 안내를 위한 상황별 에러 코드 정의
const NOT_FOUND_CODE = {
  '0000': ['요청하신 페이지가 존재하지 않아요.'],
  '0001': ['해당 페이지를 바로 접속할 수 없어요.'],
  '0002': ['찾으시는 결과가 존재하지 않아요.'],
  '0003': ['음성 녹음 장치에 문제가 있어요'],
  '0502': ['서버에서 문제가 있어요.'],
}

function Custom404() {
    const [code, setCode] = useState('0000')
    const router = useRouter()
    
    useEffect(() => {
        // 에러 코드가 함께 라우팅 되었다면 에러코드 상태값 변경
        if (router.query.code) {
            setCode(router.query.code)
        }
    }, [router])

    return (
        // ...
    )
}
```

---

## :books: 참고

- 공식문서 - <a href="https://nextjs.org/docs/routing/introduction" target="_blank">Routing</a>
