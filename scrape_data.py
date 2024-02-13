import datetime as dt
from pmaw import PushshiftAPI
import json

before = int(dt.datetime(2022,2,15,0,0).timestamp())
after = int(dt.datetime(2020,1,1,0,0).timestamp())

api = PushshiftAPI()

subreddit = "Anxiety"

limit = 4000
posts = api.search_submissions(
    subreddit=subreddit, limit=limit, filter=['title','selftext','full_link','num_comments','score'])

posts = list(posts)

arr = [thing for thing in posts]


file_name = 'reddit_'+ subreddit + '.json'

with open(file_name, 'a') as f:
    json.dump(arr, f)
