'''
This script takes in the riderhsip data and returns a single dataframe, then writes the data out to a csv
'''

import pandas as pd

def reshape(df, label):
    '''
    Takes in a csv parsed from Caltrain Visualization Challenge Excel files
    Returns a reshaped dataframe 
    
    Parameters:
    ----------
    input:
    df {dataframe}: a Pandas dataframe
    label {string}: a string identifying the time of day represented by the dataframe
    
    output:
    out {dataframe}: reshaped dataframe
    '''
    
    out = pd.DataFrame(df.set_index(['Origin_ID', 'Origin_Name', 'Dest_ID', 'Dest_Name']).stack()).reset_index()
    out["TOD"] = label
    out.rename(index=str, columns={'level_4':'Scenario', 0:'Ridership_Number'}, inplace=True)
    return out[['TOD', 'Origin_ID', 'Origin_Name', 'Dest_ID', 'Dest_Name', 'Scenario', 'Ridership_Number']]

def build_df(dataframes, labels):
    '''
    Takes lists of dataframes and labels and returns concatenated, reshaped dataframe
    
    Parameters:
    ----------
    input
    dataframes {list: dataframe}: a list of Pandas dataframe objects
    labels {list: string}: a list of labels identifying the times of day (same index as dataframes)
    
    output:
    out {dataframe}: a single reshaped and concatenated dataframe
    
    '''
    for i in range(len(dataframes)):
        if i == 0:
            out = reshape(dataframes[i], labels[i])
        else:
            out = pd.concat([out, reshape(dataframes[i], labels[i])], axis=0)
    return out

#############################################################################
if __name__ == '__main__':

    ea_df = pd.read_csv('../data/Ridership/EA-Table1.csv')
    am_df = pd.read_csv('../data/Ridership/AM-Table1.csv')
    md_df = pd.read_csv('../data/Ridership/MD-Table1.csv')
    ev_df = pd.read_csv('../data/Ridership/EV-Table1.csv')
    pm_df = pd.read_csv('../data/Ridership/PM-Table1.csv')
    wknd_df = pd.read_csv('../data/Ridership/Wknd-Table1.csv')
    dataframes = [ea_df, am_df, md_df, ev_df, pm_df, wknd_df]
    labels = ['ea', 'am', 'md', 'ev', 'pm', 'wknd']
    
    ridership = build_df(dataframes, labels)
    
    ridership.to_csv('../data/ridership/ridership.csv', index=False)
