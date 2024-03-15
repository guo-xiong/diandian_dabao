import os
import platform
import zipfile
import shutil
# def copy(path1,path2):
#     file1 = open(path1, 'r',encoding='utf-8')
#     os.makedirs(os.path.dirname(path2), exist_ok=True)
#     file_new = open(path2, 'w',encoding='utf-8')
#     #读取文件
#     indexContent = file1.read()
#     #写入文件
#     file_new.write(indexContent)
#     #关闭文件
#     file1.close()
#     file_new.close()
# def replaceFile(readPath,writePath,new):
#     with open(readPath, 'r',encoding='utf-8') as file:
#         readFile = file.read()
#     if readFile != "":
#         os.makedirs(os.path.dirname(writePath), exist_ok=True)
#         with open(writePath, 'r',encoding='utf-8') as file:
#             filedata = file.read()
#         filedata = filedata.replace(readFile, new)
#         with open(writePath, 'w',encoding='utf-8') as file:
#             file.write(filedata)

# def create_zip_with_files(zip_file_name, files_to_zip):
#     with zipfile.ZipFile(zip_file_name, 'w',compression=zipfile.ZIP_DEFLATED) as zipf:
#     # 将每个文件添加到 ZIP 文件中
#         # for file in files_to_zip:
#             zipf.write(file_path)
def zip_folder(folder_path, zip_name):
    # 创建一个新的 ZIP 文件
    with zipfile.ZipFile(zip_name, 'w',compression=zipfile.ZIP_DEFLATED) as zipf:
        # 递归地将文件夹中的所有文件添加到 ZIP 文件中
        git = folder_path+ '\\.git'
        build = folder_path+ '\\build'
        temp = folder_path+ '\\temp'
        vscode = folder_path+ '\\.vscode'
        for root, dirs, files in os.walk(folder_path):
            if git not in root:
                if build not in root:
                    if temp not in root:
                        if vscode not in root:
                        # print (root)
                            for file in files:
                                file_path = os.path.join(root, file)
                                zipf.write(file_path, os.path.relpath(file_path, folder_path))
        print(zipf)
        print("//////////////////")


begin_path = input("文件路径：")
endPath = input("保存路径：")
# 获取当前目录下的所有文件夹
folders = [f for f in os.listdir(begin_path) if os.path.isdir(os.path.join(begin_path, f))]
for folder in folders:
    print(folder)
    file_path = begin_path + "\\" + folder
    print(file_path)
    file_name = os.path.basename(file_path)
    zip_folder(file_path, file_name+".zip")
    newZIp = os.path.dirname(os.path.abspath(__file__)) + "\\" + file_name + ".zip"
    print(newZIp)
    shutil.move(newZIp, endPath)
    print("完成"+"file_name")
print("完成")

