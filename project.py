import requests
import pandas as pd
import supabase as supa

# Puxando dados da API
# symbol=IBM trocar para outras empresas
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=I7I5UKQ8ZUQNI6AE'
r = requests.get(url)
data = r.json()

df = 