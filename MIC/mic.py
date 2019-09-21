#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:10:25 2019

@author: linjunqi
"""

import numpy as np
from minepy import MINE
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

#roll_len = 24
#lag = 6
#bgn = 1
#goal = '工业增加值:当月同比'
#obj = 'M2:同比'
#num_pick = 4
#
#mine = MINE(alpha = 0.6, c = 15)
#
#
#def rolling_correlation(base, data, roll_len = roll_len):
#    length = len(base)
#    for i in range(length - roll_len):
#        base_slice = base[i: i + roll_len]
#        data_slice = data[i: i + roll_len]
#        temp = base_slice.index.strftime("%Y%m%d") 
#        print(type(str(base_slice.index)))
#        mine.compute_score(base_slice, data_slice)
#        p = pearsonr(base_slice, data_slice)[0]
#        mic = mine.mic()
#        mas = 1 - mine.mas()
#        mev = mine.mev()
#        mcn = mine.mcn_general()
#        
#        result = np.array([p, mic, mas, mev, mcn])
#        
#        roll_result.loc[str(temp[0])+" - "+str(temp[-1])] = result
##        roll_result.loc["roll-"+str(i)] = result
#        i = i + 1
#        
#    return roll_result
#
#
#def linear_sa(data):
#    
#    for i in range(len(data)):
#        if '-01' in str(data.index[i]):
#            diff = (data[i+2] - data[i-1])/3
#            data[i] = data[i-1] + diff
#            data[i+1] = data[i] + diff
#    
#    return data
#
#data = pd.read_excel('/Users/linjunqi/Desktop/mic_result/51index_data_onlyM.xls', index_col = 0)
#data = data[bgn:]
#
#
#base = data[goal]
#base = linear_sa(base)
#objeet = data[obj]
#
#data = data.drop([goal], axis = 1)
#df = pd.DataFrame(columns = [ "Pearson","MIC", "O-MAS", "MEV","MCN"])
#roll_result= pd.DataFrame(columns = [ "Pearson","MIC", "O-MAS", "MEV","MCN"])
#
#for index, row in data.iteritems():
#    slice_ = row
#    p = pearsonr(base, slice_)[0]
#    
#    mine.compute_score(base, slice_) 
#    
#    mic = mine.mic()
#    mas = 1 - mine.mas()
#    mev = mine.mev()
#    mcn = mine.mcn_general()
#    
#    result = np.array([p, mic, mas, mev, mcn])
#    df.loc[str(index)] = result
#    
#df.to_excel('/Users/linjunqi/Desktop/mic_result/最后数据/%s与%s 总结果.xls'%(goal,obj))
#mic_one = rolling_correlation(base, objeet, roll_len = roll_len)
#p_one = rolling_correlation(base, objeet, roll_len = roll_len)
#mic_one.to_excel('/Users/linjunqi/Desktop/mic_result/最后数据/%s与%s mic_rolling.xls'%(goal,obj))
#p_one.to_excel('/Users/linjunqi/Desktop/mic_result/最后数据/%s与%s pearson_rolling.xls'%(goal,obj))
##p = df.Pearson
##mic = df.MIC
##
##p = p.sort_values()[-num_pick:].index
##mic = mic.sort_values()[-num_pick:].index
##
##save_roll_p = {}
##save_roll_mic = {}
##
##for name in p:
##    r = rolling_correlation(base, data[name], roll_len = roll_len)
##    save_roll_p[name] = r
##    
##    
##for name in mic:
##    r = rolling_correlation(base, data[name], roll_len = roll_len)
##    save_roll_mic[name] = r
##
##    
##print(save_roll_p[p[0]])
##q = save_roll_p[p[0]]  
##q.plot()
##plt.show()  






#roll_len = 50
#lag = 6
#bgn = 1
##goal = '平安财险:保费收入:累计值:同比'
##obj = '汽车重点企业:工业总产值:累计同比'
#goal = '平安银行:不良贷款余额:同比:月'
#obj = '广州:中原领先指数:全市:同比'
#num_pick = 4
#
#mine = MINE(alpha = 0.6, c = 15)
#
#
#def rolling_correlation(base, data, roll_len = roll_len):
#    length = len(base)
#    for i in range(length - roll_len):
#        base_slice = base[i: i + roll_len]
#        data_slice = data[i: i + roll_len]
#        temp = base_slice.index.strftime("%Y%m%d") 
##        print(type(str(base_slice.index)))
#        mine.compute_score(base_slice, data_slice)
#
#        mic = mine.mic()
#        mas = 1 - mine.mas()
#        mev = mine.mev()
#        mcn = mine.mcn_general()
#        
#        result = np.array([ mic, mas, mev, mcn])
#        
#        roll_result.loc[str(temp[0])+" - "+str(temp[-1])] = result
##        roll_result.loc["roll-"+str(i)] = result
#        i = i + 1
#        
#    return roll_result
#
#
#
#data = pd.read_excel('/Users/linjunqi/Desktop/mic_result/最后数据/平安相关指标（公开）(1).xls', index_col = 0)
#data = data[bgn:]
#roll_result= pd.DataFrame(columns = ["MIC", "O-MAS", "MEV","MCN"])
#
#base = data[goal]
#objett = data[obj]
#
#r = rolling_correlation(base, objett, roll_len = roll_len)
#r.to_excel('/Users/linjunqi/Desktop/mic_result/最后数据/%s与%s rolling结果.xls'%(goal,obj))
#r.plot()
#plt.show()    
#
#    











roll_len = 50
lag = 6
bgn = 0
total = 195
num_pick = 30

mine = MINE(alpha = 0.6, c = 15)

path = '/Users/linjunqi/Desktop/mic_result'

def rolling_correlation(base, data, roll_len = roll_len):
    length = len(base)
    for i in range(length - roll_len):
        base_slice = base[i: i + roll_len]
        data_slice = data[i: i + roll_len]
        temp = base_slice.index.strftime("%Y%m%d") 
#        print(type(str(base_slice.index)))
        mine.compute_score(base_slice, data_slice)
#        p = pearsonr(base_slice, data_slice)[0]
        mic = mine.mic()
        mas = 1 - mine.mas()
        mev = mine.mev()
        mcn = mine.mcn_general()
        
        result = np.array([ mic, mas, mev, mcn])
        
        roll_result.loc[str(temp[0])+" - "+str(temp[-1])] = result
#        roll_result.loc["roll-"+str(i)] = result
        i = i + 1
        
    return roll_result


def linear_sa(data):
    
    for i in range(len(data)):
        if '-01' in str(data.index[i]):
            diff = (data[i+2] - data[i-1])/3
            data[i] = data[i-1] + diff
            data[i+1] = data[i] + diff
    
    return data

#var = input('请输入想要遍历的锚指标：\n  (1)GDP:不变价:当季同比 \n  (2)工业增加值:当月同比 \n  (3)CPI:当月同比 \n  (4)PPI:全部工业品:当月同比 \n  (5)M1:同比 \n  (6)M2:同比 \n  ')
#goal = var

goal_data = pd.read_excel(path+'/最后数据/平安相关指标（公开）(1).xls', index_col = 0)
data = pd.read_excel(path+'/最后数据/经济数据库（剔除少数据）.xlsx', index_col = 0)
goal_name = goal_data.columns.values.tolist()


var = input('请输入想要遍历的锚指标:%s '%(goal_name))
goal = var
#data = data[bgn:]
#one = data.iloc[bgn:len(data),0]
#m1 = data.iloc[bgn:len(data),9]
#house = data.iloc[bgn:len(data),13]
#base = data[goal]
base = goal_data[goal][-total:]
data = data[-total:]
#base = linear_sa(base)

#data = data.drop([goal], axis = 1)
df = pd.DataFrame(columns = [ "MIC", "O-MAS", "MEV","MCN"])
#roll_result= pd.DataFrame(columns = ["MIC", "O-MAS", "MEV","MCN"])

for index, row in data.iteritems():
    slice_ = row
#    p = pearsonr(base, slice_)[0]
    
    mine.compute_score(base, slice_) 
    
    mic = mine.mic()
    mas = 1 - mine.mas()
    mev = mine.mev()
    mcn = mine.mcn_general()
    
    result = np.array([ mic, mas, mev, mcn])
    df.loc[str(index)] = result
 
print("\n")
print("%s与其他指标遍历的相关系数结果是："%(var))
print(df)
#p = df.Pearson
mic = df.MIC



#p = p.sort_values()[-num_pick:].index
#mic_value = mic.sort_values()[-num_pick:]
#mic_value.to_excel('/Users/linjunqi/Desktop/mic_result/与%s相关系数最高的%s个指标MIC.xls'%(var,num_pick))

mic = mic.sort_values()[-num_pick:].index
print(df)
df_value = df.sort_values(by="MIC" , ascending=False)[:num_pick]
df_value.to_excel(path+'/与%s相关系数最高的%s个指标值.xls'%(var,num_pick))

print(df_value)

print("\n")
print("与%s相关系数最高的%s个指标分别是："%(var,num_pick))
print(mic)
#s = mic.to_series()
#s.to_excel('/Users/linjunqi/Desktop/mic_result/与%s相关系数最高的%s个指标.xls'%(var,num_pick))

save_roll_p = {}
save_roll_mic = []

#for name in p:
#    r = rolling_correlation(base, data[name], roll_len = roll_len)
#    save_roll_p[name] = r
    


for name in mic:
    roll_result= pd.DataFrame(columns = ["MIC", "O-MAS", "MEV","MCN"])
    r = rolling_correlation(base, data[name], roll_len = roll_len)
    save_roll_mic.append(r)


#    save_roll_mic[name].append(r)
#    save_roll_mic[i] = r
#fig = plt.figure(figsize=(10,5))
#ax1 = fig.add_subplot(2,2,1)
#ax2 = fig.add_subplot(2,2,2)
#ax3 = fig.add_subplot(2,2,3)
#ax4 = fig.add_subplot(2,2,4)
    
#
while True:
    print("\n")
    var1 = input("请选择目标指标进行滚动遍历,输入序号:")
    index = var1  
    index = int(index) 
    print(mic[index])
    
    print(save_roll_mic[index])
    
    q = save_roll_mic[index]  
    
#    print('/Users/linjunqi/Desktop/mic_result/%s与%s的滚动相关系数.xls'%(var,mic[index]))
    q.to_excel(path+'/%s与%s的滚动相关系数.xls'%(var,mic[index]))
    q.MIC.plot()
    q['O-MAS'].plot()
    q.MEV.plot()
    q.MCN.plot()
    plt.show()
    
#    ax1.plot(q.MIC)
#    ax1.legend(["MIC"], loc='upper left')
#    ax2.plot(q['O-MAS'])
#    ax1.legend(["O-MAS"], loc='upper left')
#    ax3.plot(q.MEV)
#    ax1.legend(["MEV"], loc='upper left')
#    ax4.plot(q.MCN)
#    ax1.legend(["MCN"], loc='upper left')
#    
#    fig.show()
#    
#






