import pandas as pd
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
sp = spotipy.Spotify() 
cid = "insert yout client ID here" #Client ID
secret = "Insert your secret ID here" #Secret ID
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
sp.trace = False 
spotify_charts = pd.read_csv("./viral_50_daily.csv") #change this file name to whatever file you want to look at audio data for 
ids = spotify_charts['spotify_id'].tolist() #if not working change name of variable 
chunks = [ids[x:x+100] for x in range(0, len(ids), 100)]
test = []
for group in chunks:
    test.append(sp.audio_features(group))

flat_list = [item for group in test for item in group]
features = pd.DataFrame(flat_list)
features.to_csv("./audioFeatures_of_top_50.csv") #popularity will be counted numerically 