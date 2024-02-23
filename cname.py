import os

# 设置文件夹路径
folder_path = './'
start=input("输入第一个文件数字:")
# 获取文件夹中所有文件名
files = os.listdir(folder_path)


# 遍历文件并重命名
for index, file_name in enumerate(files):
    # 构建新文件名
    try:
        new_file_name = str(20240205001 -int(start)+ int(os.path.splitext(file_name)[0])).zfill(10) + os.path.splitext(file_name)[1]
    except:
        continue
    # 构建文件路径
    old_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_file_name)
    
    # 重命名文件
    os.rename(old_file_path, new_file_path)