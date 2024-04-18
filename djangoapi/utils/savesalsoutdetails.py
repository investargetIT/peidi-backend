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

    datalist = []

    for row in tables:
        time_fields = ['下单时间', '支付时间', '送货时间', '创建时间', '修改时间', '交易时间', '付款时间', '递交时间', '派送时间', '发货时间']
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
        # data = {
        #     'trade_no': row['订单编号'],
        #     'tid': row['原始单号'],
        #     'oid': row['原始子单号'],
        #     'otid': row['子单原始单号'],
        #     'order_type': row['订单类别'],
        #     'trade_from': row['订单来源'],
        #     'pay_account': row['支付账号'],
        #     'stockout_no': row['出库单编号'].replace('\n', '').replace('\r', ''),
        #     'warehouse': row['仓库'],
        #     'shop_name': row['店铺'],
        #     'status_type': row['出库单状态'],
        #     'stockout_status': row['出库状态'],
        #     'spec_no': row['商家编码'],
        #     'goods_no': row['货品编号'],
        #     'goods_name': row['货品名称'],
        #     'goods_short_name': row['货品简称'],
        #     'brand_name': row['品牌'],
        #     'goods_type': row['分类'],
        #     'spec_id': row['规格码'],
        #     'spec_name': row['规格名称'],
        #     'barcode': row['条码'],
        #     'num': row['货品数量'],
        #     'unit_name': row['单位'],
        #     'aux_num': row['辅助数量'],
        #     'aux_unit_name': row['辅助单位'],
        #     'ori_price': row['货品原单价'],
        #     'ori_total_amount': row['货品原总金额'],
        #     'order_discount': row['订单总优惠'],
        #     'post_amount': row['订单邮费'],
        #     'share_post_amount': row['分摊邮费'],
        #     'deal_price': row['货品成交价'],
        #     'deal_total_price': row['货品成交总价'],
        #     'goods_discount': row['货品总优惠'],
        #     'cod_amount': row['货到付款金额'],
        #     'receivable': row['应收金额'],
        #     'ori_receivable': row['子单应收金额 '],
        #     'buyer_nick': row['客户网名'],
        #     'receiver_name': row['收货人'],
        #     'receiver_area': row['收货地区'],
        #     'receiver_address': row['收货地址'],
        #     'receiver_mobile': row['收件人手机'],
        #     'receiver_telno': row['收件人电话'],
        #     'logistics_name': row['物流公司'],
        #     'invoice_type': row['需开发票'],
        #     'flag_name': row['标记名称'],
        #     'trade_time': row['下单时间'],
        #     'pay_time': row['支付时间'],
        #     'created': row['创建时间'],
        #     'deliver_time': row['发货时间'],
        #     'gift_method': row['赠品方式'],
        #     'buyer_message': row['买家留言'],
        #     'service_remark': row['客服备注'],
        #     'remark': row['备注'],
        #
        #     'print_remark': row['打印备注'],
        #     'source_suite_no': row['来源组合装编码'],
        #     'source_suite_name': row['来源组合装名称'],
        #     'source_suite_num': row['来源组合装数量'],
        #     'stockout_tag': row['出库标签'],
        #     'order_tag': row['订单标签'],
        #     'specgoods_price': row['单品零售价'],
        #     'distributor': row['分销商名称'],
        #     'distributor_no': row['分销商编号'],
        #     'paid': row['已付'],
        #     'distribution_oid': row['分销原始单号'],
        # }
        ###  历史销售出库明细
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
    savedatatourl(datalist, base_url + 'orders/salesout')






def saveExcel(excel_path):

    if os.path.isfile(excel_path):
        print('***** path: ', excel_path)
        try:
            saveOrders(excel_path)
        except Exception:
            print(traceback.format_exc())
            destination_path = os.path.join(err_folder_path, file)
            os.rename(excel_path, destination_path)
        else:
            end_folder_path = os.path.join(home_path, 'end')
            destination_path = os.path.join(end_folder_path, file)
            os.rename(excel_path, destination_path)




if __name__=="__main__":
    home_path = r'C:\Users\wjk13\Desktop\peidi-data\销售出库明细\2022'
    all_folder_path = os.path.join(home_path, 'all')
    err_folder_path = os.path.join(home_path, 'err')
    end_folder_path = os.path.join(home_path, 'end')
    for file in os.listdir(all_folder_path):
        excel_path = os.path.join(all_folder_path, file)
        saveExcel(excel_path)