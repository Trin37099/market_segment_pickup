import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
from datetime import datetime, timedelta
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxlimport pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
from datetime import datetime, timedelta
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

st.set_page_config(
    page_title="Market segment pickup",
    layout = 'wide',
)
st.title('Market segment Report')

st.sidebar.header('Pickup Hotel')

st.subheader('Please Upload Excel Files')
uploaded_files = st.file_uploader("Choose a XLSX file",type = 'xlsx', accept_multiple_files=True)
for uploaded_file in uploaded_files:
    all = pd.read_excel(uploaded_file, engine = 'openpyxl',thousands=',',header=None)

    all = all[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,28,29,30,31,32,33,34,35,36,52,53,54,55,56,57,70,71,72,73,74,75]]
    all = all.rename(columns={ 0:'DATE'
                                  ,1:'OTA_Rms',2:'OTA_Rev',3:'OTA_Avg'
                                  ,4:'B2B_Rms',5:'B2B_Rev',6:'B2B_Avg'
                                  ,7:'TA_Rms',8:'TA_Rev',9:'TA_Avg'
                                  ,10:'GRTA_Rms',11:'GRTA_Rev',12:'GRTA_Avg'
                                  , 13:'CORP_Rms', 14:'CORP_Rev', 15:'CORP_Avg'
                                  ,28:'WIN_Rms', 29:'WIN_Rev', 30:'WIN_Avg'
                                  , 31:'HWS_Rms', 32:'HWS_Rev', 33:'HWS_Avg'
                                  ,34:'FIT_Rms', 35:"FIT_Rev", 36:'FIT_Avg'
                                  ,52:'GOV_Rms', 53:'GOV_Rev', 54:'GOV_Avg'
                                  , 55:'COM_Rms', 56:'COM_Rev',57:'COM_Avg'
                                  ,70:'Noncode_Rms', 71:'Noncode_Rev', 72:'Noncode_Avg'
                                  , 73:'Total_Rms', 74:'Total_Rev',75:'Total_Avg'})
    grass_pre = all.loc[0+3:369-1]
    grass_post = all.loc[370+3:739-1]
    arb_pre = all.loc[740+3:1109-1]
    arb_post = all.loc[1110+3:1479-1]
    as_pre = all.loc[1480+3:1849-1]
    as_post = all.loc[1850+3:2219-1]
    amp_pre = all.loc[2220+3:2589-1]
    amp_post = all.loc[2590+3:2959-1]
    ard_pre = all.loc[2960+3:3329-1]
    ard_post = all.loc[3330+3:3699-1]
    alt_pre = all.loc[3700+3:4069-1]
    alt_post = all.loc[4070+3:4439-1]
    amber_pre = all.loc[4440+3:4809-1]
    amber_post = all.loc[4810+3:5179-1]
 
def perform_data(preday,postday) :
 

    preday['DATE']= pd.to_datetime(preday['DATE'], format='%a %d/%m/%Y')
    postday['DATE']= pd.to_datetime(postday['DATE'], format='%a %d/%m/%Y')

    postday= postday.set_index('DATE')
    preday= preday.set_index('DATE')

    df = pd.merge(preday, postday, on='DATE', suffixes=('_pre', '_post'))
    prefixs =['OTA_Rms'
                ,'OTA_Rev'
                ,'OTA_Avg'
                ,'B2B_Rms'
                ,'B2B_Rev'
                ,'B2B_Avg'
                ,'TA_Rms'
                ,'TA_Rev'
                ,'TA_Avg'
                ,'GRTA_Rms'
                ,'GRTA_Rev'
                ,'GRTA_Avg'
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
        #df[diff_col] = df[diff_col].apply(lambda x: f'+{x}' if x > 0 else x)
    
    pickup_report = df[['OTA_Rms_pickup', 'OTA_Rev_pickup',
       'OTA_Avg_pickup', 'B2B_Rms_pickup', 'B2B_Rev_pickup', 'B2B_Avg_pickup',
       'TA_Rms_pickup', 'TA_Rev_pickup', 'TA_Avg_pickup','GRTA_Rms_pickup'
       ,'GRTA_Rev_pickup','GRTA_Avg_pickup', 'CORP_Rms_pickup',
       'CORP_Rev_pickup', 'CORP_Avg_pickup', 'WIN_Rms_pickup',
       'WIN_Rev_pickup', 'WIN_Avg_pickup', 'HWS_Rms_pickup', 'HWS_Rev_pickup',
       'HWS_Avg_pickup', 'FIT_Rms_pickup', 'FIT_Rev_pickup', 'FIT_Avg_pickup',
       'GOV_Rms_pickup', 'GOV_Rev_pickup', 'GOV_Avg_pickup', 'COM_Rms_pickup',
       'COM_Rev_pickup', 'COM_Avg_pickup', 'Noncode_Rms_pickup',
       'Noncode_Rev_pickup', 'Noncode_Avg_pickup', 'Total_Rms_pickup',
       'Total_Rev_pickup', 'Total_Avg_pickup']]
    
    return pickup_report


pickup_report_thegrass = perform_data(grass_pre,grass_post)
pickup_report_arb = perform_data(arb_pre,arb_post)
pickup_report_as =perform_data(as_pre,as_post)
pickup_report_amp =perform_data(amp_pre,amp_post)
pickup_report_ard =perform_data(ard_pre,ard_post)
pickup_report_alt = perform_data(alt_pre,alt_post)
pickup_report_amber = perform_data(amber_pre,amber_post)
select_hotel = ['pickup report the grass'
                ,'pickup report arb'
                ,'pickup report alt'
                ,'pickup report as'
                ,'pickup report amp'
                ,'pickup report ard'
                ,'pickup report amber'
                ,'exit']

dayname = ['Monday'
           , 'Tuesday'
           , 'Wednesday'
           , 'Thursday'
           , 'Friday'
           , 'Saturday'
           , 'Sunday']

rms = ['OTA_Rms_pickup'
       , 'B2B_Rms_pickup'
       , 'TA_Rms_pickup'
       , 'GRTA_Rms_pickup'
       , 'CORP_Rms_pickup'
       , 'WIN_Rms_pickup'
       , 'HWS_Rms_pickup'
       , 'FIT_Rms_pickup'
       , 'GOV_Rms_pickup'
       , 'COM_Rms_pickup'
       , 'Noncode_Rms_pickup'
       , 'Total_Rms_pickup']

rev = ['OTA_Rev_pickup'
       , 'B2B_Rev_pickup'
       , 'TA_Rev_pickup'
       , 'GRTA_Rev_pickup'
       , 'CORP_Rev_pickup'
       , 'WIN_Rev_pickup'
       , 'HWS_Rev_pickup'
       , 'FIT_Rev_pickup'
       , 'GOV_Rev_pickup'
       , 'COM_Rev_pickup'
       , 'Noncode_Rev_pickup'
       , 'Total_Rev_pickup']

avg = ['OTA_Avg_pickup'
        'B2B_Avg_pickup'
        , 'TA_Avg_pickup'
        , 'GRTA_Avg_pickup'
        , 'CORP_Avg_pickup'
        , 'WIN_Avg_pickup'
        , 'HWS_Avg_pickup'
        , 'FIT_Avg_pickup'
        , 'GOV_Avg_pickup'
        , 'COM_Avg_pickup'
        , 'Noncode_Avg_pickup'
        , 'Total_Avg_pickup']

selected_options = st.sidebar.selectbox('Select Hotel', select_hotel)
#----------------------------------------------------------------------------------------
if selected_options == 'pickup report the grass':
    st.markdown('**The Grass Serviced Suites**')
    start_date = st.sidebar.date_input('Start date', pickup_report_thegrass.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_thegrass.index.max())
    filtered_df = pickup_report_thegrass.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        #plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                # '+' + filtered_df_d.astype(str), filtered_df_d)
                                # , index=filtered_df_d.index, columns=filtered_df_d.columns)
        #st.write(plus)
        st.write(filtered_df_d)
        st.bar_chart(filtered_df_d)
    else:
        #plus = pd.DataFrame(np.where(filtered_df > 0
                                # , '+' + filtered_df.astype(str), filtered_df)
                                # , index=filtered_df.index, columns=filtered_df.columns)
        st.write(filtered_df)
        st.bar_chart(filtered_df)
#----------------------------------------------------------------------------------------
elif selected_options == 'pickup report arb':
    st.markdown('**Arbour Hotel and resdence**')
    start_date = st.sidebar.date_input('Start date', pickup_report_arb.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_arb.index.max())
    filtered_df = pickup_report_arb.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        filtered_df_d = filtered_df_d.fillna(0)
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        #st.write(filtered_df_d)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        #st.write(filtered_df)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report alt':
    st.markdown('**Alter Hotel and residence**')
    start_date = st.sidebar.date_input('Start date', pickup_report_alt.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_alt.index.max())
    filtered_df = pickup_report_alt.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        filtered_df_d = filtered_df_d.fillna(0)
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        #st.write(filtered_df_d)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        #st.write(filtered_df)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report as':
    st.markdown('**Aster Hotel and residence**')
    start_date = st.sidebar.date_input('Start date', pickup_report_as.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_as.index.max())
    filtered_df = pickup_report_as.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]


    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        filtered_df_d = filtered_df_d.fillna(0)
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        #st.write(filtered_df_d)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        #st.write(filtered_df)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report amp':
    st.markdown('**Hotel Amber Pattaya**')
    start_date = st.sidebar.date_input('Start date', pickup_report_amp.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_amp.index.max())
    filtered_df = pickup_report_amp.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        filtered_df_d = filtered_df_d.fillna(0)
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        #st.write(filtered_df_d)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        #st.write(filtered_df)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report ard':
    st.markdown('**Arden Hotel and residence**')
    start_date = st.sidebar.date_input('Start date', pickup_report_ard.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_ard.index.max())
    filtered_df = pickup_report_ard.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        filtered_df_d = filtered_df_d.fillna(0)
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        #st.write(filtered_df_d)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        #st.write(filtered_df)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report amber':
    st.markdown('**Hotel Amber Sukhumvit 85**')
    start_date = st.sidebar.date_input('Start date', pickup_report_amber.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_amber.index.max())
    filtered_df = pickup_report_amber.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        filtered_df_d = filtered_df_d.fillna(0)
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        #st.write(filtered_df_d)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        #st.write(filtered_df)
        st.bar_chart(filtered_df)
else :
    st.write(' ')



import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Market segment pickup",
    layout = 'wide',
)
st.title('Market segment Report')

st.sidebar.header('Pickup Hotel')

st.subheader('Please Upload Excel Files')
uploaded_files = st.file_uploader("Choose a XLSX file",type = 'xlsx', accept_multiple_files=True)
for uploaded_file in uploaded_files:
    all = pd.read_excel(uploaded_file, engine = 'openpyxl',thousands=',',header=None)

    all = all[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,28,29,30,31,32,33,34,35,36,52,53,54,55,56,57,70,71,72,73,74,75]]
    all = all.rename(columns={ 0:'DATE'
                                  ,1:'OTA_Rms',2:'OTA_Rev',3:'OTA_Avg'
                                  ,4:'B2B_Rms',5:'B2B_Rev',6:'B2B_Avg'
                                  ,7:'TA_Rms',8:'TA_Rev',9:'TA_Avg'
                                  ,10:'GRTA_Rms',11:'GRTA_Rev',12:'GRTA_Avg'
                                  , 13:'CORP_Rms', 14:'CORP_Rev', 15:'CORP_Avg'
                                  ,28:'WIN_Rms', 29:'WIN_Rev', 30:'WIN_Avg'
                                  , 31:'HWS_Rms', 32:'HWS_Rev', 33:'HWS_Avg'
                                  ,34:'FIT_Rms', 35:"FIT_Rev", 36:'FIT_Avg'
                                  ,52:'GOV_Rms', 53:'GOV_Rev', 54:'GOV_Avg'
                                  , 55:'COM_Rms', 56:'COM_Rev',57:'COM_Avg'
                                  ,70:'Noncode_Rms', 71:'Noncode_Rev', 72:'Noncode_Avg'
                                  , 73:'Total_Rms', 74:'Total_Rev',75:'Total_Avg'})
    grass_pre = all.loc[0+3:369-1]
    grass_post = all.loc[370+3:739-1]
    arb_pre = all.loc[740+3:1109-1]
    arb_post = all.loc[1110+3:1479-1]
    as_pre = all.loc[1480+3:1849-1]
    as_post = all.loc[1850+3:2219-1]
    amp_pre = all.loc[2220+3:2589-1]
    amp_post = all.loc[2590+3:2959-1]
    ard_pre = all.loc[2960+3:3329-1]
    ard_post = all.loc[3330+3:3699-1]
    alt_pre = all.loc[3700+3:4069-1]
    alt_post = all.loc[4070+3:4439-1]
    amber_pre = all.loc[4440+3:4809-1]
    amber_post = all.loc[4810+3:5179-1]
 
def perform_data(preday,postday) :
 

    preday['DATE']= pd.to_datetime(preday['DATE'], format='%a %d/%m/%Y')
    postday['DATE']= pd.to_datetime(postday['DATE'], format='%a %d/%m/%Y')

    postday= postday.set_index('DATE')
    preday= preday.set_index('DATE')

    df = pd.merge(preday, postday, on='DATE', suffixes=('_pre', '_post'))
    prefixs =['OTA_Rms'
                ,'OTA_Rev'
                ,'OTA_Avg'
                ,'B2B_Rms'
                ,'B2B_Rev'
                ,'B2B_Avg'
                ,'TA_Rms'
                ,'TA_Rev'
                ,'TA_Avg'
                ,'GRTA_Rms'
                ,'GRTA_Rev'
                ,'GRTA_Avg'
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
        #df[diff_col] = df[diff_col].apply(lambda x: f'+{x}' if x > 0 else x)
    
    pickup_report = df[['OTA_Rms_pickup', 'OTA_Rev_pickup',
       'OTA_Avg_pickup', 'B2B_Rms_pickup', 'B2B_Rev_pickup', 'B2B_Avg_pickup',
       'TA_Rms_pickup', 'TA_Rev_pickup', 'TA_Avg_pickup','GRTA_Rms_pickup'
       ,'GRTA_Rev_pickup','GRTA_Avg_pickup', 'CORP_Rms_pickup',
       'CORP_Rev_pickup', 'CORP_Avg_pickup', 'WIN_Rms_pickup',
       'WIN_Rev_pickup', 'WIN_Avg_pickup', 'HWS_Rms_pickup', 'HWS_Rev_pickup',
       'HWS_Avg_pickup', 'FIT_Rms_pickup', 'FIT_Rev_pickup', 'FIT_Avg_pickup',
       'GOV_Rms_pickup', 'GOV_Rev_pickup', 'GOV_Avg_pickup', 'COM_Rms_pickup',
       'COM_Rev_pickup', 'COM_Avg_pickup', 'Noncode_Rms_pickup',
       'Noncode_Rev_pickup', 'Noncode_Avg_pickup', 'Total_Rms_pickup',
       'Total_Rev_pickup', 'Total_Avg_pickup']]
    
    return pickup_report


pickup_report_thegrass = perform_data(grass_pre,grass_post)
pickup_report_arb = perform_data(arb_pre,arb_post)
pickup_report_as =perform_data(as_pre,as_post)
pickup_report_amp =perform_data(amp_pre,amp_post)
pickup_report_ard =perform_data(ard_pre,ard_post)
pickup_report_alt = perform_data(alt_pre,alt_post)
pickup_report_amber = perform_data(amber_pre,amber_post)
select_hotel = ['pickup report the grass'
                ,'pickup report arb'
                ,'pickup report alt'
                ,'pickup report as'
                ,'pickup report amp'
                ,'pickup report ard'
                ,'pickup report amber'
                ,'exit']

dayname = ['Monday'
           , 'Tuesday'
           , 'Wednesday'
           , 'Thursday'
           , 'Friday'
           , 'Saturday'
           , 'Sunday']

rms = ['OTA_Rms_pickup'
       , 'B2B_Rms_pickup'
       , 'TA_Rms_pickup'
       , 'GRTA_Rms_pickup'
       , 'CORP_Rms_pickup'
       , 'WIN_Rms_pickup'
       , 'HWS_Rms_pickup'
       , 'FIT_Rms_pickup'
       , 'GOV_Rms_pickup'
       , 'COM_Rms_pickup'
       , 'Noncode_Rms_pickup'
       , 'Total_Rms_pickup']

rev = ['OTA_Rev_pickup'
       , 'B2B_Rev_pickup'
       , 'TA_Rev_pickup'
       , 'GRTA_Rev_pickup'
       , 'CORP_Rev_pickup'
       , 'WIN_Rev_pickup'
       , 'HWS_Rev_pickup'
       , 'FIT_Rev_pickup'
       , 'GOV_Rev_pickup'
       , 'COM_Rev_pickup'
       , 'Noncode_Rev_pickup'
       , 'Total_Rev_pickup']

avg = ['OTA_Avg_pickup'
        'B2B_Avg_pickup'
        , 'TA_Avg_pickup'
        , 'GRTA_Avg_pickup'
        , 'CORP_Avg_pickup'
        , 'WIN_Avg_pickup'
        , 'HWS_Avg_pickup'
        , 'FIT_Avg_pickup'
        , 'GOV_Avg_pickup'
        , 'COM_Avg_pickup'
        , 'Noncode_Avg_pickup'
        , 'Total_Avg_pickup']

selected_options = st.sidebar.selectbox('Select Hotel', select_hotel)
if selected_options == 'pickup report the grass':
    st.markdown('**The Grass Serviced Suites**')
    start_date = st.sidebar.date_input('Start date', pickup_report_thegrass.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_thegrass.index.max())
    filtered_df = pickup_report_thegrass.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report arb':
    st.markdown('**Arbour Hotel and resdence**')
    start_date = st.sidebar.date_input('Start date', pickup_report_arb.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_arb.index.max())
    filtered_df = pickup_report_arb.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report alt':
    st.markdown('**Alter Hotel and residence**')
    start_date = st.sidebar.date_input('Start date', pickup_report_alt.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_alt.index.max())
    filtered_df = pickup_report_alt.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report as':
    st.markdown('**Aster Hotel and residence**')
    start_date = st.sidebar.date_input('Start date', pickup_report_as.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_as.index.max())
    filtered_df = pickup_report_as.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]


    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report amp':
    st.markdown('**Hotel Amber Pattaya**')
    start_date = st.sidebar.date_input('Start date', pickup_report_amp.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_amp.index.max())
    filtered_df = pickup_report_amp.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report ard':
    st.markdown('**Arden Hotel and residence**')
    start_date = st.sidebar.date_input('Start date', pickup_report_ard.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_ard.index.max())
    filtered_df = pickup_report_ard.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        st.bar_chart(filtered_df)
elif selected_options == 'pickup report amber':
    st.markdown('**Hotel Amber Sukhumvit 85**')
    start_date = st.sidebar.date_input('Start date', pickup_report_amber.index.min())
    end_date = st.sidebar.date_input('End date', pickup_report_amber.index.max())
    filtered_df = pickup_report_amber.loc[start_date:end_date]

    filter_type = st.sidebar.selectbox('Filter type', ['Rms','Rev','Avg'])
    if filter_type == 'Rms':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rms_pickup')]
    elif filter_type == 'Rev':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Rev_pickup')]
    elif filter_type == 'Avg':
        filtered_df = filtered_df.loc[:, filtered_df.columns.str.endswith('_Avg_pickup')]

    selected_day = st.sidebar.multiselect('Select day(s) of the week', dayname)
    if selected_day:
        filtered_df_d = filtered_df[filtered_df.index.strftime('%A').isin(selected_day)]
        plus = pd.DataFrame(np.where(filtered_df_d > 0, 
                                 '+' + filtered_df_d.astype(str), filtered_df_d)
                                 , index=filtered_df_d.index, columns=filtered_df_d.columns)
        st.write(plus)
        st.bar_chart(filtered_df_d)
    else:
        plus = pd.DataFrame(np.where(filtered_df > 0
                                 , '+' + filtered_df.astype(str), filtered_df)
                                 , index=filtered_df.index, columns=filtered_df.columns)
        st.write(plus)
        st.bar_chart(filtered_df)
else :
    st.write(' ')


