import streamlit as st
from load_data import load_questions
from calculate_scores import calculate_score

def main():
    st.title("ストレスチェック")

    # 質問をロード
    questions = load_questions("questions.csv")

    # ユーザーの回答を保持する辞書
    answers = {}

    # 質問ごとにUIを作成
    for question in questions:
        q_id, q_text, choices = question['質問ID'], question['質問文'], question['選択肢']
        answers[q_id] = st.radio(q_text, list(choices.keys()))

    if st.button("回答を提出する"):
        score = calculate_score(answers, questions)
        st.write(f"あなたのスコアは {score} です。")
        
        # スコアに基づいてメッセージを表示
        if score > 20:
            st.write("あなたは高ストレス者に該当します。医師の面接指導を受けていただくことをおすすめします。")
        else:
            st.write("高ストレスのリスクは低いようです")

if __name__ == "__main__":
    main()
