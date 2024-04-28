import json

import requests
import xlrd

# from peidiexcel import base_url

# 单品列表导入
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
    url = base_url + 'goods/specGoods'
    res = requests.post(url, data=data).content.decode()
    print(json.loads(res)['code'], json.loads(res)['errormsg'])


def main():
    # path = r'C:\Users\wjk13\Desktop\单品列表gbk.xlsx'
    path = '/code/utils/单品列表.xlsx'
    tables = excel_table_byindex(path)
    i = 1


    for row in tables:
        data = {
            'spec_no': row['商家编码'],
            'goods_no': row['货品编号'],
            'goods_name': row['货品名称'],
            'short_name': row['简称'],
            'goods_type': row['分类'],
            'brand_name': row['品牌'],
            'spec_name': row['规格名称'],
            'spec_code': row['规格码'],
            'barcode': row['主条码'],
            'wms_process_mask': row['仓库流程'],
            'lowest_price': row['最低价'],
            'retail_price': row['零售价'],

            'wholesale_price': row['批发价'],
            'member_price': row['会员价'],
            'market_price': row['市场价'],
            'single_price1': row['单品金额1'],
            'single_price2': row['单品金额2'],
            'validity_days': row['有效期天数'],
            'length': row['长[厘米]'],
            'width': row['宽[厘米]'],
            'height': row['高[厘米]'],
            'weight': row['重量[千克]'],
            'tax_code': row['税务编码'],
            'sn_type': row['启用序列号'],
            'goods_label': row['货品标签'],
            'large_type': row['大件类别'],
            'unit_name': row['基本单位'],
            'aux_unit_name': row['辅助单位'],
            'img_url': row['图片'],
            # 'tax_rate': row['税率'],
            'spec_modified': row['修改时间'],
            'spec_created': row['创建时间'],

        }
        if i >= 0:
            # time.sleep(1)
            savedatatourl(data)
        print(i)
        i = i + 1


#









if __name__=="__main__":
    main()