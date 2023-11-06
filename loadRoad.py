import os

def write_file_paths(directory, output_file):
    file_paths = []

    # 获取目标文件夹下所有文件的路径
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    # 将文件路径写入txt文件
    with open(output_file, 'w') as f:
        for file_path in file_paths:
            f.write(file_path + '\n')

    print('文件路径已保存到', output_file)

# 输入目标文件夹和输出文件路径
directory = 'D:/Programme/SmartCity/yolov7-main/datasets/bike/images/train'
output_file = 'D:/Programme/SmartCity/yolov7-main/datasets/bike/train.txt'

write_file_paths(directory, output_file)