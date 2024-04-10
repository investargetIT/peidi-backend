import datetime
import os
import traceback

import requests
import xlrd
from xlrd.xldate import xldate_as_datetime

from peidiexcel import base_url


# base_url = 'http://localhost:8000/'


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
    res = requests.post(url, data=data).content.decode()
    print(res)

def saveOrders(excel_path):

    tables1 = excel_table_byindex(excel_path, by_index=0)
    tables2 = excel_table_byindex(excel_path, by_index=1)


    for row in tables1:
        time_fields = ['下单时间', '支付时间', '送货时间', '创建时间', '修改时间']
        for time_field in time_fields:
            if row[time_field] and row[time_field] != '任意时间':
                if isinstance(row[time_field], float):
                    row[time_field] = xldate_as_datetime(row[time_field], 0).strftime('%Y-%m-%d %H:%M:%S')

        data1 = {
            'platform': row['平台'],
            'shop_name': row['店铺'],
            'tid': row['原始单号'],
            'warehouse_no': row['外部仓库编号'],
            'trade_status': row['平台状态'],
            'pay_status': row['支付状态'],
            'guarantee_mode': row['担保方式'],
            'delivery_term': row['货到付款'],
            'pay_method': row['支付方式'],
            'refund_status': row['退款状态'],
            'process_status': row['系统处理状态'],
            'bad_reason': row['递交失败原因'],
            # 'trade_time': xldate_as_datetime(row['下单时间'],0).strftime('%Y-%m-%d %H:%M:%S') if row['下单时间'] else None,
            # 'pay_time': xldate_as_datetime(row['支付时间'],0).strftime('%Y-%m-%d %H:%M:%S') if row['支付时间'] else None,
            'trade_time': row['下单时间'],
            'pay_time': row['支付时间'],
            'buyer_nick': row['客户网名'],
            'receiver_name': row['收件人姓名'],
            'receiver_area': row['省市县'],
            'receiver_ring': row['区域'],
            'receiver_address': row['收件人地址'],
            'receiver_mobile': row['手机'],
            'receiver_telno': row['电话'],
            'receiver_zip': row['邮编'],
            # 'to_deliver_time': xldate_as_datetime(row['送货时间'], 0).strftime('%Y-%m-%d %H:%M:%S') if row['送货时间'] and row['送货时间'] != '任意时间'  else None,
            'to_deliver_time': row['送货时间'] if row['送货时间'] and row['送货时间'] != '任意时间' else None,
            'buyer_message': row['买家备注'],
            'remark': row['客服备注'],
            'biaoqi': row['标旗'],
            'goods_amount': row['货款'],
            'post_amount': row['邮费'],
            'other_amount': row['其它收费'],
            'discount': row['优惠'],
            'platform_cost': row['平台费用'],
            'received': row['已收'],
            'receivable': row['应收'],
            'cash_on_delivery_amount': row['货到付款金额'],
            'refund_amount': row['退款金额'],
            'pay_id': row['支付单号'],
            'paid': row['已付'],
            'pay_account': row['支付账号'],
            'logistics_type': row['物流方式'],
            'invoice_type': row['发票类别'],
            'payer_name': row['发票抬头'],
            'invoice_content': row['发票内容'],
            'is_auto_wms': row['自流转订单'],
            'is_ware_trade': row['外部订单'],
            'logistics_no': row['物流编码'],
            'trade_from': row['订单来源'],
            'id_no': row['证件号码'],
            # 'modified': xldate_as_datetime(row['修改时间'],0).strftime('%Y-%m-%d %H:%M:%S') if row['修改时间'] else None,
            # 'created': xldate_as_datetime(row['创建时间'],0).strftime('%Y-%m-%d %H:%M:%S') if row['创建时间'] else None,
            'modified': row['修改时间'],
            'created': row['创建时间'],
            'consumer_amount': row['消费者实付金额'],
            'platform_amount': row['平台承担优惠金额'],
            'currency': row['币种'],
        }
        # print(data1)
        savedatatourl(data1, base_url + 'orders/orders')
    for row in tables2:
        time_fields = ['子单完成时间', '创建时间', '修改时间']
        for time_field in time_fields:
            if row[time_field] and row[time_field] != '任意时间':
                if isinstance(row[time_field], float):
                    row[time_field] = xldate_as_datetime(row[time_field], 0).strftime('%Y-%m-%d %H:%M:%S')
        data2 = {
            'tid': row['原始单号'],
            'oid': row['子订单编号'],
            'status': row['状态'],
            'process_status': row['处理状态'],
            'refund_status': row['退款状态'],
            'order_type': row['子订单类型'],
            'goods_id': row['平台货品ID'],
            'spec_id': row['平台规格ID'],
            'goods_no': row['货品编号'],
            'spec_no': row['规格编码'],
            'goods_name': row['货品名称'],
            'spec_name': row['规格名称'],
            'num': row['数量'],

            'price': row['单价'],
            'adjust_amount': row['调整'],
            'discount': row['优惠'],
            'total_amount': row['总价'],
            'share_discount': row['分摊优惠'],
            'share_amount': row['分摊后应收'],
            'refund_amount': row['退款金额'],
            'refund_id': row['退款单编号'],
            'end_time': row['子单完成时间'],
            # 'modified': xldate_as_datetime(row['修改时间'],0).strftime('%Y-%m-%d %H:%M:%S') if row['修改时间'] else None,
            # 'created': xldate_as_datetime(row['创建时间'],0).strftime('%Y-%m-%d %H:%M:%S') if row['创建时间'] else None,
            'modified': row['修改时间'],
            'created': row['创建时间'],
            'image': row['图片'],
            'sys_goods_name': row['系统货品名称'],
            'sys_spec_name': row['系统规格名称'],
        }
        # print(data2)
        savedatatourl(data2, base_url + 'orders/traderorders')










if __name__=="__main__":
    # date_start_str = '20221106'
    # date_obj = datetime.datetime.strptime(date_start_str, "%Y%m%d")
    # for i in range(1, 20):  # -1
    #     date_str = date_obj.strftime('%Y%m%d')
    #     excel_path = r'C:\Users\wjk13\Desktop\peidi-data\2022\2022-all\%s.xlsx' % date_str
    #     try:
    #         if os.path.exists(excel_path):
    #             print('***** path: ', excel_path)
    #             saveOrders(excel_path)
    #         else:
    #             print(excel_path, '***文件不存在***')
    #     except Exception:
    #         print(traceback.format_exc())
    #         destination_path = r'C:\Users\wjk13\Desktop\peidi-data\2022\2022-err\%s.xlsx' % date_str
    #         os.rename(excel_path, destination_path)
    #     else:
    #         destination_path = r'C:\Users\wjk13\Desktop\peidi-data\2022\2022-end\%s.xlsx' % date_str
    #         os.rename(excel_path, destination_path)
    #     date_obj = date_obj + datetime.timedelta(days=1)
    excel_folder_path = r'C:\Users\wjk13\Desktop\peidi-data\2022\2022-all'
    for file in os.listdir(excel_folder_path):
        excel_path = os.path.join(excel_folder_path, file)
        if os.path.isfile(excel_path):
            print('***** path: ', excel_path)
            try:
                saveOrders(excel_path)
            except Exception:
                print(traceback.format_exc())
                destination_path = r'C:\Users\wjk13\Desktop\peidi-data\2022\2022-err\%s' % file
                os.rename(excel_path, destination_path)
            else:
                destination_path = r'C:\Users\wjk13\Desktop\peidi-data\2022\2022-end\%s' % file
                os.rename(excel_path, destination_path)