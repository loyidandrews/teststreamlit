import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

from datetime import datetime,timedelta
import pytz
import re


st.set_page_config(layout="wide")

import time


st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",
    width=100,
)

st.title('LinkedIn Live Monitoring')
with st.expander('Monitoring Posts of CEOs from LinkedIn everyday'):
     st.write('')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)





#st.balloons()

#st.header('`streamlit_pandas_profiling`')

st.header('RWE: Andere CEOs Activities Monitoring')



df1 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/V8A8sVT6RTvnfqub1Y0iUQ/Andere_CEOS_1.csv')
df2 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/Vx2c6OJZ59781jp9zKPViw/Andere_CEOs_2.csv')
df3 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/JUeq71McCykmR5ZrlZTJdQ/Andere_CEOs_3.csv')

frames = [df1, df2, df3]

df = pd.concat(frames)

df = df.dropna(how='any', subset=['postContent'])


df.drop(['viewCount', 'sharedJobUrl', 'error', 'repostCount','imgUrl'], axis=1, inplace=True)


#st.write(df.profileUrl.value_counts())



df['CEO']  = df['action']

df.loc[df.profileUrl == "https://www.linkedin.com/in/assaadrazzouk/", "CEO"] = "Assaad Razzouk"
df.loc[df.profileUrl == "https://www.linkedin.com/in/markussteilemann/", "CEO"] = "Markus Steilemann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/buschroland/", "CEO"] = "Roland Busch"
df.loc[df.profileUrl == "https://www.linkedin.com/in/bernardlooneybp/", "CEO"] = "Bernard Looney"
df.loc[df.profileUrl == "https://www.linkedin.com/in/ola-k%C3%A4llenius/", "CEO"] = "Ola Kaellenius"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martenbunnemann/detail/recent-activity/shares/", "CEO"] = "Marten Bunnemann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jocheneickholt/recent-activity/", "CEO"] = "Jochen Eickholt"
df.loc[df.profileUrl == "https://www.linkedin.com/in/leo-birnbaum-885347b0/detail/recent-activity/", "CEO"] = "Leo Birnbaum"
df.loc[df.profileUrl == "https://www.linkedin.com/in/herbertdiess/", "CEO"] = "Herbert Diess"
df.loc[df.profileUrl == "https://www.linkedin.com/in/mike-crawley-a3308a2/recent-activity/shares/", "CEO"] = "Mike Crawley"
df.loc[df.profileUrl == "https://www.linkedin.com/in/miriam-teige-66117769/recent-activity/", "CEO"] = "Miriam Teige"
df.loc[df.profileUrl == "https://www.linkedin.com/in/werner-baumann/", "CEO"] = "Werner Baumann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/katherina-reiche/detail/recent-activity/", "CEO"] = "Katherina Reiche"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jeromepecresse/?originalSubdomain=fr", "CEO"] = "Jérôme Pécresse"
df.loc[df.profileUrl == "https://www.linkedin.com/in/marc-becker-3990826/", "CEO"] = "Marc Becker"
df.loc[df.profileUrl == "https://www.linkedin.com/in/richardlutzdb/", "CEO"] = "Dr. Richard Lutz"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martin-brudermueller/detail/recent-activity/", "CEO"] = "Dr. Martin Brudermüller"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hdsohn/recent-activity/shares/", "CEO"] = "Hans-Dieter Sohn"
df.loc[df.profileUrl == "https://www.linkedin.com/in/davidcarrascosafrancis/recent-activity/shares/", "CEO"] = "David Carrascosa"
df.loc[df.profileUrl == "https://www.linkedin.com/in/juan-gutierrez-sgre/recent-activity/", "CEO"] = "Juan Gutierrez"
df.loc[df.profileUrl == "https://www.linkedin.com/in/henrik-stiesdal-064a9374/recent-activity/", "CEO"] = "Henrik Stiesdal"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hilde-merete-aasheim-b37b38203/recent-activity/shares/", "CEO"] = "Hilde Merete Aasheim"
df.loc[df.profileUrl == "https://www.linkedin.com/in/alistair-phillips-davies-14213871/recent-activity/", "CEO"] = "Alistair Phillips-Davies"
df.loc[df.profileUrl == "https://www.linkedin.com/in/annaborgvattenfall/", "CEO"] = "Anna Borg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/giles-dickson-98607229/recent-activity/", "CEO"] = "Giles Dickson"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jean-bernard-levy/", "CEO"] = "Jean-Bernard Lévy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/florian-bieberbach/recent-activity/shares/", "CEO"] = "Florian Bieberbach"



def getActualDate(url):

    a= re.findall(r"\d{19}", url)

    a = int(''.join(a))

    a = format(a, 'b')

    first41chars = a[:41]

    ts = int(first41chars,2)

    #tz = pytz.timezone('Europe/Paris')

    actualtime = datetime.fromtimestamp(ts/1000).strftime("%Y-%m-%d %H:%M:%S %Z")

    return actualtime

df['postDate'] = df.postUrl.apply(getActualDate)


df = df.dropna(how='any', subset=['postDate'])


import datetime as dt

#def datenow(date):
     #a = re.(datetime.now() - df.postDate.days >1:)

#df5= df
#df5['date'] =  pd.to_datetime(df5['postDate'])
df['date'] =  pd.to_datetime(df['postDate'])

df['Total_Interactions'] = df['likeCount'] + df['commentCount']

df30 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=365))] #hours = 6,12, 24


st.write(df30)
st.write(df30.shape)
#df5 = df['date'].last('24h')

st.subheader('No of Posts for each CEO from last 12 Months')
st.write(df30.CEO.value_counts())

st.header('Post from last 24 hours')



df5 = df[df['date']>=(dt.datetime.now()-dt.timedelta(hours=24))] #hours = 6,12, 24

cols = ['CEO','postContent','postUrl','likeCount','commentCount','Total_Interactions','postDate','profileUrl']
df5 = df5[cols]
df5.sort_values(['Total_Interactions'], ascending=False, inplace=True)

st.write(df5.shape)
st.write(df5)

a = df5.loc[df5.CEO == df5.CEO.iloc[0]]['postContent'].to_list()

b = df5.loc[df5.CEO == df5.CEO.iloc[1]]['postContent'].to_list()

c = df5.loc[df5.CEO == df5.CEO.iloc[2]]['postContent'].to_list()

d = df5.loc[df5.CEO == df5.CEO.iloc[3]]['postContent'].to_list()



a1 = df5.loc[df5.CEO == df5.CEO.iloc[0]]['postUrl'].to_list()

a11 = df5.loc[df5.CEO == df5.CEO.iloc[0]]['profileUrl'].to_list()

a2 = df5.loc[df5.CEO == df5.CEO.iloc[0]]['Total_Interactions'].to_list()


b1 = df5.loc[df5.CEO == df5.CEO.iloc[1]]['postUrl'].to_list()

b11 = df5.loc[df5.CEO == df5.CEO.iloc[1]]['profileUrl'].to_list()

b2 = df5.loc[df5.CEO == df5.CEO.iloc[1]]['Total_Interactions'].to_list()


c1 = df5.loc[df5.CEO == df5.CEO.iloc[2]]['postUrl'].to_list()

c11 = df5.loc[df5.CEO == df5.CEO.iloc[2]]['profileUrl'].to_list()

c2 = df5.loc[df5.CEO == df5.CEO.iloc[2]]['Total_Interactions'].to_list()


d1 = df5.loc[df5.CEO == df5.CEO.iloc[3]]['postUrl'].to_list()

d11 = df5.loc[df5.CEO == df5.CEO.iloc[3]]['profileUrl'].to_list()

d2 = df5.loc[df5.CEO == df5.CEO.iloc[3]]['Total_Interactions'].to_list()




st.header('Top Four Posts in last 24 Hours')
#st.write(a)
col1, col2, col3, col4 = st.columns(4)

with col1:
   st.subheader(df5.CEO.iloc[0])
   #st.image("https://static.streamlit.io/examples/cat.jpg")
   #st.write('Post Content')
   st.markdown('_Post Content_ ')
   st.write(str(a[0])) #postContent
   st.markdown('_Total Interactions for this Post:_ ') 
   st.write(str(a2[0])) #totInteractions
   st.markdown('_Link to this Post_ ') 
   st.write(str(a1[0])) #profileUrl
   st.markdown('_Link to his Profile_ ') 
   st.write(str(a11[0])) #profileUrl

with col2:
   st.subheader(df5.CEO.iloc[1])
   #st.image("https://static.streamlit.io/examples/dog.jpg")
   st.markdown('_Post Content_ ')
   st.write(str(b[0]))
   st.markdown('_Total Interactions for this Post:_ ') 
   st.write(str(b2[0])) #totInteractions
   st.markdown('_Link to this Post_ ') 
   st.write(str(b1[0])) #profileUrl
   st.markdown('_Link to his Profile_ ') 
   st.write(str(b11[0])) #profileUrl

with col3:
   st.subheader(df5.CEO.iloc[2])
   #st.image("https://static.streamlit.io/examples/owl.jpg")
   st.markdown('_Post Content_ ')
   st.write(str(c[0]))
   st.markdown('_Total Interactions for this Post:_ ') 
   st.write(str(c2[0])) #totInteractions
   st.markdown('_Link to this Post_ ') 
   st.write(str(c1[0])) #profileUrl
   st.markdown('_Link to his Profile_ ') 
   st.write(str(c11[0])) #profileUrl

with col4:
   st.subheader(df5.CEO.iloc[3])
   #st.image("https://static.streamlit.io/examples/owl.jpg")
   st.markdown('_Post Content_ ')
   st.write(str(d[0]))

   st.markdown('_Total Interactions for this Post:_ ') 
   st.write(str(d2[0])) #totInteractions
   st.markdown('_Link to this Post_ ') 
   st.write(str(d1[0])) #profileUrl
   st.markdown('_Link to his Profile_ ') 
   st.write(str(d11[0])) #profileUrl





#x = df5.plot(kind='bar', x='CEO', y='Total_Interactions', figsize=(20,10), ylabel='View Counts')
st.bar_chart(df5, x='CEO', y='Total_Interactions',use_container_width=True)
#st.sidebar.header('Input')

#pr = df.profile_report()
#st_profile_report(pr)

##st.line_chart(df.likeCount)




# "#st.line_chart(df.commentCount)


# option = st.selectbox(
#      'What is your Post type?',
#      (df.type))

# st.write('Your favorite color is ', option)


# st.write('Contents of the ./streamlit/config.toml file of this app')








# st.subheader('Input CSV')
# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#   df = pd.read_csv(uploaded_file)
#   st.subheader('DataFrame')
#   st.write(df)
#   st.subheader('Descriptive Statistics')
#   st.write(df.describe())
# else:
#   st.info('☝️ Upload a CSV file')

# "


  

