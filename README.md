# OpenAI Streamlit 챗봇

`gpt-4o-mini`를 사용하는 간단한 스트리밍 챗봇입니다.

## 로컬 실행

```bash
pip install -r requirements.txt
streamlit run app.py
```

로컬에서 실행할 때는 프로젝트 루트에 `.streamlit/secrets.toml` 파일을 만들고 다음처럼 입력합니다.

```toml
OPENAI_API_KEY = "sk-..."
```

## Streamlit Community Cloud 배포

1. 이 폴더를 GitHub 저장소에 push합니다.
2. Streamlit Community Cloud에서 저장소와 `app.py`를 연결합니다.
3. 앱의 **Settings → Secrets**에 아래 내용을 추가합니다.

```toml
OPENAI_API_KEY = "sk-..."
```

API 키는 소스 코드나 GitHub 저장소에 직접 입력하지 마세요.
