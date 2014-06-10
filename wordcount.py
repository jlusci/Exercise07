import sys 
from string import maketrans

def main():
    word_counts = {}
    script, filename = sys.argv

    intab = '.,;!?_:"()-/'
    outtab = "            "
    transtable = maketrans(intab, outtab)
  
    f = open(filename)
    for line in f:
        line = line.rstrip()
        line = line.lower()
        line = line.translate(transtable)
        word_list = line.split(' ')

        for w in word_list:
            if w in word_counts:
                word_counts[w] += 1
            else:
                word_counts[w] = 1

    frequency = {}
    for w in word_counts:
        if word_counts[w] in frequency:
            frequency[word_counts[w]].append(w)
        else:
            frequency[word_counts[w]] = [w]

    for key, value in reversed(sorted(frequency.iteritems())):
        # print key, ", ".join(sorted(value)), "\n"
        for v in sorted(value):
            print v, key
     

if __name__ == "__main__":
    main()