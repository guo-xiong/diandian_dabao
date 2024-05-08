import os
import zipfile

def copy(path1,path2):
    file1 = open(path1, 'r',encoding='utf-8')
    os.makedirs(os.path.dirname(path2), exist_ok=True)
    file_new = open(path2, 'w',encoding='utf-8')
    #读取文件
    indexContent = file1.read()
    #写入文件
    file_new.write(indexContent)
    #关闭文件
    file1.close()
    file_new.close()
def replaceFile(writePath,readPath,newPath):
    with open(readPath, 'r',encoding='utf-8') as file:
        readFile = file.read()
    if readFile != "":
        os.makedirs(os.path.dirname(writePath), exist_ok=True)
        with open(writePath, 'r',encoding='utf-8') as file:
            filedata = file.read()
        with open(newPath, 'r',encoding='utf-8') as file:
            newPathdata = file.read()
        filedata = filedata.replace(readFile, newPathdata)
        with open(writePath, 'w',encoding='utf-8') as file:
            file.write(filedata)

#从str1一直删除直到str2
def remove_between_strings(input_str, start_str, end_str):
    start_index = input_str.find(start_str)
    end_index = input_str.find(end_str, start_index + len(start_str))

    if start_index != -1 and end_index != -1:
        result_str = input_str[:start_index] + input_str[end_index + len(end_str):]
        return result_str
    else:
        # 如果未找到指定的子字符串，则返回原始字符串
        return input_str

def create_zip_with_files(zip_filename, files_to_add):
    with zipfile.ZipFile(zip_filename, 'w',compression=zipfile.ZIP_DEFLATED) as myzip:
        for file_path in files_to_add:
            # 指定文件在 zip 文件中的路径
            arcname = os.path.basename(file_path)
            myzip.write(file_path, arcname=arcname)

#读取文件夹所有的文件
def list_files_in_folder(folder_path):
    # 使用 os.listdir() 获取文件夹中的所有文件和子文件夹
    files = os.listdir(folder_path)
    # 筛选出文件（而非文件夹）
    files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
    files_path = [os.path.join(folder_path, subfolder) for subfolder in files]
    return files_path

#读取文件夹所有的文件，返回完整路径
def list_subfolders(folder_path):
    # 使用 os.listdir() 获取文件夹中的所有文件和子文件夹
    contents = os.listdir(folder_path)

    # 筛选出子文件夹
    subfolders = [content for content in contents if os.path.isdir(os.path.join(folder_path, content))]

    # 获取子文件夹的完整路径
    subfolder_paths = [os.path.join(folder_path, subfolder) for subfolder in subfolders]

    return subfolder_paths

path = input("文件路径：")
#项目名
da_name = input("项目名:")
#当前分支路径
branch_path = "super-html\\2.3.4\\VM3\\"

print("Applovin")
indexFile = path + "\\Applovin.html"
newFile = path + "\\new\\"+da_name+"_Applovin.html"
copy(indexFile,newFile)
replaceFile(newFile,branch_path + "log.txt",branch_path+"link.txt")

print("Facebook")
indexFile = path + "\\Facebook"
files_in_folder = list_files_in_folder(indexFile)
#添加压缩文件
create_zip_with_files(path + "\\new\\" + da_name + "_Facebook.zip", files_in_folder)

print("Google")
indexFile = path + "\\Google"
files_in_folder = list_files_in_folder(indexFile)
#添加压缩文件
create_zip_with_files(path + "\\new\\" + da_name + "_Google.zip", files_in_folder)

print("Ironsource")
indexFile = path + "\\Ironsource.html"
newFile = path + "\\new\\"+da_name+"_Ironsource.html"
copy(indexFile,newFile)
# replaceFile(newFile,branch_path + "startGame.txt",branch_path+"startGame_new.txt")
# replaceFile(newFile,branch_path + "startGame_end.txt",branch_path+"startGame_end_new.txt")

print("Liftoff")
indexFile = path + "\\Liftoff"
files_in_folder = list_files_in_folder(indexFile)
#添加压缩文件
create_zip_with_files(path + "\\new\\" + da_name + "_Liftoff.zip", files_in_folder)

print("Moloco")
indexFile = path + "\\Moloco.html"
newFile = path + "\\new\\"+da_name+"_Moloco.html"
copy(indexFile,newFile)

print("Tiktok")
indexFile = path + "\\Tiktok"
files_in_folder = list_files_in_folder(indexFile)
#添加压缩文件
create_zip_with_files(path + "\\new\\" + da_name + "_Tiktok.zip", files_in_folder)

print("Unity")
indexFile = path + "\\Unity.html"
newFile = path + "\\new\\"+da_name+"_Unity.html"
copy(indexFile,newFile)
replaceFile(newFile,branch_path + "log.txt",branch_path+"link.txt")

print("Vungle")
indexFile = path + "\\Vungle"
files_in_folder = list_files_in_folder(indexFile)
#添加压缩文件
create_zip_with_files(path + "\\new\\" + da_name + "_Vungle.zip", files_in_folder)

print("完成")


