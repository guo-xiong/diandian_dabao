import os

path = input("文件路径：")
#logo文件
logo = path + '/splash.png'
#删除logo文件
os.remove(logo)
#style-mobile.css文件
style_mobile = path + '/style-mobile.css'
#检索style-mobile.css文件中的"url(./splash.png)"并替换为"url(../splash.png)"
with open(style_mobile, 'r') as file:
        filedata = file.read()
filedata = filedata.replace('url(./splash.png)', '')
with open(style_mobile, 'w') as file:
        file.write(filedata)


def replaceFile(readPath,writePath,new):
    with open(readPath, 'r') as file:
        readFile = file.read()
    if readFile != "":
        with open(writePath, 'r') as file:
            filedata = file.read()
        filedata = filedata.replace(readFile, new)
        with open(writePath, 'w') as file:
            file.write(filedata)
#main.js文件
main = path + '/main.js'
replaceFile("enableAutoFullScreen.txt",main,'')
replaceFile("jsList.txt",main,'')
with open("loadScene_new.txt", 'r') as file:
    readFile = file.read()
    replaceFile("loadScene_old.txt",main,readFile)

#结束




