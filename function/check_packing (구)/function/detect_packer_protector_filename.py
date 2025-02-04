from .calculate_entropy import CalculateEntropy
import pefile
import os

def DetectPackerProtectorFilename(file_path): #차후 데이터 수정 가능 (업그레이드)
    try:
        pe = pefile.PE(file_path)
        result = "일반 파일"
        for section in pe.sections:
            section_name = section.Name.decode('utf-8').strip('\x00')
            entropy = CalculateEntropy(section.get_data())

            if "UPX" in section_name.upper():
                result = "UPX 패커"
                break

            if entropy > 7.0:
                result = "패커 또는 프로텍터"
        
        # import가 없으면 패커 혹은 프로텍터로 판별
        if not hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
            result = "패커 또는 프로텍터"

        pe.close()
        return result
    except Exception as e:
        return f"오류 발생: {(e)}"
