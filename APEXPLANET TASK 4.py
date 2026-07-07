Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
from scipy.stats import f_oneway
data=pd.read_excel(r"c:\Users\vponn\Downloads\ApexPlanet_DataAnalytics_Dataset (1).xlsx")
data["Age"]=pd.to_numeric(data["Age"],errors="coerce")
data["Total_Sales"]=pd.to_numeric(data["Total_Sales"],errors="coerce")
data=data.dropna(subset=["Age","Total_Sales"])
data["Age Group"]=pd.cut(data["Age"],bins=[0,25,35,45,55,100],labels=["18-25","26-35","36-45","46-55","56+"])
group_18_25 = data[data["Age Group"]=="18-25"]["Total_Sales"]
group_26_35 = data[data["Age Group"]=="26-35"]["Total_Sales"]
group_36_45 = data[data["Age Group"]=="36==45"]["Total_Sales"]
group_46_55 = data[data["Age Group"]=="46-55"]["Total_Sales"]
>>> group_56_plus = data[data["Age Group"]=="56+"]["Total_Sales"]
>>> f_statistic,p_value = f_oneway(group_18_25,group_26_35,group_36_45,group_46_55,group_56_plus)

Warning (from warnings module):
  File "<pyshell#16>", line 1
SmallSampleWarning: One or more sample arguments is too small; all returned values will be NaN. See documentation for sample size requirements.
>>> print(data["Age Group"].value_counts())
Age Group
26-35    219
36-45    203
46-55    202
56+      198
18-25    158
Name: count, dtype: int64
>>> print(len(group_18_25),len(group_26_35),len(group_36_45),len(group_46_55),len(group_56_plus))
158 219 0 202 198
>>> group_36_45 =data[data["Age Group"]=="36-45"]["Total_Sales"]
>>> print(len(group_36_45))
203
>>> f_statistic,p_value = f_oneway(group_18_25,group_26_35,group_36_45,group_46_55,group_56_plus)
>>> print("F-Statistic:",f_statistic)
F-Statistic: 0.0776043814617448
>>> print("P-value;",p_value)
P-value; 0.9891139377556164
