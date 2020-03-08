YouTube Trending Videos Analysis
-----------------------

For the purposes of analyzing and interpreting the findings of a YouTube trending videos dataset.  
Data collected and released by Mitchell J. 
The data is included in this repository as it is released by Mitchell J under the CC0 license into public domain, but I would like to extend special thanks to Mitchell J for the opportunity to work on this dataset, which can be found [here](https://www.kaggle.com/datasnaek/youtube-new).

Installation
----------------------

### Install the requirements
 
* Install the requirements using `pip install -r python_requirements.txt`.
    * Make sure you install and use Python 3.
    * You may want to use a virtual environment for this.

* Install Jupyter Notebook 
    * Might be easier to do this via Miniconda3

### Download the data

* Clone this repo to your computer.

Note: The clean_data and graphs folders are included in the repo, but are not required for usage as they are generated

Usage
-----------------------

### Workflow starting from raw_data
* Run utf8\_clean.py, which generates a clean_data folder from the data found in raw\_data
* Open yt.ipynb in Jupyter Notebook, and run the code blocks sequentially to generate the graphs folder with all of its plots

About
-----------------------
In order to have an idea of what can be investigated, we first need to understand the nature of the dataset to see what we are able to explore and subsequently what information needs to be appended into the dataset.

Column | Description
 --- | ---
video_id | YouTube unique video id
trending_date | Date when video trended (down to day)
title | Title of trending video
channel_title | Channel that trending video belongs to
category_id | Unique ID that links to a category in a paired json file
publish_time | Time when video was published (down to second)
tags | Tags of the video
views | # of views
likes | # of likes
dislikes | # of dislikes
comment_count | # of comments
thumbnail_link | Link to thumbnail
comments_disabled | Comments disabled bool
ratings_disabled | Ratings disabled bool
video_error_or_removed | Video error/removed bool
description | Description of the video

Aims
-----------------------
### Examine general patterns
* Correlation between numerical data (views, likes, etc.)
* Types of categories that have higher amount of trending videos
* When are the trending videos being published/trending
* Is there a pattern to ratings/comments disabled videos?

### Find out how to improve odds of trending 
* Does increasing the amount of tags help?
* Are there blatantly favoured categories?
* Is there a peak usage time?

Findings
-------------------------
The following are my findings from the dataset, they are not exhaustive but if you would like a chance ot explore the dataset with a clean perspective you should probably stop reading here.

### Number of tags does not seem to correlate to any other numerical metric 
![Correlation heatmap](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/correlation_heatmap.png)

Aside from the tag count findings, examination of the correlation data between the numerical columns show that there is some low correlation between all the intersections except views and likes which shows high correlation. 


### Entertainment videos are the most prevalent trending category globally
![Global category barplot](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/global_categories_barplot.png)

The number of trending videos of any category is behind entertainment by a huge margin. 


### Most trending videos do not have their comments and ratings disabled
![Comments ratings venn](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/global_comments_ratings_venn.png)

The trending video count between the two groups are hugely different and it seems like trending videos tend toward not having comments and/or ratings disabled.


### Comments/ratings disabled videos exhibit a different category distribution profile
![Global disabled category barplot](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/global_comments_ratings_disabled_barplot.png)

While the barplot for videos with either ratings or comments disabled initially looked similar to the global category barplot, the real distribution can be seen by calculating the percentage of videos in each category instead. This is because the absolute count undermines the proportion of videos of each category. The high percentage of trailers seemed abnormal given the distribution and it was found that it was due to having a low sample count. (n = 5 for Trailers)


### Globally, no day or month seems to stand out particularly in terms of trending time (with the exception of November and June), suggesting that the YouTube algorithm may select relatively stably across time

![Global trending videos by month](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/global_trending_month_barplot.png)

![Global trending videos by day](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/global_trending_day_barplot.png)

It was also found that June and November were relatively low because the dataset was dependent on trending date which started 1st December and ended 31st May. They are kept in the visualization for the purpose of including all data.


### No month clearly stands out in uploading time

![Global uploaded trending videos by month](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/global_publish_month_barplot.png)


### Global trending video upload day increases through the week, peaking at Friday and then dropping when the weekend hits

![Global uploaded trending videos by day](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/global_publish_day_barplot.png)


### Global trending video upload hour seems to peak through 4PM UTC, following a gaussian distribution

![Global uploaded trending videos by hour](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/global_publish_hour_barplot.png)


### There is a global upload hour peak at around 3PM - 5PM, regardless of the day

![Global uploaded day-hour heatmap](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/global_publish_day_hour_heatmap.png)


### Upload time distribution of some countries are masked when analyzing the dataset globally

![All countries uploaded day-hour heatmap](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/all_countries_publish_day_hour_heatmap.png)

When looking at each of the individual countries, it can be seen that the peak upload hours of Asian countries as well as Mexico were masked when looking at the dataset globally. As there is likely to be a target national audience when publishing a video, I chose to zoom in into the United States (US) for a deeper look at its peak timing and its local significance.


### Upload time peaks at 9AM - 12PM across the four major time zones in the United States

![US timezones day-hour heatmap](https://github.com/caiylderek/youtube_trending/blob/master/pre_generated/graphs/US_timezones_publish_day_hour_heatmap.png)

Zooming in into the peak hours of the US and visualizing the four major timezones present in it shows the complexity of the peak hour in the country. For simplicity one could take Eastern time as a gauge because it contains more than half of US population, but it is not conclusive which parts of US are the major contributors to the trending videos at each time point.


### From these preliminary findings it seems best to upload an Entertainment-based video at around 4PM UTC on Friday without disabling ratings or comments for your best chance to trend if your content is not aimed towards any one national demographic.



Further work
-------------------------
Listed below are some of the things that I want to eventually get to or can be considered as part of further work, classified by difficulty:

Easy:
* See if different categories have different time hotspots

Medium:
* Scrape more data to fill up January - November 2017 and June - December 2018 so that the data can be examined across years, and the data per month may be meaningful
* Analyze description to see if the video description helps with trending
* Examine each country in detail specifically (might be a bit too length-y and broad)

Hard:
* Find the channels that release the most trending videos, see if there is a way to cluster them (VEVO, etc.)
* See if the publish time can be analyzed in order to find out publishing patterns of groups, however this pivots on having a good method to cluster channels
* Merge data with full YouTube video repository metadata (including non-trending videos) and see if further insights can be gained or current insights can be confirmed
