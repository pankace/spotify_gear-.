import pandas as pd
import sqlalchemy
import threading
import spotipy 
from   spotipy.oauth2         import SpotifyClientCredentials
from   fycharts.SpotifyCharts import SpotifyCharts

def main():
    api = SpotifyCharts()
    """database is created for future expansion tough technically not necessary for the project"""
    connector = sqlalchemy.create_engine(
        "sqlite:///spotifycharts.db",
        echo=False) 
    hooks = ["https://mywebhookssite.com/post/", "http://asecondsite.net/post"]

#Select what you want to study by un-commenting and changing the file name the in "get_audio_features.py" 
#defult is set to top50 weekly 
#Don't forget to uncomment threads 
    a_thread = threading.Thread(target = api.top200Daily, kwargs = 
    {"output_file": "top_200_daily.csv", "output_db": connector, "webhook": hooks, "start": "2020-01-03", "end":"2020-01-12", "region": ["global", "us"]}) #Change variables as needed
    b_thread = threading.Thread(target = api.top200Weekly, kwargs = 
    {"output_file": "top_200_weekly.csv", "output_db": connector, "webhook": hooks, "start": "2020-01-03", "end":"2020-01-12", "region": ["global", "us"]})
    c_thread = threading.Thread(target = api.viral50Daily, kwargs = 
    {"output_file": "viral_50_daily.csv", "output_db": connector, "webhook": hooks, "start": "2020-01-03", "end":"2020-01-12", "region": ["global", "us"]})
    d_thread = threading.Thread(target = api.viral50Weekly, kwargs = 
    {"output_file": "viral_50_weekly.csv", "output_db": connector, 
    "webhook": hooks, "start": "2020-01-02", "end":"2020-01-12", "region": ["global", "us"]})

#when in use uncomment these too 
    a_thread.start() 
    b_thread.start()
    c_thread.start()
    d_thread.start()

if __name__ == "__main__":
    main(

    )

sp     = spotipy.Spotify() 
cid    = "insert yout client ID here" #Client ID 
secret = "Insert your secret ID here" #Secret ID 

client_credentials_manager = SpotifyClientCredentials(
    client_id = cid,
    client_secret = secret) 

sp = spotipy.Spotify(
    client_credentials_manager = client_credentials_manager) 
sp.trace = False 

"""change this file name to whatever 
   file you want to look at audio data for"""
spotify_charts = pd.read_csv("./viral_50_weekly.csv") 

"""if not working change name of variable 
   ie. change 'spotify_id' to the name of 
   the variable that you are useing in your songlist"""
ids = spotify_charts['spotify_id'].tolist() 

chunks = [ids[x:x+100] for x in range(0, len(ids), 100)]
test   = []
for group in chunks:
    test.append(
        sp.audio_features(group))

flat_list = [item for group in test for item in group]
features  = pd.DataFrame(flat_list)
#popularity will be counted numerically 
features.to_csv("./audioFeatures_of_top_50.csv")