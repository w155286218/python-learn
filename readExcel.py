# -*- coding: utf-8 -*- 
'''
Created on 2016年7月1日

@author: Charlie
'''

import sys
import xlrd

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_index：表的索引
def excel_table_byindex(file,colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    print nrows
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
             print app
    return list
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_index：表的索引
def excel_table_byindex2(file,colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    print nrows
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = []
             for i in range(0,ncols):
                 if i==4 or i==5:
                     #app.append(xlrd.xldate_as_tuple(row[i]))#日期转换
                     xltp=xlrd.xldate_as_tuple(row[i],0)
                     print xltp
                     dts=xlrd.xldate.xldate_from_time_tuple(xltp)
                     app.append(dts)#日期转换
                 else:
                     app.append(row[i])
             #print app
             
             list.append(app)
    return list
#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
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

def main():
   tables = excel_table_byindex2('/Users/didi/Documents/深圳地区车型保有量TOP100.xlsx')
   #fw=open("F:/tag_factory/tag_config-20160705.txt",'wb')
   print tables
   for row in tables:
       print row
       fw.write(str(row))
       
   fw.close()

if __name__=="__main__":
    main()