import datetime
import json
import os
import traceback

import requests
import xlrd
from xlrd.xldate import xldate_as_datetime

# from peidiexcel import base_url


base_url = 'http://localhost:8000/'
auth_token = os.environ.get('DJANGO_AUTH_TOKEN')

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


def savedatatourl(data, url, excel_path):
    print(excel_path, '总记录数', len(data))
    res = requests.post(url, data=json.dumps(data), headers={
        "Content-Type": "application/json",
        "Authorization": f"Token {auth_token}",
    })
    res.raise_for_status()
    res = res.content.decode()
    res = json.loads(res)
    fails = []
    duplicate_fails = []
    if len(res['result']['success']) > 0:
        print('导入成功', len(res['result']['success']))
    if len(res['result']['fail']) > 0:
        print('导入失败', len(res['result']['fail']))
        for fail in res['result']['fail']:
            if 'already exists' in json.dumps(fail['errmsg']):
                duplicate_fails.append(fail['errmsg'])
            else:
                fails.append(fail)
        if len(fails) > 0:
            print('非重复造成的失败', len(fails))
        if len(duplicate_fails) > 0:
            print('重复造成的失败', len(duplicate_fails))

def saveOrders(excel_path):

    tables = excel_table_byindex(excel_path, by_index=0)
    datalist = []

    for row in tables:

        data = {
                    'type': row['采购分类.分类名称'],
                    'material_no': row['料号'],
                    'goods_name': row['品名'],
                    'invoice_goods_name': row['开票品名'],
                    'goods_no': row['货号'],
                    'no_product_series': row['重编编号(产品系列)'],
                    'barcode': row['条码'],
                    'unit': row['库存单位.名称'],
                    'feature': row['料品形态属性'],
                    'brand': row['品牌'],
                    'weight': row['(单件重)'],
                }
        datalist.append(data)
    savedatatourl(datalist, base_url + 'finance/pd_material_no', excel_path)
    return len(tables)







def saveExcel(excel_path, err_path, end_path):
    record_num = 0
    if os.path.isfile(excel_path):
        try:
            record_num = saveOrders(excel_path)
        except Exception as e:
            print('异常', e)
            os.rename(excel_path, err_path)
        else:
            os.rename(excel_path, end_path)
    return record_num


def split_array(array, num_subarrays):
    array_length = len(array)
    subarray_length = array_length // num_subarrays

    subarrays = []
    start_index = 0
    end_index = subarray_length

    for i in range(num_subarrays):
        if end_index + subarray_length > array_length-1:
            end_index = array_length
        subarray = array[start_index:end_index]
        subarrays.append(subarray)

        start_index = end_index
        end_index += subarray_length

    return subarrays

def task(task_files, file_folder_path, err_folder_path, end_folder_path):
    total = 0
    for file in task_files:
        excel_path = os.path.join(file_folder_path, file)
        err_path = os.path.join(err_folder_path, file)
        end_path = os.path.join(end_folder_path, file)
        total += saveExcel(excel_path, err_path, end_path)
    print('总行数', total)


if __name__=="__main__":
    import threading
    threading_num = 1
    # home_path = r'C:\Users\wjk13\Desktop\peidi-data\销售出库明细\2023'
    home_path = '/code/utils'
    all_folder_path = os.path.join(home_path, 'all')
    err_folder_path = os.path.join(home_path, 'err')
    end_folder_path = os.path.join(home_path, 'end')
    all_files = split_array(os.listdir(all_folder_path), threading_num)
    for task_files in all_files:
        thread = threading.Thread(target=task, args=(task_files, all_folder_path, err_folder_path, end_folder_path))
        thread.start()



