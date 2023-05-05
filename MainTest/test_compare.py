#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xlrd
import xlwt

bok_Gep = xlrd.open_workbook(r'../data/20220705 E2QL 23MY PPV1 GEPICS REPORT.xls')
sht_Gep = bok_Gep.sheets()[0]
col = sht_Gep.ncols
row = sht_Gep.nrows


for r in range(row):
    row_data = sht_Gep.row_values(r)
    print(row_data)