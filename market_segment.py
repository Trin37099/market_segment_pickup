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


fileList = []
st.subheader('Please Upload Excel Files')
uploaded_files = st.file_uploader("Choose a XLSX file",type = 'xlsx', accept_multiple_files=True)
for uploaded_file in uploaded_files:
    df = pd.read_excel(uploaded_file,skiprows=[0, 2],thousands=',')
 
    fileList.append(df)
def perform_data(fileList) :
    preday = fileList[1]
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
    postday = fileList[0]
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

    df = pd.merge(preday1, postday1, on='DATE', suffixes=('_pre', '_post'))
    prefixs =['OTA_Rms'
                ,'OTA_Rev'
                ,'OTA_Avg'
                ,'B2B_Rms'
                ,'B2B_Rev'
                ,'B2B_Avg'
                ,'TA_Rms'
                ,'TA_Rev'
                ,'TA_Avg'
                ,'CORP_Rms'
                ,'CORP_Rev'
                ,'CORP_Avg'
                ,'WIN_Rms'
                ,'WIN_Rev'
                ,'WIN_Avg'
                ,'HWS_Rms'
                ,'HWS_Rev'
                ,'HWS_Avg'
                ,'FIT_Rms'
                ,'FIT_Rev'
                ,'FIT_Avg'
                ,'GOV_Rms'
                ,'GOV_Rev'
                ,'GOV_Avg'
                ,'COM_Rms'
                ,'COM_Rev'
                ,'COM_Avg'
                ,'Noncode_Rms'
                ,'Noncode_Rev'
                ,'Noncode_Avg'
                ,'Total_Rms'
                ,'Total_Rev'
                ,'Total_Avg']
    for prefix in prefixs:
        pre_col = prefix + '_pre'
        post_col = prefix + '_post'
        diff_col = prefix + '_pickup'
        df[diff_col] = df[post_col] - df[pre_col]
    
    pickup_report = df[['OTA_Rms_pickup', 'OTA_Rev_pickup',
       'OTA_Avg_pickup', 'B2B_Rms_pickup', 'B2B_Rev_pickup', 'B2B_Avg_pickup',
       'TA_Rms_pickup', 'TA_Rev_pickup', 'TA_Avg_pickup', 'CORP_Rms_pickup',
       'CORP_Rev_pickup', 'CORP_Avg_pickup', 'WIN_Rms_pickup',
       'WIN_Rev_pickup', 'WIN_Avg_pickup', 'HWS_Rms_pickup', 'HWS_Rev_pickup',
       'HWS_Avg_pickup', 'FIT_Rms_pickup', 'FIT_Rev_pickup', 'FIT_Avg_pickup',
       'GOV_Rms_pickup', 'GOV_Rev_pickup', 'GOV_Avg_pickup', 'COM_Rms_pickup',
       'COM_Rev_pickup', 'COM_Avg_pickup', 'Noncode_Rms_pickup',
       'Noncode_Rev_pickup', 'Noncode_Avg_pickup', 'Total_Rms_pickup',
       'Total_Rev_pickup', 'Total_Avg_pickup']]

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
    pickup_report = pickup_report.reorder_levels([0, 1], axis=1)
    return pickup_report


pickup_report = perform_data(fileList)
st.markdown('Amber 85 by market segment')
st.write(pickup_report.to_html(),unsafe_allow_html=True)
