import pandas as pd

# in terminal type: python find_topics.py token_df.csv topics_df.csv
# to take token_df cluster words into 5 topics and convert df to 
# csv and output as topics_df.csv 

def find_topics(tokens, num_topics):
    from gensim.corpora import Dictionary
    from gensim.models import LdaModel
    
    dictionary = Dictionary(tokens)
    dictionary.filter_extremes(no_below=10, no_above=0.6)
    
    corpus = [dictionary.doc2bow(doc) for doc in tokens]
    
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, chunksize=2000, 
                         passes=20, iterations=400, eval_every=None, 
                         random_state=697, alpha='auto', eta='auto')
    
    return lda_model.top_topics(corpus) 
    
def topics_to_df(topics_list):
    df = pd.DataFrame()
    for i, topic in enumerate(topics_list):
        df['topic_'+str(i+1)+'_values'] = [v[0] for v in topic[0]]
        df['topic_'+str(i+1)+'_words'] = [v[1] for v in topic[0]]

    return df
    

if __name__ == '__main__':
    import argparse
    import pandas as pd
    from ast import literal_eval
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()
    
    # read in input df then tokenize
    token_df = pd.read_csv(args.input, converters={'tokens': literal_eval})
    # use find_topics to cluster words into 5 topics then use
    # topics_to_df to put it into df
    topics_df = topics_to_df(find_topics(token_df['tokens'], 5))
    
    # convert to csv for output
    topics_df.to_csv(args.output, index=False)
