import os
import json
import shutil
import pandas as pd

# === 1. 필요한 디렉토리 생성 ===
os.makedirs("exe/final", exist_ok=True)
os.makedirs("exe/final/zip", exist_ok=True)

# 최종 병합 JSON 파일 경로
final_tags_path = "exe/final/tags.json"

# 기존 tags.json이 있으면 불러오기, 없으면 빈 리스트로 초기화
if os.path.exists(final_tags_path):
    with open(final_tags_path, "r", encoding="utf-8") as f:
        try:
            final_tags = json.load(f)
        except json.JSONDecodeError:
            final_tags = []
else:
    final_tags = []

# === 2. value/data/ 내부 날짜별 폴더 순회 (도현이가 작성한 구조 반영) ===
base_dir = "value/data"
b_data_list = []  # b 데이터 리스트 (file_name, tags)
c_data_list = []  # c 데이터 리스트 (file_name, has)

for date_folder in os.listdir(base_dir):
    date_path = os.path.join(base_dir, date_folder)

    if os.path.isdir(date_path):
        unzip_path = os.path.join(date_path, "unzip_file")  # JSON 파일이 있는 폴더
        zip_path = os.path.join(date_path, "zip_file")  # ZIP 파일이 있는 폴더

        # ✅ ZIP 파일 이동 (value/data/(날짜)/zip_file → exe/final/zip)
        if os.path.exists(zip_path):
            for zip_file in os.listdir(zip_path):
                zip_file_path = os.path.join(zip_path, zip_file)
                if os.path.isfile(zip_file_path) and zip_file.lower().endswith(".zip"):
                    shutil.move(zip_file_path, os.path.join("exe/final/zip", zip_file))
                    print(f"ZIP 파일 이동 완료: {zip_file}")
                    c_data_list.append({"file_name": zip_file.replace(".zip", ""), "has": 1})  # c 데이터 추가

        # ✅ JSON 파일 처리 (이름 변경 후 exe/final로 이동)
        if os.path.exists(unzip_path):
            for file in ["tag.json", "no_file.json", "no_tag.json"]:
                file_path = os.path.join(unzip_path, file)
                if os.path.exists(file_path):
                    target_name = file.replace("tag", "tag_list") \
                                      .replace("no_file", "no_file_list") \
                                      .replace("no_tag", "no_tag_list")
                    target_path = os.path.join("exe/final", target_name)

                    # 기존 데이터가 있으면 병합
                    if os.path.exists(target_path):
                        with open(target_path, "r", encoding="utf-8") as f:
                            try:
                                existing_data = json.load(f)
                            except json.JSONDecodeError:
                                existing_data = []
                    else:
                        existing_data = []

                    # 현재 파일의 데이터를 불러와 추가
                    with open(file_path, "r", encoding="utf-8") as f:
                        try:
                            new_data = json.load(f)
                        except json.JSONDecodeError:
                            new_data = []

                    # 병합된 데이터를 저장
                    merged_data = existing_data + new_data

                    with open(target_path, "w", encoding="utf-8") as f:
                        json.dump(merged_data, f, indent=4, ensure_ascii=False)

                    print(f"{file} → {target_path} 병합 완료")

        # ✅ file_tag.json 병합 (태그 정보 종합)
        file_tag_path = os.path.join(unzip_path, "file_tag.json")
        if os.path.exists(file_tag_path):
            try:
                with open(file_tag_path, "r", encoding="utf-8") as f:
                    tag_data = json.load(f)

                # 리스트 형태이면 추가
                if isinstance(tag_data, list):
                    b_data_list.extend(tag_data)
                elif isinstance(tag_data, dict):
                    b_data_list.append(tag_data)

                print(f"file_tag.json 병합 완료: {file_tag_path}")

            except Exception as e:
                print(f"file_tag.json 처리 중 오류 발생: {e}")

# === 3. b, c 데이터 병합 ===
b_data = pd.DataFrame(b_data_list) if b_data_list else pd.DataFrame(columns=["file_name", "tags"])
c_data = pd.DataFrame(c_data_list) if c_data_list else pd.DataFrame(columns=["file_name", "has"])

# c 데이터에 'has' 값 추가 (1로 설정)
c_data["has"] = 1

# file_name 기준으로 병합
merged_data = pd.merge(b_data, c_data, on="file_name", how="outer")

# === 4. 최종 JSON 파일 생성 ===
output_tag = "exe/final/tag.json"
output_no_file = "exe/final/no_file.json"
output_no_tag = "exe/final/no_tag.json"

tag_json = merged_data.dropna(subset=["tags", "has"]).to_dict(orient="records")  # b, c 모두 존재
no_file_json = merged_data[merged_data["has"].isna()][["file_name", "tags"]].dropna(subset=["tags"]).to_dict(orient="records")  # b만 존재
no_tag_json = merged_data[merged_data["tags"].isna()][["file_name"]].dropna(subset=["file_name"]).to_dict(orient="records")  # c만 존재

# 저장
with open(output_tag, "w", encoding="utf-8") as f:
    json.dump(tag_json, f, indent=4, ensure_ascii=False)

with open(output_no_file, "w", encoding="utf-8") as f:
    json.dump(no_file_json, f, indent=4, ensure_ascii=False)

with open(output_no_tag, "w", encoding="utf-8") as f:
    json.dump(no_tag_json, f, indent=4, ensure_ascii=False)

print(f"✅ 데이터 병합 완료: {output_tag}, {output_no_file}, {output_no_tag}")

# === 5. 최종 tags.json 저장 ===
with open(final_tags_path, "w", encoding="utf-8") as f:
    json.dump(final_tags, f, indent=4, ensure_ascii=False)

print(f"✅ 최종 tags.json 저장 완료: {final_tags_path}")
