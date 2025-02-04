from .save_malware_to_zip import SaveMalwareToZip

def GetTagsInFilename(filenaem_sha256, dir_save_path, csv_path, json_path):
    print(f"파일 개수 : {len(filenaem_sha256)}")
    file_num = 0
    for filename in filenaem_sha256:
        print(f"------- {file_num} : {filename} --------")
        SaveMalwareToZip(filename, dir_save_path, csv_path, json_path)
        file_num += 1