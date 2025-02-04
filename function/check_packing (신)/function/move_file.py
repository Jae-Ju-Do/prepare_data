import os, shutil
from .detect_packer_with_die import DetectPackerWithDie

def MoveFile(dir_path, target_dirs):
    if not os.path.exists(dir_path):
        print(f"목표 디렉토리가 없습니다.")
    
    files = os.listdir(dir_path)
    if not files:
        print(f"목표 디렉토리({dir_path}) 내에 파일이 없습니다.")

    for target_dir in target_dirs.values():
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)

    try:
        for file_path in os.listdir(dir_path):
            full_path = os.path.join(dir_path, file_path)
            result = DetectPackerWithDie(full_path)
            print(f"--------{file_path}-----------")
            if result['result']: # 패커
                if result['packer'] == "UPX":
                    shutil.move(full_path, target_dirs["UPX 패커"])
                    print(f"{file_path} -> upx")
                else:
                    shutil.move(full_path, target_dirs["패커 또는 프로텍터"])
                    print(f"{file_path} -> packer")
            else:
                if result['message'] == "": # 일반 파일로 이동
                    shutil.move(full_path, target_dirs["일반 파일"])
                    print(f"{file_path} -> nomal")
                else: # 에러 코드 (unknown으로 이동)
                    shutil.move(full_path, target_dirs["알 수 없는 파일"])
                    print(f"{file_path} -> unknown")
    except Exception as e:
        print(f"오류 : {e}")