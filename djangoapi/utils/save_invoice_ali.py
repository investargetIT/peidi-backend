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
            if 'Duplicate' not in fail['errmsg']:
                fails.append(fail)
            else:
                duplicate_fails.append(fail['errmsg'])
        if len(fails) > 0:
            print('非重复造成的失败', len(fails), fails)
        if len(duplicate_fails) > 0:
            print('重复造成的失败', len(duplicate_fails), duplicate_fails)

def saveOrders(excel_path):

    tables = excel_table_byindex(excel_path, by_index=0)
    datalist = []

    for row in tables:
        time_fields = ['开票日期']
        for time_field in time_fields:
            if time_field in row.keys():
                if row[time_field]:
                    if row[time_field] != '任意时间':
                        if isinstance(row[time_field], float):
                            row[time_field] = xldate_as_datetime(row[time_field], 0).strftime('%Y-%m-%d %H:%M:%S')
                        else:
                            row[time_field] = row[time_field].strip().replace('/', '-')
                    else:
                        row[time_field] = None
                else:
                    row[time_field] = None
        
        float_fields = ["数量", "单价"]
        for float_field in float_fields:
            if row[float_field]:
                row[float_field] = "{:.4f}".format(float(row[float_field]))
        
        if row['店铺名称'] == 'smartbones旗舰店':
            row['店铺名称'] = '杭州-天猫-smartbones旗舰店'
        elif row['店铺名称'] == '哈宠宠物用品专营店':
            row['店铺名称'] = '上海-天猫-哈宠宠物用品专营店'
        elif row['店铺名称'] == '好适嘉旗舰店':
            row['店铺名称'] = '杭州-天猫-好适嘉旗舰店'
        elif row['店铺名称'] == '佩蒂旗舰店':
            row['店铺名称'] = '杭州-天猫-佩蒂旗舰店'
        elif row['店铺名称'] == '千百仓宠物用品专营店':
            row['店铺名称'] = '上海-天猫-千百仓宠物用品专营店'
        
        data = {
                    'trade_no': row['订单id'],
                    'invoice_time': row['开票日期'],
                    'shop_name': row['店铺名称'],
                    'invoice_category': row['发票种类'],
                    'invoice_type': row['发票类型'],
                    'invoice_no': row['发票号码发票代码'],
                    'seller_tax_no': row['税号'],
                    'seller_corp_name': row['企业名称'],
                    'invoice_title': row['发票抬头'],
                    'payer_tax_no': row['付款人税号'],
                    'invoice_tax': row['总税额'],
                    'invoice_amount': row['发票总金额'],
                    'red_to_blue': row['红票对应蓝票'],
                    'remark': row['备注'],
                    'goods_name': row['商品名称'],
                    'goods_model': row['商品型号'],
                    'goods_unit': row['商品单位'],
                    'goods_price': row['单价'],
                    'goods_num': row['数量'],
                    'goods_amount_without_tax': row['不含税金额'],
                    'goods_tax': row['税额'],
                    'goods_total_amount': row['总金额'],
                    'tax_rate': row['税率'],
        }
        datalist.append(data)
    savedatatourl(datalist, base_url + 'finance/invoice', excel_path)
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



