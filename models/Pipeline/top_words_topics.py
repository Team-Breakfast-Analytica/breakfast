import pandas as pd

# in terminal type: python top_words_topics.py token_df.csv words_topics_df.csv
# to take token_df tokens cluster by neighborhood, apply pre generated topic labels,
# and combine to one panda df, output as word_topics_df.csv

def top_words_neighborhood(df,n):
    from collections import defaultdict
    # n = number of top words to return
    group_words = defaultdict(list)
    neighborhoods = set(['Central Area', 'Other neighborhoods', 'West Seattle', 'Ballard', 'Cascade',
         'Capitol Hill', 'Queen Anne', 'Downtown', 'Magnolia', 'Beacon Hill',
         'Lake City', 'Rainier Valley', 'University District', 'Delridge', 'Northgate',
         'Seward Park', 'Interbay'])
    for group in neighborhoods:
        word_freq = defaultdict(int)
        for sent in df[df['neighbourhood_group_cleansed']==group]['tokens']:
            for i in sent:
                word_freq[i] += 1
                
        # uncomment to print top 3 words per neighborhood
        # print(group, sorted(word_freq, key=word_freq.get, reverse=True)[:3])
        group_words[group] = sorted(word_freq, key=word_freq.get, reverse=True)[:n]
    return group_words
  
def topics_label(word):
    '''Function to return label if the words
    is found in a topic from 5 topics df (topics_df)'''
    topics_df = pd.read_csv('topics_df.csv')
    
    if word in set(topics_df['topic_1_words']):
        return 'topic_1'
    if word in set(topics_df['topic_2_words']):
        return 'topic_2'
    if word in set(topics_df['topic_3_words']):
        return 'topic_3'
    if word in set(topics_df['topic_4_words']):
        return 'topic_4'
    if word in set(topics_df['topic_5_words']):
        return 'topic_5'
      # return no topic if none found
    else:
        return 'no_topic'
    
def combine_words_topics(words_df):
    df = words_df.reset_index()
    df = pd.melt(df,id_vars=['index'], value_vars=df.columns,
            var_name='Neighborhood', value_name='Word')
    
    # use topics_label function to apply labels using the
    # labels from the 5 topics df (topics_df)
    df['Topic'] = df['Word'].apply(lambda x: topics_label(x))
    df = df.rename(columns={'index':'Rank'})
    
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
    # use top_words_neighborhood to find top 30 words per neighborhood
    # convert to panda df then use combine_words_topics to 
    top_words = pd.DataFrame(top_words_neighborhood(token_df,30))
    words_topics_df = combine_words_topics(top_words)
    
    # convert to csv for output
    words_topics_df.to_csv(args.output, index=False)
