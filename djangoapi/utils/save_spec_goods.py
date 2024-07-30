import os, requests
import pandas as pd

# 单品列表导入
base_url = 'http://localhost:8000/'
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
    url = base_url + 'goods/spec-goods/'
    res = requests.post(url, json=data, headers={
        "Authorization": f"Token {auth_token}",
    })
    res.raise_for_status()
    res = res.content.decode()
    print(res)

def main():
    path = '/code/utils/单品列表.xlsx'
    tables = excel_table_byindex(path)
    datalist = []
    for row in tables:
        data = {
            'spec_no': row['商家编码'],
            'goods_no': row['货品编号'],
            'goods_name': row['货品名称'],
            'goods_type': row['分类'],
            'brand_name': row['品牌'],
            'spec_name': row['规格名称'],
            'barcode': row['主条码'],
            'validity_days': row['有效期天数'],
            'u9_no': row['U9料号'],
            'tax_rate': row['税率'],
            'spec_modified': row['修改时间'],
            'spec_created': row['创建时间'],
        }
        datalist.append(data)
    savedatatourl(datalist)

if __name__=="__main__":
    main()
