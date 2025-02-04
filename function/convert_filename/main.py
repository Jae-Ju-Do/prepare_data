from function.convert_filename import ConvertFilename

# 파일명 sha256 변환
if __name__ == "__main__":
    input_path = input("변경할 파일이 저장된 디렉토리 위치 : ")
    output_path = input("변경된 파일이 저장될 디렉토리 위치 : ")

    ConvertFilename(input_path, output_path)
