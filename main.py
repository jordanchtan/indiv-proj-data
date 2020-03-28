import pandas as pd
import glob
import dask
import dask.dataframe as dd
import os

# path = r'C:\\Users\\jorda\\Desktop\\martinchek-2012-2016-facebook-posts\\martinchek-2012-2016-facebook-posts\\data'  # use your path
path = r'C:\Users\jorda\Desktop\complete-data\name_msg_desc_like_reacts'
all_files = glob.glob(os.path.join(path, "*.csv"))


cols = ['name', 'message', 'description', 'likes_count',
        'love_count', 'wow_count', 'haha_count', 'sad_count', 'angry_count']

df = pd.read_csv(path + r"\name_msg_desc_like_reacts.csv",
                 usecols=cols, encoding='utf8')
df['react_sum'] = df['love_count'] + df['wow_count'] + \
    df['haha_count'] + df['sad_count'] + df['angry_count']
df = df[df['react_sum'] > 100]

df = df.drop('react_sum', axis=1)


df.to_csv('name_msg_desc_like_reacts_min_100.csv', index=False)
