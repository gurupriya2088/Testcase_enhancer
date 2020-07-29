import pandas as pd
import numpy as np
import re
import pickle
import copy
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse.csr import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
df1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\18. 35 Release_HPBX_SIT_14_08-2018.xlsx",sheet_name='Scenarios',names=['id','name','steps','result'],parse_cols=[6,8,9,10])
df2_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\18.3 Release Final Version_Consolidated.xlsx",sheet_name='Regression',names=['id','name','steps','result'],parse_cols=[5,6,7,8,]) 
df2_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\18.3 Release Final Version_Consolidated.xlsx",sheet_name='Sales',names=['id','name','steps','result'],parse_cols=[5,7,8,9])
df3=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\18.3_Test Design_Final.xlsx",sheet_name='Scenarios',names=['id','name','steps','result'],parse_cols=[6,8,9,10])
df4=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\CATGOV -692 Testcases V0.2.xlsx",sheet_name='CSR User',names=['id','name','steps','result'],parse_cols=[6,8,9,11])
df5=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\CATGOV-330 Testcase sheet.xlsx",names=['id','name','steps','result'],sheet_name='CATGOV-330 Testcase sheet',parse_cols=[5,7,8,9])
#df6=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\CATGOV-552 TV complete_Test pack.xlsx",names=['id','name','steps','result'],sheet_name='Small',parse_cols=[6,11,12,13])
df7=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\CATGOV-649 testcase sheet.xlsx",names=['id','name','steps','result'],sheet_name='CATGOV-649',parse_cols=[6,9,10,11])
#df8=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\CATGOV-650_Test case sheet.xlsx",names=['id','name','steps','result'],sheet_name='Scenarios',parse_cols=[4,9,10,11])
df9=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\CATGOV-722 final TC sheet.xlsx",names=['id','name','steps','result'],sheet_name='CSR Profile',parse_cols=[3,4,5,6])
df10=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Catgov-805 testcase sheet_Baseline.xlsx",names=['id','name','steps','result'],sheet_name='Partner Manager',parse_cols=[6,9,10,11])
df11=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\CEE MVP CR'S PI8-V1.0 -CL after removal of few Sales stories.xlsx",names=['id','name','steps','result'],sheet_name='Test case sheet',parse_cols=[7,9,10,11])
df12=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\CEE PI7 Test Design_V 05_Draft.xlsx",names=['id','name','steps','result'],sheet_name='Test case sheet',parse_cols=[7,9,10,11])
df13=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\CHG-9522_VFZG_SIT_TC sheet.xlsx",names=['id','name','steps','result'],sheet_name='EDR Scenarios',parse_cols=[2,3,6,7])
df14=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Data Refresh Regression Testpack.xlsx",names=['id','name','steps','result'],sheet_name='Regression scenarios',parse_cols=[6,8,9,11])
df15=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Lightning_UI_Test Scenario Pack_19th Nov.xlsx",names=['id','name','steps','result'],sheet_name='sheet2',parse_cols=[4,5,6,7])
df16=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\R 18.35_SIT_Test Design_V.2.xlsx",names=['id','name','steps','result'],sheet_name='Test Design',parse_cols=[6,8,9,10])
df17=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Release 18.4 Sales Test pack.xlsx",names=['id','name','steps','result'],sheet_name='QNT_779',parse_cols=[4,6,7,8])
df18_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 1_Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-402',parse_cols=[0,2,4,6])
df18_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 1_Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-411',parse_cols=[0,2,4,6])
df18_3=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 1_Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-383',parse_cols=[0,2,3,5])
#df19_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 2_Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-405',parse_cols=[0,2,3,5])
df19_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 2_Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-394',parse_cols=[0,4,5,6])
df20_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 3_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-423',parse_cols=[0,2,4,6])
#df20_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 3_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-16',parse_cols=[0,2,4,6])
df20_3=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 3_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-343',parse_cols=[0,2,4,6])
df20_4=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 3_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-6',parse_cols=[0,2,4,6])
df20_5=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 3_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-55',parse_cols=[0,2,4,6])
df20_6=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 3_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-3',parse_cols=[0,2,4,6])
df20_7=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 3_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-388',parse_cols=[0,2,4,6])
df21_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 4_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-20',parse_cols=[0,2,4,6])
df21_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 4_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-9',parse_cols=[0,2,4,6])
df21_3=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 4_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-393',parse_cols=[0,2,4,6])
df21_4=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 4_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-21',parse_cols=[0,2,4,6])
df21_5=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 4_Test Suite_V6.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-14',parse_cols=[0,2,4,6])
df22_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 5_Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-87',parse_cols=[0,2,4,6])
df22_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 5_Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-59',parse_cols=[0,2,4,6])
df23_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 6 - Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-15',parse_cols=[0,2,3,5])
df23_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 6 - Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-408',parse_cols=[0,2,3,5])
df23_3=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 6 - Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-10',parse_cols=[0,2,3,5])
df23_4=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 6 - Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-345',parse_cols=[0,2,3,5])
df23_5=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 6 - Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-397',parse_cols=[0,2,3,5])
df23_6=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 6 - Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-407',parse_cols=[0,2,3,5])
df23_7=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 6 - Test Suite_V3.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-344',parse_cols=[0,2,3,5])
df24_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 7 - Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-384',parse_cols=[0,2,4,6])
df24_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 7 - Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-562',parse_cols=[0,2,3,5])
df24_3=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 7 - Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-389',parse_cols=[0,2,3,5])
df24_4=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 7 - Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-58',parse_cols=[0,2,4,6])
df25_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 9 - Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-666',parse_cols=[0,2,3,5])
df25_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 9 - Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-395',parse_cols=[0,2,4,6])
df26_1=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 10_Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-673',parse_cols=[0,2,4,6])
df26_2=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 10_Test Suite_V2.0.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-425',parse_cols=[0,2,4,6])
df27=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 11_Test Suite_V1 2.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-724',parse_cols=[0,2,4,6])
df28=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Sprint 12_Test Suite_V1 2.xlsx",names=['id','name','steps','result'],sheet_name='SCB2BPE-777',parse_cols=[0,2,4,6])
df29=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Testcase sheet_CHG_9561.xlsx",names=['id','name','steps','result'],sheet_name='CHG-9561 Testcase sheet',parse_cols=[4,8,9,10])
df30=pd.read_excel("D:\\TestOptimizer\\TestOptimizer\\NL\\um\\Tracy Rehoming updated TC sheet_Baseline.xlsx",names=['id','name','steps','result'],sheet_name='Tracy Rehoming TC',parse_cols=[6,9,10,11])

df1['Project']="df18. 35 Release_HPBX_SIT_14_08-2018"
df2_1['Project']="18.3 Release Final Version_Consolidated"
df2_2['Project']="18.3 Release Final Version_Consolidated"
df3['Project']="18.3_Test Design_Final"
df4['Project']="CATGOV -692 Testcases V0.2"
df5['Project']="CATGOV-330 Testcase sheet"
df7['Project']="CATGOV-649 testcase sheet"
df9['Project']="CATGOV-722 final TC sheet"
df10['Project']="Catgov-805 testcase sheet_Baseline"
df11['Project']="CEE MVP CR'S PI8-V1.0 -CL after removal of few Sales stories"
df12['Project']="CEE PI7 Test Design_V 05_Draft"
df13['Project']="CHG-9522_VFZG_SIT_TC sheet"
df14['Project']="Data Refresh Regression Testpack"
df15['Project']="Lightning_UI_Test Scenario Pack_19th Nov"
df16['Project']="R 18.35_SIT_Test Design_V.2"
df17['Project']="Release 18.4 Sales Test pack"
df18_1['Project']="Sprint 10_Test Suite_V2.0"
df18_2['Project']="Sprint 10_Test Suite_V2.0"
df18_3['Project']="Sprint 10_Test Suite_V2.0"
df19_2['Project']="Sprint 11_Test Suite_V1 2"
df20_1['Project']="Sprint 12_Test Suite_V1 2"
df20_3['Project']="Sprint 12_Test Suite_V1 2"
df20_4['Project']="Sprint 12_Test Suite_V1 2"
df20_5['Project']="Sprint 12_Test Suite_V1 2"
df20_6['Project']="Sprint 12_Test Suite_V1 2"
df20_7['Project']="Sprint 12_Test Suite_V1 2"
df21_1['Project']="Sprint 1_Test Suite_V3.0"
df21_2['Project']="Sprint 1_Test Suite_V3.0"
df21_3['Project']="Sprint 1_Test Suite_V3.0"
df21_4['Project']="Sprint 1_Test Suite_V3.0"
df21_5['Project']="Sprint 1_Test Suite_V3.0"
df22_1['Project']="Sprint 2_Test Suite_V3.0"
df22_2['Project']="Sprint 2_Test Suite_V3.0"
df23_1['Project']="Sprint 3_Test Suite_V6.0"
df23_2['Project']="Sprint 3_Test Suite_V6.0"
df23_3['Project']="Sprint 3_Test Suite_V6.0"
df23_4['Project']="Sprint 3_Test Suite_V6.0"
df23_5['Project']="Sprint 3_Test Suite_V6.0"
df23_6['Project']="Sprint 3_Test Suite_V6.0"
df23_7['Project']="Sprint 3_Test Suite_V6.0"
df24_1['Project']="Sprint 4_Test Suite_V6.0"
df24_2['Project']="Sprint 4_Test Suite_V6.0"
df24_3['Project']="Sprint 4_Test Suite_V6.0"
df24_4['Project']="Sprint 4_Test Suite_V6.0"
df25_1['Project']="Sprint 5_Test Suite_V2.0"
df25_2['Project']="Sprint 5_Test Suite_V2.0"
df26_1['Project']="Sprint 6 - Test Suite_V3.0"
df26_2['Project']="Sprint 6 - Test Suite_V3.0"
df27['Project']="Sprint 7 - Test Suite_V2.0"
df28['Project']="Sprint 9 - Test Suite_V2.0"
df29['Project']="Testcase sheet_CHG_9561"
df30['Project']="Tracy Rehoming updated TC sheet_Baseline"





df1['combined']=df1['name'].astype(str)+'.'+df1['steps'].astype(str)+df1['result'].astype(str)

df2_1['combined']=df2_1['name'].astype(str)+'.'+df2_1['steps'].astype(str)+df2_1['result'].astype(str)

df2_2['combined']=df2_2['name'].astype(str)+'.'+df2_2['steps'].astype(str)+df2_2['result'].astype(str)

df3['combined']=df3['name'].astype(str)+'.'+df3['steps'].astype(str)+df3['result'].astype(str)

df4['count']=df4['steps']





count=0
for i in range(len(df4['count'])):
    if df4['count'][i] !='Step1':
        df4['count'][i]=count
    else:
        count=count+1
        df4['count'][i]=count





df4=df4.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df4.columns=['count','steps','combined','Project']

df5.columns=['id','steps','name','result','Project']

df5['count']=df5['steps']


count=0
for i in range(len(df5['count'])):
    if df5['count'][i] !='Step1':
        df5['count'][i]=count
    else:
        count=count+1
        df5['count'][i]=count





df5=df5.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df5.columns=['count','steps','combined','result','Project']

df7

df7.columns=['id','steps','name','result','Project']
df7['count']=df7['steps']
count=0
for i in range(len(df7['count'])):
    if df7['count'][i] !='Step1':
        df7['count'][i]=count
    else:
        count=count+1
        df7['count'][i]=count
df7=df7.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df7

df7.columns=['count','steps','combined','result','Project']


df9['count']=df9['steps']
count=0
for i in range(len(df9['count'])):
    if df9['count'][i] !='Step1':
        df9['count'][i]=count
    else:
        count=count+1
        df9['count'][i]=count










df9=df9.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df9.columns=['count','steps','combined','Project']

df10.columns=['id','steps','name','result','Project']
df10['count']=df10['steps']
count=0
for i in range(len(df10['count'])):
    if df10['count'][i] !='Step1':
        df10['count'][i]=count
    else:
        count=count+1
        df10['count'][i]=count

df10=df10.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df10.columns=['count','combined','result','Project']

df11['combined']=df11['name'].astype(str)+'.'+df11['steps'].astype(str)+df11['result'].astype(str)

df12['combined']=df12['name'].astype(str)+'.'+df12['steps'].astype(str)+df12['result'].astype(str)

df13['combined']=df13['name'].astype(str)+'.'+df13['steps'].astype(str)+df13['result'].astype(str)


df14['count']=df14['steps']
count=0
for i in range(len(df14['count'])):
    if df14['count'][i] !='Step1':
        df14['count'][i]=count
    else:
        count=count+1
        df14['count'][i]=count










df14=df14.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df14.columns=['count','steps','combined','Project']

df15['combined']=df15['name'].replace('nan','').astype(str)+'.'+df15['steps'].astype(str)+df15['result'].astype(str)

df16['combined']=df16['name'].astype(str)+'.'+df16['steps'].astype(str)+df16['result'].astype(str)

df17['combined']=df17['name'].astype(str)+'.'+df17['steps'].astype(str)+df17['result'].astype(str)

df30.columns=['id','steps','name','result','Project']
df30['count']=df30['steps']
count=0
for i in range(len(df30['count'])):
    if df30['count'][i] !='Step1':
        df30['count'][i]=count
    else:
        count=count+1
        df30['count'][i]=count

df30=df30.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df30.columns=['count','steps','combined','Project']

df29.columns=['id','steps','name','result','Project']
df29['count']=df29['steps']
count=0
for i in range(len(df29['count'])):
    if df29['count'][i] !='Step1':
        df29['count'][i]=count
    else:
        count=count+1
        df29['count'][i]=count

df29=df29.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df29.columns=['count','steps','combined','result','Project']

df28['count']=df28['steps']
count=0
for i in range(len(df28['count'])):
    if df28['count'][i] !='Step 1':
        df28['count'][i]=count
    else:
        count=count+1
        df28['count'][i]=count

df28=df28.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df28.columns=['count','steps','combined','Project']

df27['count']=df27['steps']
count=0
for i in range(len(df28['count'])):
    if df27['count'][i] !='Step 1':
        df27['count'][i]=count
    else:
        count=count+1
        df27['count'][i]=count

df27=df27.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df27.columns=['count','steps','combined','Project']

df26_1['count']=df26_1['steps']
count=0
for i in range(len(df26_1['count'])):
    if df26_1['count'][i] !='Step 1':
        df26_1['count'][i]=count
    else:
        count=count+1
        df26_1['count'][i]=count

df26_1=df26_1.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df26_1.columns=['count','steps','combined','Project']

df26_2['count']=df26_2['steps']
count=0
for i in range(len(df26_2['count'])):
    if df26_2['count'][i] !='Step 1':
        df26_2['count'][i]=count
    else:
        count=count+1
        df26_2['count'][i]=count

df26_2=df26_2.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df26_2.columns=['count','steps','combined','Project']

df25_1['count']=df25_1['steps']
count=0
for i in range(len(df26_2['count'])):
    if df25_1['count'][i] !='Step 1':
        df25_1['count'][i]=count
    else:
        count=count+1
        df25_1['count'][i]=count

df25_1=df25_1.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df25_1.columns=['count','steps','combined','Project']

df25_2['count']=df25_2['steps']
count=0
for i in range(len(df25_2['count'])):
    if df25_2['count'][i] !='Step 1':
        df25_2['count'][i]=count
    else:
        count=count+1
        df25_2['count'][i]=count

df25_2=df25_2.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df25_2.columns=['count','steps','combined','Project']

df24_1['count']=df24_1['steps']
count=0
for i in range(len(df24_1['count'])):
    if df24_1['count'][i] !='Step 1':
        df24_1['count'][i]=count
    else:
        count=count+1
        df24_1['count'][i]=count

df24_1=df24_1.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df24_1.columns=['count','steps','combined','Project']

df24_2['count']=df24_2['steps']
count=0
for i in range(len(df24_2['count'])):
    if df24_2['count'][i] !='Step 1':
        df24_2['count'][i]=count
    else:
        count=count+1
        df24_2['count'][i]=count

df24_2=df24_2.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df24_2.columns=['count','steps','combined','Project']

df24_3['count']=df24_3['steps']
count=0
for i in range(len(df24_3['count'])):
    if df24_3['count'][i] !='Step 1':
        df24_3['count'][i]=count
    else:
        count=count+1
        df24_3['count'][i]=count

df24_3=df24_3.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df24_3.columns=['count','steps','combined','Project']

df23_1['count']=df23_1['steps']
count=0
for i in range(len(df23_1['count'])):
    if df23_1['count'][i] !='Step 1':
        df23_1['count'][i]=count
    else:
        count=count+1
        df23_1['count'][i]=count

df23_1=df23_1.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df23_1.columns=['count','steps','combined','Project']

df23_2['count']=df23_2['steps']
count=0
for i in range(len(df23_2['count'])):
    if df23_2['count'][i] !='Step 1':
        df23_2['count'][i]=count
    else:
        count=count+1
        df23_2['count'][i]=count

df23_2=df23_2.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df23_2.columns=['count','steps','combined','Project']

df23_3['count']=df23_3['steps']
count=0
for i in range(len(df23_3['count'])):
    if df23_3['count'][i] !='Step 1':
        df23_3['count'][i]=count
    else:
        count=count+1
        df23_3['count'][i]=count

df23_3=df23_3.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df23_3.columns=['count','steps','combined','Project']

df23_4['count']=df23_4['steps']
count=0
for i in range(len(df23_4['count'])):
    if df23_4['count'][i] !='Step 1':
        df23_4['count'][i]=count
    else:
        count=count+1
        df23_4['count'][i]=count

df23_4=df23_4.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df23_4.columns=['count','steps','combined','Project']

df23_5['count']=df23_5['steps']
count=0
for i in range(len(df23_5['count'])):
    if df23_5['count'][i] !='Step 1':
        df23_5['count'][i]=count
    else:
        count=count+1
        df23_5['count'][i]=count

df23_5=df23_5.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df23_5.columns=['count','steps','combined','Project']

df23_6['count']=df23_6['steps']
count=0
for i in range(len(df23_6['count'])):
    if df23_6['count'][i] !='Step 1':
        df23_6['count'][i]=count
    else:
        count=count+1
        df23_6['count'][i]=count

df23_6=df24_3.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df23_6.columns=['count','steps','combined','Project']

df23_7['count']=df23_7['steps']
count=0
for i in range(len(df23_7['count'])):
    if df23_7['count'][i] !='Step 1':
        df23_7['count'][i]=count
    else:
        count=count+1
        df23_7['count'][i]=count

df23_7=df23_7.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df23_7.columns=['count','steps','combined','Project']

df22_1['count']=df22_1['steps']
count=0
for i in range(len(df22_1['count'])):
    if df22_1['count'][i] !='Step 1':
        df22_1['count'][i]=count
    else:
        count=count+1
        df22_1['count'][i]=count

df22_1=df22_1.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df22_1.columns=['count','steps','combined','Project']

df22_2['count']=df22_2['steps']
count=0
for i in range(len(df22_1['count'])):
    if df22_2['count'][i] !='Step 1':
        df22_2['count'][i]=count
    else:
        count=count+1
        df22_2['count'][i]=count

df22_2=df22_2.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df22_2.columns=['count','steps','combined','Project']

df21_1['count']=df21_1['steps']
count=0
for i in range(len(df21_1['count'])):
    if df21_1['count'][i] !='Step 1':
        df21_1['count'][i]=count
    else:
        count=count+1
        df21_1['count'][i]=count

df21_1=df21_1.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df21_1.columns=['count','steps','combined','Project']

df21_2['count']=df21_2['steps']
count=0
for i in range(len(df21_2['count'])):
    if df21_2['count'][i] !='Step 1':
        df21_2['count'][i]=count
    else:
        count=count+1
        df21_2['count'][i]=count

df21_2=df21_2.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df21_2.columns=['count','steps','combined','Project']

df21_3['count']=df21_3['steps']
count=0
for i in range(len(df21_3['count'])):
    if df21_3['count'][i] !='Step 1':
        df21_3['count'][i]=count
    else:
        count=count+1
        df21_3['count'][i]=count

df21_3=df21_3.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df21_3.columns=['count','steps','combined','Project']

df21_4['count']=df21_4['steps']
count=0
for i in range(len(df21_4['count'])):
    if df21_4['count'][i] !='Step 1':
        df21_4['count'][i]=count
    else:
        count=count+1
        df21_4['count'][i]=count

df21_4=df21_4.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df21_4.columns=['count','steps','combined','Project']

df20_1['count']=df20_1['steps']
count=0
for i in range(len(df20_1['count'])):
    if df20_1['count'][i] !='Step 1':
        df20_1['count'][i]=count
    else:
        count=count+1
        df20_1['count'][i]=count

df20_1=df20_1.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df20_1.columns=['count','steps','combined','Project']

df20_3['count']=df20_3['steps']
count=0
for i in range(len(df20_3['count'])):
    if df20_3['count'][i] !='Step 1':
        df20_3['count'][i]=count
    else:
        count=count+1
        df20_3['count'][i]=count

df20_3=df20_3.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df20_3.columns=['count','steps','combined','Project']

df20_4['count']=df20_4['steps']
count=0
for i in range(len(df20_4['count'])):
    if df20_4['count'][i] !='Step 1':
        df20_4['count'][i]=count
    else:
        count=count+1
        df20_4['count'][i]=count

df20_4=df20_4.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df20_4.columns=['count','steps','combined','Project']

df20_5['count']=df20_5['steps']
count=0
for i in range(len(df20_5['count'])):
    if df20_5['count'][i] !='Step 1':
        df20_5['count'][i]=count
    else:
        count=count+1
        df20_5['count'][i]=count

df20_5=df20_5.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df20_5.columns=['count','steps','combined','Project']

df20_6['count']=df20_6['steps']
count=0
for i in range(len(df20_6['count'])):
    if df20_6['count'][i] !='Step 1':
        df20_6['count'][i]=count
    else:
        count=count+1
        df20_6['count'][i]=count

df20_6=df20_6.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df20_6.columns=['count','steps','combined','Project']

df20_7['count']=df20_7['steps']
count=0
for i in range(len(df20_7['count'])):
    if df20_7['count'][i] !='Step 1':
        df20_7['count'][i]=count
    else:
        count=count+1
        df20_7['count'][i]=count

df20_7=df20_7.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df20_7.columns=['count','steps','combined','Project']

df19_2.columns=['id','steps','name','result','Project']

df19_2['count']=df19_2['steps']
count=0
for i in range(len(df19_2['count'])):
    if df19_2['count'][i] !='Step 1':
        df19_2['count'][i]=count
    else:
        count=count+1
        df19_2['count'][i]=count

df19_2=df19_2.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df19_2.columns=['count','steps','combined','result','Project']

df18_2['count']=df18_2['steps']
count=0
for i in range(len(df18_2['count'])):
    if df18_2['count'][i] !='Step 1':
        df18_2['count'][i]=count
    else:
        count=count+1
        df18_2['count'][i]=count

df18_2=df18_2.replace('nan','').groupby('count',as_index=False).agg(' '.join)


df18_2.columns=['count','steps','combined','Project']

df18_1['count']=df18_1['steps']
count=0
for i in range(len(df18_1['count'])):
    if df18_1['count'][i] !='Step 1':
        df18_1['count'][i]=count
    else:
        count=count+1
        df18_1['count'][i]=count

df18_1=df18_1.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df18_1.columns=['count','steps','combined','Project']

df18_3['count']=df18_3['steps']
count=0
for i in range(len(df18_3['count'])):
    if df18_3['count'][i] !='Step 1':
        df18_3['count'][i]=count
    else:
        count=count+1
        df18_3['count'][i]=count

df18_3=df18_3.replace('nan','').groupby('count',as_index=False).agg(' '.join)

df18_3.columns=['count','steps','combined','Project']

dfr=[
df2_1,
df2_2,
df3,
df4,
df5,
df7,
df9,
df10,
df11,
df12,
df13,
df14,
df15,
df16,
df17,
df18_1,
df18_2,
df18_3,
df19_2,
df20_1,
df20_3,
df20_4,
df20_5,
df20_6,
df20_7,
df21_1,
df21_2,
df21_3,
df21_4,
df21_5,
df22_1,
df22_2,
df23_1,
df23_2,
df23_3,
df23_4,
df23_5,
df23_6,
df23_7,
df24_1,
df24_2,
df24_3,
df24_4,
df25_1,
df25_2,
df26_1,
df26_2,
df27,
df28,
df29,
df30]

df=df1.append(dfr)

li=[]
for i in range(len(df)):
    li.append(i)

df['l']=li

df.set_index(df['l'],inplace=True)

df.drop(columns='count',inplace=True)


df.dropna(inplace=True)

df['combined']=df['combined'].apply(lambda x: x.split('-')[-1])


p = re.compile(r'\(.*\)')
df['combined']= [p.sub('', x) for x in df['combined']]
punctuation = re.compile(r'[-_.?!,":;()/>&|0-9]')
df['combined']= [punctuation.sub(" ", word) for word in df['combined']]   
p = re.compile(r'[^\w\s]+')
df['combined'] = [p.sub('', x) for x in df['combined']] 

df['combined'].apply(lambda x: x.replace('\n',''))

dff=copy.deepcopy(df)

x=df['combined']
tf = TfidfVectorizer( analyzer = 'word',stop_words= 'english')
tfidf_matrix =  tf.fit_transform(x)

feature_names = tf.get_feature_names()



df['100']=df['combined']
df['90_99']=df['combined']
df['80_89']=df['combined']
for i in range(len(df['combined'])):
    a=cosine_similarity(tfidf_matrix[i], tfidf_matrix)
    df['80_89'].iloc[i]=[df['l'].iloc[i]  for i in range(len(a[0])) if a[0][i] >=0.80 and a[0][i] <= 0.89 ]
    df['90_99'].iloc[i]=[df['l'].iloc[i]  for i in range(len(a[0])) if a[0][i] >=0.90 and a[0][i] <= 0.99 ]
    df['100'].iloc[i]=[df['l'].iloc[i]  for i in range(len(a[0])) if a[0][i] > 0.99]

pickle.dump(df,open("first.pkl",'wb'))
pickle.dump(dff,open("data_final.pkl",'wb'))