#This is junk for now

import os
from datetime import datetime
import spotipy
import spotipy.oauth2 as oauth2

#Global settings
playlistPrefix = 'sz'
#Format with milliseconds: "%Y%m%d-%H%M%S-%f"
#Format without milliseconds: "%Y%m%d-%H%M%S"
timeFormat='%Y%m%d-%H%M%S'

def get_cred():
    with open(os.path.expanduser('~/.spotify'), 'r') as file:
        content=file.read()
        if '\r' in content:
            data = content.split('\r\n')
        else:
            data = content.split('\n')
        return {'userName': data[0], 'clientId': data[1], 'clientSecret': data[2]}

def generate_token(credential):
    credentials = oauth2.SpotifyClientCredentials(
        client_id=credential['clientId'],
        client_secret=credential['clientSecret'])
    return credentials.get_access_token()

timestamp=datetime.now().strftime(timeFormat)
playlistName= playlistPrefix.upper() + timestamp
cred=get_cred()
token=generate_token(cred)

print(token)

spotify = spotipy.Spotify(auth=token)
playlists = spotify.user_playlist_create(cred['userName'], playlistName, description="Channel playlist: " + timestamp)

#playlists = spotify.user_playlists(cred['userName'])
#print(playlists['items'])