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

path = input("文件路径：")
#项目名
IM_name = input("项目名:")

indexFile = path + "\\index.html"
res = path + "\\res.js"




print("Applovin")
#创建一个新文件Applovin.html
newFile = path + "\\"+IM_name+"_Applovin.html"
copy(indexFile,newFile)
with open("IM(2d)\\IM_link.txt",'r',encoding='utf-8') as file:
    IM_link = file.read()
    replaceFile("IM(2d)\\log.txt",newFile,IM_link)

print("Facebook")
#Facebook
newFile = path + "\\"+IM_name+"_Facebook\\index.html"
copy(indexFile,newFile)
copy(res,path + "\\"+IM_name+"_Facebook\\res.js")
#删除第一个script
with open(newFile, 'r',encoding='utf-8') as file:
    filedata = file.read()
    filedata = remove_between_strings(filedata,"<script","</script>")
with open(newFile, 'w',encoding='utf-8') as file:
    file.write(filedata)
with open("IM(2d)\\Facebook_tz.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("IM(2d)\\log.txt",newFile,new)
with open("IM(2d)\\Facebook_head_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("IM(2d)\\Facebook_head.txt",newFile,new)
    zip_file_path = path + "\\"+IM_name+"_Facebook.zip"

create_zip_with_files(zip_file_path,[path + "\\"+IM_name+"_Facebook\\index.html",path + "\\"+IM_name+"_Facebook\\res.js"])


print("Ironsource")
#Ironsource
newFile = path + "\\"+IM_name+"_Ironsource.html"
copy(indexFile,newFile)
with open("IM(2d)\\Ironsource_tz.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("IM(2d)\\log.txt",newFile,new)
with open("IM(2d)\\Ironsource_head_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("IM(2d)\\Ironsource_head.txt",newFile,new)
with open("IM(2d)\\Ironsource_end_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("IM(2d)\\Ironsource_end.txt",newFile,new)
    

print("Google")
#Google
newFile = path + "\\"+IM_name+"_Google\\index.html"
copy(indexFile,newFile)
with open("IM(2d)\\Google_tz.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("IM(2d)\\log.txt",newFile,new)

with open("IM(2d)\\Google_head_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("IM(2d)\\Google_head.txt",newFile,new)
    zip_file_path = path + "\\"+IM_name+"_Google.zip"

create_zip_with_files(zip_file_path,[path + "\\"+IM_name+"_Google\\index.html"])

print("Moloco")
newFile = path + "\\"+IM_name+"_Moloco.html"
copy(indexFile,newFile)
with open("IM(2d)\\moloco_tz.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("IM(2d)\\log.txt",newFile,new)
with open("IM(2d)\\moloco_new1.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("IM(2d)\\moloco_old1.txt",newFile,new)

