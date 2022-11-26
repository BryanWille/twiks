import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import services.database as db
import datetime as dt

class Charts:
    def __init__(self, username: str):
        self.username = username
        self.db = db.Database
        self.mapStatus = db.Database.retrieveStatusInfo(username)
    
    def pieChartLikes(self, count: int):
        map = self.mapStatus
        user_names = []
        for name in map:
            user_names.append(name['user']['screen_name'])
            
        names = user_names
        
        for c in range(0, len(user_names)):
            if user_names.count(user_names[c%len(user_names)]) < count:
                names.pop(c%len(user_names))
        
        likes = pd.value_counts(np.array(user_names))
        
        likes.plot.pie(x="Amount of likes", y='Users', figsize=(5, 5))
        plt.title(f"Users that {self.username} liked status most!")
        plt.show()
    
    def mostCommonLikedCreatedHour(self):
        map = db.Database.retrieveStatusInfo(username=self.username)
        created_at = []
        
        for hour in map:
            created_at.append(hour['created_at'])
        
        df = np.array(created_at)
        df = pd.to_datetime(df)

        x = pd.value_counts(df.hour)
        plt.bar(x.index, x.values )
        
        plt.title(f"Most common likes from tweet created hour from {self.username}")
        plt.ylabel("Amount of likes")
        plt.xlabel("Liked hour")
        
        plt.show()