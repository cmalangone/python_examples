
def open_tsv(filename):
    stats = {}
    with open(filename) as csvfile:
        # by default delimiter is comma. Tab -> delimiter = '\t'
        n = 1
        intestazione = ''
        for line in csvfile:
            if line.startswith('##'):
                continue
            elif line.startswith('#'):
                intestazione = line.split('\t')
                for item in intestazione:
                    stats[item] = {}
            else:
                row = line.split('\t')
                for nomecampo, valore in zip(intestazione,row):
                    stats[nomecampo][n] = valore
                n += 1


    csvfile.close()
    return stats

def main():
    dict_stats = open_tsv("../ceu.cvf")
    #print(dict_stats)
    for ids, key in enumerate(dict_stats['ID'].keys()):
        print("{} : {}".format(ids,dict_stats['ID'][ids+1]))

    for ids in range(len(dict_stats['ID'])):
        print("{} : {}".format(ids,dict_stats['ID'][ids+1]))

    #print(dict_stats['ID'][2])

if __name__ == "__main__":
    main()