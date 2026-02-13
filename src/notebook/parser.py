from bronze import csv_reader ,parquet_reader,json_reader
paths = "/Volumes/test_cata/new_schema/vol/"

csv_files = []
parquet_files = []
json_files = []

for item in dbutils.fs.ls(paths):

    file_path = item.path.lower()

    if file_path.endswith(".csv"):
        csv_files.append(item.path)

    if file_path.endswith(".parquet"):
        parquet_files.append(item.path)

    if file_path.endswith(".json"):
        json_files.append(item.path)

# Now process in batch
csv_reader(csv_files[0])
parquet_reader(parquet_files[0])
json_reader(json_files[0])