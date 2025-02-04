from json_check_dup import json_check_dup

import os
import json


# file_tag.json 파일과 zip 파일 이름 비교
def manipulate(root_path):
    for dirpath, dirnames, filenames in os.walk(root_path):
        if "zip_file" in dirnames:
            print(f"----------{os.path.basename(dirpath)}----------")

            file_dir = os.path.join(dirpath, "zip_file")
            json_path = os.path.join(dirpath, "file_tag.json")

            # 파일 이름 목록
            file_names = [os.path.splitext(f)[0] for f in os.listdir(file_dir)]

            # file_tag.json 에서 "file_name" 중복 체크
            tag_list = json_check_dup(json_path)

            # file_names 에는 존재하는데 tag_list의 'file_name' 에 없는 항목 no_tag.json 생성
            no_tag = [{"file_name": f} for f in file_names if not any(f == entry["file_name"] for entry in tag_list)]
            if no_tag:
                with open(os.path.join(dirpath, "no_tag.json"), "w", encoding="utf-8") as f:
                    json.dump(no_tag, f, indent=4, ensure_ascii=False)
                print("no_tag.json 저장 완료")

            # tag_list 의 'file_name' 에는 존재하는데 file_names 에 없는 항목 no_file.json 생성
            no_file = [entry for entry in tag_list if entry["file_name"] not in file_names]
            if no_file:
                with open(os.path.join(dirpath, "no_file.json"), "w", encoding="utf-8") as f:
                    json.dump(no_file, f, indent=4, ensure_ascii=False)
                print("no_file.json 저장 완료")

            # 공통으로 존재하는 항목 최종 tag.json 생성
            final_tag = [entry for entry in tag_list if entry["file_name"] in file_names]
            if final_tag:
                with open(os.path.join(dirpath, "final_tag.json"), "w", encoding="utf-8") as f:
                    json.dump(final_tag, f, indent=4, ensure_ascii=False)
                print("final_tag.json 저장 완료")

