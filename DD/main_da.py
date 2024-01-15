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
            fileDDta = file.read()
        fileDDta = fileDDta.replace(readFile, new)
        with open(writePath, 'w',encoding='utf-8') as file:
            file.write(fileDDta)

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

def create_zip_with_files(zip_filename, files_to_aDD):
    with zipfile.ZipFile(zip_filename, 'w',compression=zipfile.ZIP_DEFLATED) as myzip:
        for file_path in files_to_aDD:
            # 指定文件在 zip 文件中的路径
            arcname = os.path.basename(file_path)
            myzip.write(file_path, arcname=arcname)

# 示例用法
# zip_filename = 'example.zip'
# files_to_aDD = ['DD\\config.json', 'DD\\DD_link.txt', 'DD\\Facebook_head.txt']

# create_zip_with_files(zip_filename, files_to_aDD)



path = input("文件路径：")
#项目名
DD_name = input("项目名:")

indexFile = path + "\\index.html"
res = path + "\\res.js"

print("Applovin")
#创建一个新文件Applovin.html
newFile = path + "\\"+DD_name+"_Applovin.html"
copy(indexFile,newFile)
with open("DD\\DD_link.txt",'r',encoding='utf-8') as file:
    DD_link = file.read()
    replaceFile("DD\\log.txt",newFile,DD_link)


print("Ironsource")
#Ironsource
newFile = path + "\\"+DD_name+"_Ironsource.html"
copy(indexFile,newFile)
with open("DD\\Ironsource_tz.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DD\\log.txt",newFile,new)
with open("DD\\Ironsource_head_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DD\\Ironsource_head.txt",newFile,new)
with open("DD\\Ironsource_end_new.txt",'r',encoding='utf-8') as file:
    new = file.read()
    replaceFile("DD\\Ironsource_end.txt",newFile,new)

print("Liftoff")
newFile = path + "\\"+DD_name+"_Liftoff\\index.html"
copy(indexFile,newFile)
with open("DD\\DD_link.txt",'r',encoding='utf-8') as file:
    DD_link = file.read()
    replaceFile("DD\\log.txt",newFile,DD_link)
#添加压缩文件
create_zip_with_files(path + "\\"+DD_name+"_Liftoff.zip", [newFile])