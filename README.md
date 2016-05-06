# twitterMiner
A tweet retrieval app that gets tweets according to specific keywords and count of tweets from each locations.

# Running Locally
1. Create an application on Twitter Developers.
2. Configure config.py using config-template.py to authorize application with twitter.
3. Open terminal or command prompt
4. Type "python _twitter_data_stream.py -> output.json"
5. Hit Ctrl+C when you want the data streaming to stop
6. Type "python _tags_count.py" to get the count of tweets as per the location in a .csv file in a (Place_Name, Tweet_Count) format.
