import streamlit as st
from openai import OpenAI


st.set_page_config(
    page_title="OpenAI 챗봇",
    page_icon="💬",
    layout="centered",
)


def get_api_key() -> str | None:
    """Read the API key from Streamlit Community Cloud secrets."""
    try:
        return st.secrets["OPENAI_API_KEY"]
    except (KeyError, FileNotFoundError):
        return None


st.title("💬 OpenAI 챗봇")
st.caption("gpt-4o-mini · Streamlit Community Cloud")

with st.sidebar:
    st.subheader("설정")
    st.write("사용 모델: `gpt-4o-mini`")
    st.write("API 키는 Streamlit Secrets에서 안전하게 불러옵니다.")
    if st.button("대화 초기화", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

api_key = get_api_key()
if not api_key:
    st.error("OPENAI_API_KEY가 설정되지 않았습니다.")
    st.info(
        "Streamlit Community Cloud의 앱 설정에서 Secrets를 열고 "
        '`OPENAI_API_KEY = "sk-..."` 형식으로 추가해 주세요.'
    )
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        try:
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
                stream=True,
            )
            for chunk in stream:
                content = chunk.choices[0].delta.content or ""
                full_response += content
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )
        except Exception as exc:
            response_placeholder.error(f"응답을 가져오는 중 오류가 발생했습니다: {exc}")
