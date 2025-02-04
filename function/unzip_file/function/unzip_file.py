import os
import pyzipper

# zip 파일 압축 해제 (추후 변경 예정)
def UnzipFile(zip_path, unzip_path):
    try:
        if not os.path.exists(zip_path):
            print(f"디렉토리가 존재하지 않습니다.")
            return
        
        for file_name in os.listdir(zip_path):
            if file_name.endswith(".zip"):
                zip_file = os.path.join(zip_path, file_name)
                with pyzipper.AESZipFile(zip_file) as zf:
                    zf.pwd = b'infected'
                    zf.extractall(unzip_path)
    except Exception as e:
        print(e)
