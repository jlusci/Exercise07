import sys 
# import string

def main():
    word_counts = {}
    script, filename = sys.argv

    # t = string.maketrans('--', '  ')
  
    f = open(filename)
    for line in f:
        line = line.rstrip()
        line = line.lower()
        line = line.translate(None, '.,;!?--_:"()')
        word_list = line.split(' ')

        for w in word_list:
            # w = w.translate(None, '.,;!?--_:"()')
            if w in word_counts:
                word_counts[w] += 1
            else:
                word_counts[w] = 1

    # for key, value in word_counts.iteritems():
    #     print key, value
    frequency = {}
    for w in word_counts:
        if word_counts[w] in frequency:
            frequency[word_counts[w]].append(w)
        else:
            frequency[word_counts[w]] = [w]

    for key, value in reversed(sorted(frequency.iteritems())):
        print key, ", ".join(sorted(value))
     

if __name__ == "__main__":
    main()