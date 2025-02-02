import json


def json_check_dup(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)

    no_duplicate = []
    dup = {}
    dup_logs = [] # 중복된 항목 로그

    for entry in data:
        file_name = entry["file_name"]

        # 중복 체크
        if file_name in dup:
            dup_logs.append(  # 중복 발견 시 로그를 append
                f"{file_name} 중복 발견\n"
                f"기존 데이터: {json.dumps(dup[file_name], ensure_ascii=False, indent=3)}\n"
                f"중복 데이터: {json.dumps(entry, ensure_ascii=False, indent=3)}"
            )
        else:
            no_duplicate.append(entry)
            dup[file_name] = entry

    # 로그 출력
    if dup_logs:
        print("\n".join(dup_logs))
    else:
        print("file_name.json에 중복된 'file_name'이 없습니다.")
    print(f"{len(data) - len(no_duplicate)}개 중복 제거됨.")

    return no_duplicate

