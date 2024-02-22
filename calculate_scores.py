def calculate_score(answers, questions):
    total_score = 0

    # ユーザーの回答と質問データを照合してスコアを計算
    for question in questions:
        q_id = question['質問ID']
        user_answer = answers[q_id]
        question_score = question['選択肢'][user_answer]
        total_score += question_score

    return total_score
