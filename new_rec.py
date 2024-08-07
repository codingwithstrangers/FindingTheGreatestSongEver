
from operator import length_hint
from unicodedata import name
from main import access_token
import requests
import json
import xlsxwriter
import csv
import os
import pprint
import export
import rec


def main():
<<<<<<< HEAD
    tracks = rec.get_recommended_tracks(3, '6XyY86QOPPrYVGvF9ch6wz') # number will populate tracks plus artist
=======
<<<<<<< HEAD
    tracks = rec.get_recommended_tracks(100, '6XyY86QOPPrYVGvF9ch6wz') #number will populate tracks plus artist
=======
    tracks = rec.get_recommended_tracks(3, '6XyY86QOPPrYVGvF9ch6wz') #number will populate tracks plus artist
>>>>>>> 74b2f8b9fa8d5e9fe240bacd54d021d147d56c72
>>>>>>> 4b3ca784d0311239dc1ccaeb25dacf8f23abd3dd

    track_details = []
    
    for track in tracks:
        if len(track["artist_id"]) > 1:
            for artist_id in track["artist_id"]:
                track_detail = get_details(track["track_id"], artist_id)
                track_details.append(track_detail)
        else:
            track_detail = get_details(track["track_id"], track["artist_id"][0])
            track_details.append(track_detail)

    print('track_load')
    
    # Export to CSV using rec_export
    rec_export(input_dicts=track_details, export_filename="F:\\Coding with Strangers\\bestsongever-main\\find_song\\Rec_export.csv")
    print('Task_done')
      
  

def get_details(track_id, artist_id):
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'
    endpoint_url = "https://api.spotify.com/v1/recommendations?"


    # actual GET request with proper header as of now you need to make one for each stat
    t = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    r = requests.get(BASE_URL + 'audio-analysis/' + track_id, headers=headers)
    h = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)
    s = requests.get(BASE_URL + 'artists/'+ artist_id, headers=headers)
    

    t_content = json.loads(t.content)
    h_content = json.loads(h.content)
    r_content = json.loads(r.content)
    s_content = json.loads(s.content)
   
    #My Big DICt. 
    data = r_content

    def loop(input_list:list, value):
        index = 0
        start = 0
        for x in input_list:
            new_number = x.get(value)
            index += 1
            start += new_number

        math = start / index
        Math = float(math)

        return {
          'amount': index,
          'result': start,
          'math': Math
        }



    #you have 2 choices here loop it all to do less
    #or print each one seen below
    track_id_info = {
        
    "spotify_artists_name_0" : 'NA',
    "spotify_artists_name_1" : 'NA',
    "spotify_artists_name_2" : 'NA',
    "spotify_artist_id_0" : 'NA',
    "spotify_artist_id_1" : 'NA',
    "spotify_artist_id_2" : 'NA',
    "song_name" : h_content.get('name'),
    "spotify_track_id" : h_content.get('id', 'NA'),
    "album_name" : h_content.get('album').get('name', 'NA'),
    "http_status_code" : f'{t.status_code}{h.status_code}',
    "genre_1" :'NA',
    "genre_2" :'NA',
    "genre_3" :'NA',
    "genre_4" :'NA',
    "genre_5" :'NA',
    "genre_6" :'NA',
    "genre_7" :'NA',
    "genre_8" :'NA',
    "genre_9" :'NA',
    "genre_10" :'NA',
    "popularity_track" : h_content.get('popularity', 'NA'),
    "popularity_artist" : s_content.get('popularity', 'NA'),
    "album_release_date" : h_content.get('album').get('release_date', 'NA'),
    "total_tracks" : h_content.get('album').get('total_tracks', 'NA'),
    'duration_min' : h_content.get('duration_ms', 'NA')//1000/60,
    'BPM' : t_content.get('tempo'),
    'danceability' : t_content.get('danceability', 'NA') , 
    'energy' : t_content.get('energy', 'NA'),
    'loudness' : t_content.get('loudness', 'NA'),
    'mode' : t_content.get('mode', 'NA'),
    'speechiness' : t_content.get('speechiness', 'NA'),
    'acousticness' : t_content.get('acousticness', 'NA'),
    'instrumentalness' : t_content.get('instrumentalness', 'NA'),
    'liveness' : t_content.get('liveness', 'NA'),
    'valence' : t_content.get('valence', 'NA'),
    'time_signature' : t_content.get('time_signature', 'NA'),
    'time_signature_confidence' : r_content.get('track').get('time_signature_confidence', 'NA'),
    'end_of_fade_in' : r_content.get('track').get('end_of_fade_in', 'NA'),
    'start_of_fade_out' : r_content.get('track').get('start_of_fade_out', 'NA'),
    'tempo_confidence' : r_content.get('track').get('tempo_confidence', 'NA'),
    'mode_confidence' : r_content.get('track').get('mode_confidence', 'NA'),
    'key_confidence' : r_content.get('track').get('key_confidence', 'NA'),
    'beat_start' :  loop(r_content.get('beats'), 'start').get('math', 'NA'),
    'beat_duration' :  loop(r_content.get('beats'), 'duration').get('math', 'NA'),
    'beat_confidence' :  loop(r_content.get('beats'), 'confidence').get('math', 'NA'),
    'beats_length' : len(r_content.get('beats', 'NA')),
    'tatum_start' :  loop(r_content.get('tatums'), 'start').get('math', 'NA'),
    'tatum_duration' :  loop(r_content.get('tatums'), 'duration').get('math', 'NA'),
    'tatum_confidence' :  loop(r_content.get('tatums'), 'confidence').get('math', 'NA'),
    'tatum_length' : len(r_content.get('tatums', 'NA')),
    'bars_start' :  loop(r_content.get('bars'), 'start').get('math', 'NA'),
    'bars_duration' :  loop(r_content.get('bars'), 'duration').get('math', 'NA'),
    'bars_confidence' :  loop(r_content.get('bars'), 'confidence').get('math', 'NA'),
    'bars_length' : len(r_content.get('bars', 'NA')),
    }

    
    #loop for finding all genres and placing them in plce holders in track_id_info DICt.
    songtype = s_content.get('genres')

    for genre_position, genre_value in enumerate(songtype, start=1):
        track_id_info[f"genre_{genre_position}"] = genre_value


    #loop for finding all ft artist and placing them in plce holders in track_id_info DICt.
    artistft =  h_content.get('artists')
    count = 0
    for artist in artistft:
        track_id_info[f"spotify_artists_name_{count}"] = artist['name']
        count+=1

    #loop for finding all ft artist and placing them in plce holders in track_id_info DICt.
    artistid =  h_content.get('artists')
    count = 0
    for newartistid in artistid:
        track_id_info[f"spotify_artist_id_{count}"] = newartistid['id']
        count+=1


    return track_id_info

# Define rec_export function
def rec_export(input_dicts, export_filename):
    keys = input_dicts[0].keys() if input_dicts else []
    
    with open(export_filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(input_dicts)
    
    print("csv done")


if __name__ == "__main__":
    main()
