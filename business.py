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

if __name__ == "__main__":

    get_data()