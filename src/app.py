import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import seaborn as sns
import sys

load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

con = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                            client_secret = client_secret))

artist_id = "31W5EY0aAly4Qieq6OFu6I"

response = con.artist_top_tracks(artist_id)

if response:
    columns=['name', 'duration_ms', 'popularity']
    tracks_df = pd.DataFrame(columns=columns)

    # We keep the "tracks" object of the answer
    for track in response['tracks'][:10]:
        tracks_df = tracks_df.append({'name': track['name'], 'duration_ms': track['duration_ms'], 'popularity': track['popularity']}, ignore_index=True)


tracks_df.sort_values(["popularity"], inplace=True)
print(tracks_df)

scatter_plot = sns.scatterplot(data=tracks_df, x="popularity", y="duration_ms")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")
