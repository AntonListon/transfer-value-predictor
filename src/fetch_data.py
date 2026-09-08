#File for fetching data, first dummy run

import pandas as pd

## DUMMY DATA
def get_player_data():
    raw_data = [
        {"name": "Player A", "age": 22, "minutes": 2100, "goals": 15, "assists": 5, "position": "Forward", "value_m_euro": 50.0},
        {"name": "Player B", "age": 28, "minutes": 3200, "goals": 2, "assists": 10, "position": "Midfielder", "value_m_euro": 45.0},
        {"name": "Player C", "age": 25, "minutes": 1500, "goals": 0, "assists": 2, "position": "Defender", "value_m_euro": 15.0},
        {"name": "Player D", "age": 21, "minutes": 1800, "goals": 5, "assists": 8, "position": "Midfielder", "value_m_euro": 30.0},
        {"name": "Player E", "age": 30, "minutes": 2800, "goals": 20, "assists": 3, "position": "Forward", "value_m_euro": 60.0}
    ]
    return pd.DataFrame(raw_data)

if __name__ == "__main__":
    df = get_player_data()
    print("Data fetched succesfully:")
    print(df)