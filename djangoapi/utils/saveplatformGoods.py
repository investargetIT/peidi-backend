import json
import time

import requests
import xlrd

# from peidiexcel import base_url

# 平台货品导入
base_url = 'http://localhost:8000/'


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_index：表的索引
def excel_table_byindex(file, colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list


def savedatatourl(data):
    url = base_url + 'goods/platformGoods'
    res = requests.post(url, data=data).content.decode()
    code = json.loads(res)['code']
    if code != 1000:
        detail = json.loads(res)['detail']
        print(detail)

def main():
    # path = r'C:\Users\wjk13\Desktop\平台货品gbk.xlsx'
    path = '/code/utils/平台货品.xlsx'
    tables = excel_table_byindex(path)
    i = 1

    for row in tables:
        data = {
            'shop_name': row['店铺'],
            'platform_goods_name': row['平台货品名称'],
            'platform_spec_name': row['平台规格名称'],
            'platform_spec_no': row['平台商家编码'],
            'platform_outer_id': row['平台货品编号'],
            'img_url': row['图片链接'],
            'platform_spec_outer_id': row['平台规格编码'],
            'platform_spec_type': row['平台类目'],
            'platform_goods_id': row['平台货品ID'],
            'platform_spec_id': row['平台规格ID'],
            'platform_price': row['平台价格'],
            'platform_status': row['平台状态'],

            'match_target_type': row['是否组合装'],
            'spec_no': row['商家编码'],
            'outer_id': row['货品编号'],
            'spec_code': row['规格码'],
            'spec_name': row['规格名称'],
            'retail_price': row['零售价'],
            'goods_name': row['货品名称'],
            'goods_type': row['货品分类'],
            'goods_brand': row['货品品牌'],
            'stock_num': row['平台库存'],
            'hold_stock': row['平台库存占用量'],
        }
        # if i >= 12782:
            # time.sleep(1)
        savedatatourl(data)
        # print(i)
        i += 1

#









if __name__=="__main__":
    main()