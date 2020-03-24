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
username = cred['userName']
if len(sys.argv) > 1:
    playlist_name = sys.argv[1]
else:
    playlist_name = playlistPrefix + Utility.getTimestamp()

playlist_description = "Twitch playlist " + playlist_name


token = util.prompt_for_user_token(username, scope)
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlist = sp.user_playlist_create(username, playlist_name,
                                        description=playlist_description)
    pprint.pprint(playlist)
    print(divider)
    print("Playlist \"" + playlist['name'] + "\" created")
    print(divider)
else:
    print("Can't get token for", username)