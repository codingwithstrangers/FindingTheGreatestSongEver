import json
import pprint
import requests
from main import access_token

def main():
    print("Starting main function...")
    limit = 3
    seed_artists ="5KDIH2gF0VpelTqyQS7udb"
    # seed_genres = ['alternative', 'rap']
    tracks = get_recommended_tracks(limit, seed_artists)
    if tracks:
        print("Tracks received:", tracks)
        save_to_json(tracks)
    else:
        print("No tracks received.")


def get_recommended_tracks(limit, seed_artists):
    print("Getting recommended tracks...")
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    # For all known ranges, best for using with genre and artist
    seed_genres = "rap"
    seed_tracks = ""
    target_tempo = "101.061"
    target_danceability = "0.898"
    target_liveness = "0.0731"
    target_popularity = "97"
    target_acousticness = ".315"
    target_energy = ".472"
    target_instrumentalness = "0"
    target_key = "1"
    target_speechiness = ".0351"
    target_valence = ".246"

    endpoint_url = "https://api.spotify.com/v1/recommendations?"
    query = f'{endpoint_url}limit={limit}&seed_genres={seed_genres}&seed_tracks={seed_tracks}&seed_artists={seed_artists}'
    query += f'&target_tempo={target_tempo}'
    query += f'&target_danceability={target_danceability}'
    query += f'&target_liveness={target_liveness}'
    query += f'&target_popularity={target_popularity}'
    query += f'&target_acousticness={target_acousticness}'
    query += f'&target_energy={target_energy}'
    query += f'&target_instrumentalness={target_instrumentalness}'
    query += f'&target_key={target_key}'
    query += f'&target_speechiness={target_speechiness}'
    query += f'&target_valence={target_valence}'

    print("Query:", query)
    result = requests.get(query, headers=headers)
    print("API response status code:", result.status_code)

    if result.status_code != 200:
        print("Error in API call:", result.content)
        return []

    result_content = result.json()
    print("API response content:", json.dumps(result_content, indent=4))

    tracks = []

    # For each track in results
    for track in result_content.get("tracks", []):
        track_id = track["id"]
        artist_ids = [artist["id"] for artist in track["artists"]]
        artist_names = [artist["name"] for artist in track["artists"]]

        tracks.append({
            "track_id": track_id,
            "artist_id": artist_ids,
            "artist_names": artist_names
        })

    return tracks


def save_to_json(tracks):
    print("Saving to JSON file...")
    # Write the result to a JSON file
    with open('target_based.json', 'w') as f:
        json.dump(tracks, f, indent=4)
    print("JSON file saved.")


if __name__ == "__main__":
    main()
