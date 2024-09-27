import pandas as pd
import music_practice_generator

def test_rhythm_output():
    assert isinstance(music_practice_generator.generate_sample_rhythms(), str)

def test_tune_selection():
    df = pd.DataFrame(data = {'Title': ['Test Tune Name']})
    assert isinstance(music_practice_generator.select_random_tune(df), str)
    
def test_chord_generater():
    assert isinstance(music_practice_generator.generate_random_chords(), str)
