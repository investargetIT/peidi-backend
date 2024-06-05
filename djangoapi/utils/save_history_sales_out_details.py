import datetime
import json
import os
import traceback

import requests
import xlrd
from xlrd.xldate import xldate_as_datetime

# from peidiexcel import base_url


base_url = 'http://api.peidigroup.cn/'
auth_token = "b66e429324071cc2bc3fea621c542d4c498e2aa8"


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
        # if ',' in row['原始单号']:
        #     continue
        time_fields = ['下单时间', '支付时间', '送货时间', '创建时间', '修改时间', '交易时间', '付款时间', '递交时间', '派送时间', '发货时间', '赠品方式']
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

        if row["订单邮费"] == "无权限":
            row ["订单邮费"] = None

        ##  历史销售出库明细
        data = {
            'trade_no': row['订单编号'],
            'tid': row['原始单号'],
            'oid': row['原始子单号'],
            'otid': row['子单原始单号'],
            'order_type': row['订单类别'],
            'pay_account': row['支付账号'],
            'stockout_no': row['出库单编号'].replace('\n', '').replace('\r', ''),
            'warehouse': row['仓库'],
            'shop_name': row['店铺'],
            'status_type': row['出库单状态'],
            'stockout_status': row['出库状态'],
            'spec_no': row['商家编码'],
            'goods_no': row['货品编号'],
            'goods_name': row['货品名称'],
            'goods_short_name': row['货品简称'],
            'brand_name': row['品牌'],
            'goods_type': row['分类'],
            'spec_id': row['规格码'],
            'spec_name': row['规格名称'],
            'barcode': row['条码'],
            'num': row['货品数量'],
            'ori_price': row['货品原单价'],
            'ori_total_amount': row['货品原总金额'],
            'order_discount': row['订单总优惠'],
            'post_amount': row['订单邮费'],
            'share_post_amount': row['分摊邮费'],
            'deal_price': row['货品成交价'],
            'deal_total_price': row['货品成交总价'],
            'goods_discount': row['货品总优惠'],
            'cod_amount': row['货到付款金额'],
            'receivable': row['应收金额'],
            'buyer_nick': row['客户网名'],
            'receiver_name': row['收货人'],
            'receiver_area': row['收货地区'],
            'receiver_address': row['收货地址'],
            'receiver_mobile': row['收件人手机'],
            'receiver_telno': row['收件人电话'],
            'logistics_name': row['物流公司'],
            'invoice_type': row['需开发票'],
            'pay_time': row['支付时间'],
            'deliver_time': row['发货时间'],
            'gift_method': row['赠品方式'],
            'buyer_message': row['买家留言'],
            'service_remark': row['客服备注'],
            'remark': row['备注'],
        
            'print_remark': row['打印备注'],
            'source_suite_no': row['来源组合装编码'],
            'source_suite_name': row['来源组合装名称'],
            'source_suite_num': row['来源组合装数量'],
        }
        datalist.append(data)
    savedatatourl(datalist, base_url + 'orders/hissalesout', excel_path)
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



