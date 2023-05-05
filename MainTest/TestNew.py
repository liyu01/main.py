# -*- coding: utf-8 -*-
import os
import sys
import xlrd #导入xlrd模块

from MainTest.DataDeal import DataDeal

# 导入3PD

files_3pd = os.listdir('../data/3PD/')
path_3pd = os.path.join('../data/3PD/'+files_3pd[0])
bok = xlrd.open_workbook(path_3pd)
sht = bok.sheets()[0]
row = sht.nrows
row_data = sht.row_values(4)

#bok_rpo = xlrd.open_workbook(r'../data/RPO_LIST.xls')
#sht_rpo = bok_rpo.sheets()[0]

#  导入单车rpo_list
files_rpo_txt = os.listdir('../data/RPO_list/')
path_rpo_txt = os.path.join('../data/RPO_list/'+files_rpo_txt[0])
Tx_open = open(path_rpo_txt)
dataMode = Tx_open.read()

np = open('../result/Gepics.txt', 'w')
np2 = open('../result/Cal.txt', 'w')

data_all = []
data_all_id = []
data_all_value = []
data_all_address = []
data_all_list = []

for c in range(row):
    row_data = sht.row_values(c)
    value1 = row_data[11]   # Embedded Module ID
    value2 = row_data[12]   # PDS / Model / Option Statement
    value3 = row_data[15]   # Latest Part Number
    value4 = row_data[7]    # Family Address

    data_all.append(value2)
    data_all_id.append(value1)
    data_all_value.append(value3)
    data_all_address.append(value4)

if __name__ == '__main__':

    d = DataDeal(data_all_list,data_all, data_all_id, data_all_value, data_all_address)
    #str_rpo = d.split_excel_por_list(sht_rpo)
    #print(str_rpo)
    str_Gepics = d.split_cal(dataMode)
    # print(str_Gepics)

    # for i in (str_rpo):
    #     str_Gepics = d.split_cal(i)
    #
    #     print(len(str_Gepics))
    #     print(str_Gepics)

    for n in range(len(str_Gepics)):
      #  print(str_Gepics[n][0], str_Gepics[n][1], str_Gepics[n][2])
        str_data = str(str_Gepics[n][0] + " " + str_Gepics[n][1] + " " + str_Gepics[n][2])
        np.write(str_data + "\n")


    # # 标定
    str_Gepics.sort(key=lambda k: k[1])
    for i in range(len(str_Gepics)):
        #print(str_Gepics[i][0],str_Gepics[i][1],str_Gepics[i][2])
        str_data = str(str_Gepics[i][0] + " " + str_Gepics[i][1] + " " + str_Gepics[i][2])
        np2.write(str_data + "\n")

COUNT_FILE = os.path.join('../data/cycle', '.myprog.count')
if not os.path.exists(COUNT_FILE):
    num = 0
else:
    f = open(COUNT_FILE, 'r')
    num = int(f.read())
    f.close()

if num+1 > 2:
    print >>sys.stderr, "You have exceeded your %d uses"%(num,)
    sys.exit(0)

num += 1
f = open(COUNT_FILE, 'w')
f.write(str(num))
f.close()
