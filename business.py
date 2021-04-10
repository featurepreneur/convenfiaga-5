import pandas as pd

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['ontario'])

if __name__ == "__main__":

    get_data()