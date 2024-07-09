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
    print(res)

def saveOrders(excel_path):

    tables = excel_table_byindex(excel_path, by_index=0)
    datalist = []

    for row in tables:
        time_fields = ['同步时间', '首销时间', '最后盘点时间', '创建时间', '修改时间', '交易时间', '付款时间', '递交时间', '派送时间', '发货时间', '最晚发货时间']
        for time_field in time_fields:
            if time_field in row.keys():
                if row[time_field]:
                    if row[time_field] != '任意时间':
                        if isinstance(row[time_field], float):
                            row[time_field] = xldate_as_datetime(row[time_field], 0).strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        row[time_field] = None
                else:
                    row[time_field] = None

        data = {
                    'spec_no': row['商家编码'],
                    'barcode': row['条码'],
                    'goods_no': row['货品编号'],
                    'goods_name': row['货品名称'],
                    'goods_short_name': row['货品简称'],
                    'goods_tag': row['货品标签'],
                    'spec_name': row['规格名称'],
                    'spec_id': row['规格码'],
                    'brand_name': row['品牌'],
                    'qa_num': row['已质检库存'],
                    'todeliver_order_num': row['未发货订单总数'],
                    'retail_price': row['零售价'],
                    'wholesale_price': row['批发价'],
                    'market_price': row['市场价'],
                    'member_price': row['会员价'],
                    'lowest_price': row['最低价'],
                    'goods_type': row['分类'],
                    'stock': row['库存'],
                    'weight': row['单品重量'],
                    # 'total_weight': row['库存总重量'],
                    'is_defective': row['残次品'],
                    'unit_name': row['单位'],
                    'aux_unit_name': row['辅助单位'],
                    'aux_remark': row['辅助说明'],
                    'deliverable_stock': row['可发库存'],
                    'usable_stock': row['可用库存'],
                    'min_alert_stock': row['警戒库存下限'],
                    'max_alert_stock': row['警戒库存上限'],
                    'unpaid_num': row['未付款量'],
                    'preorder_num': row['预订单量'],
                    'toreview_num': row['待审核量'],
                    'todeliver_num': row['待发货量'],
                    'lock_num': row['锁定量'],
                    'topurchase_num': row['待采购量'],
                    'purchase_ontheway_num': row['采购在途'],
                    'purchase_arrival_num': row['采购到货量'],
                    'totransfer_num': row['待调拨量'],
                    'totransout_num': row['待调出量'],
                    'toinstock_num': row['其他待入库量'],
                    'tooutstock_num': row['其他待出库量'],
                    'transfer_ontheway_num': row['调拨在途'],
                    'purchase_return_num': row['采购退货'],
                    'sale_return_ontheway_num': row['销售退货在途量'],
                    'produce_tooutstock_num': row['生产待出库量'],
                    'produce_toinstock_num': row['生产待入库量'],
                    'toqa_num': row['待质检量'],
                    # 'outside_stock_num': row['外部库存'],
                    # 'stock_diff': row['库存差异'],
                    # 'sync_time': row['同步时间'],
                    'remark': row['备注'],
                    'goods_remark': row['货品备注'],
                    'specgoods_remark': row['单品备注'],
                    'tax_rate': row['税率'],
                    # 'onsale_time': row['首销时间'],
                    'spec_created': row['单品创建时间'],
                    'last_inventory_time': row['最后盘点时间'],
                    'actual_stock_num': row['实际库存'],
                    'actual_todelivery_stock_num': row['实际可发库存'],
                    'img_url': row['图片链接'],
                    'img': row['图片'],
                    'major_supplier': row['主供应商'],
                    'custom_stock_one': row['自定义库存1'],
                    'custom_stock_two': row['自定义库存2'],
                    'custom_stock_three': row['自定义库存3'],
                    'custom_stock_four': row['自定义库存4'],
                    'custom_stock_five': row['自定义库存5'],
                }
        datalist.append(data)
    savedatatourl(datalist, base_url + 'orders/stockdetails', excel_path)
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



