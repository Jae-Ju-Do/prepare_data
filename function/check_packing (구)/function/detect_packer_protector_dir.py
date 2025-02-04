import os
import shutil
from .detect_packer_protector_filename import DetectPackerProtectorFilename

def DetectPackerProtectorDir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        files = os.listdir(dir_path)
        if not files:
            print(f"디렉토리 '{dir_path}'에 파일이 없습니다.")
            return

        target_dirs = {
            "UPX 패커": "..\\file\\upx",
            "패커 또는 프로텍터": "..\\file\\packer",
            "일반 파일": "..\\file\\nomal",
        }

        for target_dir in target_dirs.values():
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

        for file_name in files:
            dir_file_path = os.path.join(dir_path, file_name)
            
            if os.path.isfile(dir_file_path):
                file_extension = os.path.splitext(file_name)[1]
                if file_extension in [".exe", ".vir"]:
                    try:
                        result = DetectPackerProtectorFilename(dir_file_path)
                        target_dir = target_dirs.get(result)
                        if target_dir:
                            shutil.move(dir_file_path, target_dir)
                            # print(f"파일 이동: {dir_file_path} -> {target_dir}")
                        else:
                            shutil.move(dir_file_path, "..\\file\\unkown")
                            # print(f"알 수 없는 결과: {result}, 파일 이동하지 않음.")
                    except Exception as e:
                        shutil.move(dir_file_path, "..\\file\\unkown")
                        # print(f"파일 처리 중 오류 발생: {file_name}, 에러: {e}")

    except Exception as e:
        print(f"오류 발생: {e}")
        pass
