import json
import os


# json 파일 list로 읽어오기 위한 utility 함수
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else [data]
    return []


# json 저장 위한 utility 함수
def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def merge_json(base_dir, output_dir):
    no_tag_list = []
    no_file_list = []
    tag_info = []

    for date_folder in os.listdir(base_dir):
        date_path = os.path.join(base_dir, date_folder)

        print(f"{date_folder} 순회중")

        if os.path.isdir(date_path):
            tag_path = os.path.join(date_path, "final_tag.json")  # JSON 파일 경로
            no_file_path = os.path.join(date_path, "no_file.json")
            no_tag_path = os.path.join(date_path, "no_tag.json")

            # ✅ JSON 파일 처리 (exe/final에 생성)
            tag_info.extend(load_json(tag_path))
            no_file_list.extend(load_json(no_file_path))
            no_tag_list.extend(load_json(no_tag_path))

    # === 최종 JSON 파일 생성 후 저장 ===
    output_tag = os.path.join(output_dir, "tag_info.json")
    output_no_file = os.path.join(output_dir, "no_file_list.json")
    output_no_tag = os.path.join(output_dir, "no_tag_list.json")

    save_json(output_tag, tag_info)
    save_json(output_no_file, no_file_list)
    save_json(output_no_tag, no_tag_list)

    print(f"✅ 데이터 병합 완료: {output_tag}, {output_no_file}, {output_no_tag}")
