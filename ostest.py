import  os
path = "G:/test/tiaozhanbeitest"
files = os.listdir(path)
files_count = 0
for i in files:
    if os.path.isfile(os.path.join(path, i)):
        files_count += 1
imgurl = str(files_count+1)+".jpg"
print(imgurl)

