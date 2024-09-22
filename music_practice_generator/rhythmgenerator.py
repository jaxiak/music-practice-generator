from random import shuffle

def incremented(enc, simultaneous:bool = False):
    new_enc = ''
    g = True
    i = 0
    while g and i < 8:
        if enc[i] == 'r':
            new_enc += 'b'
            g = False
            i += 1
        elif enc[i] == 'b':
            new_enc += 's'
            g = False
            i += 1
        else:
            new_enc += 'r'
            i += 1
    while i < 8:
        new_enc += enc[i]
        i += 1
    return new_enc

def decode_measure(enc, simultaneous:bool = False):
    measure = "\t"
    i = 0
    
    encoding = {'r': 'r', 'b': 'bd', 's': 'sn'}
    while i < 8:
        #this_measure += str(i)
        measure += encoding[enc[i]]
        duration = 1
        for ii in range(i+1, 4 if i < 4 else 8):
            if enc[ii] == 'r':
                duration += 1
                i += 1
            else:
                break
        if duration == 3:
            measure += "4. "
        else:
            measure += str(int(8 / duration))
            measure += " "
        i += 1
    measure += "\n"
    return measure

def check_measure(enc, simultaneous:bool = False):
    for i in range(8):
        if enc[i] == 'b' and enc[(i+1)%8] == 'b' and enc[(i + 2 ) % 8] == 'b':
            return False
        if enc[i] == 's' and enc[(i + 1) % 8] == 's' and enc[(i + 2 ) % 8] == 's':
            return False
    return True

def generate_sample_rhythms(n:int = 500, simultaneous:bool = False) -> str:
    """Will generate a string for an .ly file.\n
    n is the number of measure that will be in the file.
    simultaneous is whether two notes can happen at the same time."""
    list_of_encodes = []
    rhythms_string = ''
    
    rhythms_string += '\\header { \\tagline = ##f}\n'
    rhythms_string += "\\drums {\n"
    rhythms_string += "\t\\time 4/4\n"
    
    checked = set()
    encoded_measure = 'rrrrrrrr'
    for i in range(100000):
        if encoded_measure in checked:
            break
        checked.add(encoded_measure)
        if check_measure(encoded_measure, simultaneous = simultaneous):
            list_of_encodes.append(encoded_measure)
        encoded_measure = incremented(encoded_measure, simultaneous = simultaneous)
    shuffle(list_of_encodes)

    for i in range(min(n, len(list_of_encodes))):
        rhythms_string += "\t"
        rhythms_string += decode_measure(list_of_encodes[i], simultaneous = simultaneous)
        rhythms_string += "\n"
    
    rhythms_string += "}\n"
    
    return rhythms_string

if __name__ == '__main__':
    import os
    sample_rhythms_string = generate_sample_rhythms()
    f = open(os.path.join(os.path.dirname(__file__), 'output/random_rhythms.ly'),'w')
    f.write(sample_rhythms_string)
    f.close()
