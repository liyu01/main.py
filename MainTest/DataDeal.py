#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


class DataDeal():

    def __init__(self,all_list, data02, data_02_id, data_02_value, data_02_address):
        # self.data_result = data_result
        self.all_list = all_list
        self.data02 = data02  # model
        # self.dataMode = dataMode
        self.data_02_id = data_02_id #  id
        self.data_02_value = data_02_value  #  last number
        self.data_02_address = data_02_address #  address

    def split_cal(self,dataMode):
        for n in range(len(self.data02)):
            if self.data02[n] == '':
                pass
            else:
                data_long = re.findall(r'\S+', self.data02[n])

                if len(data_long) == 3:
                    data_s = ''.join(self.data02[n].split())
                    #print(data_s)
                    #print(len(data_s))
                    if data_s in dataMode:
                        print(self.data_02_address[n], self.data_02_id[n], self.data_02_value[n], "1")
                        data_a = self.data_02_address[n], self.data_02_id[n], self.data_02_value[n]
                        self.all_list.append(data_a)
                        # print(data_a)
                        # f.write(self.data_02_address[n], self.data_02_id[n], self.data_02_value[n], "1")
                    elif data_s == "6ZUZVZXZY26":
                        # print(self.data_02_address[n], self.data_02_id[n], self.data_02_value[n], "2")
                        data_a = self.data_02_address[n], self.data_02_id[n], self.data_02_value[n]
                        self.all_list.append(data_a)
                    elif data_s == "6DQDRDSDUDV79":
                        data_a = self.data_02_address[n], self.data_02_id[n], self.data_02_value[n]
                        self.all_list.append(data_a)
                    elif data_s == "6KBKDKE69":
                        data_a = self.data_02_address[n], self.data_02_id[n], self.data_02_value[n]
                        self.all_list.append(data_a)
                else:
                    # print(self.data02[4])
                    data_cut = re.findall(r'\S+', self.data02[n])[3]
                    # print(data_cut,"hehhhhh")
                    judge = 0
                    if '-' in data_cut:
                        data_D = re.split('-', data_cut)
                        data_10_1 = data_D[0]
                        data_10_2 = data_D[1]
                        data_deal_1 = (re.split('&', data_10_1))
                        data_deal_2 = (re.split('/', data_10_2))
                        # print(data_deal_1)
                        # print(data_deal_2)
                        if len(data_D) == 2:
                            for j in data_deal_1:
                                data_r = j in dataMode
                                if data_r == True:
                                    pass
                                else:
                                    judge = 1
                            for k in data_deal_2:
                                data_u = k in dataMode
                                if data_u == False:
                                    pass
                                else:
                                    judge = 1
                            if judge == 0:
                                # print(self.data_02_address[n], self.data_02_id[n], self.data_02_value[n], '3')
                                data_a = self.data_02_address[n], self.data_02_id[n], self.data_02_value[n]
                                self.all_list.append(data_a)
                            else:
                                pass
                        else:
                            for j in data_deal_1:
                                data_r = j in dataMode
                                if data_r == False:
                                    pass
                                else:
                                    judge = 1
                            if judge == 0:
                                # print(self.data_02_address[n], self.data_02_id[n], self.data_02_value[n], "4")
                                data_a = self.data_02_address[n], self.data_02_id[n], self.data_02_value[n]
                                self.all_list.append(data_a)
                                break
                            else:
                                pass
                    else:
                        if len(data_cut) > 1:
                            data_deal10 = re.split('&', data_cut)
                            # print(data_deal10,"hoooohh")
                            # data_e = ''.join(data_deal10.split())
                            # print(data_e, "22222")
                            for k in data_deal10:
                                data_u = k in dataMode
                                if data_u == True:
                                    pass
                                else:
                                    judge = 1

                            if judge == 0:
                                # print(self.data_02_address[n], self.data_02_id[n], self.data_02_value[n], "5")
                                data_a = self.data_02_address[n], self.data_02_id[n], self.data_02_value[n]
                                self.all_list.append(data_a)
                            else:
                                pass
        return self.all_list

    def write_data_cal(self):
        for i in range(len(self.all_list)):
            return self.all_list[i][2]


    def split_excel_por_list(slef,sht):
        list_all = []
        row = sht.nrows
        Num = sht.col_values(0)
        i = 1
        cal_data = []
        for n in range(len(Num)):
            if Num[n] == str(i):
                str_data = n
                cal_data.append(str_data)
                i += 1
        for y in range(len(cal_data)):
            list1 = []
            if y == len(cal_data) - 1:
                for r in range(cal_data[y], row):
                    row_data = sht.row_values(r)
                    t = tuple(row_data)
                    list1.extend(t)
                    t2 = tuple(list1)
            else:
                for r in range(cal_data[y], cal_data[y + 1]):
                    row_data = sht.row_values(r)
                    t = tuple(row_data)
                    list1.extend(t)
                    t2 = tuple(list1)
            list_all.append(t2)
        return list_all

