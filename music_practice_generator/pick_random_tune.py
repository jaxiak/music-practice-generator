

def select_random_tune(df):
  tune = df.sample()['Title'].values[0]
  print(tune)
  return tune

if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('input/tunes.csv')
    Go = True
    while Go:
       select_random_tune(df)
       if input().upper() in ['BREAKPOINT']:
          breakpoint()
          


       
