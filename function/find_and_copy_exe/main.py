from function.find_and_copy_exe_file import FindAndCopyExeFile

# 디바이스 내 exe 파일 추출
if __name__ == "__main__":
    source_directory = r"C:\\"  
    destination_directory = r"..\..\value\extract_exe_file"  
    FindAndCopyExeFile(source_directory, destination_directory)
