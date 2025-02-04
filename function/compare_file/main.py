from function.compare_file import CompareFile

# 두 파일읟 동일성 여부 확인
if __name__ == "__main__":
    file_a = input("1. 파일 위치 입력 : ")
    file_b = input("2. 비교할 파일 위치 입력 : ")

    if CompareFile(file_a, file_b):
        print("파일이 동일합니다.")
    else:
        print("파일이 다릅니다.")