import os
import scipy.io
import pandas as pd
import numpy as np


def mat_to_csv(mat_file_path, csv_file_path):
    # 读取.mat文件
    mat_data = scipy.io.loadmat(mat_file_path)

    # 将.mat文件的数据转换为DataFrame
    for key, value in mat_data.items():
        if isinstance(value, (np.ndarray, np.generic)) and key[0] != '_':
            df = pd.DataFrame(value)
            df.to_csv(csv_file_path, index=False, header=None)  # 在这里设置header=None以避免保存列名
            break


def remove_first_row(csv_file_path):
    df = pd.read_csv(csv_file_path, header=None)
    df = df.iloc[0:]
    df.to_csv(csv_file_path, index=False, header=None)


def main():
    source_folder = 'inclined_Telesat/delay'
    target_folder = 'inclined_Telesat_csv/delay'

    # 如果目标文件夹不存在，则创建它
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        if filename.endswith('.mat'):
            mat_file_path = os.path.join(source_folder, filename)
            csv_file_name = "result" + filename.replace('.mat', '.csv')
            csv_file_path = os.path.join(target_folder, csv_file_name)

            # 转换.mat文件为.csv文件
            mat_to_csv(mat_file_path, csv_file_path)
            # 删除.csv文件的第一行数据
            remove_first_row(csv_file_path)

            print(f"Converted {filename} to {csv_file_name}")


if __name__ == '__main__':
    main()
