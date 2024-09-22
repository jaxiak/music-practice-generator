import random

all_qualities = ['', 'm', 'aug', 'dim', '7', 'maj7', 'maj', 'm7', 'dim7', 'aug7', 'm7.5-','7.9-',  'm7+', '6', 'm6m', '9', 'maj9', 'm9', '11', 'maj11', 'm11', '13', '13.11', 'maj13.11', 'm13.11', 'sus2', 'sus4', '1.5', '1.5.8']
def generate_random_chords(n:int=12, m:int= 4, qualities:list = None, notes:list = None)->str:
    """Creates a string for a lilypond file which will write random chords to practice.\n
    n is the number of lines\n
    m is the number of measures per line
    qualities will be the lilypond chord qualities, from '', 'm', 'aug', '7.9-', 'dim', '7', 'maj7', 'maj', 'm7', 'dim7', 'aug7', 'm7.5-', 'm7+', '6', 'm6m', '9', 'maj9', 'm9', '11', 'maj11', 'm11', '13', '13.11', 'maj13.11', 'm13.11', 'sus2', 'sus4', '1.5', '1.5.8'"""
    if qualities == None:
        qualities = ['dim7', '7.9-']
    if notes == None:
        notes = ['c', 'c', 'cis', 'des', 'd', 'd', 'dis', 'ees', 'e', 'e', 'eis', 'f', 'f', 'fis', 'ges', 'g', 'g', 'gis', 'aes', 'a', 'a', 'ais', 'bes', 'b', 'b']
    
    # f = open('/output/random_chords.ly','w')
    chords_string = ''
    chords_string += '\\header { \\tagline = ##f}\n'
    chords_string += '\\score {\n'
    chords_string += '\t<<'
    chords_string += '\t\\new ChordNames {\n'
    chords_string += '\t\t\\chordmode {\n'

    for i in range(n):
        chords_string += '\t\t\t'
        for ii in range(m): 
            for iii in range(4):
                chords_string += random.choice(notes) + ':' + random.choice(qualities) + ' '
            chords_string += ' | '
        chords_string += '\\break'
        chords_string += '\n'

    chords_string += '\t\t}\n'
    chords_string += '\t}\n'
    chords_string += '\t\\new RhythmicStaff {\n'
    chords_string += "\t\t\\override NoteHead.style = #'slash\n"
    chords_string += "\t\t\\time 4/4\n"
    chords_string += '\t\\omit Stem\n'
    for i in range(n):
        chords_string += '\t\t\t'
        for ii in range(m):
            for iii in range(4):
                chords_string += 'c4 '
            chords_string += ' | '
        chords_string += '\\break'
        chords_string += '\n'

    chords_string += '\t}\n'
    chords_string += '\t>>\n'
    chords_string += '}'

    return chords_string

if __name__ == '__main__':
    import os
    random_chords_string = generate_random_chords(qualities=all_qualities)
    f = open(os.path.join(os.path.dirname(__file__), 'output/random_chords.ly'),'w')
    f.write(random_chords_string)
    f.close()