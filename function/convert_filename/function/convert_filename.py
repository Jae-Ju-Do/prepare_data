from .file_to_hash import FileToHash
import os
import shutil

# sha256으로 파일 명 변경
def ConvertFilename(input_dir, output_dir):
    try:
        if not os.path.exists(input_dir):
            print(f"입력 디렉토리 '{input_dir}'가 존재하지 않습니다.")
            return
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        files = os.listdir(input_dir)
        if not files:
            print(f"입력 디렉토리 '{input_dir}'에 파일이 없습니다.")
            return

        for file_name in files:
            input_file_path = os.path.join(input_dir, file_name)
            output_file_path = os.path.join(output_dir, file_name)

            if os.path.isfile(input_file_path):
                hash_name = FileToHash(input_file_path)
                if hash_name:
                    file_extension = os.path.splitext(file_name)[1]
                    if file_extension == ".exe" or file_extension == ".vir":
                        new_file_name = f"{hash_name}{file_extension}"
                        output_file_path = os.path.join(output_dir, new_file_name)
                        shutil.move(input_file_path, output_file_path)
                        print(f"파일 '{file_name}'를 '{new_file_name}'로 저장했습니다.")

    except Exception as e:
        print(f"오류 발생: {e}")