
import pandas as pd 
from datetime import date
import streamlit as st
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

data = pd.read_csv('TIGB_TICKET_STATUS_AGEWISE.csv');
print(data)
color = st.sidebar.color_picker('Choose a background color', '#00f900')
st.markdown(f'''
<div style='background-color: {color}; padding: 10px; border-radius: 5px;'>
    <h1>Support ticket status analysis report </h1>     
</div>
''', unsafe_allow_html=True) 
data['Ticket ID'] = data['#']
data.drop('#',axis=1,inplace=True)
total = f"Total Number of Tickets Available:{len(data['Ticket ID'])}"
st.markdown(f'## {total}')

#values_Count = data[['Status','Assignee']].value_counts()
values_Count = data.groupby(['Status','Assignee'])['Status'].count().reset_index(name='counts').sort_values(by='Assignee',ascending=True)  
values_Count = pd.DataFrame(data=values_Count,index=None)
#print(values_Count.columns)
#values_Count.reset_index(drop=True, inplace=True)

values_Count = values_Count.replace(np.nan, 0)
print('values count after replace:\n',values_Count) 
#st.write(values_Count)
tickets_total = pd.pivot_table(data=values_Count.fillna(0),values='counts',index='Status',columns='Assignee',aggfunc='sum')
print('total tickets:\n',tickets_total.fillna(0))

st.write(tickets_total.fillna(0))

Olabels =  data['Status'].unique()
Olabels = np.sort(Olabels)
print('label is :',type(Olabels))
print('just print label:',Olabels)
Osizes = []
for i in Olabels:
  Osizes.append(len(data[data['Status'] == i ]))

fig1, ax1 = plt.subplots(figsize=(12, 6))
        #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
ax1.pie(Osizes, labels=Olabels, autopct='%1.1f%%',
                #shadow=True, startangle=90)
                shadow=True)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
  
#calslist = pd.DataFrame(data=[Olabels,Osizes] ,columns=Olabels,index=['Status','Count'])  
calslist = pd.DataFrame(data=[Osizes] ,columns=Olabels,index=['Status']) 
callist  = pd.DataFrame(data=calslist,index=None) 
print('Call list columns are\n',callist.columns)
st.markdown('### Total tickets count based on Stauts:')
st.write(callist)

data['Curr_date'] = date.today() 

# Convert the columns to datetime
data['start_date'] = pd.to_datetime(data['Start date'],format="mixed", dayfirst=True)
data['Curr_date'] =  pd.to_datetime(data['Curr_date'])
print(data.info())
#Calculate the difference in days
data['Ticket_Age'] = (data['Curr_date'] - data['start_date']).dt.days 
print(data['Ticket_Age'])

all_data = data
st.sidebar.title('Query Ticket List based on Below Category')
#data.drop('Age In Days',axis=1,inplace=True)
#data['Start date'] = pd.to_datetime(data['start_date'],format='%d/%m/%Y',errors='coerce')
#data['Start date'] = data.sort_values(by='Start date', ascending=True, inplace=True) 
age = st.sidebar.selectbox('Age In Days',data['Ticket_Age'].unique())
Name = st.sidebar.selectbox('Assignee',data['Assignee'].unique())
Date1 = st.sidebar.selectbox('Start Date',data['start_date'].unique())
#Date1 = st.sidebar.selectbox('Start Date',data.sort_values(by='Start date', ascending=True, inplace=True) )
Date2 = st.sidebar.selectbox('Enddate',data['start_date'].unique())
dates = pd.date_range(start='14/10/2024',end='29/09/2021',freq='D')

mask = (data['start_date'] > Date1) & (data['start_date'] <= Date2)
data = data.loc[mask]

#dates = data['start_date'].agg(['min', 'max'])
print('date1 =\n',Date1)
print('date1 =\n',Date2)
print('Dates =:\n',dates)
print('type of start date:',type(data['start_date']))
 
print('Age is:',age)
#data = pd.DataFrame(data= ( (data[data['Ticket_Age'] >= age]) &  [data['Assignee'] == Name] 
#data =    data[(data['Ticket_Age'] >= age ) & (data['Assignee'] == Name) & ((data['Start date'] >= Date1) & (data['Start date'] <=Date2))] 

print('Start date:\n',data['Start date'] )
print('Date1 :',Date1)
data =    data[((data['Ticket_Age'] >= age ) & ( data['Assignee'] == Name) )   & ((data['start_date'] > Date1) & (data['start_date'] <= Date2))]  
 
#data = pd.DataFrame(data=data[data['Assignee'] == Name])
#data = pd.concat([data_age, data_Name])
print(data) 
st.markdown(f'### Tickets list under assignee = {Name}')
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
fig1, ax1 = plt.subplots(figsize=(12,6))
        #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                #shadow=True, startangle=90)
                shadow=True)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

if st.sidebar.button('Show all tickets') :
    st.markdown('## All Tickets List ')    
    all_data.to_string(index=False)
    all_data['Ticket ID'] = all_data['Ticket ID'].astype(str)
    all_data['Ticket ID'] = all_data['Ticket ID'].str.replace(',', '', regex=False)
    all_data['Ticket ID'] = all_data['Ticket ID'].astype(int)
    st.write(all_data[['Sr No','Ticket ID','Ticket_Age', 'Project', 'Tracker', 'Parent task', 'Parent task subject',
       'Status', 'Priority', 'Subject', 'Author', 'Assignee', 'Updated',
       'Category', 'Target version', 'Start date', 'Due date',
       'Estimated time', 'Total estimated time', 'Spent time',
       'Total spent time', '% Done', 'Created', 'Closed', 'Last updated by',
       'Related issues', 'System', 'Original Requester', 'ISSD PIC',
       'ISSD Remark', 'Root Cause', 'Resolved Date', 'Closed Date',
       'Department', 'Remark'
       ]])
        
 
