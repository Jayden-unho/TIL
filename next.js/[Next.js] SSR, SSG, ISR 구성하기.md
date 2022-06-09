# [Next.js] SSR, SSG, ISR 구성하기

이전 포스트를 통해 Next.js 에서 `SSR(Server Side Rendering)` 과 `SSG(Static Site Generation)`의 방식으로 페이지를 생성하는 방법에 대해 다루었습니다.\
이번 포스트에서는 SSR, SSG 과 함께 추가적으로 `ISR(Incremental Static Regeneration)`도 함께 다루어보겠습니다.

이전의 [`Next.js 기본 개념과 프로젝트에 사용한 이유`](https://unho94.tistory.com/201?category=1250021) 포스트에서 CSR, SSR, SSG 방식에 대한 설명을 이미 다루었으므로 관련된 설명은 생략하도록 하겠습니다.\
관련 내용 확인이 필요한 경우 위의 포스트를 확인해주시기 바랍니다.

&nbsp;

---

## 📘 SSR (Server Side Rendering)

SSR 은 사용자가 서비스에 접속하여 서버로 요청을 보내는 경우, 서버에서 렌더링을 진행하고 렌더링 된 페이지를 클라이언트로 응답하게 됩니다.\
이후에 나올 SSG 의 방식과는 다르게 사용자가 매번 요청을 보낼때 마다 서버에서 렌더링 과정을 거치게 됩니다.

이러한 과정은 사용자의 요청에 따라 특정 데이터들이 빈번하게 변경이 일어나는 경우에 유용합니다.

&nbsp;

### [getServerSideProps](https://nextjs.org/docs/basic-features/data-fetching/get-server-side-props)

SSR 을 구현하는 방법은 어렵지 않습니다.\
일반적인 컴포넌트가 아닌 페이지 파일에서 `getServerSideProps` 함수를 정의하여 사용할 수 있습니다.

getServerSideProps 함수 내에서 외부의 데이터를 비동기로 요청 한 이후 페이지 컴포넌트 내에서 데이터를 사용할 수 있습니다.

```javascript
// indexPage.js

// 페이지 컴포넌트 외부에 함수 선언
export async function getServerSideProps() {
  const response = await fetch('https://...');
  const jsonData = await response.json();

  return {                      // 객체 반환
    props: { jsonData }         // props 를 키값으로 하는 객체 안에 데이터 추가
  }
}

// 페이지
function IndexPage({ jsonData }) {  // 페이지에서 Props 로 넘겨받아서 데이터 사용 가능
  // ...
  return (
    <> 
      {/* ... */}
    </>
  )
}

export default IndexPage;
```

추가적으로 응답 헤더에 캐시 정보를 추가하여, 브라우저에 페이지 캐싱을 이용할 수 있습니다.\
[`SSR 페이지의 캐싱`](https://nextjs.org/docs/basic-features/data-fetching/get-server-side-props#caching-with-server-side-rendering-ssr)에 관련된 사항은 공식문서를 참고해주시기 바랍니다.

```javascript
export async function getServerSideProps({ req, res }) {
  res.setHeader(
    'Cache-Control', 'public, s-maxage=10, stale-while-revalidate=59'
  );

  return { props: {} }
}
```

getServerSideProps 는 서버에서만 실행이 되며, 클라이언트에서는 실행되지 않습니다.

&nbsp;

## 📗 SSG (Static Site Generation)

SSG 는 정적 페이지를 생성하는 것으로 빌드하는 과정에서 페이지를 생성하게 됩니다.\
이후 사용자들이 해당 페이지를 요청하는 경우에 서버는 이미 생성된 정적 페이지를 제공합니다.

이러한 과정은 페이지에 구성된 데이터들이 변하지 않는 경우에 유용합니다.

&nbsp;

### [getStaticProps](https://nextjs.org/docs/basic-features/data-fetching/get-static-props)

SSR 의 getServerSideProps 와 유사하게 getStaticProps 함수를 이용하여 SSG 를 구성할 수 있습니다.

```javascript
// staticPage.js

export async function getStaticProps() {
  const response = await fetch('https://...');
  const jsonData = await response.json();

  return {
    props : { jsonData }
  }
}

function StaticPage({ jsonData }) {
  // ...

  return (
    <>
      {/* ... */}
    </>
  )
}

export default StaticPage;
```

&nbsp;

### [getStaticPaths](https://nextjs.org/docs/basic-features/data-fetching/get-static-paths)

동적 라우팅으로 구성된 페이지들은 getStaticPaths 를 이용하여 동적 경로의 페이지를 정적페이지로 구성할 수 있습니다.\
이때, `getStaticPaths` 는 `getStaticProps` 와 함께 사용되어야 합니다.

getStaticPaths 에서 동적 라우팅으로 구성된 페이지들을 배열로 모아 반환합니다.\
이후 getStaticProps 에서 배열에서 각 요소들의 파라미터의 값을 이용하여 정적 페이지를 생성하게 됩니다.

getStaticProps 와 다르게 반환값은 `paths` 와 `fallback` 을 반환합니다.

```javascript
// [dynamicPages]/index.js

export async function getStaticPaths() {
  // ...
  return {
    paths: [                        // 동적 페이지들의 묶음 (배열)
      { params: { id: 0 } },        // 각 페이지 하나의 파라미터
      { params: { id: 1 } },
      // ...
    ],
    fallback: false                 // 빌드시 생성되지 않은 주소로 요청이 오는 경우에 대한 옵션
  };
}

export async function getStaticProps({ params }) {
  const response = await fetch(`https://.../${params.id}`);
  const jsonData = await response.json();

  return {
    props : { jsonData }
  }
}

// 페이지 컴포넌트
function StaticPage({ jsonData }) {
  // ...

  return (
    <>
      {/* ... */}
    </>
  )
}

export default StaticPage;
```

&nbsp;

#### [fallback](https://nextjs.org/docs/api-reference/data-fetching/get-static-paths#getstaticpaths-return-values)

getStaticPaths 반환 값 중 fallback 값이 있습니다.\
fallback 은 `true | false | blocking` 을 값으로 가질 수 있습니다.

getStaticPaths 와 getStaticProps 는 빌드하는 과정에서 정적 페이지를 생성하게 됩니다.\
이후에 사용자가 요청을 보내는 경우에 해당 함수들을 실행하지 않고, 이미 생성된 정적 페이지의 파일들을 응답하게 됩니다.

그런데 동적 페이지의 경우 빌드시에 생성되지 않은 주소로 사용자가 요청을 보내는 경우가 존재합니다.\
이러한 경우에 fallback 값에 따라 서로 다른 대응을 할수 있습니다.

- **true**
  
    빌드시에 생성되지 않은 정적 페이지를 사용자가 요청하는 경우, 요청이 들어왔을 때 fallback 페이지를 제공합니다.\
    서버에서 정적 페이지를 생성하고, 생성되면 사용자에게 해당 페이지를 제공합니다.\
    이렇게 추가적으로 생성된 정적 페이지는 빌드시에 생성된 정적 페이지들과 함께 보관이 되며, 이후에 해당 페이지를 요청하는 경우에 정적 페이지를 응답합니다.

- **false**

    빌드시에 생성되지 않은 정적 페이지를 사용자가 요청하는 경우, 404 페이지를 응답합니다.

- **blocking**

    빌드시에 생성되지 않은 정적 페이지를 사용자가 요청하는 경우, SSR 방식으로 제작한 정적 페이지를 사용자에게 응답합니다.\
    이후에 해당 주소로 요청이 들어오면 정적 페이지를 응답합니다.

&nbsp;

fallback 값의 true 와 blocking 은 빌드시에 생성하지 못한 페이지에 대해 요청이 들어오면 정적 페이지를 생성하는 부분이 유사합니다.

그러나 true 는 정적 페이지가 생성되는 동안 fallback 페이지를 제공하고, 정적 페이지가 생성되면 fallback 페이지 대신 새로 생성된 정적 페이지를 제공합니다.\
blocking 은 fallback 페이지를 제공하지 않고, SSR 방식으로 정적 페이지를 생성하여 사용자에게 제공합니다.

&nbsp;

## [📕 ISR (Incremental Static Regeneration)](https://nextjs.org/docs/basic-features/data-fetching/incremental-static-regeneration)

SSG 는 빌드시에만 정적 페이지를 생성(fallback 제외) 한다는 특징이 있습니다.\
그러나 ISR 을 이용하면 빌드시에만 생성하는 것이 아니라 특정 시간(초)마다 정적 페이지를 재생성할 수 있습니다.

getStaticProps 의 반환값으로 `revalidate` 값을 주면 해당 시간(초)마다 정적 페이지에 필요한 데이터를 업데이트하여 재생성합니다.

```javascript
export async function getStaticProps() {
  const response = await fetch('https://...');
  const jsonData = await response.json();

  return {
    props: {
      jsonData
    },
    revalidate: 100
  }
}
```

&nbsp;

---

## 💻 프로젝트에서 사용하기

### 커스텀 페이지

말듣꾸 서비스의 커스텀 페이지는 사용자의 테스트 결과에 따라 다른 화면을 나타나게 됩니다.\
테스트는 총 60여개로 고정되어 있어 SSR 방식 보다 정적 페이지로 생성하여 테스트에 맞게 페이지를 응답하는 것이 효율적이라 생각하였습니다.

동적 주소의 개수는 고정되어 있으므로 빌드시 모두 정적 페이지로 생성하였습니다.\
또한, 다른 주소로 요청이 들어오는 경우는 테스트 결과가 아닌 잘못된 주소이므로 fallback 값을 false 로 설정하였습니다.

![custom](https://user-images.githubusercontent.com/84773475/172644474-d1c9c021-c154-40a9-8423-1d299ce2ca4a.png)

```javascript
export async function getStaticPaths() {
  // 테스트 결과로 나올 수 있는 모든 지역의 수
  const province = ['gangwon', 'chungcheong', 'gyeonggi', 'gyeongsang', 'jeju', 'jeolla'];

  // ... (지역들을 조합하여 나올 수 있는 경로를 구함)

  return {
    paths,
    fallback: false       // 테스트 결과의 수는 고정이 되어 있으므로 그 외에 해당하는 동적 주소는 404 페이지 반환
  }
}

export async function getStaticProps({ params }) {
  // 페이지를 구성하기 위한 데이터를 받아옴
  const characterFiles = await getFileList('character', params.customizeId);
  const itemFiles = await getFileList('items', params.customizeId);
  const backgroundFiles = await getBackgroundList();

  return {
    props: { characterFiles, itemFiles, backgroundFiles }
  }
}

function Customize({ characterFiles, itemFiles, backgroundFiles }) {
  // ...
}
```

&nbsp;

### 결과 공유 페이지

말듣꾸 서비스는 테스트마다 고유의 id 값을 가지게 됩니다.\
결과 공유 페이지는 테스트 id 값을 주소의 파라미터로 이용하여 동적 페이지를 구성하였습니다.

테스트의 결과 화면을 SNS를 통해 공유할 수 있습니다.\
공유를 받은 사용자들은 해당 페이지에 접속을 시도하면 모두 같은 화면을 제공받기 때문에, 정적 페이지로 생성하엿습니다.\
그러나 테스트를 받기 이전인 빌드시에 정적 페이지 생성이 불가능하므로 fallback 값을 true 로 설정하여, 테스트가 완료된 시점에 정적 페이지를 추가적으로 생성하도록 구성하였습니다.

![share](https://user-images.githubusercontent.com/84773475/172645749-6401416b-0280-485b-b01b-a36857d19c51.png)

```javascript
export async function getStaticPaths() {
  // 빌드시 테스트 기록이 없으므로 임의의 빈 정적 페이지 생성
  return {
    paths: [
      { params: { shareId: '0' } }
    ],
    fallback: true  // 새로운 테스트 결과가 생길때 마다 정적 페이지 생성이 필요하므로 true 로 설정
  }
}

export async function getStaticProps({ params }) {
  // 정적 페이지 생성시 필요한 데이터 받아옴
  const image = await getRequest(`/${params.shareId}/my`);
  const result = await getRequest(`/${params.shareId}/result`);
  
  // ...

  return {
    props: {
      // ...
    }
  }
}

function Share({ /* ... */ }) {
  // 정적 페이지 생성하는 동안 사용자에게 제공할 fallback 페이지
  if (router.isFallback) {
    return <ThreeDotsWave contents={'결과를 찾아오고 있어요.'}></ThreeDotsWave>;
  }

  // ...
}
```

&nbsp;

### 메인 페이지 (다른 유저들의 커스텀 이미지 목록)

메인 페이지의 하단에는 다른 유저들이 생성한 커스텀 이미지 목록을 확인할 수 있습니다.\
렌더링 과정에서 다수의 이미지 데이터를 이용하기 때문에 SSR 을 이용하는 경우에 시간이 지연되는 경우가 발생할 것으로 예상하였습니다.

해당 컴포넌트는 CSR 로 구성하였고, React의 lazy 를 이용하였습니다.\
그리하여 해당 컴포넌트를 제외한 다른 컴포넌트를 사용자에게 빠르게 제공하고, 해당 컴포넌트는 이미지들이 모두 로드가 되었을 때 사용자에게 제공하는 사용자 경험을 고려하였습니다.

![index_bottom](https://user-images.githubusercontent.com/84773475/172650055-ef3941d4-e7bd-40e7-adf7-578052f8b621.png)

```javascript
const SharedImages = lazy(() => import('../containers/sharedImages/sharedImages'));

function Home({ staticState, changeStaticState }) {
  const [sharedImages, setSharedImages] = useState({});

  // ...

  return (
    <>
      {/* ... */}
      {
        sharedImages.length
          ? (
            <Suspense fallback={<Text contents='이미지를 불러오고 있어요.'></Text>}>
              <SharedImages data={sharedImages} staticState={staticState}></SharedImages>
            </Suspense>
          )
          : null
      }
    </>
  )
}
```

&nbsp;

---

## :books: 참고

- 공식문서 - <a href="https://nextjs.org/docs/basic-features/data-fetching/overview" target="_blank">Data Fetching Overview</a>
