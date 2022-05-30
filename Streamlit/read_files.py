
## BACKUP FOR EXCEL DATA
# #get excel and sheet names, sheet name = sentiment average
# tabs:list = pd.ExcelFile("26-04-2022_stream.xlsx").sheet_names
# slider_value = st.slider("Choose Sheet",min_value= 1,max_value=len(tabs))
# dict_df = pd.read_excel("26-04-2022_stream.xlsx",sheet_name=None)
# sent_avg = float(tabs[slider_value-1])

# df = pd.DataFrame(dict_df[tabs[slider_value-1]])
# time_col = df["Time"].values
# time = st.text(f"Duration: '{time_col[0]}'  ->  '{time_col[-1]}'")
# st.dataframe(df.head(5))
# df.style.hide(level = 1)  
# st.markdown("---")

## BACKUP FOR SQL 
# if st.slider:
#     st.text(f"Rows: {len(df)}")
#     st.subheader = "Metrics"
#     st.metric("Sentiment is",sent_avg_eval,f"{sent_avg:5f}")
#     #st.line_chart(tabs)
#     wordCloud(df)

# @st.cache(allow_output_mutation=True, show_spinner=False)
# def get_con():
#     return create_engine('postgresql://{}:{}@{}/tweets'.format(ConfigDB.USER, ConfigDB.PASS, ConfigDB.HOST),convert_unicode=True)

# @st.cache(allow_output_mutation=True,show_spinner=False, ttl=5*60)
# def get_data():
#     timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#     df = pd.read_sql_table("tweets",get_con())
#     df = df.rename(columns={"body": "Tweet", "tweet_date":"Timestamp", 
#         "followers": "Followers", "sentiment": "Sentiment", "keyword": "Keyword",
#         "verified_user": "User verified"})
#     return df, timestamp