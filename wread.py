#!/d/sysutils/conda/python.exe
# -*- coding: utf-8 -*-
import pandas as pd
import operator,sys

# for chart
import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = pd.read_csv('./address.txt',sep='|',names=['주소번호1', '시명', '구명', '동명', '기타1','지번1','지번2','주소번호2','도로명','기타2','건물번호'], header=None,engine='python')

print(data)

## Creating Subplots
#fig, ax = plt.subplots()
#
#smadi = SMADI(1,True,sys.argv[1])
#smadi = smadi.GetValD()
#
#profitL = []
#profitSum = 0
#
##날짜별오름차순으로 정렬
#data = data.sort_values(by=['date'],axis=0)
##파일이 있는 날짜만 추출
#dateL = list(data.date.drop_duplicates()) 
#dateL = dateL[:-3]
#print(dateL)
#
#
#for day in dateL:
#    day = str(day)
#    weekday = datetime.datetime.weekday(datetime.date(int(day[:4]),int(day[4:6]),int(day[6:])))
#    #월요일만 찾는다.
#    if weekday == 0:
#        #3일전(금요일)날짜를 구한다.
#        friday = datetime.datetime(int(day[:4]),int(day[4:6]),int(day[6:]),12,00,00)+datetime.timedelta(days=+4)
#        fridaystr = '%4d%02d%02d'%(friday.year,friday.month,friday.day)
#
#        #예외 경우들
#        if fridaystr == '20200501':
#            fridaystr = '20200429'
#        #설날인가봐
#        if fridaystr == '20200124':
#            fridaystr = '20200123'
#
#        #한글날인가봐
#        if fridaystr == '20201009':
#            fridaystr = '20201008'
#
#        #추석인가봐
#        if fridaystr == '20201002':
#            fridaystr = '20200929'
#
#        #크리스마스
#        if fridaystr == '20151225':
#            fridaystr = '20151224'
#
#        #신년
#        if fridaystr == '20160101':
#            fridaystr = '20151230'
#
#        #어린이날
#        if fridaystr == '20160506':
#            fridaystr = '20160504'
#
#        #추석인가봐
#        if fridaystr == '20160916':
#            fridaystr = '20160913'
#
#        #말년인가봐
#        if fridaystr == '20161230':
#            fridaystr = '20161229'
#
#        #설날인가봐
#        if fridaystr == '20170127':
#            fridaystr = '20170126'
#
#        #설날인가봐
#        if fridaystr == '20180216':
#            fridaystr = '20180214'
#
#        #31절이네
#        if fridaystr == '20190301':
#            fridaystr = '20190228'
#
#        #추석인가봐
#        if fridaystr == '20190913':
#            fridaystr = '20190911'
#
#        dt_idx = pd.bdate_range(start=day,end=friday+datetime.timedelta(days=+7))
#        dt_list = dt_idx.strftime('%Y%m%d').tolist()
#        isstart = data.date >= int(dt_list[0])
#        isend   = data.date <= int(dt_list[-1])
#        weekdata = data[isstart & isend]
#        weekdata = weekdata.sort_values(by=['date','chetime'],axis=0)
#
#        IsUp = False
#        IsDown = False
#        profit = 0
#        closeprice = 0
#        openprice = 0
#        for i in range(len(weekdata)):
#            #print(weekdata.iloc[i]['date'],weekdata.iloc[i]['chetime'],weekdata.iloc[i]['close'])
#            closeprice = weekdata.iloc[i]['close']
#            if openprice == 0:
#                openprice = weekdata.iloc[i]['open']
#                upband = openprice + smadi[fridaystr][0]*openprice*0.1
#                downband = openprice - smadi[fridaystr][0]*openprice*0.1
#                print(day, '시작!%10.2f'%upband,'%10.2f'%downband,openprice,smadi[fridaystr][0])
#
#            if upband < weekdata.iloc[i]['high'] and not IsUp:
#                if IsDown:
#                    #print(weekdata.iloc[i]['date'],weekdata.iloc[i]['chetime'],'하단청산 상단 스위칭!',GetHogaPrice(upband,'BUY'))
#                    profit -= (GetHogaPrice(upband,'BUY')-GetHogaPrice(downband,'SELL'))
#                    IsDown = False
#                else:
#                    #print(weekdata.iloc[i]['date'],weekdata.iloc[i]['chetime'],'상단돌파 진입!',GetHogaPrice(upband,'BUY'))
#                    pass
#                enterPrice = GetHogaPrice(upband,'BUY')
#                IsUp = True
#    
#            if downband > weekdata.iloc[i]['low'] and not IsDown:
#                if IsUp:
#                    #print(weekdata.iloc[i]['date'],weekdata.iloc[i]['chetime'],'상단청산 하단 스위칭!',GetHogaPrice(downband,'SELL'))
#                    profit -= (GetHogaPrice(upband,'BUY')-GetHogaPrice(downband,'SELL'))
#                    IsUp = False
#                else:
#                    #print(weekdata.iloc[i]['date'],weekdata.iloc[i]['chetime'],'하단돌파 진입!',GetHogaPrice(downband,'SELL'))
#                    pass
#                enterPrice = GetHogaPrice(downband,'SELL')
#                IsDown = True
#
#        if IsUp:
#            profit += closeprice - enterPrice
#
#        if IsDown:
#            profit += enterPrice - closeprice
#
#        profitSum += profit
#        profitL.append(profitSum)
#        print(day,'결과%7d %7d %7d(%6.2f) %7d' %(upband,downband,profit,profit*100/openprice,closeprice))
#        #print('%7d' %(profit))
#plt.plot(profitL,marker='*',markersize=4)
#plt.show()
