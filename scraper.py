from facebook_scraper import get_posts
import json
import csv
import pandas as pd
import collections


def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


# sources = ['abc-news', 'bbc', 'cbs-news', 'cnn', 'fox-and-friends', 'fox-news', 'nbc-news', 'npr',
#                'the-los-angeles-times', 'the-new-york-times', 'the-wall-street-journal',
#                'the-washington-post', 'time', 'usa-today', 'the-huffington-post']
sources = ['abc-news']
for source in sources:
    # with open(source + '.json', 'w', encoding='utf-8') as f:
    with open(source + ".csv", "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["post_id", "text", "post_text", "shared_text", "time", "image", "likes",
                         "comments", "shares", "post_url", "link", "reactions_like", "reactions_sorry",
                         "reactions_wow", "reactions_love", "reactions_anger", "reactions_haha",
                         "w3_fb_url", "fetched_time"])
        print(source)
        for index, post in enumerate(get_posts(source, pages=200, extra_info=True, timeout=1000)):
            if index % 10 == 0:
                print(index)
            # json.dump(post, f, ensure_ascii=False, indent=4, default=str)

            post_template = {'post_id': "", 'text': "", 'post_text': "", 'shared_text': "",
                             'time': "", 'image': "", 'likes': 0, 'w3_fb_url': "",
                             "fetched_time": "", 'comments': 0, 'shares': 0, 'post_url': "",
                             'link': "", "reactions": {'like': 0, 'sorry': 0, 'wow': 0, 'love': 0,
                                                        'anger': 0, 'haha': 0}}

            for key in ['text', 'post_text', 'shared_text']:
                post[key] = post[key].replace("\n", " ")

            post_template = flatten(post_template)
            post = flatten(post)
            # print(json.dumps(post, indent=4, default=str))
            post = {**post_template, **post}
            # print(json.dumps(post, indent=4, default=str))

            writer.writerow([post["post_id"], post["text"], post["post_text"],
                             post["shared_text"], post["time"], post["image"],
                             post["likes"], post["comments"], post["shares"],
                             post["post_url"], post["link"], post["reactions_like"],
                             post["reactions_sorry"], post["reactions_wow"],
                             post["reactions_love"], post["reactions_anger"],
                             post["reactions_haha"], post["w3_fb_url"],
                             post["fetched_time"]])

# df = pd.read_csv(source + ".csv")
# # more options can be specified also
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df)
