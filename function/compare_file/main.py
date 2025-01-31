from compare_file import CompareFile

# 두 파일읟 동일성 여부 확인
if __name__ == "__main__":
    file_a = r".\87374fe6088ffe47d90d6de599aeeb8784ef0334c6d159fdeec2df3a2f92d9ba.exe" 
    file_b = r"..\87374fe6088ffe47d90d6de599aeeb8784ef0334c6d159fdeec2df3a2f92d9ba.exe"  

    if CompareFile(file_a, file_b):
        print("파일이 동일합니다.")
    else:
        print("파일이 다릅니다.")