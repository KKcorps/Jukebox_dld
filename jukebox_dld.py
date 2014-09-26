import urllib2
import json
import os

download_url = "https://channeli.in/songsmedia/download/songs/english/"
playlist_url = "https://channeli.in/jukebox/playlists_public/"
user_url = "https://channeli.in/jukebox/playlists/"

playlist_name = raw_input('Enter playlist name: ')

js = urllib2.urlopen(playlist_url)
js_load = json.load(js)

id = ''
#pn = "u'"+playlist_name+"'"
#print pn
for l in js_load:
    ##print l['name']
    if(l['name']==playlist_name):
        id = l['id']

if(id==''):
     print "Sorry, playlist not found"
     ##return

playlist = urllib2.urlopen(user_url+str(id))
playlist = json.load(playlist)
songs_list = playlist['songs_list']

location = "Downloads/Jukebox/"+playlist_name+"/"
if not os.path.exists(location):
    os.makedirs(location)
    
for song in songs_list:
    file_name = songs_list[song]['file_name']
    url_file_name = file_name.replace(' ','%20')
    song_download = urllib2.urlopen(download_url+url_file_name)
    name = file_name.split('/')[-1]
    if not os.path.exists(location+name):
        local_file = open(location+name,'w')
        local_file.write(song_download.read())
        local_file.close()
    print "Downloaded Song: "+name

    
    
    

