import pandas as pd

# 파일명 리스트 반환
def GetFilename(csv_path, start_day, end_day, filetype):
    data = []
    df = pd.read_csv(csv_path, skiprows=0, encoding='ISO-8859-1', low_memory=False,  on_bad_lines='skip')
    
    print(df.columns)

    df['# "first_seen_utc"'] = pd.to_datetime(df['# "first_seen_utc"'], errors='coerce')
    
    start_day = pd.to_datetime(start_day).normalize() 
    end_day = pd.to_datetime(end_day).normalize() 
    
    df = df[(df['# "first_seen_utc"'] >= start_day) & (df['# "first_seen_utc"'] < end_day)]
    df = df[(df['file_type_guess'] == filetype)]
    
    for file_name in df['sha256_hash']:
        try:
            format_file_name = file_name.lstrip().replace('\"', "")
            data.append(format_file_name)
        except Exception as e:
            print(e)
            pass
    return data