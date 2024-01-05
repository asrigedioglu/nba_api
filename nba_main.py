# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:45:01 2023

@author: agedioglu
"""

import nba_modul

api = nba_modul.Api_nba()
api.get_query({"page":1, "per_page": 100,"search":"David"})
nba_data = api.get_data()
nba_data

visual = nba_modul.Visualization()
df = visual.create_dataframe({"page":1, "per_page": 100,"search":"David"})  
df = df.drop("team",axis=1)
df

# Team içeriği tabloya farklı sutunlarda eklendiğinden, dict(team) drop edilir.



