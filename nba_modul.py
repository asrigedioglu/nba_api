# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:24:33 2023

@author: agedioglu
"""

import requests
import pandas as pd

class Api_nba():
    
    # Api bilgileri ve datayı çekmeye yarayacak temel bilgileri baz fonksiyonda döndürür..
    def __init__(self):
        self.url = "https://free-nba.p.rapidapi.com/players"
        self.api_key = "db28c8c196msh3e51d0c49d03f45p1960cejsn23b99e6e01b6"
        self.host = "free-nba.p.rapidapi.com"
        self.headers = {
           "X-RapidAPI-Key": self.api_key,
           "X-RapidAPI-Host":self.host
       }
        self.query = {}
        
        
    def get_query(self,query):
        # Belirli parametreleri bildirmeye yarar.
        self.query = query
        
        
    def get_data(self):
        # Tüm datayı çekecek fonksiyon. 
        response = requests.get(self.url, headers=self.headers,params=self.query)
        
        if response.status_code == 200:
            return response.json()
        
        else:
            response.raise_for_status()

class Visualization(Api_nba):
    # Çekilen datayı dataframe tablosuna aktarır.
    
    def __init__(self):
        super().__init__()
        # Baz bilgiler kalıtım fonksiyonunda gelir.
        
    def create_dataframe(self,query):
        self.query = query
        nba_data = self.get_data()
        player_data = nba_data.get("data",[])
        
        # Karmaşık bir data yapısı olduğundan öncelikle sözlük yapısı içinde data key'i çekilir.
        # Ardından sadeleşmiş datayı dataframe olarak çeker.
        # Sözlük yapısı içinde ki "team" sözlüğünden dolayı json.normalize ile normalizasyon sağlanır.
        # Son olarak team_df ve player_df tek bir tabloda birleştirilir.
        
        player_df = pd.DataFrame(player_data)
        team_df = pd.json_normalize(player_df["team"])
        df = pd.concat([player_df,team_df],axis=1)
        return df
    
       
    
        

        
    
        
    
        
    
        
                
        