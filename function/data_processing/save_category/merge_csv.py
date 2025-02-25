import pandas as pd
import os


root_path = r"../../../exe/final/all-results"
final_df = pd.DataFrame()

num = 0
for subdir, dirs, files in os.walk(root_path):
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(subdir, file)
            print(f"{num} : {file}")

            file_df = pd.read_csv(file_path)
            file_df = file_df[['file_name', 'type']]
            final_df = pd.concat([final_df, file_df], ignore_index=True)
            print("final-results.csv에 병합 완료.")
            num += 1

final_df.sort_values(by=['file_name'], ascending=True, inplace=True)
final_df.to_csv(os.path.join(root_path,"final-results.csv"), index=False)
print("병합 종료.")

