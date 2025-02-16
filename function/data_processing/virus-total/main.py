import os
import pandas as pd

from get_threat_category import crawl


if __name__ == '__main__':
    # input_path = r"../../../exe/final/virus-total-input.csv"
    input_path = r"../../../exe/final/" + input("input 파일명: ") + ".csv"
    # result_path = r"../../../exe/final/virus-total-result2.csv"
    result_path = r"../../../exe/final/" + input("result 파일명: ") + ".csv"
    # none_path = "../../../exe/final/virus-total-none.csv"
    none_path = "../../../exe/final/" + input("none 파일명: ") + ".csv"

    input_data = pd.read_csv(input_path)

    print(f"------데이터 개수 : {len(input_data)}------- ")
    num = 0
    for index, row in input_data.iterrows():
        file_name = row["file_name"]
        file_type = row["type"]

        num += 1
        print(f"----- {num} : {file_name} -----")
        crawl_result = crawl(file_name)
        print(f"crawl result : {crawl_result}")

        if crawl_result is None or crawl_result == "Notfound":
            input_data.at[index, "type"] = "Notfound"
            input_data.to_csv(input_path, index=False)
            continue
        elif crawl_result == "no_tag":
            if os.path.exists(none_path):
                none_data = pd.read_csv(none_path)
            else:
                none_data = pd.DataFrame(columns=["file_name", "type"])
            none_row = pd.DataFrame({"file_name": [file_name], "type": ["none"]})
            none_data = pd.concat([none_data, none_row], ignore_index=True)

            none_data.to_csv(none_path, index=False)
            input_data = input_data.drop(index)
            input_data.to_csv(input_path, index=False)
            print(f"None 데이터로 저장됨.")
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

