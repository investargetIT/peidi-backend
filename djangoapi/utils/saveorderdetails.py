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
        time_fields = ['下单时间', '支付时间', '送货时间', '创建时间', '修改时间', '交易时间', '付款时间', '递交时间', '派送时间', '发货时间', '最晚发货时间']
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

        ###  销售出库明细
        data = {
                    'trade_no': row['订单编号'],
                    'shop_name': row['店铺名称'],
                    'trade_from': row['订单来源'],
                    'warehouse': row['仓库'],
                    'tid': row['原始单号'],
                    'oid': row['原始子单号'],
                    'process_status': row['订单状态'],
                    'order_type': row['订单类型'],
                    'delivery_term': row['发货条件'],
                    'refund_status': row['订单退款状态'],
                    'refund_status_of_details': row['订单明细退款状态'],
                    'trade_time': row['交易时间'],
                    'pay_time': row['付款时间'],
                    'deliver_time': row['发货时间'],
                    'buyer_nick': row['客户网名'],
                    'receiver_name': row['收件人'],
                    'receiver_area': row['省市县'],
                    'receiver_address': row['地址'],
                    'receiver_mobile': row['手机'],
                    'receiver_telno': row['电话'],
                    'receiver_zip': row['邮编'],
                    'logistics_name': row['物流公司'],
                    'logistics_no': row['物流单号'],
                    'buyer_message': row['买家留言'],
                    'service_remark': row['客服备注'],
                    'print_remark': row['打印备注'],
                    'remark': row['备注'],
                    'biaoqi': row['客服标旗'],
                    'post_amount': row['订单邮费'],
                    'other_amount': row['其它费用'],
                    'order_discount': row['订单总优惠'],
                    'receivable': row['应收金额'],
                    'cod_amount': row['货到付款金额'],
                    'invoice_type': row['需要发票'],
                    'payer_name': row['发票抬头'],
                    'invoice_content': row['发票内容'],
                    'flag_name': row['标记名称'],
                    'spec_no': row['商家编码'],
                    'goods_no': row['货品编号'],
                    'goods_name': row['货品名称'],
                    'spec_name': row['规格名称'],
                    'goods_type': row['分类'],
                    'num': row['数量'],
                    'ori_price': row['标价'],
                    'discount': row['优惠'],
                    'deal_price': row['成交价'],
                    'share_price': row['分摊后价格'],
                    'share_post_amount': row['分摊邮费'],
                    'discount_rate': row['打折比'],
                    'share_total_price': row['分摊后总价'],
                    'commission': row['佣金'],
                    'source_suite_name': row['拆自组合装'],
                    'source_suite_no': row['组合装编码'],
                    'source_suite_num': row['组合装数量'],
                    'gift_method': row['赠品方式'],
                    'platform_goods_name': row['平台货品名称'],
                    'platform_spec_name': row['平台规格名称'],
                    'order_tag': row['订单标签'],
                    'distributor': row['分销商名称'],
                    'distributor_no': row['分销商编号'],
                    'paid': row['已付'],
                    'pay_account': row['付款账号'],
                    'deadline_deliver_time': row['最晚发货时间'],
                    'buyer_no': row['客户编号'],
                    'distribution_oid': row['分销原始单号'],
                }
        datalist.append(data)
    savedatatourl(datalist, base_url + 'orders/orderdetails', excel_path)
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



