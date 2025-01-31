from unzip_file import UnzipFile

# zip 파일 압축 해제 (추후 변경 예정)
if __name__ == "__main__":
    zip_path = r"..\data\zip_file"
    unzip_path = r"..\data\unzip_file"
    UnzipFile(zip_path, unzip_path)
