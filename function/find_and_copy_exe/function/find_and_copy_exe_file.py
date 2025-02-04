import os
import shutil

# 컴퓨터 시스템 내 전체 exe 파일 추출 코드
def FindAndCopyExeFile(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.exe'):
                source_file = os.path.join(root, file)
                dest_file = os.path.join(destination_directory, file)
                
                try:
                    shutil.copy2(source_file, dest_file)
                    message = f"복사 완료: {source_file} -> {dest_file}\n"
                    print(message)
                except Exception as e:
                    message = f"복사 실패: {source_file}, 에러: {e}\n"
                    print(message)
                    