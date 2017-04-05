# Crawling YelpSG restaurant details using (Scrapy) 

* __[Part 1] Crawled on restaurant's data ['foodreview' folder]__
	* title
	* url
	* image
	* rating
	* cuisine
	* location

* __[Part 2] Crawled on restaurant's reviews ['foodreview_reviews' folder]__
	* review
	* url
	* title


## __To run [Part 1]__ ##

* __Go to the foodreview/foodreview/spiders__
	* Issue this command to use Spider to crawl : 
		* scrapy crawl yelppy -o itemRecord.json
			* this will also generate itemRecord.json
		* scrapy crawl yelppy 
			* will not generate itemRecord.json



## __To run [Part 2]__ ##

* __Go to the foodreview_reviews/foodreview/spiders__ 
	* Issue this command to use Spider to crawl : 
		* scrapy crawl yelppyDetails_review -o itemRecord.json
			* this will also generate itemRecord.json


