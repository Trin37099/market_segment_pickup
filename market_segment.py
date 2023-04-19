import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Market segment pickup",
    layout = 'wide',
)
st.title('Market segment Report')

#----------------------------------------------------------------------------------------------------------------
st.subheader('Please Upload Market segment Hotel Amber Sukhumvit 85 yesterder xlsx Files')
uploaded_files = st.file_uploader("Choose Hotel Amber Sukhumvit 85 yesterder xlsx file",type = 'xlsx', accept_multiple_files=True)
for uploaded_file in uploaded_files:
    preday = pd.read_excel(uploaded_files,skiprows=[0, 2],thousands=',')
    
st.subheader('Please Upload Market segment Hotel Amber Sukhumvit 85 today xlsx Files')
uploaded_files1 = st.file_uploader("Choose Hotel Amber Sukhumvit 85 today xlsx file",type = 'xlsx', accept_multiple_files=True)
for uploaded_file1 in uploaded_files1:
    postday = pd.read_excel(uploaded_files1,skiprows=[0, 2],thousands=',')

preday1 = preday[['Unnamed: 0',
                  'OTA','Online Travel Agent', 'OTA.1'
                  , 'B2B','Travel Agent B2B', 'B2B.1'
                  , 'TA', 'Travel Agent', 'TA.1'
                  , 'CORP', 'Corporate', 'CORP.1'
                  ,'WIN', 'Walk In', 'WIN.1'
                  , 'HWS', 'Hotel Website', 'HWS.1'
                  ,'FIT', 'Free Individaul Traveler', 'FIT.1'
                  ,'GOV', 'Government Rate', 'GOV.1'
                  , 'COM', 'Complimentary','COM.1'
                  ,'NON code', 'Other', 'NON code.1'
                  , 'Unnamed: 73', 'Total','Unnamed: 75']]

postday1 = postday[['Unnamed: 0',
                  'OTA','Online Travel Agent', 'OTA.1'
                  , 'B2B','Travel Agent B2B', 'B2B.1'
                  , 'TA', 'Travel Agent', 'TA.1'
                  , 'CORP', 'Corporate', 'CORP.1'
                  ,'WIN', 'Walk In', 'WIN.1'
                  , 'HWS', 'Hotel Website', 'HWS.1'
                  ,'FIT', 'Free Individaul Traveler', 'FIT.1'
                  ,'GOV', 'Government Rate', 'GOV.1'
                  , 'COM', 'Complimentary','COM.1'
                  ,'NON code', 'Other', 'NON code.1'
                  , 'Unnamed: 73', 'Total','Unnamed: 75']]

preday1 = preday1.drop(preday1[(preday1['Unnamed: 0'] == 'Total')].index)
preday1 = preday1.rename(columns={'Unnamed: 0':'DATE'
                                  ,'OTA':'OTA_Rms','Online Travel Agent':'OTA_Rev','OTA.1':'OTA_Avg'
                                  ,"B2B":'B2B_Rms','Travel Agent B2B':'B2B_Rev','B2B.1':'B2B_Avg'
                                  ,'TA':'TA_Rms','Travel Agent':'TA_Rev','TA.1':'TA_Avg'
                                  , 'CORP':'CORP_Rms', 'Corporate':'CORP_Rev', 'CORP.1':'CORP_Avg'
                                  ,'WIN':'WIN_Rms', 'Walk In':'WIN_Rev', 'WIN.1':'WIN_Avg'
                                  , 'HWS':'HWS_Rms', 'Hotel Website':'HWS_Rev', 'HWS.1':'HWS_Avg'
                                  ,'FIT':'FIT_Rms', 'Free Individaul Traveler':"FIT_Rev", 'FIT.1':'FIT_Avg'
                                  ,'GOV':'GOV_Rms', 'Government Rate':'GOV_Rev', 'GOV.1':'GOV_Avg'
                                  , 'COM':'COM_Rms', 'Complimentary':'COM_Rev','COM.1':'COM_Avg'
                                  ,'NON code':'Noncode_Rms', 'Other':'Noncode_Rev', 'NON code.1':'Noncode_Avg'
                                  , 'Unnamed: 73':'Total_Rms', 'Total':'Total_Rev','Unnamed: 75':'Total_Avg'})

postday1 = postday1.drop(postday1[(postday1['Unnamed: 0'] == 'Total')].index)
postday1 = postday1.rename(columns={'Unnamed: 0':'DATE'
                                  ,'OTA':'OTA_Rms','Online Travel Agent':'OTA_Rev','OTA.1':'OTA_Avg'
                                  ,"B2B":'B2B_Rms','Travel Agent B2B':'B2B_Rev','B2B.1':'B2B_Avg'
                                  ,'TA':'TA_Rms','Travel Agent':'TA_Rev','TA.1':'TA_Avg'
                                  , 'CORP':'CORP_Rms', 'Corporate':'CORP_Rev', 'CORP.1':'CORP_Avg'
                                  ,'WIN':'WIN_Rms', 'Walk In':'WIN_Rev', 'WIN.1':'WIN_Avg'
                                  , 'HWS':'HWS_Rms', 'Hotel Website':'HWS_Rev', 'HWS.1':'HWS_Avg'
                                  ,'FIT':'FIT_Rms', 'Free Individaul Traveler':"FIT_Rev", 'FIT.1':'FIT_Avg'
                                  ,'GOV':'GOV_Rms', 'Government Rate':'GOV_Rev', 'GOV.1':'GOV_Avg'
                                  , 'COM':'COM_Rms', 'Complimentary':'COM_Rev','COM.1':'COM_Avg'
                                  ,'NON code':'Noncode_Rms', 'Other':'Noncode_Rev', 'NON code.1':'Noncode_Avg'
                                  , 'Unnamed: 73':'Total_Rms', 'Total':'Total_Rev','Unnamed: 75':'Total_Avg'})

preday1['DATE']= pd.to_datetime(preday1['DATE'], format='%a %d/%m/%Y')
postday1['DATE']= pd.to_datetime(postday1['DATE'], format='%a %d/%m/%Y')

postday1= postday1.set_index('DATE')
preday1= preday1.set_index('DATE')

pickup_report = preday1.iloc[1:] - postday1.iloc[0:]

cols = pd.MultiIndex.from_tuples([('OTA', 'Rms.'), ('OTA', 'Rev.'), ('OTA', 'Avg.')
                                                  , ('B2B', 'Rms.'), ('B2B', 'Rev.'), ('B2B', 'Avg.')
                                                  , ('TA', 'Rms.'), ('TA', 'Rev.'), ('TA', 'Avg.')
                                                  ,('CORP', 'Rms.'), ('CORP', 'Rev.'), ('CORP', 'Avg.')
                                                  ,('WIN', 'Rms.'), ('WIN', 'Rev.'), ('WIN', 'Avg.')
                                                  ,('HWS', 'Rms.'), ('HWS', 'Rev.'), ('HWS', 'Avg.')
                                                  ,('FIT', 'Rms.'), ('FIT', 'Rev.'), ('FIT', 'Avg.')
                                                  ,('GOV', 'Rms.'), ('GOV', 'Rev.'), ('GOV', 'Avg.')
                                                  ,('COM', 'Rms.'), ('COM', 'Rev.'), ('COM', 'Avg.')
                                                  ,('Noncode', 'Rms.'), ('Noncode', 'Rev.'), ('Noncode', 'Avg.')
                                                  ,('Total', 'Rms.'), ('Total', 'Rev.'), ('Total', 'Avg.')])

pickup_report.columns = cols
pickup_report = pickup_report.reorder_levels([0, 1], axis=1).sort_index(axis=1)


st.write(pickup_report.to_html(),unsafe_allow_html=True)
