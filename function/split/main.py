from split_csv import split_by_moth, split_csv

if __name__ == '__main__':
# 월 단위 분할
#     csv_path = r"../../value/csv/full.csv"
#     split_by_moth(csv_path)

# 6개로 분할
    csv_name = input("Enter csv file name: ")
    split_by = int(input("Enter split by: "))
    split_csv(csv_name, split_by)
