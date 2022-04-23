import pandas as pd
from clean import clean
from create_tokens import clean_tokenize_text
from find_topics import find_topics, topics_to_df
from top_words_topics import top_words_neighborhood, topics_label, combine_words_topics

# to run this type: python pipeline.py
# with no locations specified, this pipeline will use
# 'seattle_listings_df.csv' to clean, tokenize, and 
# cluster then output at 'pipeline_results.csv', 
# specifying file locations can change these such as
# python pipeline.py seattle_listings_df.csv pipeline_df.csv

if __name__ == '__main__':
    '''Find top words and topics of seattle listings descriptions in one pipeline'''
    
    import argparse
    # argparse used to be able to input different files
    parser = argparse.ArgumentParser()
    # const values for file locations allow pipeline.py to be ran without input
    # these can be changed
    parser.add_argument('input', nargs='?', const='seattle_listings_df.csv', default='seattle_listings_df.csv')
    parser.add_argument('output', nargs='?', const='pipeline_results.csv', default='pipeline_results.csv')
    args = parser.parse_args()
    
    print('input: ', args.input)
    print('...cleaning data and removing host columns:')
    cleaned_listings = clean(args.input) # can change input
    
    print('...creating tokens')
    # create tokens from listing descriptions
    token_df = clean_tokenize_text(cleaned_listings)
    
    print('...clustering tokens into topics')
    # use find_topics to cluster words into 5 topics then use
    # topics_to_df to put it into df
    topics_df = topics_to_df(find_topics(token_df['tokens'], 5))
    topics_df.to_csv('topics_df.csv', index=False)
    
    print('...combining top words with assigned topic')
    top_words = pd.DataFrame(top_words_neighborhood(token_df,30))
    words_topics_df = combine_words_topics(top_words)

    # convert to csv for output
    words_topics_df.to_csv(args.output, index=False)
    
    print('results output as: ', args.output)