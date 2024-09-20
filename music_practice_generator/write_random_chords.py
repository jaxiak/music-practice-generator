import random
def generate_random_chords(n:int=12, m:int= 4)->str:
    """Creates a string for a lilypond file which will write random chords to practice.\n
    n is the number of lines\n
    m is the number of measures per line"""
    notes = ['c', 'c', 'cis', 'des', 'd', 'd', 'dis', 'ees', 'e', 'e', 'eis', 'f', 'f', 'fis', 'ges', 'g', 'g', 'gis', 'aes', 'a', 'a', 'ais', 'bes', 'b', 'b']
    qualities = ['dim7', '7.9-']
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
    random_chords_string = generate_random_chords()
    f = open(os.path.join(os.path.dirname(__file__), 'output/random_chords.ly'),'w')
    f.write(random_chords_string)
    f.close()