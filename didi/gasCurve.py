# -*- coding:utf-8 -*-
'''
Created on 2017年3月29日

@author: didi
'''


import matplotlib.pyplot as plt
import sys
import os
import glob
import codecs # for utf8

#reload(sys)
#sys.setdefaultencoding('utf8')



def parse_time_series(time_series):
    unit_list = time_series.strip().split(";")
    order_date = []
    order_count = []
    filter_value = []
    status_list = []
    for unit in unit_list:
        unit_key_value = unit.strip().split(":")
        value_list = unit_key_value[1].strip().split(",")
        order_date.append(unit_key_value[0])
        order_count.append(float(value_list[0]))
        filter_value.append(float(value_list[1]))
        status_list.append(int(value_list[2]))
    return order_count, filter_value, status_list


def plot_time_series(order_count, filter_value, status_list, title, output_file):
    plt.figure(figsize=(20, 5))
    plt.plot(order_count, color='blue', label=u'原始')
    plt.plot(filter_value, color='green', label=u'滤波')
    color_list = ['red', 'blue', 'green']
    for i in range(len(status_list)):
        if status_list[i]==1:
            plt.plot(i, filter_value[i], marker='o', color=color_list[0])
        elif status_list[i]==2:
            plt.plot(i, filter_value[i], marker='o', color=color_list[1])
        elif status_list[i]==3:
            plt.plot(i, filter_value[i], marker='o', color=color_list[2])
        else:
            print 'Incorrect Status: '+str(status_list[i])
    plt.legend(loc='best')
    plt.title(title)
    plt.savefig(output_file)
    plt.close('all')


def main(input_file, output_dir):
    reader = codecs.open(input_file, 'rb', encoding='utf-8')
    text = reader.readlines()
    for plot in glob.glob(output_dir+'*.jpg'):
        os.remove(plot)
    for line in text:
        print line
        line_split = line.strip().split()
        store_id = line_split[0]
        store_name = line_split[1]
        city_id = line_split[2]
        city_name = line_split[3]
        if len(line_split[4]) == 1:
            continue
        component = parse_time_series(line_split[4])
        #print type(city_name),type(store_name)

        #plot_time_series(component[0], component[1], component[2], store_name+'('+city_name.decode('utf-8')+')', output_dir+store_id+'.jpg')        
        plot_time_series(component[0], component[1], component[2], store_name+'('+city_name+')', output_dir+store_id+'.jpg')
    reader.close()

if __name__ == '__main__':
    main('/Users/didi/Documents/fuel_growth_analysis_output.txt',
         '/Users/didi/Documents/plot/')