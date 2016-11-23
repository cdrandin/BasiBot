import requests
import random

MAIN_URL = 'https://www.reddit.com/r/'


def get_json(category, next_page=None):
    params = ''
    if next_page is not None:
        params = '?after=' + next_page

    url = MAIN_URL + category + '/.json' + params
    print('Getting info from: ' + url)

    req = requests.get(url, headers={'User-agent': 'Random Pic Bot 0.1'})
    return req


def get_image_url(subreddit):

    category = None
    data = None
    urls = []
    for i in range(0, 5):
        # get initial request
        status_code = 0
        while status_code != 200:
            if category is None or status_code != 0:
                # select category
                category = subreddit

            next_page = None
            if data is not None:
                next_page = data['after']

            # do the request
            resp = get_json(category, next_page)

            # update status code
            status_code = resp.status_code
            if status_code != 200:
                print(status_code)
            if status_code == 403 or status_code == 404:
                return 'Nothing Found (403 or 404)'

        data = resp.json()['data']
        urls = []
        for post in data['children']:
            info = post['data']

            if 'selftext' in info and len(info['selftext']) == 0:
                url = info['url']
                if 'reddituploads' not in url:
                    urls.append(url)
    try:
        return random.choice(urls)
    except Exception:
        return "Nothing Found"


