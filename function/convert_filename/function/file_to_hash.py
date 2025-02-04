import hashlib

# 파일명을 sha256으로 변경
def FileToHash(file_name, hash_algo="sha256"):
    try:
        hash_func = hashlib.new(hash_algo)
        with open(file_name, "rb") as f:
            data = f.read()
            hash_func.update(data)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"해시 생성 중 오류 발생: {e}")
        return None
    
