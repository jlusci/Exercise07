import sys 

def main():
    word_counts = {}
    script, filename = sys.argv
  
    f = open(filename)
    for line in f:
        line = line.rstrip()
        line = line.lower()
        word_list = line.split(' ')

        for w in word_list:
            if w in word_counts:
                word_counts[w] += 1
            else:
                word_counts[w] = 1

    for key, value in word_counts.iteritems():
        print key, value

    # for v in sorted(word_counts.itervalues()):
    #     print v
     

if __name__ == "__main__":
    main()