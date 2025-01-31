# 바이트 단위(4096) 별 데이터 동일성 확인
def CompareFile(file_a, file_b):
    try:
        with open(file_a, 'rb') as f1, open(file_b, 'rb') as f2:
            byte_a = f1.read(4096) 
            byte_b = f2.read(4096)
            
            while byte_a and byte_b:
                if byte_a != byte_b:
                    return False 
                byte_a = f1.read(4096)
                byte_b = f2.read(4096)
            
            if byte_a or byte_b:
                return False
        return True 
    except Exception as e:
        print(f"파일 비교 중 오류 발생: {e}")
        return False



