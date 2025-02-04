import os

from merge_json import merge_json
from move_zip import move_zip


if __name__ == '__main__':
    # === 필요한 디렉토리 생성 ===
    base_dir = "../../../value/data"
    output_dir = "../../../exe/final"
    zipfile_dir = "../../../exe/final/zip"

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(zipfile_dir, exist_ok=True)

    # zip 파일 이동
    # move_zip(base_dir, zipfile_dir)

    # 최종 json 파일 생성
    merge_json(base_dir, output_dir)
