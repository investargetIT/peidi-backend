import json

import requests
import xlrd

# from peidiexcel import base_url

# 组合装导入
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
    url = base_url + 'goods/suiteGoodsRec'
    res = requests.post(url, data=data).content.decode()
    print(json.loads(res)['code'], json.loads(res)['errormsg'])


def main():
    # path = r'C:\Users\wjk13\Desktop\组合装gbk.xlsx'
    path = '/code/utils/组合装.xlsx'
    tables = excel_table_byindex(path)
    i = 1

    for row in tables:
        data = {
            'suite_name': row['组合装名称'],
            'suite_short_name': row['组合装简称'],
            'suite_no': row['商家编码'],
            'barcode': row['条码'],

            'brand_name': row['品牌'],
            'goods_type': row['类别'],
            'retail_price': row['零售价'],
            'wholesale_price': row['批发价'],
            'member_price': row['会员价'],
            'market_price': row['市场价'],
            'weight': row['重量'],
            'remark': row['备注'],

            'goods_name': row['单品名称'],
            'goods_no': row['单品货品编号'],
            'spec_no': row['单品商家编码'],
            'spec_name': row['单品规格名称'],
            'ware_code': row['外部编码'],
            'num': row['数量'],
            'fixed_price': row['固定售价'],
            'ratio': row['金额占比'],
            'is_fixed_price': row['是否固定价格'],
        }
        if i >= 0:
            # time.sleep(1)
            savedatatourl(data)
        print(i)
        i = i + 1


#









if __name__=="__main__":
    main()