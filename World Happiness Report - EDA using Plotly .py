#!/usr/bin/env python
# coding: utf-8

# ### The World Happiness Report

# The World Happiness Report is a landmark survey of the state of global happiness. The first report was published in 2012, the second in 2013, the third in 2015, and the fourth in the 2016 Update. The World Happiness 2017, which ranks 155 countries by their happiness levels, was released at the United Nations at an event celebrating International Day of Happiness on March 20th.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import plotly.express as px
import plotly.graph_objs as go
import statsmodels.api as sm
import math
import pycountry
import dash            
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df_2015 = pd.read_csv("2015.csv")


# In[3]:


df_2016 = pd.read_csv("2016.csv")


# In[4]:


df_2017 = pd.read_csv("2017.csv")


# In[5]:


df_2018 = pd.read_csv("2018.csv")


# In[26]:


df_2019 = pd.read_csv("2019.csv")


# ## Cleaning and Merging of data from each year
# 
# We have five different files for every from 2015 - 2019. Lets see what are all the columns in every dataset, look into which columns we would required for EDA. We will look for each year, include additional column to identify from the year and eventually merge the data to final dataset for our analysis.

# ### Year 2015

# In[6]:


df_2015.head()


# In[7]:


df_2015.columns


# In[8]:


# Use Year 2015 columns in our analysis and insert another column for year. 

df_2015_temp = df_2015.filter(['Happiness Rank', 'Country', 'Region','Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity', 
                        'Happiness Score' ])


# In[53]:


df_2015_temp.insert(0, "Year", 2015)


# ### Year 2016

# In[14]:


df_2016.head()


# In[11]:


df_2016.columns


# In[12]:


# Use Year 2016 columns in our analysis and insert another column for year. 

df_2016_temp = df_2016.filter(['Happiness Rank','Country', 'Region','Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity',
                        'Happiness Score'])


# In[54]:


df_2016_temp.insert(0, "Year", 2016)


# ### Year 2017

# In[15]:


df_2017.head()


# In[16]:


df_2017.columns


# In[17]:


df_2017.rename(columns = {'Happiness.Rank':'Happiness Rank',
                          'Happiness.Score':'Happiness Score',
                          'Economy..GDP.per.Capita.' : 'Economy (GDP per Capita)',
                          'Health..Life.Expectancy.' : 'Health (Life Expectancy)',
                          'Trust..Government.Corruption.' : 'Trust (Government Corruption)',
                           }, inplace = True)


# In[18]:


# Use Year 2017 columns in our analysis and insert another column for year. 

df_2017_temp = df_2017.filter(['Happiness Rank','Country','Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity',
                        'Happiness Score'])


# In[19]:


df_2017_temp.insert(0, "Year", 2017)


# ### Year 2018

# In[20]:


df_2018.head()


# In[21]:


df_2018.columns


# In[22]:


df_2018.rename(columns = {'Overall rank' : 'Happiness Rank',
                          'Country or region' : 'Country',
                          'Score' : 'Happiness Score',
                          'Social support' : 'Family',
                          'GDP per capita' : 'Economy (GDP per Capita)',
                          'Healthy life expectancy' : 'Health (Life Expectancy)',
                          'Freedom to make life choices' :'Freedom',
                          'Perceptions of corruption' : 'Trust (Government Corruption)'
                          }, inplace = True)


# In[23]:


# Use Year 2018 columns in our analysis and insert another column for year. 

df_2018_temp = df_2018.filter(['Happiness Rank','Country','Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity',
                        'Happiness Score'])


# In[24]:


df_2018_temp.insert(0, "Year", 2018)


# ### Year 2019

# In[27]:


df_2019.head()


# In[28]:


df_2019.rename(columns = {'Overall rank' : 'Happiness Rank',
                          'Country or region' : 'Country',
                          'Score' : 'Happiness Score',
                          'Social support' : 'Family',
                          'GDP per capita' : 'Economy (GDP per Capita)',
                          'Healthy life expectancy' : 'Health (Life Expectancy)',
                          'Freedom to make life choices' :'Freedom',
                          'Perceptions of corruption' : 'Trust (Government Corruption)'
                          }, inplace = True)


# In[29]:


# Use Year 2019 columns in our analysis and insert another column for year. 

df_2019_temp = df_2019.filter(['Happiness Rank','Country','Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity',
                        'Happiness Score'])


# In[30]:


df_2019_temp.insert(0, "Year", 2019)


# In[69]:


df_2016_temp


# In[55]:


print ('Numbers of rows and columns in year 2015 :', df_2015_temp.shape)
print ('Numbers of rows and columns in year 2016 :', df_2016_temp.shape)
print ('Numbers of rows and columns in year 2017 :', df_2017_temp.shape)
print ('Numbers of rows and columns in year 2018 :', df_2018_temp.shape)
print ('Numbers of rows and columns in year 2019 :', df_2019_temp.shape)


# In[32]:


# Merge Data so that we can get Region in each missing database. This can be done using comparing two columns from 
# to different databases and merging it together and dropping all the columns. Run this once!

#df_2017_temp = df_2017_temp.merge(df_2016_temp,left_on = 'Country', right_on = 'Country', how = 'inner')
#df_2018_temp = df_2018_temp.merge(df_2016_temp,left_on = 'Country', right_on = 'Country', how = 'inner')
#df_2019_temp = df_2019_temp.merge(df_2015_temp,left_on = 'Country', right_on = 'Country', how = 'inner')


# In[38]:


print (df_2017_temp.columns)
print (df_2018_temp.columns)
print (df_2019_temp.columns)


# In[35]:


df_2017_temp.drop(columns = ['Year_y', 'Happiness Rank_y','Economy (GDP per Capita)_y',
       'Family_y', 'Health (Life Expectancy)_y', 'Freedom_y',
       'Trust (Government Corruption)_y', 'Generosity_y', 'Happiness Score_y'], inplace = True)


# In[36]:


df_2018_temp.drop(columns = ['Year_y','Happiness Rank_y','Economy (GDP per Capita)_y',
       'Family_y', 'Health (Life Expectancy)_y', 'Freedom_y','Year_y',
       'Trust (Government Corruption)_y', 'Generosity_y', 'Happiness Score_y'], inplace = True)


# In[37]:


df_2019_temp.drop(columns = ['Year_y', 'Happiness Rank_y','Economy (GDP per Capita)_y',
       'Family_y', 'Health (Life Expectancy)_y', 'Freedom_y',
       'Trust (Government Corruption)_y', 'Generosity_y', 'Happiness Score_y'], inplace = True)


# In[39]:


df_2017_temp.rename(columns = {'Year_x' : 'Year',
                          'Happiness Rank_x' : 'Happiness Rank',
                          'Happiness Score_x':'Happiness Score',
                          'Family_x':'Family',
                          'Economy (GDP per Capita)_x':'Economy (GDP per Capita)',
                          'Health (Life Expectancy)_x': 'Health (Life Expectancy)',
                          'Freedom_x' : 'Freedom',
                          'Trust (Government Corruption)_x': 'Trust (Government Corruption)',
                          'Generosity_x':'Generosity'
                          }, inplace = True)


# In[40]:


df_2018_temp.rename(columns = {'Year_x' : 'Year',
                          'Happiness Rank_x' : 'Happiness Rank',
                          'Happiness Score_x':'Happiness Score',
                          'Family_x':'Family',
                          'Economy (GDP per Capita)_x':'Economy (GDP per Capita)',
                          'Health (Life Expectancy)_x': 'Health (Life Expectancy)',
                          'Freedom_x' : 'Freedom',
                          'Trust (Government Corruption)_x': 'Trust (Government Corruption)',
                          'Generosity_x':'Generosity'
                          }, inplace = True)


# In[41]:


df_2019_temp.rename(columns = {'Year_x' : 'Year',
                          'Happiness Rank_x' : 'Happiness Rank',
                          'Happiness Score_x':'Happiness Score',
                          'Family_x':'Family',
                          'Economy (GDP per Capita)_x':'Economy (GDP per Capita)',
                          'Health (Life Expectancy)_x': 'Health (Life Expectancy)',
                          'Freedom_x' : 'Freedom',
                          'Trust (Government Corruption)_x': 'Trust (Government Corruption)',
                          'Generosity_x':'Generosity'
                          }, inplace = True)


# In[42]:


df_2015_temp = df_2015.filter(['Year','Country','Region', 'Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity', 
                        'Happiness Score', 'Happiness Rank'])


# In[43]:


df_2016_temp = df_2016.filter(['Year','Country','Region', 'Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity', 
                        'Happiness Score', 'Happiness Rank'])


# In[44]:


df_2017_temp = df_2017_temp.filter(['Year','Country','Region', 'Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity', 
                        'Happiness Score', 'Happiness Rank'])


# In[45]:


df_2018_temp = df_2018_temp.filter(['Year','Country','Region', 'Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity', 
                        'Happiness Score', 'Happiness Rank'])


# In[46]:


df_2019_temp = df_2019_temp.filter(['Year','Country','Region', 'Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity', 
                        'Happiness Score', 'Happiness Rank'])


# In[56]:


df_2015_temp


# In[57]:


# Create dataset including all the data from all the years together.

df_final = pd.concat([df_2015_temp,df_2016_temp,df_2017_temp,df_2018_temp,df_2019_temp], 
                     sort = False, ignore_index=True)


# In[58]:


df_final


# In[51]:


df_final.columns


# In[65]:


df_final.isna().sum()


# In[60]:


#identify the NA value

df_final[df_final['Trust (Government Corruption)'].isna()]


# In[61]:


df_final.info()


# In[62]:


#Replace the NaN value with the mean of all values from each year for United Arab Emirates.

df_UAE = df_final[df_final['Country'] == 'United Arab Emirates']
df_UAE


# In[63]:


df_UAE['Trust (Government Corruption)'].mean()  #find mean 


# In[64]:


# repace the value to mean

df_final.fillna(0.311982, inplace=True)


# ### Exploratory Data Analysis

# #### 1. Finding Correlation between different columns with Happiness Score.

# In[66]:


corr=df_final.corr()
plt.figure(figsize=(30, 30))

sns.heatmap(corr[(corr >= 0.5) | (corr <= -0.5)], vmax=3, linewidths=0.01,
            square=True,annot=True,cmap='GnBu',linecolor="green")
plt.title('Correlation between features')


# From the above correlation, it can be inferred that Generosity and Trust in Government has less impact to the individual happiness. GDP and Health programs in the country has most impact to the individual happiness.

# ### 2. Pair Plot:

# In[81]:


sns.pairplot(df_final)


# ### 3. Relationship of Economy (GDP per Capita) and Happiness Score by each Region

# In[67]:


df_final


# In[68]:


df_final.columns


# In[69]:


df_final['Region'].value_counts()


# ### 3.1 GDP per Capita w.r.t. Asia Region
# 
# Intested in different GDP for the countries, we first find only the southern Asia region and then combine Southeastrn and Eastern together.

# In[121]:


#only for Southern Asia

df_region_southasia = df_final[df_final['Region'] == 'Southern Asia']

#df_region_southasia['Year'].value_counts()


# In[71]:


fig = px.bar(data_frame=df_region_southasia,
            x = 'Year',
            y = 'Economy (GDP per Capita)',
            color = 'Country',
            opacity=0.5,
             
            title='Economy per Capita For Souther Asian Countries',
             
            barmode='group')
            #template='plotly_dark')
            #color_= ['grey', 'yellow','red', ''])
fig.show()


# In[72]:


#Combining Southeastern and Eastern Regions from Asia

df_region_asia = df_final[df_final['Region'].isin(['Southeastern Asia', 'Eastern Asia'])]

df_region_asia.head()


# In[73]:


fig = px.bar(data_frame=df_region_asia,
            x = 'Country',
            y = 'Economy (GDP per Capita)',
            color = 'Country',
            barmode='group',
            orientation= 'v',
            
            title='Economy per Capita For Eastern and Southern Eastern Asia Countries',
             
            animation_frame='Year', 
            range_y=[0,2],
             
            template='plotly_dark',
            text='Happiness Score'
            )
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside',
                 width = [0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4]) # thickness of the bar
fig.show()


#  

#  

# ### 3.2  GDP per Capita w.r.t. African Countries.
# 
# Different GDP for the countries, we look for Countries in Africa and their GDP per Capita.

# In[89]:


df_final


# In[74]:


df_region_africa1 = df_final.groupby('Year')['Year','Country','Region', 'Economy (GDP per Capita)' ]


# In[75]:


df_region_africa1 = df_final[df_final['Region'] == 'Sub-Saharan Africa']

df_region_africa1 = df_region_africa1.sort_values(['Happiness Score'], ascending=False)

#df_region_africa1 = df_region_africa1.groupby(['Year'])['Year', 'Country','Region', 'Economy (GDP per Capita)']


# In[77]:


fig = px.bar(data_frame=df_region_africa1,
            x = 'Year',
            y = 'Economy (GDP per Capita)',
            color = 'Country',
            barmode='group',
            orientation= 'v',
             
            text='Happiness Score',            
           
            labels={'Economy (GDP per Capita)':'Economy',
                    'Year':'Year'},           
            title='Economy per Capita For Sub - African Countries', 
            )

fig.update_traces(texttemplate='%{text:.2s}')#, textposition='outside')

fig.show()


# 
# ### 3.3 GDP per Capita w.r.t. European Countries.

# In[78]:


df_region_europe = df_final[df_final['Region'].isin(['Western Europe', 'Central and Eastern Europe'])]

#df_region_europe


# In[79]:


fig = px.sunburst(
    data_frame = df_region_europe,
    path = ['Region', "Country",'Year',"Happiness Score"], values = ("Economy (GDP per Capita)"),
    color = "Country",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    maxdepth = 3,
    branchvalues='total',
    #title='Economy per Capita For European Countries'
)

fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))


fig.show()


#  

#  

# 
# ### 3.4 GDP per Capita and Happiness Score, for the World, listing for each Year

# In[80]:


fig = px.sunburst(
    data_frame = df_final,
    path = ['Region', "Country",'Year',"Happiness Score"], 
    values = ("Economy (GDP per Capita)"),
    color = "Country",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    maxdepth = 3,
    branchvalues='remainder',
    labels = {"Economy (GDP per Capita)":"Economy",#},
                    "Year":"Year"}
)

fig.update_traces(textinfo='label')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))


fig.show()


# ### 4. Heath (Life Expectancy) and Happiness Score by each Region and Country
# 
# From teh correlation table the next highly influencial index for Happiness score is health of the country. Lets find out how health of the country has changed over years.

# #### 4.1 Health (Life Expectancy) for Southern Asia Countries for different  Years

# In[81]:


df_final['Region'].value_counts()


# In[82]:


df_region_southasia.shape


# In[84]:


fig = px.scatter(df_region_southasia,
                x = 'Health (Life Expectancy)',
                y = 'Happiness Score',
                color = 'Country',
                size = 'Economy (GDP per Capita)', 
                facet_row = 'Year',
                labels ={"Happiness Score":"H Score"},
                #trendline = 'ols',
                title = 'Health vs Happiness Score for South Asia, with Bubble size indication of GDP',
                )

fig.show()


# #### 4.2 Life Expectency vs Happiness for European Countries

# In[85]:



df_region_europe1 = df_region_europe[df_region_europe['Country'].isin(['Switzerland', 
                                                                       'Norway','Finland','Netherlands',
                                                                      'Sweden', 'Austria'])]
#df_region_europe1
#'Greece', 'Ukraine','Georgia', 'Bulgaria', 'Tajikistan','Armenia'])] 


# In[86]:


fig = px.scatter(df_region_europe,
                x = 'Health (Life Expectancy)',
                y = 'Happiness Score',
                color = 'Country',
                size = 'Economy (GDP per Capita)', 
                #facet_row = 'Year',
                facet_col = 'Year',
                facet_col_wrap = 5,
                labels ={"Health (Life Expectancy)":"Health"},
                title = 'Health vs Happiness Score for Europe, with Bubble size indication of GDP',
                )
fig.show()


# There is bigger difference in European Countries from Western Europe which has higher Happiness score than Central and Eastern countries having less happiness score.

# In[87]:


fig = px.scatter(df_region_europe1,
                x = 'Health (Life Expectancy)',
                y = 'Happiness Score',
                color = 'Country',
                size = 'Economy (GDP per Capita)', 
                #facet_row = 'Year',
                facet_col = 'Year',
                facet_col_wrap = 5,
                labels ={"Health (Life Expectancy)":"Health"},
                title = 'Health vs Happiness Score for Western European Countries, with Bubble size indicating of GDP',
                )
fig.show()


# From the above graph, can see how Western European have increased their Health(Life Expectancy) over the years. Next, lets compare with Central and Eastern European Countries.
# 
# Autria had dip from year 2015 to 2017 since one of the factor Health(Life Expectancy) was dropping, as the countries Health improved the Happiness score also gained.
# 
# Finland has most gain in Europe in Happiness score, as they constantly improved the countries health. Switzerland has better health score and GDP than Finland but lack in overall Happiness Score.

# In[88]:


df_region_europe2 = df_final[df_final['Region']=='Central and Eastern Europe']

#df_region_europe2


# In[89]:


fig = px.scatter(df_region_europe2,
                x = 'Health (Life Expectancy)',
                y = 'Happiness Score',
                color = 'Country',
                size = 'Economy (GDP per Capita)', 
                #facet_row = 'Year',
                facet_col = 'Year',
                facet_col_wrap = 5,
                labels ={"Health (Life Expectancy)":"Health"},
                title = 'Health vs Happiness Score for Central and Eastern Europe, with Bubble size indicating of GDP',
                )
fig.show()


# #### 4.3 Life Expectency vs Happiness for North America Countries

# In[93]:


df_final['Happiness Score'].median()


# In[91]:


df_region_america = df_final[df_final['Region']=='North America']
#df_region_america


# In[92]:


fig = px.scatter(df_region_america,
                x = 'Health (Life Expectancy)',
                y = 'Happiness Score',
                color = 'Country',
                #labels ={"Happiness Score":"H Score"},
                #facet_col = 'Year',
                #facet_col_wrap = 5,
                trendline = 'ols',
                title = 'Health vs Happiness Score for America, with Bubble size indication of GDP',
                marginal_x = 'rug',
                marginal_y = 'box'
                )

fig.show()


# From scatterplot above, Canada has better Happiness Score than United States, from the graph also, Canda has better Life Expectancy than US. Understandably, Canada has free health care, but over the year Canada Happiness has got lower score. This can be seen in graph below.

# #### 4.3 Life Expectency vs Happiness for Selected Countries and changes over the year in Life Expectancy vs Happiness. 

# Handpicked countries from all region. Will try using animation over scatter plot.

# In[94]:


#custom selecting countries from parent database.

df_custom_countries = df_final[df_final['Country'].isin(['Switzerland', 'Norway',
                               'Austria', 'New Zealand',  'Israel', 'Bhutan',  'India'
                                'Bangladesh', 'Mauritius', 'Nigeria', 'Zambia', 'Czech Republic', 
                                'Uzbekistan', 'Slovakia','Canada', 'United States', 
                                'Poland', 'Turkmenistan', 'Costa Rica', 'Mexico', 'Brazil',
                                'Israel', 'United Arab Emirates', 
                                'Qatar', 'Saudi Arabia', 'Singapore', 'Thailand', 
                                'Philippines', 'Malaysia', 
                                'South Korea', 'Japan',  'China'
                                 ])]

#'Finland','Netherlands', 'Sweden','Australia','Pakistan','Oman','Taiwan','Hong Kong',


# In[95]:


fig = px.scatter(df_custom_countries,
                x = 'Health (Life Expectancy)',
                y = 'Happiness Score',
                color = 'Country',
                size = 'Happiness Score', 
                #facet_row = 'Year',
                #labels ={"Happiness Score":"H Score"},
                #trendline = 'ols',
                title = 'Health vs Happiness Score, with Bubble size indication of GDP',
                animation_frame = 'Year',
                range_x = [-0.05,1.3], # define the x and y limit so that graph is not outbound.
                range_y = [2,9],
                category_orders={'Year': [2015,2016,2017,2018,2019]},
                )

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000 #speed of change from one from to next frames.
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500 #speed of change in graph.

fig.show()


# Try selecting US, Canada, Austria and Norway, on year 2015, they clustered together closely. By year 2017, they get declustered. US by year 2019 not only falls back in Health (Life Expectancy) but also gets lower score in Happiness Index. Where other three country have similiar Happiness Index and Health (Life Expectancy) by year 2019.

# ### 5. Importance of Family Support in Happiness Index
# 
# Another important index for the dataset is Family Support. We will compare with various region and country to check  its importance.

# #### 5.1 Intested in effect of Family Support for countries, we lookinto southern Asia region.

# In[96]:


df_region_southasia_2019 =  df_region_southasia[df_region_southasia['Year'] == 2019]
df_region_southasia_2019 


# In[97]:


fig = px.pie(data_frame=df_region_southasia_2019,
             values='Family',
             names='Country',
             color='Country',                      
             title='2019 Family Support Index for Southasia Country',     
             template='seaborn',           
             width=800,                          
             height=600,                         
             hole=0.5,                          
            )

fig.update_traces(textposition='inside', textinfo='percent+label')

fig.show()


# From the above piechart, can see for year 2019, Bhutan has higher percent in pie for Family Support Index. It can also be inferred as another index for higher Happiness Score. Bhutan has highest Happiness Score for year 2019. 

# #### 5.2 Lets see if compares well other regions as well. For next pie chart we shall use African Region

# In[98]:


df_region_africa1_2019 =  df_region_africa1[df_region_africa1['Year'] == 2019]


# In[99]:


fig = px.pie(data_frame=df_region_africa1_2019,
             values='Family',
             names='Country',
             color='Country',                    
             title='2019 Family Support Index for Sub-Sahara African Countries',     
             template='seaborn',            
             width=800,                       
             height=600,                         
             #hole=0.5,                           
            )

fig.show()


# From the piechart above, Mauritius has highest percent for Family Support Index, and also has most Happiness Index in the region. 

# #### 5.3 Lets see for combined regions. For next pie chart we shall use North America, Australia and New Zealand Region

# In[100]:


df_region_comb = df_final[df_final['Region'].isin(['North America', 'Australia and New Zealand'])]
#df_region_comb


# In[101]:


fig = px.pie(data_frame=df_region_comb,
             values='Family',
             names='Country',
             color='Country',                      
             title='Family Index for America, Australia and New Zealand Countries for Years 2015 - 2019',     
             template='seaborn',            
             width=800,                          
             height=600,                         
             hole=0.5,                           
            )
fig.update_traces(textposition='inside', textinfo='percent+label'),
#                         marker=dict(line=dict(color='#000000', width=4)),
#                         pull=[0, 0, 0.2, 0], opacity=0.7, rotation=180)

fig.show()


# Of the four countries above, US has least Family Support Index, so is its Happiness Score lower than the other countries.

# #### 5.4 Effect of Family Support for countries, we look into Eastern Asia region.

# In[102]:


df_region_eastasia = df_final[df_final['Region'] == 'Eastern Asia']
df_region_eastasia_2019 = df_region_eastasia[df_region_eastasia['Year'] == 2019]
df_region_eastasia_2019


# In[104]:


fig = px.pie(data_frame=df_region_eastasia_2019,
             values='Family',
             names='Country',
             color='Country',                      
             hover_name='Happiness Score',             
             #hover_data=['Happiness Score'],    
             title='2019 Family Support Index for East Asian Countries wiht Happiness Score.',     
             template='seaborn',                                         
             width=800,                          
             height=600,                         
             hole=0.5,                           
            )

fig.update_traces(textposition='outside', textinfo='percent+label',
                         marker=dict(line=dict(color='#000000', width=4)),
                         pull=[0.2, 0, 0, 0, 0, 0.2], opacity=0.7, rotation=15)



fig.show()


# From the above pie chart, can find that China has least Family Support Index whereas Taiwan has better Family support, so is the rank of Taiwan on overall East Asian countries.

# Thanks to Adam (Charming Data) Guy - good way to start Plotly. Your tutorials were super helpful.
# Thank you for the data, was fun exploring! 
