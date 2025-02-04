import os
import shutil


def move_zip(base_dir, zipfile_dir):
    for date_folder in os.listdir(base_dir):
        date_path = os.path.join(base_dir, date_folder)

        print(f"{date_folder} 순회중")

        if os.path.isdir(date_path):
            zip_path = os.path.join(date_path, "zip_file")  # ZIP 파일이 있는 폴더

            # ✅ ZIP 파일 이동 (value/data/(날짜)/zip_file → exe/final/zip)
            if os.path.exists(zip_path):
                for zip_file in os.listdir(zip_path):
                    zip_file_path = os.path.join(zip_path, zip_file)

                    if os.path.isfile(zip_file_path) and zip_file.lower().endswith(".zip"):
                        dest_path = os.path.join(zipfile_dir, zip_file)

                        # 파일명 중복 방지
                        if os.path.exists(dest_path):
                            print(f"⚠️ 이미 존재하는 ZIP 파일: {dest_path} 이동하지 않음.")
                            continue

                        try:
                            shutil.move(zip_file_path, dest_path)
                            print(f"ZIP 파일 이동 완료: {zip_file}")
                        except Exception as e:
                            print(f"❌ ZIP 파일 이동 실패: {zip_file}, 오류: {e}")