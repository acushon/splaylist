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

# User variables
divider='***********************************'
scope = "playlist-modify-public"
playlistPrefix='zs'
defaultSong="Redbone"
searchDividers=['|',';',':',',']
searchRemoves=[(' by '," "), ("'",""), ('"',"")]

# Operational variables
cred=Utility.getCred()
token = util.prompt_for_user_token(cred['userName'], scope)
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
else:
    print("Can't get token for", cred['userName'])
    exit()

# Functions
def createPlaylist(playlist_name, silent=False):
    try:
        playlist=sp.user_playlist_create(cred['userName'], playlist_name,description="Twitch playlist " + playlist_name)
        return playlist
    except:
        print("Unable to create " + playlist_name)
        exit()

def songUri(findMe):
    result=sp.search(findMe)
    return result['tracks']['items'][0]['uri']

def addToPlaylist(playlist_id, track_id):
    return sp.user_playlist_add_tracks(cred['userName'], playlist_id, track_id)

# Main
# This clause allows a command line override of playlist name
if len(sys.argv) > 1:
    playlist_name = sys.argv[1]
else:
    playlist_name = playlistPrefix + Utility.getTimestamp()

# Create the new playlist and update user
playlist=createPlaylist(playlist_name, True)
print(playlist_name + ' playlist created')

# Add default song to the playlist
result=addToPlaylist(playlist['id'],[songUri(defaultSong)])

# Take live input for new songs for playlist
input_active=True
while input_active:
    searchTerm=input("Enter song to search for: ")
    if searchTerm.lower()=='!quit':
        input_active=False
    else:
        inputArray = Utility.processInput(searchDividers, searchRemoves, searchTerm)
        searchArray=[]
        for element in inputArray:
            searchArray.append(songUri(element))
        addToPlaylist(playlist['id'],searchArray)
        print(searchArray)
        print('Song added')

