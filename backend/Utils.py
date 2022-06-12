"""
Generic helper functions for the project
"""

import Params
from apiclient.discovery import build
from urllib import parse
import string

def get_video_id_from_url(video_url):
    url_parsed = parse.urlparse(video_url)
    qsl = parse.parse_qs(url_parsed.query)
    return qsl['v'][0]

def get_category_name_from_id(video_category_id):
    data = client.videoCategories().list(part='snippet', regionCode=Params.YT_REGION).execute()

    categories = data['items']

    for category in categories: 
        if category['id'] == video_category_id: return category['snippet']['title']

def remove_punctuation(text):
    # Clean text from punctuation
    return "".join([c.lower() for c in text if c not in string.punctuation])