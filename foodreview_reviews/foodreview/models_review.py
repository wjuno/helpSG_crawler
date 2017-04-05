import psycopg2

import settings

conn = psycopg2.connect(database=settings.database,password=settings.password,host=settings.host,user=settings.user)
cur = conn.cursor()



class YelpDetailRecord(object):
    
    def __init__(self, title, review, url):
        super(YelpDetailRecord, self).__init__()
        self.title = title
        self.review = review
        self.url = url

        # self.url = url
        # self.review = review
        

    def save(self):
        cur.execute("INSERT INTO yelp_review (title, review, url) VALUES (%s, %s, %s) RETURNING id", (
            self.title,
            self.review,
            self.url,
        ))

        # cur.execute("UPDATE yelp SET review=%s WHERE url=%s RETURNING id", (
        #     self.review,
        #     self.url,
        # ))
        conn.commit()
        return cur.fetchone()[0]


