import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import joblib
import pandas as pd

x = np.array([[4. , 0.5,
               1. , 0. ,
               0. , 1. , 0. , 0. ,
               0. , 0. , 1. , 0. ,
               0. , 0. , 1. , 0. , 0. ,
               0. , 0. , 0. , 1. , 0. ,
               0. , 1. , 0. , 0. ,

               0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. ,
               0. , 0. , 0. , 0. , 0. , 0. , 1. , 0. , 0. , 0. , 0. , 0. , 0. ,
               0. , 0. ,0. ,

               0. , 0. , 0. , 1. ,
               1. , 0. , 0. , 0. ,
               1. , 0. ,0. ]])

y = np.zeros((1, 66))

st.title('疫苗接种情况诊断系统')

num_1 = st.number_input('疫苗接种剂次', value=4.)
y[0][0] = num_1

num_2 = st.number_input('疫苗接种剂量', value=0.5)
y[0][1] = num_2

option_1 = st.selectbox('性别',
                        ('女','男'),
                        index=0)
list1 = ['女', '男']
for i, item in enumerate(list1):
    if item == option_1:
        y[0][2+i] = 1
        break

option_2 = st.selectbox('发热情况',
                        ('37.1-37.5', '37.6-38.5',
                         '>=38.6', 'None'),
                        index=1)
list2 = ['37.1-37.5', '37.6-38.5', '>=38.6', 'None']
for i, item in enumerate(list2):
    if item == option_2:
        y[0][4+i] = 1
        break

option_3 = st.selectbox('局部红肿情况',
                        ('2.5-5.0', '<=2.5',
                         'None', '>5.0'),
                        index=2)
list3 = ['2.5-5.0', '<=2.5', 'None', '>5.0']
for i, item in enumerate(list3):
    if item == option_3:
        y[0][8+i] = 1
        break

option_4 = st.selectbox('局部硬结',
                        ('2.6-5.0', '<=2.5', 'None',
                         'Unknown', '>5.0'),
                        index=2)
list4 = ['2.6-5.0', '<=2.5', 'None', 'Unknown', '>5.0']
for i, item in enumerate(list4):
    if item == option_4:
        y[0][12+i] = 1
        break


option_5 = st.selectbox('接种年龄',
                        ('baby(0-258days)', 'baby+(259-429days)',
                         'baby++(430-741days)', 'baby+++(742-1058days)',
                         'baby++++(1059-3649days)'),
                        index=3)
list5 = ['baby(0-258days)', 'baby+(259-429days)',
         'baby++(430-741days)', 'baby+++(742-1058days)',
         'baby++++(1059-3649days)']
for i, item in enumerate(list5):
    if item == option_5:
        y[0][17+i] = 1
        break

option_6 = st.selectbox('接种组织形式',
                        ('不详', '常规', '应急', '强化'),
                        index=1)
list6 = ['不详', '常规', '应急', '强化']
for i, item in enumerate(list6):
    if item == option_6:
        y[0][22+i] = 1
        break

option_7 = st.selectbox('疫苗名称',
                        ('23价肺炎', '7价肺炎', 'Hib', '乙肝(酵母)', '乙脑(减毒)',
                         '乙脑(灭活)', '卡介苗', '水痘', '流感(裂解)', '流脑A+C群',
                         '流脑A+C（结合）', '流脑A群', '甲型流感(裂解无佐剂)', '甲肝(减毒)',
                         '甲肝(减毒冻干)', '甲肝(灭活)', '白喉', '白破', '百白破', '百白破(无细胞)',
                         '百白破(青少年)', '百白破Hib四联', '百白破IPV和Hib五联', '脊灰(减毒二倍体)'
                         '脊灰(灭活)', '轮状病毒', '麻疹', '麻腮风', '麻风'),
                        index=19)
list7 = ['23价肺炎', '7价肺炎', 'Hib', '乙肝(酵母)', '乙脑(减毒)',
                         '乙脑(灭活)', '卡介苗', '水痘', '流感(裂解)', '流脑A+C群',
                         '流脑A+C（结合）', '流脑A群', '甲型流感(裂解无佐剂)', '甲肝(减毒)',
                         '甲肝(减毒冻干)', '甲肝(灭活)', '白喉', '白破', '百白破', '百白破(无细胞)',
                         '百白破(青少年)', '百白破Hib四联', '百白破IPV和Hib五联', '脊灰(减毒二倍体)'
                         '脊灰(灭活)', '轮状病毒', '麻疹', '麻腮风', '麻风']
for i, item in enumerate(list7):
    if item == option_7:
        y[0][26+i] = 1
        break

option_8 = st.selectbox('接种途径',
                        ('口服', '皮下', '皮内', '肌内'),
                        index=3)
list8 = ['口服', '皮下', '皮内', '肌内']
for i, item in enumerate(list8):
    if item == option_8:
        y[0][55+i] = 1
        break

option_9 = st.selectbox('接诊间隔',
                        ('0-9days', '10-29days', '30-49days', '50-399days'),
                        index=0)
list9 = ['0-9days', '10-29days', '30-49days', '50-399days']
for i, item in enumerate(list9):
    if item == option_9:
        y[0][59+i] = 1
        break

option_10 = st.selectbox('接种部位',
                         ('上臂三角肌', '其它部位', '大腿'),
                         index=0)
list10 = ['上臂三角肌', '其它部位', '大腿']
for i, item in enumerate(list10):
    if item == option_10:
        y[0][63+i] = 1
        break

if st.button('预测'):

    searcher_1 = joblib.load('saved_model/searcher_1.pkl')
    searcher_2 = joblib.load('saved_model/searcher_2.pkl')

    yesorno = searcher_1.predict(x)
    st.write('是否住院:', str(yesorno))

    proba_1 = searcher_1.predict_proba(x)


    state = searcher_2.predict(x)
    st.write('转归情况:', str(state))

    proba_2 = searcher_2.predict_proba(x)

    st.write(list(y))
