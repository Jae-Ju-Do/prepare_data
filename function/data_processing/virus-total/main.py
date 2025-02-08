import os
import pandas as pd

from get_threat_category import crawl


if __name__ == '__main__':
    input_path = r"../../../exe/final/virus-total-input.csv"
    result_path = r"../../../exe/final/virus-total-result.csv"
    input_data = pd.read_csv(input_path)

    print(f"------데이터 개수 : {len(result_path)}------- ")
    num = 0
    for index, row in input_data.iterrows():
        file_name = row["file_name"]
        file_type = row["type"]
        num += 1
        print(f"----- {num} : {file_name} -----")
        crawl_result = crawl(file_name)
        print(f"crawl result : {crawl_result}")

        if crawl_result is None:
            continue

        input_data = input_data.drop(index)

        if os.path.exists(result_path):
            result_data = pd.read_csv(result_path)
        else:
            result_data = pd.DataFrame(columns=["file_name", "type"])

        new_row = pd.DataFrame({"file_name": [file_name], "type": [crawl_result]})
        result_data = pd.concat([result_data, new_row], ignore_index=True)

        input_data.to_csv(input_path, index=False)
        result_data.to_csv(result_path, index=False)


    # print(crawl("ab9aa981e24b6dbe183fff66d17e38fbb7ac1fa54fd1dbf3c4878c65ff18efa4"))

