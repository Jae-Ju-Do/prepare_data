import pandas as pd
import ast


if __name__ == '__main__':
    csv_path = r"../../../exe/final/all-results/" + input("csv 파일명: ") + ".csv"
    save_path = r"../../../exe/final/tag-lists/" + input("result 파일명: ") + ".csv"

    df = pd.read_csv(csv_path)
    df['type'] = df['type'].apply(ast.literal_eval)

    all_types = sorted(set(t for types in df['type'] for t in types))
    result_dict = {t: [] for t in all_types}

    for _, row in df.iterrows():
        for t in row['type']:
            result_dict[t].append(row['file_name'])

    max_length = max(len(v) for v in result_dict.values())

    for t in all_types:
        result_dict[t] += [''] * (max_length - len(result_dict[t]))

    result_df = pd.DataFrame(result_dict)
    result_df.to_csv(save_path, index=False)

