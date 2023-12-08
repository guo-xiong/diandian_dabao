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

path = input("文件路径：")
#项目名
da_name = input("项目名:")
indexFile = path + "\\index.html"
res = path + "\\res.js"
#当前分支路径
branch_path = "GOF_2.3\\"

print("Applovin")
newFile = path + "\\"+da_name+"_Applovin.html"
copy(indexFile,newFile)
replaceFile(newFile,branch_path + "log.txt",branch_path+"link.txt")

print("Facebook")
newFile = path + "\\"+da_name+"_Facebook\\index.html"
copy(indexFile,newFile)
copy(res,path + "\\"+da_name+"_Facebook\\res.js")
#删除第一个script
with open(newFile, 'r',encoding='utf-8') as file:
    filedata = file.read()
    filedata = remove_between_strings(filedata,"<script","</script>")
    with open(newFile, 'w',encoding='utf-8') as file:
            file.write(filedata)

replaceFile(newFile,branch_path + "head.txt",branch_path+"res.txt")
replaceFile(newFile,branch_path + "log.txt",branch_path+"facebook_tz.txt")
#添加压缩文件
create_zip_with_files(path + "\\"+da_name+"_Facebook.zip", [newFile,path + "\\"+da_name+"_Facebook\\res.js"])

print("Google")
newFile = path + "\\"+da_name+"_Google\\index.html"
copy(indexFile,newFile)
replaceFile(newFile,branch_path + "log.txt",branch_path+"Google_tz.txt")
replaceFile(newFile,branch_path + "head.txt",branch_path+"google_new_head.txt")
#添加压缩文件
create_zip_with_files(path + "\\"+da_name+"_Google.zip", [newFile])

print("Ironsource")
newFile = path + "\\"+da_name+"_Ironsource.html"
copy(indexFile,newFile)
replaceFile(newFile,branch_path + "head.txt",branch_path+"lr_new_head.txt")
replaceFile(newFile,branch_path + "log.txt",branch_path+"lr_tz.txt")
replaceFile(newFile,branch_path + "lr_old1.txt",branch_path+"lr_new1.txt")

print("Liftoff")
newFile = path + "\\"+da_name+"_Liftoff\\index.html"
copy(indexFile,newFile)
replaceFile(newFile,branch_path + "log.txt",branch_path+"link.txt")
#添加压缩文件
create_zip_with_files(path + "\\"+da_name+"_Liftoff.zip", [newFile])

print("Moloco")
newFile = path + "\\"+da_name+"_Moloco.html"
copy(indexFile,newFile)
replaceFile(newFile,branch_path + "log.txt",branch_path+"moloco_tz.txt")
replaceFile(newFile,branch_path + "moloco_old1.txt",branch_path+"moloco_new1.txt")

print("Tiktok")
newFile = path + "\\"+da_name+"_Tiktok\\index.html"
copy(indexFile,newFile)
copy(branch_path+"config.json",path + "\\"+da_name+"_Tiktok\\config.json")
replaceFile(newFile,branch_path + "head.txt",branch_path+"tiktok_head.txt")
replaceFile(newFile,branch_path + "log.txt",branch_path+"Tiktok_tz.txt")
#添加压缩文件
create_zip_with_files(path + "\\"+da_name+"_Tiktok.zip", [newFile,path + "\\"+da_name+"_Tiktok\\config.json"])

print("Unity")
newFile = path + "\\"+da_name+"_Unity.html"
copy(indexFile,newFile)
replaceFile(newFile,branch_path + "log.txt",branch_path+"link.txt")
replaceFile(newFile,branch_path + "unity_old1.txt",branch_path+"unity_new1.txt")

print("Vungle")
newFile = path + "\\"+da_name+"_Vungle.html"
copy(indexFile,newFile)


