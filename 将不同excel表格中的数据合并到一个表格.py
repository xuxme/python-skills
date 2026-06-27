import pandas as pd
import os

def merge_excel_files(source_folder, output_file):
    """
    将指定文件夹中的所有Excel文件数据合并到一个Excel文件中。
    
    :param source_folder: 包含源Excel文件的文件夹路径
    :param output_file: 合并后输出的Excel文件路径
    """
    # 获取文件夹中所有Excel文件
    all_files = [f for f in os.listdir(source_folder) if f.endswith('.xlsx') or f.endswith('.xls')]
    if not all_files:
        print("指定文件夹中没有找到任何Excel文件。")
        return
    
    # 初始化一个空的DataFrame用于存储所有数据
    merged_data = pd.DataFrame()
    
    # 遍历每个Excel文件并读取数据
    for file_name in all_files:
        file_path = os.path.join(source_folder, file_name)
        try:
            # 读取Excel文件（假设数据在第一个工作表中）
            data = pd.read_excel(file_path)
            # 将读取的数据追加到merged_data中
            merged_data = pd.concat([merged_data, data], ignore_index=True)
            print(f"已成功读取文件：{file_name}")
        except Exception as e:
            print(f"读取文件 {file_name} 时出错：{e}")
    
    # 将合并后的数据写入新的Excel文件
    try:
        merged_data.to_excel(output_file, index=False)
        print(f"所有数据已成功合并到文件：{output_file}")
    except Exception as e:
        print(f"写入目标文件时出错：{e}")

# 示例用法
source_folder = "你的源文件夹路径"  # 替换为包含源Excel文件的文件夹路径
output_file = "合并后的文件.xlsx"  # 替换为你想要保存的目标Excel文件路径
merge_excel_files(source_folder, output_file)