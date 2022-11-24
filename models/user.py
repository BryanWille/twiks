class User:
    
    def __init__(self, friends_count, id, statuses_count, name, favorites_count, screen_name, created_at, location, profile_location, description, protected, followers_count):
        self.friends_count = friends_count
        self.id = id
        self.statuses_count = statuses_count
        self.name = name
        self.favorites_count = favorites_count
        self.screen_name = screen_name
        self.created_at = created_at
        self.location = location
        self.profile_location = profile_location
        self.description = description
        self.protected = protected
        self.followers_count = followers_count
    
    def userToMap(self):
        return {
            'friends_count': self.friends_count,
            'id': self.id,
            'statuses_count': self.statuses_count,
            'name': self.name,
            'favorites_count': self.favorites_count,
            'screen_name': self.screen_name,
            'created_at': self.created_at,
            'location': self.location,
            'profile_location': self.profile_location,
            'description': self.description,
            'protected': self.protected,
            'followers_count': self.followers_count
        }
        
    def mapToUser(self, user_map):
            id = user_map['id']
            name = user_map['name']
            screen_name = user_map['screen_name']
            location = user_map['location']
            profile_location = user_map['profile_location']
            description = user_map['description']
            protected = user_map['protected']
            followers_count = user_map['followers_count']
            friends_count = user_map['friends_count']
            created_at = user_map['created_at']
            favourites_count = user_map['favorites_count']
            verified = user_map['verified']
            statuses_count = user_map['statuses_count']
            return User(id=id, name=name, screen_name = screen_name, location=location, profile_locatio=profile_location, description=description, protected=protected, followers_count=followers_count, friends_count=friends_count,
                        created_at=created_at, favorites_count=favourites_count, statuses_count=statuses_count, verified=verified)