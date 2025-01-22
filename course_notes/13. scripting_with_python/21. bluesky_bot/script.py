# ==== bluesky bot ====

from atproto import Client
from atproto.exceptions import NetworkError
import time

client = Client()

# Login
try:
    login = client.login('yourhandle.bsky.social', 'NoyMyRealPassword')
    print(login.handle, login.display_name, login.followers_count)
except NetworkError as e:
    print(f"Login failed: {e}")
    exit()

# Posting
try:
    post = client.send_post(
        'Testing my Python script. Hey there, fellow Final Fantasy nerds!')
except NetworkError as e:
    print(f"Failed to send post: {e}")

# Fetch Timeline
try:
    data = client.get_timeline(limit=30)
    feed = data.feed
    next_page = data.cursor
    for item in feed:
        print(item.post)
except NetworkError as e:
    print(f"Error fetching timeline: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

# Generous Bot


def limit_handler(follower_bundle):
    try:
        while len(follower_bundle.followers) > 0:
            yield follower_bundle.followers.pop()
    except NetworkError as error:
        print(f"Error fetching followers: {error}")
        time.sleep(10)  # Retry after 10 seconds


try:
    followers = client.get_followers(login.did)
    for follower in limit_handler(followers):
        print(f"Follower: {follower}")
        if hasattr(follower, 'display_name') and follower.display_name == "whomever":
            client.follow(follower.did)
except NetworkError as e:
    print(f"Error processing followers: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

# Like Bot
search_string = 'Final Fantasy'
numberOfPosts = 2
count = 0
try:
    data = client.get_timeline(limit=30)
    feed = data.feed
    for item in feed:
        if item.post.record.text.find(search_string) > -1:
            count += 1
            client.like(item.post.uri, item.post.cid)
            if count >= numberOfPosts:
                break
except NetworkError as e:
    print(f"Error liking posts: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
