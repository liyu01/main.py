# -*- coding: utf-8 -*-
import re

import xlrd #导入xlrd模块

from MainTest.DataDeal import DataDeal

bok = xlrd.open_workbook(r'../data/E2QL.xlsx')
sht = bok.sheets()[0]
row =sht.nrows
row_date = sht.row_values(4)

Tx_open = open('../data/E2QL.txt', 'r')
dataMode = Tx_open.read()
data02 = []
data03 = []
data04 = []
data05 = []
data06 = []
data07 = []
data08 = []
data09 = []
data10 = []
data12 = []
data13 = []
data14 = []
data15 = []
data16 = []
data17 = []
data18 = []
data19 = []
data20 = []
data22 = []
data23 = []
data24 = []
data25 = []
data26 = []
data27 = []
data28 = []
data29 = []
data30 = []
data32 = []
data33 = []



data_02_id = []
data_03_id = []
data_04_id = []
data_05_id = []
data_06_id = []
data_07_id = []
data_08_id = []
data_09_id = []
data_10_id = []
data_12_id = []
data_13_id = []
data_14_id = []
data_15_id = []
data_16_id = []
data_17_id = []
data_18_id = []
data_19_id = []
data_20_id = []
data_22_id = []
data_23_id = []
data_24_id = []
data_25_id = []
data_26_id = []
data_27_id = []
data_28_id = []
data_29_id = []
data_30_id = []
data_32_id = []
data_33_id = []




data_02_value = []
data_03_value = []
data_04_value = []
data_05_value = []
data_06_value = []
data_07_value = []
data_08_value = []
data_09_value = []
data_10_value = []
data_12_value = []
data_13_value = []
data_14_value = []
data_15_value = []
data_16_value = []
data_17_value = []
data_18_value = []
data_19_value = []
data_20_value = []
data_22_value = []
data_23_value = []
data_24_value = []
data_25_value = []
data_26_value = []
data_27_value = []
data_28_value = []
data_29_value = []
data_30_value = []
data_32_value = []
data_33_value = []

data_02_address = []
data_03_address = []
data_04_address = []
data_05_address = []
data_06_address = []
data_07_address = []
data_08_address = []
data_09_address = []
data_10_address = []
data_12_address = []
data_13_address = []
data_14_address = []
data_15_address = []
data_16_address = []
data_17_address = []
data_18_address = []
data_19_address = []
data_20_address = []
data_22_address = []
data_23_address = []
data_24_address = []
data_25_address = []
data_26_address = []
data_27_address = []
data_28_address = []
data_29_address = []
data_30_address = []
data_32_address = []
data_33_address = []

data_all = []
data_all_id = []
data_all_value = []
data_all_address = []



for c in range(row):
    row_date = sht.row_values(c)

    value1 = row_date[11]   # Embedded Module ID
    value2 = row_date[12]   # PDS / Model / Option Statement
    value3 = row_date[15]   # Latest Part Number
    value4 = row_date[7]    # Family Address

    data_all.append(value2)
    data_all_id.append(value1)
    data_all_value.append(value3)
    data_all_address.append(value4)



    if value1 == '00':
        fna = row_date[10]
        if 'ETHERNET' in fna:
            pass
        else:
            print(value4,value1, value3)

    if value1 == '02':
        data02.append(value2)
        data_02_id.append(value1)
        data_02_value.append(value3)
        data_02_address.append(value4)

    if value1 == '03':
        data03.append(value2)
        data_03_id.append(value1)
        data_03_value.append(value3)
        data_03_address.append(value4)

    if value1 == '04':
        data04.append(value2)
        data_04_id.append(value1)
        data_04_value.append(value3)
        data_04_address.append(value4)

    if value1 == '05':
        data05.append(value2)
        data_05_id.append(value1)
        data_05_value.append(value3)
        data_05_address.append(value4)

    if value1 == '06':
        data06.append(value2)
        data_06_id.append(value1)
        data_06_value.append(value3)
        data_06_address.append(value4)

    if value1 == '07':
        data07.append(value2)
        data_07_id.append(value1)
        data_07_value.append(value3)
        data_07_address.append(value4)

    if value1 == '08':
        data08.append(value2)
        data_08_id.append(value1)
        data_08_value.append(value3)
        data_08_address.append(value4)

    if value1 == '09':
        data09.append(value2)
        data_09_id.append(value1)
        data_09_value.append(value3)
        data_09_address.append(value4)
    if value1 == '10':
        data10.append(value2)
        data_10_id.append(value1)
        data_10_value.append(value3)
        data_10_address.append(value4)

    if value1 == '12':
        data12.append(value2)
        data_12_id.append(value1)
        data_12_value.append(value3)
        data_12_address.append(value4)

    if value1 == '13':
        data13.append(value2)
        data_13_id.append(value1)
        data_13_value.append(value3)
        data_13_address.append(value4)

    if value1 == '14':
        data14.append(value2)
        data_14_id.append(value1)
        data_14_value.append(value3)
        data_14_address.append(value4)

    if value1 == '15':
        data15.append(value2)
        data_15_id.append(value1)
        data_15_value.append(value3)
        data_15_address.append(value4)

    if value1 == '16':
        data16.append(value2)
        data_16_id.append(value1)
        data_16_value.append(value3)
        data_16_address.append(value4)

    if value1 == '17':
        data17.append(value2)
        data_17_id.append(value1)
        data_17_value.append(value3)
        data_17_address.append(value4)

    if value1 == '18':
        data18.append(value2)
        data_18_id.append(value1)
        data_18_value.append(value3)
        data_18_address.append(value4)

    if value1 == '19':
        data19.append(value2)
        data_19_id.append(value1)
        data_19_value.append(value3)
        data_19_address.append(value4)

    if value1 == '20':
        data20.append(value2)
        data_20_id.append(value1)
        data_20_value.append(value3)
        data_20_address.append(value4)

    if value1 == '22':
        data22.append(value2)
        data_22_id.append(value1)
        data_22_value.append(value3)
        data_22_address.append(value4)


    if value1 == '23':
        data23.append(value2)
        data_23_id.append(value1)
        data_23_value.append(value3)
        data_23_address.append(value4)


    if value1 == '24':
        data24.append(value2)
        data_24_id.append(value1)
        data_24_value.append(value3)
        data_24_address.append(value4)


    if value1 == '25':
        data25.append(value2)
        data_25_id.append(value1)
        data_25_value.append(value3)
        data_25_address.append(value4)


    if value1 == '26':
        data26.append(value2)
        data_26_id.append(value1)
        data_26_value.append(value3)
        data_26_address.append(value4)


    if value1 == '27':
        data27.append(value2)
        data_27_id.append(value1)
        data_27_value.append(value3)
        data_27_address.append(value4)


    if value1 == '28':
        data28.append(value2)
        data_28_id.append(value1)
        data_28_value.append(value3)
        data_28_address.append(value4)


    if value1 == '29':
        data29.append(value2)
        data_29_id.append(value1)
        data_29_value.append(value3)
        data_29_address.append(value4)


    if value1 == '30':
        data30.append(value2)
        data_30_id.append(value1)
        data_30_value.append(value3)
        data_30_address.append(value4)

    if value1 == '32':
        data32.append(value2)
        data_32_id.append(value1)
        data_32_value.append(value3)
        data_32_address.append(value4)

    if value1 == '33':
        data33.append(value2)
        data_33_id.append(value1)
        data_33_value.append(value3)
        data_33_address.append(value4)







d = DataDeal(data02, dataMode, data_02_id, data_02_value,data_02_address)
d.split_cal2()

d = DataDeal(data03, dataMode, data_03_id, data_03_value,data_03_address)
d.split_cal2()

t = DataDeal(data04, dataMode, data_04_id, data_04_value,data_04_address)
t.split_cal2()

t = DataDeal(data05, dataMode, data_05_id, data_05_value,data_05_address)
t.split_cal2()

e = DataDeal(data06, dataMode, data_06_id, data_06_value,data_06_address)
e.split_cal2()

t = DataDeal(data07, dataMode, data_07_id, data_07_value,data_07_address)
t.split_cal2()

t = DataDeal(data08, dataMode, data_08_id, data_08_value,data_08_address)
t.split_cal2()

t = DataDeal(data09, dataMode, data_09_id, data_09_value,data_09_address)
t.split_cal2()

f = DataDeal(data10, dataMode, data_10_id, data_10_value,data_10_address)
f.split_cal2()

f = DataDeal(data12, dataMode, data_12_id, data_12_value,data_12_address)
f.split_cal2()

t = DataDeal(data13, dataMode, data_13_id, data_13_value,data_13_address)
t.split_cal2()

t = DataDeal(data15, dataMode, data_15_id, data_15_value,data_15_address)
t.split_cal2()

t = DataDeal(data16, dataMode, data_16_id, data_16_value,data_16_address)
t.split_cal2()

t = DataDeal(data17, dataMode, data_17_id, data_17_value,data_17_address)
t.split_cal2()

d = DataDeal(data18, dataMode, data_18_id, data_03_value,data_18_address)
d.split_cal2()

t = DataDeal(data19, dataMode, data_19_id, data_19_value,data_19_address)
t.split_cal2()

t = DataDeal(data20, dataMode, data_20_id, data_20_value,data_20_address)
t.split_cal2()

t = DataDeal(data22, dataMode, data_22_id, data_22_value,data_22_address)
t.split_cal2()

t = DataDeal(data23, dataMode, data_23_id, data_23_value,data_23_address)
t.split_cal2()

t = DataDeal(data24, dataMode, data_24_id, data_24_value,data_24_address)
t.split_cal2()

t = DataDeal(data25, dataMode, data_25_id, data_25_value,data_25_address)
t.split_cal2()

t = DataDeal(data26, dataMode, data_26_id, data_26_value,data_26_address)
t.split_cal2()

t = DataDeal(data27, dataMode, data_27_id, data_27_value,data_27_address)
t.split_cal2()

t = DataDeal(data28, dataMode, data_28_id, data_28_value,data_28_address)
t.split_cal2()

t = DataDeal(data29, dataMode, data_29_id, data_29_value,data_29_address)
t.split_cal2()

t = DataDeal(data30, dataMode, data_30_id, data_30_value,data_30_address)
t.split_cal2()

t = DataDeal(data32, dataMode, data_32_id, data_32_value,data_32_address)
t.split_cal2()

t = DataDeal(data33, dataMode, data_33_id, data_33_value,data_33_address)
t.split_cal2()






