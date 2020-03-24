# Creates a playlist for a user
# •  To run this you need python3 and spotipy.  You may need to run sudo ln -sf /usr/bin/python3 /usr/bin/python to link to correct version
# •  To install spotipy on Ubuntu
#     1.  sudo apt install python3-pip
#     2.  pip3 install spotipy
#     3.  create .spotify in the user's HOME directory using this format
#         username
#         client id
#         client secret
import pprint
import sys
from utility import Utility

import spotipy
import spotipy.util as util

#User variables
divider='***********************************'
scope = "playlist-modify-public"
playlistPrefix='sz'

#Operational variables
cred=Utility.getCred()
token = util.prompt_for_user_token(cred['userName'], scope)
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
else:
    print("Can't get token for", cred['userName'])
    exit()

#Main code
def createPlaylist(playlist_name, silent=False):
    if not silent:
        print(divider)
        print("Creating playlist: " + playlist_name)
    try:
        playlist=sp.user_playlist_create(cred['userName'], playlist_name,description="Twitch playlist " + playlist_name)
        if not silent:
            print("Playlist " + playlist_name + " created.")
            print(divider)
            pprint.pprint(playlist)
        return playlist
    except:
        if not silent:
            print("Unable to create " + playlist_name)
            pprint.ppritn(playlist)


#This clause allows a command line override of playlist name
if len(sys.argv) > 1:
    playlist_name = sys.argv[1]
else:
    playlist_name = playlistPrefix + Utility.getTimestamp()

playlist=createPlaylist(playlist_name, True)
pprint.pprint(playlist)