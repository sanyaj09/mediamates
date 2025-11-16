import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist(playlist_id: str) -> list:
    # Set your client ID and client secret as environment variables
    # export SPOTIPY_CLIENT_ID='your_client_id'
    # export SPOTIPY_CLIENT_SECRET='your_client_secret'

    # $clientId = 'eb809076738747ae8a40642f3ce96674';
    # $clientSecret = '7b32bd08157741c7b4d2897d40af5d85';

    client_id = os.environ.get('SPOTIPY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

    # Authenticate using Client Credentials Flow (for public data)
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    try:
        tracks = []
        playlist = sp.playlist(playlist_id)

        print(f"Playlist Name: {playlist['name']}")
        print(f"Playlist Description: {playlist['description']}")
        print(f"Number of Tracks: {playlist['tracks']['total']}")

        print("\nTracks:")
        for i, item in enumerate(playlist['tracks']['items']):
            track = item['track']
            print(f"{i+1}. {track['name']} by {track['artists'][0]['name']}")
            tracks.append(f"{i+1}. {track['name']} by {track['artists'][0]['name']}")

        return tracks

    except spotipy.exceptions.SpotifyException as e:
        print(f"Error retrieving playlist: {e}")

    return []

if __name__ == '__main__':
    # Replace with the actual playlist ID
    playlist_id = '3cEYpjA9oz9GiPac4AsH4n'  # Example: Today's Top Hits
    get_playlist(playlist_id)
