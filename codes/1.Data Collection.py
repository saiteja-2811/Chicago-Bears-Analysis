import pandas as pd
url = 'https://www.chicagobears.com/team/players-roster/'
dfs = pd.read_html(url,header=0)