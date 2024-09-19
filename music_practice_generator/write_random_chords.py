import random

def write_random_chords(n=12, m= 4, delay = 10):
    notes = ['c', 'c', 'cis', 'des', 'd', 'd', 'dis', 'ees', 'e', 'e', 'eis', 'f', 'f', 'fis', 'ges', 'g', 'g', 'gis', 'aes', 'a', 'a', 'ais', 'bes', 'b', 'b']
    qualities = ['dim7', '7.9-']
    # f = open('/output/random_chords.ly','w')
    f = open('random_chords.ly','w')
    f.write('\\score {\n')
    f.write('\t<<')
    f.write('\t\\new ChordNames {\n')
    f.write('\t\t\\chordmode {\n')

    for i in range(n):
        f.write('\t\t\t')
        for ii in range(m): 
            for iii in range(4):
                f.write(random.choice(notes) + ':' + random.choice(qualities) + ' ')
            f.write(' | ')
        f.write('\\break')
        f.write('\n')

    f.write('\t\t}\n')
    f.write('\t}\n')
    f.write('\t\\new RhythmicStaff {\n')
    f.write("\t\t\\override NoteHead.style = #'slash\n")
    f.write("\t\t\\time 4/4\n")
    f.write('\t\\omit Stem\n')
    for i in range(n):
        f.write('\t\t\t')
        for ii in range(m):
            for iii in range(4):
                f.write('c4 ')
            f.write(' | ')
        f.write('\\break')
        f.write('\n')

    f.write('\t}\n')
    f.write('\t>>\n')
    f.write('}')

    f.close()
    pass

if __name__ == '__main__':
    write_random_chords()