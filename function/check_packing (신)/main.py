from function.move_file import MoveFile

if __name__ == "__main__":
    dir_path = input("파일이 저장된 디렉토리 위치 입력 : ")
    target_dirs = {
        "UPX 패커": input("UPX 파일이 저장될 디렉토리 위치 입력 : "),
        "패커 또는 프로텍터": input("패커 파일이 저장될 디렉토리 위치 입력 : "),
        "일반 파일": input("일반 파일이 저장될 디렉토리 위치 입력 : "),
        "알 수 없는 파일": input("알 수 없는 파일이 저장될 디렉토리 위치 입력 : ")
    }

    MoveFile(dir_path, target_dirs)