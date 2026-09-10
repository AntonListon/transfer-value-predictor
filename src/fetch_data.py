#File for fetching data, first dummy run

import pandas as pd

# Load Dataset
def get_player_data():
    df = pd.read_csv('data/dataset.csv')
    # Rewriting the turkish column names to english
    column_mapping = {
        'Oyuncu': 'name',
        'Yaş': 'age',
        'Uyruk': 'nationality',
        'Mevki': 'position',
        'DK': 'minutes',
        'GLS': 'goals',
        'AST': 'assists',
        'Bonservis': 'value_m_euro'
    }

    df = df.rename(columns=column_mapping)

    selected_columns = ['name', 'age', 'position', 'minutes', 'goals', 'assists', 'xG', 'xA', 'KEYP', 'value_m_euro']
    # removes all but selected columns
    df = df[selected_columns].dropna()

    # remove "." from value in the dataset and convert to millions (EURO)
    df['value_m_euro'] = df['value_m_euro'].astype(str).str.replace('.', '', regex=False)
    df['value_m_euro'] = pd.to_numeric(df['value_m_euro'], errors='coerce')
    df['value_m_euro'] = df['value_m_euro'] / 1000000

    return df


if __name__ == "__main__":
    df = get_player_data()
    print("Data fetched succesfully:")
    print(df)