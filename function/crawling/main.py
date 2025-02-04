from function.get_filename import GetFilename
from function.get_tags_in_filename import GetTagsInFilename
import os, json

# malware bazaar에서 zip 파일 다운로드 (크롤링)
if __name__ == "__main__":
    # 입력
    csv_path = r"..\..\value\csv" 
    csv_path = os.path.join(csv_path, input("파일명: ") + ".csv")
    start_day = input("시작 날짜: ")
    end_day = input("  끝 날짜: ")
    select_filetype = input("{0 : exe}, {1 : elf} : ")
    filetype = {"0": " \"exe\"", "1": " \"elf\""}

    # 경로 지정
    save_path =  start_day + "~" + end_day
    if select_filetype == "1":
        save_path += " (elf)"
    elif select_filetype == "0":
        save_path += " (exe)"
    else:
        print("잘못된 번호입니다.")
        exit(0)

    dir_path = r"..\..\value\data"
    dir_save_path = os.path.join(dir_path, save_path)
    
    zip_path = os.path.join(dir_save_path, "zip_file")
    unzip_path = os.path.join(dir_save_path, "unzip_file")
    
    # 디렉토리 초기 생성
    try:
        os.makedirs(dir_save_path, exist_ok=True)
        os.makedirs(zip_path, exist_ok=True)
        os.makedirs(unzip_path, exist_ok=True)
    except Exception as e:
        print(f"디렉토리 생성 오류: {e}")


    # json 초기 생성
    json_path = os.path.join(dir_save_path, "file_tag.json")
    if not os.path.exists(json_path):
        with open(json_path, 'w') as json_file:
            initial_json_data = []
            json.dump(initial_json_data, json_file, indent=4)

    # 크롤링에 이용될 파일명 list화
    filename_sha256 = GetFilename(csv_path, start_day, end_day, filetype[select_filetype])
    
    # 크롤링 : tag 정보, 파일 저장
    GetTagsInFilename(filename_sha256, dir_save_path, csv_path, json_path)

   
