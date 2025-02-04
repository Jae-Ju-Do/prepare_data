import json
import os


def create_tag_list(root_dir):
    tag_info_path = os.path.join(root_dir, 'tag_info.json')
    tag_list_path = os.path.join(root_dir, 'tag_list.json')

    try:
        with open(tag_info_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not data or not isinstance(data, list):
            print("json 파일 형식이 list가 아니거나 데이터가 없습니다.")
            return

        tag_list = sorted(set(
            tag for item in data if isinstance(item, dict)
            and "tags" in item and isinstance(item["tags"], list)
            for tag in item["tags"] if tag
        ))
        with open(tag_list_path, 'w', encoding='utf-8') as f:
            json.dump(tag_list, f, ensure_ascii=False, indent=4)
        print("tag_list.json 저장 완료.")

    except FileNotFoundError:
        print("❌ tag_info.json 파일이 존재하지 않습니다.")
    except json.decoder.JSONDecodeError:
        print("❌ tag_info.json 파일이 올바른 JSON 형식이 아닙니다.")
    except Exception as e:
        print(f"❌ 알 수 없는 오류 발생: {e}")
