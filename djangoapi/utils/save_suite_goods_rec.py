import os, requests
import pandas as pd

# 组合装导入
base_url = 'http://localhost:8000'
auth_token = os.environ.get('DJANGO_AUTH_TOKEN')

def excel_table_byindex(file):
    list = []
    df = pd.read_excel(file, keep_default_na=False)
    df = df.replace('_x000D_\n', '', regex=True)
    for row in df.values:
        data = {}
        for idx, x in enumerate(row):
            data[df.columns.values[idx]] = x
        list.append(data)
    return list

def savedatatourl(data):
    url = base_url + '/goods/suite-goods-rec/'
    res = requests.post(url, json=data, headers={
        "Authorization": f"Token {auth_token}",
    })
    res.raise_for_status()
    res = res.content.decode()
    print(res)

def main():
    path = '/code/utils/组合装.xlsx'
    tables = excel_table_byindex(path)
    datalist = []
    for row in tables:
        data = {
            'suite_no': row['商家编码'],
            'suite_name': row['组合装名称'],
            'brand_name': row['品牌'],
            'goods_type': row['类别'],
            'spec_no': row['单品商家编码'],
            'goods_no': row['单品货品编号'],
            'goods_name': row['单品名称'],
            'spec_name': row['单品规格名称'],
            'num': row['数量'],
            'fixed_price': row['固定售价'],
            'ratio': row['金额占比'],
            'is_fixed_price': row['是否固定价格'],
        }
        datalist.append(data)
    savedatatourl(datalist)

if __name__=="__main__":
    main()
