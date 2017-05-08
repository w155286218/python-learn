#coding:utf-8
'''
Created on 2016-11-11

@author: Charlie
'''

import json
import pandas as pd
import numpy


f300=open("/Users/didi/Documents/car_300_shard_output_201611151135.txt")
f300_format=open("/Users/didi/Documents/car_300_total_format.txt",'w')
i=0
j=0
k=0
while 1:
    lines = f300.readlines(10000)
    if not lines:
        break
    for line in lines:
        i=i+1
        if i>20000:
             break
        vehicle_data=[]
        params=line.split("\001")
        car_id= params[0]
        style_id= params[1]
        car_reg_time= params[2]
        mileage= params[3]
        gulfstream_city_id= params[4]
        color= params[5]
        vehicle_data.append(car_id)
        vehicle_data.append(style_id)
        vehicle_data.append(car_reg_time)
        vehicle_data.append(mileage)
        vehicle_data.append(gulfstream_city_id)
        vehicle_data.append(color)

        current_prices = {}
        trends_prices = {}

        ##当前预估价
        if len(params[6])>1:
            #print len(params[6])
            try:
                paramsjson6 = json.loads(params[6])
                #print paramsjson.keys()
                if "error_msg" not in set(paramsjson6.keys()):
                    #print paramsjson["eval_prices"]
                    # print paramsjson["eval_prices"][0]
                    for c_price in paramsjson6["eval_prices"]:
                        trends_prices[c_price["condition"]]=[]

                        current_prices[c_price["condition"]]=\
                            str(c_price["dealer_buy_price"])+','+str(c_price["individual_price"])\
                            +','+str(c_price["dealer_price"])
                    j=j+1
                else:
                    print "error_type:current price error message"
                    print paramsjson6["error_msg"]
                    print vehicle_data
            except Exception,e:
                print e
        else:
            print "error_type:current price empty result"

        ###趋势价格
        if len(params[7]) > 1:
            try:
                paramsjson7 = json.loads(params[7])
                #print "param7:"+str(paramsjson7)
                #print "kes:"+str(paramsjson7.keys())
                if paramsjson7.keys().count("error_msg")==0:
                    #print paramsjson7["trends"]
                    for trend_value in paramsjson7["trends"]:
                            # print monthtrendv
                            # print monthtrendv["dealer_buy_price"]
                            # print monthtrendv["individual_price"]
                            # print monthtrendv["dealer_price"]
                        for monthtrendv in trend_value["eval_prices"]:
                            for condition in trends_prices.keys():
                                if condition==monthtrendv["condition"]:
                                    trends_prices.get(condition).append(monthtrendv["dealer_buy_price"])
                                    trends_prices.get(condition).append(monthtrendv["individual_price"])
                                    trends_prices.get(condition).append(monthtrendv["dealer_price"])
                    k = k + 1
                else:
                    print "error_type:trends price error message"
                    # for prc in range(1, 334):
                    #     t_arr.append(0)
            except Exception, e:
                print e
                # for prc in range(1, 334):
                #     t_arr.append(0)
        else:
            print "error_type:trends price empty result"
            # for prc in range(1, 334):
            #     t_arr.append(0)
        ##写入文件
        for condition_current in current_prices.keys():
            #print condition_current
            f300_format.write(condition_current+",")
            for data in vehicle_data:
                f300_format.write(str(data).decode("string_escape")+",")
            f300_format.write(current_prices.get(condition_current))

            # f300_format.write(current_prices.get(condition_current)+",")
            # for condition_trend in trends_prices.keys():
            #     if condition_current==condition_trend:
            #         prices_trends=str(trends_prices.get(condition_trend))
            #         price_trends_format=prices_trends.replace("[","").replace("]","").replace(" ","")
            #         f300_format.write(price_trends_format)

            f300_format.write("\n")


print j
print k
f300.close()
f300_format.close()