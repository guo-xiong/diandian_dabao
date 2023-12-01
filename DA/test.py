import os
import zipfile

def create_zip_with_files(zip_filename, files_to_add):
    with zipfile.ZipFile(zip_filename, 'w') as myzip:
        for file_path in files_to_add:
            # 指定文件在 zip 文件中的路径
            arcname = os.path.basename(file_path)
            myzip.write(file_path, arcname=arcname)

# 示例用法
zip_filename = 'example.zip'
files_to_add = ['DA\\config.json', 'DA\\da_link.txt', 'DA\\Facebook_head.txt']

create_zip_with_files(zip_filename, files_to_add)