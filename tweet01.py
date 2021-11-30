import tweepy

consumer_key = 'qdbEUoaBrr54j81FuXoCSjTaG'
consumer_secret = 'NqmkGfzTs5EXq7zPeGMX9DfRFTPulYQmVJjeajL0VKjqfWOyo9'

access_token = '1464064838389272577-ng4KyPmQEILWEgr07ULdEPtRwIDW53'
access_secret = 'XDipZfQqXROCksGvfjSq1JEtBTR0xqTgZ5V8VxrTqH17I'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#print(api.verify_credentials().name)

#tweet_update_status = api.update_status('파이썬에서 tweepy 라이브러리를 이용한 첫 번째 트윗')
#tweet_media_update_status = api.update_status_with_media('tweepy를 이용한 이미지 올리기', './ch15_webAPI/pororo.png')

for status in tweepy.Cursor(api.home_timeline).items(2):
    print("*", status._json['text'])
    print(" ==> Created at", status._json['created_at'])


class MyStream(tweepy.Stream):
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret, max_num):
        super().__init__(consumer_key, consumer_secret, access_token, access_secret)
        self.tweet_num = 0
        self.max_num = max_num

    def on_status(self, status):
        self.tweet_num = self.tweet_num + 1
        file_name = "./ch15_webAPI/twitter_stream_test.txt"
        if(self.tweet_num <= self.max_num):
            with open(file_name, 'a', encoding="utf-8") as f:
                write_text = "***" + status.text + "\n"
                f.write(write_text)
            return True
        else:
            self.disconnect()
            return False

    def on_error(self, status):
        print(status)
        return False

if __name__ == '__main__':
    myStream = MyStream(consumer_key, consumer_secret, access_token, access_secret, 3)
    myStream.filter(track=['머신 러닝', 'Machine Learning'])
    print("End of Streaming!")