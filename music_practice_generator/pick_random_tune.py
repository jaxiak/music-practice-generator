

def select_random_tune(df):
  tune = df.sample()['Title'].values[0]
  return tune

if __name__ == '__main__':
    import pandas as pd
    # df = pd.read_csv('input/tunes.csv')
    df = pd.DataFrame(data = {'Title': ['Test Tune Name']})
    Go = True
    while Go:
       print(select_random_tune(df))
       if input().upper() in ['BREAKPOINT']:
          breakpoint()
          


       
