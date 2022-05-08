# Next.js 사용하기

## :book: Next.js 에 대하여

Next.js 를 사용하기에 앞서 Next.js 가 어떠한 프레임워크이고, 어느 용도로 사용이 이루어지는지 알아보겠습니다.

&nbsp;

> Next.js 는 Node.js 를 기반으로 구축된 오픈 소스 웹 개발 프레임워크로, 서버 측 렌더링 및 정적 웹사이트 생성과 같은 React 기반 웹 애플리케이션 기능을 가능하게 합니다.\
> \
> 위키 백과 : [https://en.wikipedia.org/wiki/Next.js](https://en.wikipedia.org/wiki/Next.js)

&nbsp;

Next.js 는 React 기반으로 SSR(서버 사이드 렌더링)이 가능하여, SSR을 이용하고자 할때 사용을 하게 됩니다.

&nbsp;

### CSR, SSR, SSG

#### CSR (Client Side Rendering)

클라이언트 사이드 렌더링으로 서비스를 이용하는 사용자의 클라이언트(브라우저 또는 기기)에서 페이지를 렌더링 하는 방식입니다.\
CSR 은 사용자가 서버에 최초 접속시 HTML, JS 등의 서비스 이용에 필요한 모든 파일들을 받아옵니다.\
그 이후 동작에 대한 페이지 렌더링은 클라이언트에서 실시하게 되어, 사용자에게 빠른 사용자경험을 제공하게 됩니다.

장점으로는 서버와 잦은 연결이 필요하지 않아, 서버에 부담이 

#### SSR (Server Side Rendering)

#### SSG (Static Site Generation)

&nbsp;

### Next.js 사용하게 된 이유

저는 [`말듣꾸`](https://unho94.tistory.com/170) 라는 프로젝트를 진행하게 되면서 Next.js 를 사용하게 되었습니다.\
[`말듣꾸`](https://unho94.tistory.com/170) 서비스는 일종의 테스트 서비스로 많은 사용자들이 테스트에 참여하기 위하여 `SEO`를 고려한 서비스 개발이 필요하였습니다.\
또한, `SSR` 와 함께 `SSG`을 이용하여 정적 페이지를 생성하여, 매번 렌더링을 진행하지 않고 미리 제작된 페이지를 제공할 필요가 있어 Next.js 를 이용하게 되었습니다.

&nbsp;




## 참고

- if(kakao) 2021 - <a href="https://if.kakao.com/session/40" target="_blank">Next.js와 Typescript를 이용한 프론트엔드 개발기</a>
