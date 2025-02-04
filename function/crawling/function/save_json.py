import json

# json에 파일명, 태그 정보 저장
def SaveJson(json_path, tag_info):
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
        
        json_data.append(tag_info)
        
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=True)
        
        print(f"'{tag_info.get('file_name')}'을 포함한 행을 JSON에 저장했습니다.")
        
    except Exception as e:
        print(f"JSON 저장 오류: {e}")            
            