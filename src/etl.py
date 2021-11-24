import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def ngram_output(file):
    twt_data = pd.read_json(file,header=None)
    with open(file) as f:
        twt_data = f.readlines()
    
    def flat_tweet(tweets):
        
        tweets_edited = []
        
        for t in tweets:
            
            t['user-id'] = t['user']['id']
            t['user-name'] = t['user']['name']
            t['user-screen_name'] = t['user']['screen_name']
            t['user-location'] = t['user']['location']
            t['user-url'] = t['user']['url']
            t['user-description'] = t['user']['description']
            
            
            if 'extended_tweet' in t:
                t['extended_tweet-full_text'] = t['extended_tweet']['full_text']
                t['text'] = t['extended_tweet-full_text']
                
        
            if 'retweeted_status' in t:
                t['retweeted_status-user-screen_name'] = t['retweeted_status']['user']['screen_name']
                t['retweeted_status-text'] = t['retweeted_status']['text']
                t['text'] = t['retweeted_status-text']
                
                if 'extended_tweet' in t['retweeted_status']:
                    t['retweeted_status-extended_tweet-full_text'] = t['retweeted_status']['extended_tweet']['full_text']
                    t['text'] = t['retweeted_status-extended_tweet-full_text']
                    
                    
            if 'quoted_status' in t:
                t['quoted_status-user-screen_name'] = t['quoted_status']['user']['screen_name']
                t['quoted_status-text'] = t['quoted_status']['text']
        
                if 'extended_tweet' in t['quoted_status']:
                    t['quoted_status-extended_tweet-full_text'] = t['quoted_status']['extended_tweet']['full_text']
            

            if 'place' in t:
                try:
                    t['place-country'] = t['place']['country']
                    t['place-country_code'] = t['place']['country_code']
                    t['location-coordinates'] = t['place']['bounding_box']['coordinates']
                except: pass
            
            tweets_edited.append(t)
            
        return tweets_edited

    def gen_ngrams(text,ngram=1):

        words = [w for w in text.split(" ") if w not in set(stopwords.words('english'))]  
        temp = zip(*[words[i:] for i in range(0,ngram)])
        a = [' '.join(ngram) for ngram in temp]

        return a

    tweets = flat_tweet(twt_data)
    cols = ['text', 'user-id','user-screen_name']
    twt_df = pd.DataFrame(tweets, columns=cols)

    twt_df["ngrams_1"] = twt_df["text"].apply(gen_ngrams)
    twt_df["ngrams_2"] = twt_df["text"].apply(lambda x: gen_ngrams(x,ngram=2))
    twt_df["ngrams_3"] = twt_df["text"].apply(lambda x: gen_ngrams(x,ngram=3))

    print(twt_df.head(5))

    return twt_df