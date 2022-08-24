from os import link
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtubesearchpython import VideosSearch


def get_video_links(videos_names):
    links = []

    for name in videos_names:
        videosSearch = VideosSearch(name, limit = 2)

        links.append((videosSearch.result()['result'])[0]['link'])

    return links




# ignore this code. (it uses the google api which allow only few requests per day
#  --> use youtube-search instead).

# DEVELOPER_KEY = 'fill_me'
# YOUTUBE_API_SERVICE_NAME = 'youtube'
# YOUTUBE_API_VERSION = 'v3'

# def youtube_search(songs_names):
#     youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
#     developerKey=DEVELOPER_KEY)

#   # Call the search.list method to retrieve results matching the specified
#   # query term.
#     links_return = []
#     # for song in songs_names:
#         # search_response = (youtube.search().list(part='snippet', q=song).execute())['items']
#         # videos_id = [item['id']['videoId'] for item in search_response]
#         # links = [f'https://www.youtube.com/watch?v={id}' for id in videos_id]
#         # links_return.append(links[0])
#     links = [f'https://www.youtube.com/watch?v={id}' for id in videos_id]
#     return links_return


# ids = youtube_search()
# links = [f'https://www.youtube.com/watch?v={id}' for id in ids]
# print(links)

# names = ['Black With N V (No Vision)', 'Keep The Faith', '1, 2, 3 (feat. Jason Derulo & De La Ghetto)', 'Can I Get Wit Ya (Otherside)', 'Wait a Minute!', 'On & On', 'A Thousand Miles', 'ICONIC (ft. Jaden Smith)', 'Just Can’t Get Enough', 'On the Road Again - Live', 'Take My Heart (You Can Have It If You Want It)', 'Girl Friend', 'Toxic', 'Wobble', 'Closing Time', 'Bumbum Granada', 'Energy', 'N.Y. State of Mind', 'Represent', 'N.Y. State of Mind', 'Come With Me', 'B.Y.O.B.', 'Here In Spirit', 'a lot']
# youtube_search(names)











