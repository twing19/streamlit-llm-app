from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

st.title("lesson21:課題提出用アプリ")

st.write("##### 専門家1:法律に関する専門家")
st.write("法律に関する質問に、専門的に答えてくれます。")
st.write("##### 専門家2: 科学技術の専門家")
st.write("科学技術に関する質問に、専門的に答えてくれます。")

selected_item = st.radio(
    "専門家を選択してください。",
    ["法律に関する専門家", "科学技術に関する専門家"]
)

st.divider()

if selected_item == "法律に関する専門家":
    input_message = st.text_input(label="法律に関する質問を入力してください。")
else:
    input_message = st.text_input(label="科学技術に関する質問を入力してください。")



def get_llm_answer(input_message: str, selected_item: str) -> str:
    """
    入力テキストと選択値を受け取り、LLMからの回答を返す
    """
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    messages = [
        SystemMessage(content=f"[{selected_item}]として、以下の質問に専門的に答えてください。"),
        HumanMessage(content=input_message),
    ]
    result = llm(messages)
    return result.content

if st.button("実行"):
    st.divider()

    if selected_item == "法律に関する専門家":
        if input_message:
            st.write(f"法律に関する質問: **{input_message}**")
        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")
            st.stop()
    else:
        if input_message:
            st.write(f"科学技術に関する質問: **{input_message}**")
        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")
            st.stop()

    answer = get_llm_answer(input_message, selected_item)
    st.write(f"専門家の回答: {answer}")