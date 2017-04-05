# Crawling YelpSG restaurant details using (Scrapy) 

* ** [Part 1] Crawled on Restaurant's data ['foodreview' folder]**
	* title
	* url
	* image
	* rating
	* cuisine
	* location

* ** [Part 2] Crawled on Restaurant's reviews ['foodreview_reviews' folder]**
	* review
	* url
	* title


** To run [Part 1] **

* **Go to the foodreview/foodreview/spiders **
	* Issue this command to use Spider to crawl : 
		* scrapy crawl yelppy -o itemRecord.json
			* this will also generate itemRecord.json
		* scrapy crawl yelppy 
			* will not generate itemRecord.json



** To run [Part 2] **

* **Go to the foodreview_reviews/foodreview/spiders **
	* Issue this command to use Spider to crawl : 
		* scrapy crawl yelppyDetails_review -o itemRecord.json
			* this will also generate itemRecord.json


