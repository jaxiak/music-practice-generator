import os
import music_practice_generator

def test_sample_rhythms():
    import random
    random.seed(1729)
    f = open(os.path.join(os.path.dirname(__file__), 'test_samples/sample_rhythms.ly'))
    test_sample = f.read()
    f.close()
    assert test_sample == music_practice_generator.generate_sample_rhythms()

def test_sample_tunes():
    import pandas as pd
    import numpy as np
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test_samples/sample_tunes.csv'))
    np.random.seed(1729)
    assert music_practice_generator.select_random_tune(df) == 'But Beautiful'

def test_sample_chords():
    import random
    random.seed(1729)
    f = open(os.path.join(os.path.dirname(__file__), 'test_samples/sample_chords.ly'))
    test_sample = f.read()
    f.close()
    assert test_sample == music_practice_generator.generate_random_chords()

if __name__ == '__main__':
    test_sample_rhythms()
    test_sample_tunes()
    test_sample_rhythms()
