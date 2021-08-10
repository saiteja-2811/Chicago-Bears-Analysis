# Import the libraries
import pandas as pd
import os

# Change the directory
os.chdir("C:/Users/saite/PycharmProjects/py38/0.GH/Chicago-Bears-Analysis")

# Pull the win-loss ratio table
win_los_wiki = 'https://en.wikipedia.org/wiki/Super_Bowl'
win_los_info = pd.read_html(win_los_wiki,header=0)
win_los_tm = pd.DataFrame(win_los_info[4])
win_los_tm.to_csv("./data/win_los_tm.csv",header=True)

# Chicago Bears Data
url = 'https://www.chicagobears.com/team/players-roster/'