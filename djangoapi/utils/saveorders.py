import datetime
import json
import os
import traceback

import requests
import xlrd
from xlrd.xldate import xldate_as_datetime

# from peidiexcel import base_url


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


def savedatatourl(data, url):
    res = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"}).content.decode()
    print(res)

def saveOrders(excel_path):

    tables = excel_table_byindex(excel_path, by_index=0)

    # datalist = []

    for row in tables:
        if ',' in row['原始单号']:
            continue
        time_fields = ['下单时间', '支付时间', '送货时间', '创建时间', '修改时间', '交易时间', '付款时间', '递交时间', '派送时间']
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
        ### 原始订单
        # data = {
        #     'platform': row['平台'],
        #     'shop_name': row['店铺'],
        #     'tid': row['原始单号'],
        #     'warehouse_no': row['外部仓库编号'],
        #     'trade_status': row['平台状态'],
        #     'pay_status': row['支付状态'],
        #     'guarantee_mode': row['担保方式'],
        #     'delivery_term': row['货到付款'],
        #     'pay_method': row['支付方式'],
        #     'refund_status': row['退款状态'],
        #     'process_status': row['系统处理状态'],
        #     'bad_reason': row['递交失败原因'],
        #     'trade_time': row['下单时间'],
        #     'pay_time': row['支付时间'],
        #     'buyer_nick': row['客户网名'],
        #     'receiver_name': row['收件人姓名'],
        #     'receiver_area': row['省市县'],
        #     'receiver_ring': row['区域'],
        #     'receiver_address': row['收件人地址'],
        #     'receiver_mobile': row['手机'],
        #     'receiver_telno': row['电话'],
        #     'receiver_zip': row['邮编'],
        #     'to_deliver_time': row['送货时间'] if row['送货时间'] and row['送货时间'] != '任意时间' else None,
        #     'buyer_message': row['买家备注'],
        #     'remark': row['客服备注'],
        #     'biaoqi': row['标旗'],
        #     'goods_amount': row['货款'],
        #     'post_amount': row['邮费'],
        #     'other_amount': row['其它收费'],
        #     'discount': row['优惠'],
        #     'platform_cost': row['平台费用'],
        #     'received': row['已收'],
        #     'receivable': row['应收'],
        #     'cash_on_delivery_amount': row['货到付款金额'],
        #     'refund_amount': row['退款金额'],
        #     'pay_id': row['支付单号'],
        #     'paid': row['已付'],
        #     'pay_account': row['支付账号'],
        #     'logistics_type': row['物流方式'],
        #     'invoice_type': row['发票类别'],
        #     'payer_name': row['发票抬头'],
        #     'invoice_content': row['发票内容'],
        #     'is_auto_wms': row['自流转订单'],
        #     'is_ware_trade': row['外部订单'],
        #     'logistics_no': row['物流编码'],
        #     'trade_from': row['订单来源'],
        #     'id_no': row['证件号码'],
        #     'modified': row['修改时间'],
        #     'created': row['创建时间'],
        #     'consumer_amount': row['消费者实付金额'],
        #     'platform_amount': row['平台承担优惠金额'],
        #     'currency': row['币种'],
        # }
        # print(data)

        ### 历史订单
        data = {
            'trade_no': row['订单编号'],
            'warehouse': row['仓库名称'],
            'shop_name': row['店铺名称'],
            'tid': row['原始单号'],
            'order_type': row['订单类型'],
            'delivery_term': row['发货条件'],
            'freeze_reason': row['冻结原因'],
            'refund_status': row['退款状态'],
            'process_status': row['订单状态'],
            'trade_time': row['交易时间'],
            'pay_time': row['付款时间'],
            'buyer_nick': row['客户网名'],
            'receiver_name': row['收件人'],
            'receiver_area': row['省市县'],
            'receiver_address': row['地址'],
            'receiver_mobile': row['手机'],
            'receiver_telno': row['电话'],
            'receiver_zip': row['邮编'],
            'receiver_dtb': row['大头笔'],
            'to_deliver_time': row['派送时间'],
            'logistics_name': row['物流公司'],
            'buyer_message': row['客户备注'],
            'remark': row['客服备注'],
            'biaoqi': row['客服标旗'],
            'print_remark': row['打印备注'],
            'goods_type_count': row['货品种类数'],
            'goods_count': row['货品总数'],
            'goods_amount': row['货品总额'],
            'post_amount': row['邮资'],
            'other_amount': row['其它费用'],
            'discount': row['优惠'],
            'ext_cod_fee': row['买家COD费用'],
            'receivable': row['应收金额'],
            'cash_on_delivery_amount': row['COD金额'],
            'commission': row['佣金'],
            'pay_account': row['买家付款账号'],
            'invoice_type': row['需要发票'],
            'payer_name': row['发票抬头'],
            'invoice_content': row['发票内容'],
            'flag_name': row['标记名称'],
            'single_spec_no': row['货品商家编码'],
            'logistics_no': row['物流单号'],
            'trade_from': row['订单来源'],
            'id_no': row['证件号码'],
            'stockout_no': row['出库单号'],
            'created': row['递交时间'],
            'raw_goods_count': row['原始货品数量'],
            'raw_goods_type_count': row['原始货品种类数'],
            'currency': row['币种'],
        }
        # datalist.append(data)
        savedatatourl(data, base_url + 'orders/orders')






def saveExcel(excel_path):

    if os.path.isfile(excel_path):
        print('***** path: ', excel_path)
        try:
            saveOrders(excel_path)
        except Exception:
            print(traceback.format_exc())
            destination_path = os.path.join(err_folder_path, file)
            # os.rename(excel_path, destination_path)
        else:
            end_folder_path = os.path.join(home_path, 'end')
            destination_path = os.path.join(end_folder_path, file)
            # os.rename(excel_path, destination_path)




if __name__=="__main__":
    home_path = r'C:\Users\wjk13\Desktop\peidi-data\历史订单\2022'
    all_folder_path = os.path.join(home_path, 'all')
    err_folder_path = os.path.join(home_path, 'err')
    end_folder_path = os.path.join(home_path, 'end')
    for file in os.listdir(all_folder_path):
        excel_path = os.path.join(all_folder_path, file)
        saveExcel(excel_path)