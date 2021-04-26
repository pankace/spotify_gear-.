import sqlalchemy
import threading
from fycharts.SpotifyCharts import SpotifyCharts

def main():
    api = SpotifyCharts()
    connector = sqlalchemy.create_engine("sqlite:///spotifycharts.db", echo=False) #database is created for future expansion tough technically not necessary for the project 
    hooks = ["https://mywebhookssite.com/post/", "http://asecondsite.net/post"]
#Select what you want to study by un-commenting and changing the file name the in "get_audio_features.py"
#defult is set to top50 weekly 
#Don't forget to uncomment threads 
    a_thread = threading.Thread(target = api.top200Daily, kwargs = 
    {"output_file": "top_200_daily.csv", "output_db": connector, "webhook": hooks, "start": "2020-01-03", "end":"2020-01-12", "region": ["global", "us"]}) #Change variables as needed
    b_thread = threading.Thread(target = api.top200Weekly, kwargs = 
    {"output_file": "top_200_weekly.csv", "output_db": connector, "webhook": hooks, "start": "2020-01-03", "end":"2020-01-12", "region": ["global", "us"]}) #
    c_thread = threading.Thread(target = api.viral50Daily, kwargs = 
    {"output_file": "viral_50_daily.csv", "output_db": connector, "webhook": hooks, "start": "2020-01-03", "end":"2020-01-12", "region": ["global", "us"]}) #
    d_thread = threading.Thread(target = api.viral50Weekly, kwargs = 
    {"output_file": "viral_50_weekly.csv", "output_db": connector, "webhook": hooks, "start": "2020-01-02", "end":"2020-01-12", "region": ["global", "us"]}) #

#when in use uncomment these too 
    a_thread.start() 
    b_thread.start()
    c_thread.start()
    d_thread.start()

if __name__ == "__main__":
    main()