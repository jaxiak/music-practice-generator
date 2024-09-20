

def select_random_tune(df):
  tune = df.sample()['Title'].values[0]
  return tune

if __name__ == '__main__':
    import pandas as pd
    import os
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'input/tunes.csv'))
    Go = True
    while Go:
       print(select_random_tune(df))
       if input().upper() in ['BREAKPOINT']:
          breakpoint()
          


       
