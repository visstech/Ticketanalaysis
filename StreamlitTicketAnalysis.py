import pandas as pd 
from datetime import date
import streamlit as st
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
#data = pd.read_excel('C:\\Users\\visse\\OneDrive - iorta TechNXT\\2024\\TIGB\OCT-2024\\11-OCT-2024\\TIGB_TICKET_STATUS_AGEWISE_AS_ON_10_OCT_24.xlsx')
data = pd.read_csv('C:\\ML\\TIGB_TICKET_STATUS_AGEWISE.csv');
print(data)
data['Ticket ID'] = data['#']
total = f"Total Number of Tickets Available:{len(data['Ticket ID'])}"
st.markdown(f'## {total}')

Olabels =  data['Status'].unique()
Olabels = np.sort(Olabels)
print('label is :',type(Olabels))
print('just print label:',Olabels)
Osizes = []
for i in Olabels:
  Osizes.append(len(data[data['Status'] == i ]))

fig1, ax1 = plt.subplots()
        #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
ax1.pie(Osizes, labels=Olabels, autopct='%1.1f%%',
                #shadow=True, startangle=90)
                shadow=True)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
  
calslist = pd.DataFrame(data=[Olabels,Osizes] ,columns=None,index=['Status','Count'])  
st.write(calslist)
data['Curr_date'] = date.today() 

# Convert the columns to datetime
data['start_date'] = pd.to_datetime(data['Start date'])
data['Curr_date'] =  pd.to_datetime(data['Curr_date'])
#Calculate the difference in days
data['Ticket_Age'] = (data['Curr_date'] - data['start_date']).dt.days 
print(data['Ticket_Age'])

color = st.sidebar.color_picker('Choose a background color', '#00f900')
st.markdown(f'''
<div style='background-color: {color}; padding: 10px; border-radius: 5px;'>
    <h1>Support ticket status analysis report </h1>     
</div>
''', unsafe_allow_html=True) 
st.sidebar.title('Query Ticket List based on Below Category')
#data.drop('Age In Days',axis=1,inplace=True)
age = st.sidebar.selectbox('Age In Days',data['Ticket_Age'].unique())
Name = st.sidebar.selectbox('Assignee',data['Assignee'].unique())
Date1 = st.sidebar.selectbox('Start Date',data['Start date'].unique())
Date2 = st.sidebar.selectbox('Enddate',data['Start date'].unique())
 
print('Age is:',age)
#data = pd.DataFrame(data= ( (data[data['Ticket_Age'] >= age]) &  [data['Assignee'] == Name] 
data =    data[(data['Ticket_Age'] >= age ) & (data['Assignee'] == Name) & ((data['Start date'] >= Date1) & (data['Start date'] <=Date2))]  
 
#data = pd.DataFrame(data=data[data['Assignee'] == Name])
#data = pd.concat([data_age, data_Name])
print(data) 
st.write(data)
 
print(data.columns) 
 
 
print('After filter:',data)
st.write(f'Total Number of Tickets Under {Name}=',len(data['Ticket ID']))

st.markdown(
    """
<style>
.reportview-container .markdown-text-container {
    font-family: monospace;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
.Widget>label {
    color: white;
    font-family: monospace;
}
[class^="st-b"]  {
    color: white;
    font-family: monospace;
}
.st-bb {
    background-color: transparent;
}
.st-at {
    background-color: #0c0080;
}
footer {
    font-family: monospace;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: #0c0080;
}
header .decoration {
    background-image: none;
}

</style>
""",
    unsafe_allow_html=True,
)


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels =  data['Status'].unique()
labels = np.sort(labels)
print('label is :',type(labels))
print('just print label:',labels)
sizes = []
for i in labels:
  sizes.append(len(data[data['Status'] == i ])) 
print('values of count is:',sizes)       
#if len(labels) > 1  :    
    #sizes = data['Status'].value_counts() 
  
    #print('value of :',sizes)
 
    #print()
    #if len(sizes) > 1 :
        #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
        #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                #shadow=True, startangle=90)
                shadow=True)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
        
 
