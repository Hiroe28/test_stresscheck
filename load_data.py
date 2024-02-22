import pandas as pd

def load_questions(filename):
    # CSVファイルを読み込む
    df = pd.read_csv(filename)
    questions = []

    for _, row in df.iterrows():
        question = {}
        question['質問ID'] = row['質問ID']
        question['質問文'] = row['質問文']
        
        # 選択肢とスコアを辞書形式で格納
        question['選択肢'] = {
            row['選択肢1']: row['選択肢1_スコア'],
            row['選択肢2']: row['選択肢2_スコア'],
            row['選択肢3']: row['選択肢3_スコア'],
            row['選択肢4']: row['選択肢4_スコア'],
        }
        
        questions.append(question)

    return questions
