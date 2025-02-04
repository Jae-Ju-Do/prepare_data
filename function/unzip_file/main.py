from function.unzip_file import UnzipFile

# zip 파일 압축 해제 (추후 변경 예정)
if __name__ == "__main__":
    zip_path = input("zip 파일 위치 입력 : ")
    unzip_path = input("unzip 파일 위치 입력 : ")
    UnzipFile(zip_path, unzip_path)
