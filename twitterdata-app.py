pip install snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
tweets_list1 = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('elonmusk').get_items()):
    if i > 100:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user, tweet.replyCount, tweet.retweetCount, tweet.source, tweet.likeCount])
tweets_df1 = pd.DataFrame (tweets_list1, columns = ['Date', 'Id','URL','Tweet_content','User','Reply_count','Retweet_count','Source','Like_count'])
import streamlit as st
st.write ('Twitter_data')
title = st.text_input('Search data by keyword')
st.write('Keyword', title)
import datetime
d = st.date_input(
    "Data by date",
    datetime.date(2019, 7, 6))
st.write('Data from:', d)
t = st.time_input('Search data by time', datetime.time(8, 45))
st.write('Data from', t)
st.dataframe(tweets_df1)
def convert_df(df):
    return df.to_csv().encode('utf-8')
csv = convert_df(tweets_df1)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='tweets_df1.csv',
    mime='text/csv',
)
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

