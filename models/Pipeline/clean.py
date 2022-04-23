import pandas as pd

# in terminal type: python clean.py seattle_listings_df.csv cleaned_listing.csv
# to take seattle-listing, clean it, and output a csv names cleaned_listing
# output name can be changed

def clean(input_file):
    '''Cleans file inputed and returns a panda df,
    drops defined columns and cleans price and date'''

    df = pd.read_csv(input_file)
    
    # list of columns to drop if found in df 
    # to protect host information
    drop_list = ['host_url','host_name','host_thumbnail_url','host_picture_url','host_location']

    for column in drop_list:
        print(column)
        if column in df.columns:
            df = df.drop(column, axis=1)

    # remove dollar sign and commas from price column
    if 'price' in df.columns:
        df['price'] = df['price'].replace({'\$':''}, regex = True)
        df['price'] = df['price'].replace(',','', regex = True).astype('float')

    # make sure date is datetime  
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    return df

if __name__ == '__main__':
    import argparse
    # argparse used to be able to input different files
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()
    
    # convert panda df to csv for output
    cleaned = clean(args.input)
    cleaned.to_csv(args.output, index=False)