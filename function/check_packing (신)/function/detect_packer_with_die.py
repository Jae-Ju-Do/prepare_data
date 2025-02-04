import subprocess, json

def DetectPackerWithDie(file_path):
    die_path = "C:\\Users\\USER\\Desktop\\die_win64_portable_3.10_x64\\diec.exe"
    result_dict = { "result": False, "packer": "", "message": "" } 
    try:
        process_result = subprocess.run(
            [die_path, "-j", "--heuristicscan", "--verbose", file_path],
            capture_output=True,
            text=True
        )

        if process_result.returncode == 0:
            start_index = process_result.stdout.find("{")
            end_index = process_result.stdout.rfind("}")
            if start_index != -1 and end_index != -1:
                json_output = process_result.stdout[start_index:end_index + 1]
                die_output = json.loads(json_output)
                detects = die_output.get("detects", [])
                for detect in detects:
                    for value in detect.get("values", []):
                        if value["name"] == "Compressed or packed data":
                            result_dict["result"] = True
                            if "upx" in value.get("string", "").lower():
                                result_dict["packer"] = "UPX"
                            else:
                                result_dict["packer"] = "Other packer"
            else:
                result_dict["message"] = f"오류: JSON 형식의 결과를 찾을 수 없습니다."
        else:
            result_dict["message"] = f"DiE 실행 중 오류: {process_result.stderr}"
    except Exception as e:
        result_dict["message"] = f"오류: {str(e)}"
    finally:
        return result_dict