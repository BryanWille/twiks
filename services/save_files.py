import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import services.database as db
import datetime as dt
import os
import json

class Save:
    def __init__(self, username: str):
        self.username = username
        self.db = db.Database
        self.username = username
        
    def saveAllTweets(self):
        map = self.db.retrievePostsInfo(self.username)    
        for hour in map:
            hour['created_at'] = pd.to_datetime(hour['created_at'])
        
        
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        for data in map:
            path = f"{self.username}/{data['created_at'].year}/{data['created_at'].month}-{months[data['created_at'].month-1]}/{data['created_at'].day}"
            if not os.path.isdir(path):
                os.makedirs(f"{path}")
            file = open(f"{path}/{data['id_str']}", 'w')
            try:
                file.write(f"{data['text']}")
            except:
                file.write("error")