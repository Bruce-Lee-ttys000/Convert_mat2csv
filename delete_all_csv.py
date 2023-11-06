import os
import shutil

# 设置目录路径
directory = 'inclined_Telesat_csv/delay'

# 检查目录是否存在
if os.path.exists(directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            # 如果是文件，则删除
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            # 如果是目录，则删除该目录及其中的所有内容
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
else:
    print(f"The directory {directory} does not exist.")
