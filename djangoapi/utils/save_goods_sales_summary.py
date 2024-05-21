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

start_date = '2024-04-01'
end_date = '2024-04-30'

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
            if 'Duplicate' not in fail['errmsg']:
                fails.append(fail)
            else:
                duplicate_fails.append(fail['errmsg'])
        if len(fails) > 0:
            print('非重复造成的失败', len(fails))
        if len(duplicate_fails) > 0:
            print('重复造成的失败', len(duplicate_fails))

def saveOrders(excel_path):

    tables = excel_table_byindex(excel_path, by_index=0)
    datalist = []

    for row in tables:

        data = {
                    'start_date': start_date,
                    'end_date': end_date,
                    'spec_no': row['商家编码'],
                    'major_supplier': row['主供应商'],
                    'shop_name': row['店铺'],
                    'brand_name': row['品牌'],
                    'goods_type': row['分类'],
                    'goods_no': row['货品编号'],
                    'goods_name': row['货品名称'],
                    'spec_name': row['规格名称'],
                    'goods_category': row['货品类别'],
                    'average_price': row['均价'],
                    'retail_price': row['零售价'],
                    'ship_num': row['发货总量'],
                    'return_num': row['退货入库量（原退货总量）'],
                    'return_count_num': row['退货入库结算量'],
                    'sales_num': row['实际销售量'],
                    'ship_amount': row['发货总金额'],
                    'sales_amount': row['销售总金额'],
                    'sales_amount_unknown_cost': row['未知成本销售总额'],
                    'return_amount': row['退货总金额（结算）'],
                    'actual_sales_amount': row['实际销售额'],
                    'gift_sales_num': row['赠品销量'],
                    'post_amount': row['邮费'],
                    'post_cost': row['邮资成本'],
                    'ship_refund_num': row['系统发货但平台退款量'],
                    'ship_refund_amount': row['系统发货但平台退款金额'],
                    'abnormal_warehouse_sales_num': row['异常仓销量'],
                    'refund_stockin': row['退货总金额（入库）'],
                }
        datalist.append(data)
    savedatatourl(datalist, base_url + 'finance/goods_sales_summary', excel_path)
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



