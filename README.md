YouTube Trending Videos Analysis
-----------------------

Analyze and interpret the findings of a YouTube trending videos dataset.  Data collected and released by Mitchell J. The data is included in this repository as it is released by Mitchell J under the CC0 license into public domain, but I would like to extend special thanks to Mitchell J for the opportunity to work on this dataset, which can be found [here](https://www.kaggle.com/datasnaek/youtube-new).

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


Further work
-------------------------
Listed below are some of the things that I want to eventually get to or can be considered as part of further work:

* To-do