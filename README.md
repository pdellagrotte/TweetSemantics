# Twitter Semantics

This is a personal project to utilize the [Twitter API](https://developer.twitter.com/en/docs.html/) to extract tweets
and determine text polarity (Text Analytics). The tweets are stored in a database. This repo contains the
functions to 1.) Authenticate with the Twitter API 2.) Extract tweet data (JSON) 3.) Analyze tweet text and 4.) Create
and save to a SQLite database

<a href="https://pdellagrotte.github.io/>"<img src="https://github.com/pdellagrotte/TweetSemantics/blob/master/diagram.JPG" title="Diagram" alt="Author: Paul DellaGrotte"></a>

## Getting Started

To get this project running, clone the repository and add the Twitter API keys to the api_keys.txt file. API keys need
to be requested by applying for a [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access).

Add the Twitter handles to the handles.txt document to return the tweet history for that handle. Each line should
contain 1 twitter handle with no added special characters, quotes, or spaces. Use as many twitter handles as needed.

### Prerequisites

Python 3 or later version
Twitter API Developer account

### Installing

A few packages need to be installed

```
pip3 install tweepy
pip3 install TextBlob
pip3 install ctypes
```


## Running the tests
TBD

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Tweepy](http://www.tweepy.org/) - For accessing Twitter API
* [TextBlob](https://textblob.readthedocs.io/en/dev/) - Text processing package

## Contributing

TBD

## Versioning

GitHub

## Authors

* **Paul DellaGrotte** - *Initial work* - [Personal Site](https://pdellagrotte.github.io/)

See also the list of [contributors](https://github.com/pdellagrotte/TweetSemantics/contributors) 
who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to Bruce Van Horn whose Lynda.com PyCharm course gave me the idea for this project