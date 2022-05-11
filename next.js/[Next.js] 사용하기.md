# Next.js 사용하기

진행하는 프로젝트의 프론트엔드 기술 스택으로 Next.js 를 사용하게 되었습니다.\
해당 포스트는 Next.js 에 대한 간략한 설명과 진행한 프로젝트에서 Next.js 를 사용하게 된 이유에 관한 내용을 담았습니다.

이후의 Next.js 관련 포스트는 Next.js 를 이용하면서 발생한 이슈들에 대해 다룰 예정입니다.

&nbsp;

## :book: Next.js 에 대하여

위키백과에서는 Next.js 를 아래와 같이 설명하고 있습니다.

> Next.js 는 Node.js 를 기반으로 구축된 오픈 소스 웹 개발 프레임워크로, 서버 측 렌더링 및 정적 웹사이트 생성과 같은 React 기반 웹 애플리케이션 기능을 가능하게 합니다.\
> \
> 위키 백과 : [https://en.wikipedia.org/wiki/Next.js](https://en.wikipedia.org/wiki/Next.js)

&nbsp;

위의 내용에서 Next.js 에 대해 잘 설명이 되어 있지만, 조금 더 쉽게 표현하자면 `Next.js 는 서버에서 페이지를 구성하여 제공할 수 있는 React 기반의 프레임워크` 입니다.

&nbsp;

---

## :question: CSR, SSR, SSG

앞서 언급된 '서버측 렌더링' 에 대한 내용을 이해하기 위해서는 기본적으로 CSR, SSR 에 대한 이해가 필요하여 간략하게 CSR, SSR, SSG 에 대하여 이해하고 넘어가겠습니다.

CSR 과 SSR 을 비교하기 이전에 SPA 와 MPA 에 대한 개념도 추가적으로 필요하여 함께 다루어 보겠습니다.

&nbsp;

### SPA 와 MPA

#### SPA (Single Page Application)

SPA 는 하나의 페이지로 구성되어 있습니다.\
서버로 처음에만 페이지를 응답 받고 이후에는 JavaScript 를 이용하여 동적으로 페이지를 구성하게 됩니다.

사용자가 페이지를 이동하더라도 서버로 새로운 페이지를 응답 받지 않습니다.\
그러므로 페이지 새로고침이 발생하지 않고, 다른 페이지로 이동이 되지 않습니다.\
(다만, 사용자가 페이지 이동시 실제로 페이지가 이동하는 경험을 제공하기 위하여 주소창의 주소가 변경되는것과 같은 행동이 발생합니다.)

페이지를 한번만 응답 받고 이후 동작에 대해서는 클라이언트(브라우저)에서 새로운 페이지를 구성하기 때문에 `CSR` 방식을 이용합니다.

&nbsp;

#### MPA (Multi Page Application)

MPA 는 여러 페이지로 구성이 되어 있습니다.\
사용자가 다른 페이지를 이동할때마다 서버로부터 다른 페이지 응답 받게 됩니다.

페이지가 이동이 될때마다 서버로부터 페이지 제공을 받기 때문에 `SSR` 방식을 이용합니다.

&nbsp;

#### SPA vs MPA

두가지의 방식은 각각 장단점이 존재합니다.

- **초기 페이지 응답**

  **SPA** : SPA 는 동적인 동작이 이루어질 모든 파일들을 한번에 응답 받아야하기 때문에 많은 시간이 소요됩니다.

  **MPA** : MPA 는 해당 페이지에 관련된 파일들만 응답 받으면 되기 때문에 적은 시간이 소요됩니다.

- **이후 페이지 이동**

  **SPA** : 이후에 페이지 이동과 같은 동작은 클라이언트에서 바로 렌더링이 이루어지기 떄문에 빠르게 페이지 이동이 가능하며, 새로고침(화면 깜빡임)이 발생하지 않습니다.

  **MPA** : 페이지 이동할때마다 서버로부터 해당 페이지의 파일을 응답 받아야하기 때문에 페이지 이동에 시간이 다소 소요됩니다. 또한, 새로고침(화면 깜빡임)이 발생합니다.

&nbsp;

### CSR (Client Side Rendering)

CSR 은 클라이언트 사이드 렌더링으로 웹페이지를 클라이언트(브라우저)에서 렌더링(구성)하는 방식입니다.

&nbsp;

![CSR 실행 순서 그림](https://user-images.githubusercontent.com/84773475/167907400-fdd83d30-204b-473e-abd3-8d3f5091ba51.png)\
출처 : [The Benefits of Server Side Rendering Over Client Side Rendering](https://medium.com/walmartglobaltech/the-benefits-of-server-side-rendering-over-client-side-rendering-5d07ff2cefe8)

사용자가 웹페이지를 접속하면 서버로부터 페이지를 구성하는 기본적인 HTML(데이터 없이 비어있음) 과 JavaScript 파일을 응답받게 됩니다.\
이후 클라이언트(브라우저)에서 React, Angular, Vue 들의 라이브러리 및 프레임워크가 실행이 되어 페이지를 렌더링하여 사용자에게 제공합니다.

&nbsp;

#### CSR 장점과 단점

CSR 은 서버로부터 페이지 구성을 위한 HTML 과 JavaScript 파일을 응답 받으면 되기 때문에 SSR 보다 빠르게 전송 받을 수 있습니다.

렌더링 이전에는 사용자에게 비어있는 화면이 보여지게 됩니다.\
네트워크 상황과 클라이언트 성능이 좋다면 아주 짧은 시간으로 사용자는 비어있는 화면을 보지 않게 되지만, 네트워크 상황이 좋지 않거나 클라이언트 성능이 많이 떨어진다면 비어있는 화면을 오랫동안 보게 된다는 단점이 있습니다.

&nbsp;

### SSR (Server Side Rendering)

SSR 은 서버 사이드 렌더링으로 웹페이지를 서버에서 렌더링하여 제공하는 방식입니다.

&nbsp;

![SSR 실행 순서 그림](https://user-images.githubusercontent.com/84773475/167907009-8439f42b-bd86-44be-853a-3e10ccbbe1db.png)\
출처 : [The Benefits of Server Side Rendering Over Client Side Rendering](https://medium.com/walmartglobaltech/the-benefits-of-server-side-rendering-over-client-side-rendering-5d07ff2cefe8)

사용자가 웹페이지를 접속하면 서버에서 페이지를 구성하여 클라이언트에게 응답하게 됩니다.\
클라이언트가 HTML을 응답 받으면 바로 사용자에게 페이지가 보여지게 되고, 추가적인 동적인 동작이 필요한 JavaScript 를 다운 받고 실행하게 됩니다.

&nbsp;

#### SSR 장점과 단점

SSR 은 서버에서 렌더링 과정을 거치고 응답을 주기 때문에 CSR 에 비해 초기에 페이지 전송이 느리다는 단점이 있습니다.

그러나 CSR 은 클라이언트에서 렌더링 작업을 거친 이후에 사용자에게 페이지가 보여지게 되지만, SSR 은 렌더링 된 페이지를 응답 받고 바로 페이지가 보여지기 때문에 전체적인 페이지 완료 시점은 SSR 이 조금 더 빠르다는 장점이 있습니다.

또한, 서버에서 렌더링 과정이 이루어지고 제공되기 때문에 SEO(Search Engine Optimization) 을 구성하기 수월하다는 장점이 있습니다.

&nbsp;

### SSG (Static Site Generation)

SSG 은 정적 페이지 생성입니다.\
Next.js 에서 제공하는 기능 중 하나로, 변하지 않는 정적인 페이지를 생성하는 것을 말합니다.

CSR 또는 SSR 은 사용자의 요청이 있을때 마다 렌더링 작업이 이루어져야 하는 특징이 있습니다.\
이러한 방식들은 블로그 포스트처럼 한번 작성이 되면 내용이 변하지 않는 경우에 불필요한 렌더링이 발생하게 됩니다.

항상 같은 내용의 페이지를 제공할때 마다 렌더링 작업을 거치지 않도록 정적인 페이지를 미리 생성하여, 렌더링 과정을 줄여 사용자에게 빠르게 페이지를 제공할 수 있습니다.

&nbsp;

---

## :bulb: Next.js 사용하게 된 이유

[`말듣꾸`](https://unho94.tistory.com/170) 라는 프로젝트를 진행하게 되면서 Next.js 를 사용하게 되었습니다.\
해당 프로젝트는 일종의 테스트 서비스로 많은 사용자들이 테스트에 참여하는것이 중요하여 `SEO` 를 고려하여야 했습니다.

프로젝트의 서비스 화면을 기획하는 단계에서 `시작 페이지` , `결과 공유 페이지` , `진행 페이지` 등이 데이터가 고정되어 사용자에게 제공되는 경우가 많았습니다.\
위의 페이지들을 `SSR` 와 함께 `SSG`을 이용하여 정적 페이지를 생성하고, 매번 렌더링을 진행하지 않고 미리 제작된 페이지를 제공하는 방식이 효율적이라 판단하여 `Next.js` 를 이용하게 되었습니다.

&nbsp;

---

## :books: 참고

- if(kakao) 2021 - <a href="https://if.kakao.com/session/40" target="_blank">Next.js와 Typescript를 이용한 프론트엔드 개발기</a>

- NAVER D2 - <a href="https://d2.naver.com/helloworld/7804182" target="_blank">어서 와, SSR은 처음이지? - 도입 편</a>

- Blog 프로그래밍 - <a href="https://proglish.tistory.com/216" target="_blank">SSR과 CSR의 차이</a>

- <a href="https://blog.hahus.kr/csr-ssr-spa-mpa-ede7b55c5f6f" target="_blank">CSR, SSR, SPA, MPA? 상사한테 혼나기 전에 알아야하는 것</a>
