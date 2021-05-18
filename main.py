from collections import Counter
import sys


def main(argv):
    fil_inn = argv[0]
    f = open(fil_inn, 'r')
    lest_fil = f.readlines()
    ordliste = {}
    splittet = []

    for linje in lest_fil:
        ordLinje = linje.split(' ')
        for ord in ordLinje:
            ord = ord.lower()
            ord = ord.strip('.,\n')
            splittet.append(ord)

    mest_vanlig = Counter(splittet).most_common(10)

    print(mest_vanlig)





if __name__ == "__main__":
    main(sys.argv[1:])