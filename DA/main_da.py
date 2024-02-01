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
def replaceFile(readPath,writePath,new):
    with open(readPath, 'r',encoding='utf-8') as file:
        readFile = file.read()
    if readFile != "":
        os.makedirs(os.path.dirname(writePath), exist_ok=True)
        with open(writePath, 'r',encoding='utf-8') as file:
            filedata = file.read()
        filedata = filedata.replace(readFile, new)
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

# 示例用法
# zip_filename = 'example.zip'
# files_to_add = ['DA\\config.json', 'DA\\da_link.txt', 'DA\\Facebook_head.txt']

# create_zip_with_files(zip_filename, files_to_add)



path = input("文件路径：")
#项目名
da_name = input("项目名:")

indexFile = path + "\\index.html"
res = path + "\\res.js"

print("Applovin")
#创建一个新文件Applovin.html
newFile = path + "\\"+da_name+"_Applovin.html"
copy(indexFile,newFile)
with open("DA\\da_link.txt",'r',encoding='utf-8') as file:
    da_link = file.read()
    replaceFile("DA\\log.txt",newFile,da_link)



print("Facebook")
#Facebook
newFile = path + "\\"+da_name+"_Facebook\\index.html"
copy(indexFile,newFile)
copy(res,path + "\\"+da_name+"_Facebook\\res.js")
#删除第一个script
with open(newFile, 'r',encoding='utf-8') as file:
    filedata = file.read()
    filedata = remove_between_strings(filedata,"<script","</script>")
    with open(newFile, 'w',encoding='utf-8') as file:
            file.write(filedata)
            
with open("DA\\Facebook_tz.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DA\\log.txt",newFile,new)

with open("DA\\Facebook_head_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DA\\Facebook_head.txt",newFile,new)

#添加压缩文件
create_zip_with_files(path + "\\"+da_name+"_Facebook.zip", [newFile,path + "\\"+da_name+"_Facebook\\res.js"])


print("Ironsource")
#Ironsource
newFile = path + "\\"+da_name+"_Ironsource.html"
copy(indexFile,newFile)
with open("DA\\Ironsource_tz.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DA\\log.txt",newFile,new)
with open("DA\\Ironsource_head_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DA\\Ironsource_head.txt",newFile,new)
with open("DA\\Ironsource_end_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DA\\Ironsource_end.txt",newFile,new)

print("Google")
#Google
newFile = path + "\\"+da_name+"_Google\\index.html"
copy(indexFile,newFile)
with open("DA\\Google_tz.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DA\\log.txt",newFile,new)

with open("DA\\Google_head_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DA\\Google_head.txt",newFile,new)

#添加压缩文件
create_zip_with_files(path + "\\"+da_name+"_Google.zip", [newFile])

print("Tiktok")
#Tiktok
newFile = path + "\\"+da_name+"_Tiktok\\index.html"
copy(indexFile,newFile)
copy("DA\\config.json",path + "\\"+da_name+"_Tiktok\\config.json")
with open("DA\\Tiktok_tz.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DA\\log.txt",newFile,new)

with open("DA\\Tiktok_head_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DA\\Tiktok_head.txt",newFile,new)

print("Liftoff")
newFile = path + "\\"+da_name+"_Liftoff\\index.html"
copy(indexFile,newFile)
replaceFile(newFile,"DA\\log.txt","DA\\da_link.txt")
#添加压缩文件
create_zip_with_files(path + "\\"+da_name+"_Liftoff.zip", [newFile])

#添加压缩文件
create_zip_with_files(path + "\\"+da_name+"_Tiktok.zip", [newFile,path + "\\"+da_name+"_Tiktok\\config.json"])

print("Moloco")
newFile = path + "\\"+da_name+"_Moloco.html"
copy(indexFile,newFile)
replaceFile("DA\\log.txt",newFile,new)
replaceFile("DA\\moloco_old1.txt",newFile,"DA\\moloco_new1.txt")