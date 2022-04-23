import pandas as pd
from gensim.parsing.preprocessing import preprocess_string, STOPWORDS

# in terminal type: python create_tokens.py cleaned_listing.csv token_df.csv
# to take cleaned_listing df, tokenize it, and output a csv named 
# token_df.csv output name can be changed

def clean_tokenize_text(input_df):
    # create list of custom stop words and combine with gensim's stopwords
    CUSTOM_STOP_WORDS = ['seattl','bedroom', 'home', 'room', 'kitchen','bed', 'bathroom', 'hous', 'apart', 'unit', 'guest','locat','live','stai']
    stopword_list = set.union(set(STOPWORDS), CUSTOM_STOP_WORDS)

    # pick columns and make type string
    df = input_df[['neighbourhood_group_cleansed','description']].astype(str)
    df['id'] = input_df['id']
    
    # process and tokenize
    df['tokens'] = df['description'].apply(lambda x: preprocess_string(x))
    df['tokens'] = df['tokens'].apply(lambda x: [t for t in x if t not in stopword_list])
    
    return df
    

if __name__ == '__main__':
    import argparse
    import pandas as pd
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()
    
    # read in input df then tokenize
    df = pd.read_csv(args.input)
    token_df = clean_tokenize_text(df)
    
    # convert to csv for output
    token_df.to_csv(args.output, index=False)
