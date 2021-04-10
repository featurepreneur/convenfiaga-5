import pandas as pd

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['ontario'].tolist())

    ontario_data = df['ontario'].tolist()

    quebec_data = df['quebec'].tolist()

    print(df['quebec'].tolist())

    result_dict = {
        'ontario' : ontario_data,
        'quebec'  : quebec_data
    }


    return result_dict

def add_row(year, ontario_tourist, quebec_tourist):
    
    df = pd.read_csv('data.csv') 

    new_row = {
    
        'year':year, 
        'ontario':ontario_tourist, 
        'quebec':quebec_tourist
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

'''
new_row = {'name':'Geo', 'physics':87, 'chemistry':92, 'algebra':97}
#append row to the dataframe
df_marks = df_marks.append(new_row, ignore_index=True)
'''
    

if __name__ == "__main__":

    get_data()