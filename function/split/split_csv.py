import os
import pandas as pd


# 너무 큰 csv 파일 소분용
def split_csv(csv_path):
    save_path = r"../../value/csv"
    os.makedirs(save_path, exist_ok=True)

    df = pd.read_csv(csv_path, encoding='ISO-8859-1', low_memory=False, on_bad_lines='skip')
    total_rows = len(df)
    chunk_size = total_rows // 6

    for i in range(6):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < 5 else total_rows  # 마지막 청크는 나머지 포함
        chunk_df = df.iloc[start_idx:end_idx]
        output_path = os.path.join(save_path, f"2020-11_{i + 1}.csv")
        chunk_df.to_csv(output_path, index=False, encoding='ISO-8859-1')
        print(f"Saved: {output_path}")


# 월 별로 csv 분할
def split_by_moth(csv_path):
    save_path = r"../../value/csv/split_result"
    os.makedirs(save_path, exist_ok=True)
    columns_to_keep = ['# "first_seen_utc"', 'sha256_hash', 'file_type_guess']

    # 원본 csv 읽어온 후 날짜 정보 추출
    df = pd.read_csv(csv_path, skiprows=8, encoding='ISO-8859-1', low_memory=False, on_bad_lines='skip')
    df['# "first_seen_utc"'] = pd.to_datetime(df['# "first_seen_utc"'], errors='coerce')

    # 필요한 정보만 남기기
    df["year_month"] = df['# "first_seen_utc"'].dt.strftime('%Y-%m')
    df_filtered = df[df['file_type_guess'].isin([' "exe"', ' "elf"'])]
    filtered_df = df_filtered[columns_to_keep + ["year_month"]]

    for month, group in filtered_df.groupby(['year_month']):
        if pd.notna(month):
            month_str = month if isinstance(month, str) else str(month[0])
            result_csv = os.path.join(save_path, f"{month_str}.csv")
            group.drop(columns=["year_month"], inplace=True)
            group.to_csv(result_csv, index=False)
            print(f"{result_csv} 로 저장되었습니다.")
