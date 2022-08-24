from flask import Flask, render_template, request, redirect, url_for
from package import tokens
from youtube_links import get_video_links
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import requests
from convert_and_download import downloadVideosFromIds

app = Flask(__name__)

# tokens are from package- can't share them online -> in gitignore.
CLIENT_ID = tokens.CLIENT_ID
CLIENT_SECRET = tokens.CLIENT_SECRET

token = util.prompt_for_user_token(username='shai',
                                   scope='playlist-read-collaborative',
                                   client_id=CLIENT_ID,
                                   client_secret=CLIENT_SECRET,
                                   redirect_uri='http://localhost/8000')
                                   

sp = spotipy.Spotify(auth=token)

# some other stuff to get from the api (scope needs to be changed accordingly):
# playlists = sp.current_user_playlists(3)
# curr_track = sp.current_user_recently_played(5)

playlist_uri = 'spotify:playlist:0tr5mLKBrWLIECYe2Qf58Y'
playlist_songs = sp.playlist_items(playlist_id=playlist_uri)
songs_names = [item['track']['name'] for item in playlist_songs['items']]

@app.route('/')
def home():

    return render_template('songs.html', songs_links=get_video_links(songs_names), songs_names=songs_names)


@app.route('/download')
def download():
    vids_links = get_video_links(songs_names)
    songs_links_each_as_arr = [[link] for link in vids_links]
    downloadVideosFromIds(songs_links_each_as_arr)
    return redirect(url_for('home'))



if __name__ == '__main__':
    # app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0') -> if you trust the local network, make this webpage available for all.
    app.run(debug=True)

