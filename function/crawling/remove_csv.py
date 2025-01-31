import pandas as pd
import os

# csv내 파일 데이터 제거
def RemoveCsv(filename, csv_path):
    try:
        df = pd.read_csv(csv_path, encoding='utf-8')
        os.remove(csv_path)
        df_filtered = df[df['sha256_hash'] != " \"" + filename + "\""]
        df_filtered.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"'{filename}'을 포함한 행이 CSV에서 삭제되었습니다.")
    except Exception as e:
        print(f"CSV 제거 오류: {e}")