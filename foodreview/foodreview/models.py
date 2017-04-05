

import psycopg2

import settings

conn = psycopg2.connect(database=settings.database,password=settings.password,host=settings.host,user=settings.user)
cur = conn.cursor()



class YelpDetailRecord(object):
    
    def __init__(self, title, url, img, rating, cuisine,location):
        super(YelpDetailRecord, self).__init__()
        self.title = title
        self.url = url
        self.img = img
        self.rating = rating
        self.cuisine = cuisine
        self.location = location

        # self.url = url
        # self.review = review
        

    def save(self):
        cur.execute("INSERT INTO yelp (title, url, img, rating, cuisine,location) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id", (
            self.title,
            self.url,
            self.img,
            self.rating,
            self.cuisine,
            self.location
        ))

        # cur.execute("UPDATE yelp SET review=%s WHERE url=%s RETURNING id", (
        #     self.review,
        #     self.url,
        # ))
        conn.commit()
        return cur.fetchone()[0]


