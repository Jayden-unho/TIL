# 음성 녹음 크로스브라우징

이번 포스트는 말듣꾸 프로젝트를 진행하는 당시 겪었던 이슈로 음성 녹음 기능을 구현하는 과정에서 OS와 브라우저에 따라 녹음이 불가능한 문제를 대응하였던 내용을 다루었습니다.

[말듣꾸 프로젝트](https://unho94.tistory.com/170?category=1246528)는 테스트 서비스로 사용자가 음성을 녹음하여 제출하면, 사용자가 어느 지역의 방언을 구사하는지 학습된 인공지능이 추론하여 결과를 제공하는 서비스입니다.\
프로젝트에 관한 자세한 사항은 [링크](https://unho94.tistory.com/170?category=1246528)를 통해 확인 부탁드립니다.

&nbsp;

## 🔥 발생한 이슈

음성 녹음 기능을 추가하기 위하여 [MediaRecorder](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder) 를 이용하였습니다.

해당 기능을 Chrome 브라우저를 기준으로하여 개발을 진행하였는데, MediaRecorder 인스턴스 생성시 옵션으로 mimeType 을 Chrome 에서 사용가능한 `audio/webm` 으로 지정하였습니다.\
기능 동작 테스트 진행을 윈도우 OS의 Chrome 브라우저에서만 테스트를 진행하였습니다.

<div style="width: 100%; display: flex; justify-content: center;">
  <div>
    <img src="https://user-images.githubusercontent.com/84773475/172760347-10efdafb-1f22-4fee-b7e1-65906c468620.png" alt="record" width="300">
    <p style="text-align: center;">녹음 페이지</p>
  </div>
  <div>
    <img src="https://user-images.githubusercontent.com/84773475/172760368-cc45e6b2-19cf-4c21-86ef-b81455e27205.png" alt="recording" width="300">
    <p style="text-align: center;">녹음 진행중</p>
  </div>
</div>

```javascript
function startRecord() {
  try {
    // ...

    // MediaRecorder 인스턴스 생성시 옵션으로 mimeType 을 audio/webm 으로 지정
    const mediaRecorder = new MediaRecorder(stream, { mimeType: `audio/webm` })   
    mediaRecorder.start()

    // ...
  } catch (error) {
    // ...
  }
}
```

그러나 이후 `Mac Os의 Safari` 및 `모바일(ios)의 Safari`, `인앱 브라우저(Kakao)` 등의 환경에서 테스트를 진행하였을 때, 녹음 진행이 불가능한 이슈가 발생하였습니다.

&nbsp;

## 🛠 이슈 대응

관련 이슈에 대한 알아보던 중 일부 ios 와 Safari 의 경우 `mimeType`이 `audio/webm` 을 지원하지 않기 때문에 녹음이 진행되지 않는 문제였습니다.\
일부 ios와 Safari 에서도 녹음이 가능하게 하기 위하여 `mimeType`을 `audio/mp4` 를 지정하여 버그를 해결하였습니다.

서비스 최초 접속시 `navigator` 의 `userAgent` 를 이용하여 서비스에 접속한 브라우저를 감지하였습니다.\
그리고 모바일 OS와 브라우저에 따라 mimeType을 다르게 지정할 필요가 있었기에 상태 값으로 관리하였습니다.

```javascript
// _app.js
function MyApp() {
  useEffect(() => {
    // 안드로이드 모바일 기기인 경우 webm 지정
    if (/Android/i.test(navigator.userAgent)) {
      setState({...state, settings: { browser: { name: 'android', audioType: 'webm' }}})
    }
    // ios 모바일 기기인 경우 mp4 지정
    else if (/iPhone|iPad|iPod/i.test(navigator.userAgent)) {
      setState({...state, settings: { browser: { name: 'ios', audioType: 'mp4' }}})
    }
    // Windows 의 Chrome 브라우저인 경우 webm 지정
    else if (navigator.userAgent.indexOf("Chrome") > -1) {
      setState({...state, settings: { browser: { name: 'chrome', audioType: 'webm' }}})
    }
    // Mac OS 의 Safari 브라우저인 경우 mp4 지정
    else if (navigator.userAgent.indexOf("Safari") > -1) {
      setState({...state, settings: { browser: { name: 'safari', audioType: 'mp4' }}})
    }
  }, [])

  // ...
}

export default MyApp

// 녹음 관련 컴포넌트 내 함수
function startRecord() {
  try {
    // ...

    // 사용자의 OS 와 브라우저의 환경에 따라 mimeType 지정
    const mediaRecorder = new MediaRecorder(stream, { mimeType: `audio/${state.settings.browser.audioType}` })   
    mediaRecorder.start()

    // ...
  } catch (error) {
    // ...
  }
}
```

&nbsp;

## 📦 이슈 결과

해당 이슈를 해결하고 웹(Windows, Mac), 모바일(Android, ios)의 여러 브라우저에서 확인한 이용 가능 여부는 아래의 표와 같습니다.

<img width="643" alt="issue_result" src="https://user-images.githubusercontent.com/84773475/172836064-899b8dc8-df0f-4830-9ab3-e567f26bbb4a.png" style="display: block; margin: 0 auto;">

&nbsp;

## 📚 참고

- MDN 공식 문서 - <a href="https://developer.mozilla.org/en-US/" target="_blank">MDN</a>
