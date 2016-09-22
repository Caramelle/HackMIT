# Worth Watching

## What is this?
![app-screenshot](http://i.imgur.com/1XVKjU2.png,"Splash page of the app")
This project was built for HackMIT 2016. It's aim was to determine wheter upcoming movies would be good based on what people currently thought of them.

## How does it work?

![details-screenshot](https://i.imgur.com/uL4HJzi.png,"Details of each movie")
It uses machine learning and emotion analysis on tweets about upcoming movies to predict wether a movie will be good or not.
Tweets from before a movie was released were pulled and fed through IBM-Watson emotion analysis, extracting the emotions in the tweets, and creating an average emotion felt by people for each movie.
Using Microsoft Azure Machine Learning, we trained a classifier on these emotions to classify movies as good or bad.
The classifier was then used to determine whether upcoming movies were going to be good, based on what people were currently tweeting about them.

## How did it perform?

As we were limited by the 1000 API calls that IBM-Watson gave us, we could not use as much training data as we would have liked. However, with about 700 movies fed into the classifier, we reached an average correct-classification rate of 75%.
We think that if we were to train it on more data, and do a more thorough search on tweets, we could get a higher accuracy.
