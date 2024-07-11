
    # df = pd.read_excel('C:/Users/pd/Desktop/财务需求/旺店通/订单明细/订单明细.xlsx')
    # output_folder = 'C:/Users/pd/Desktop/财务需求/旺店通/订单明细/all'
import pandas as pd
import os

# 读取原始Excel文件
df = pd.read_excel('/code/utils/to_chunk.xlsx')

# 定义要存储拆分文件的文件夹路径
output_folder = '/code/utils/all'

# 如果文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 计算需要拆分的数量
n = len(df) // 10000 + (1 if len(df) % 10000 else 0)

# 用于给每个新文件命名的计数器
file_counter = 1

# 遍历DataFrame并拆分
for i in range(0, len(df), 10000):
    # 获取当前批次的数据
    chunk = df.iloc[i:i + 10000]

    # 创建新的Excel文件名，可以根据需要自定义命名规则
    output_file = os.path.join(output_folder, f'data_1chunk_{file_counter}.xlsx')

    # 将拆分的数据保存到新的Excel文件中
    chunk.to_excel(output_file, index=False)

    # 增加文件计数器，用于下一个文件的命名
    file_counter += 1
