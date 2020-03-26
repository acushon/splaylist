# Command Line Playlist
Spaylist creates a new Spotify playlist and allows for the addition of additional songs, all from the command line.

## Getting started
Download the source code or clone the git repository.

### Prerequisites
* Python 3.5.2 or greater
* pip3
* Spotipy
* Spotify account
* Access to https://developer.spotify.com
* An app created at https://developer.spotify.com/dashboard/applications which will provide a Client ID and Client Secret.  You must include http://localhost/ as a Redirect URI or the app won't work.

### Installing
#### Installing Spotipy
Use pip to install Spotipy.  Here's an example for Linux
```
user@host:~/splaylist/pip3 install spotipy
```
#### File locations
All files from the git clone must reside in the same directory.  There is one file, .spotify, that must reside in the user's home directory.
* /home/username/.spotify:  This file contains username, Client ID, and Client Secret and are required for normal operations.  Here's an example of the file.
```
joeuser
34c60e24843157360671b982de732374
935db90f5b18332170b2507cc06d6d32
```
Line 1 is the Spotify userid

Line 2 is the Client ID

Line 3 is the Client Secret

Note:  Each item should be on a line of it's own.
* ~/splaylist/utility.py:  Contains generic/utility functions for use by the main program.
* ~/splaylist/newpl.py:  Main program the delivers the bulk of the functionality.




