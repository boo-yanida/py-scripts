import enum

def main():
    sample = 'abcde'
    result = pairwise_offset(sample)
    print(result)

def pairwise_offset(sequence, fillvalue='*', offset=0):
    sequence = list(sequence)
    #print(sequence)
    result = []
    if offset <= 0:
        result = tuple((x,x) for x in sequence)
    else:
        dummy_seq1 = sequence.copy()
        dummy_seq2 = sequence.copy()
        for i in range(offset):
            dummy_seq1.append(fillvalue)
        for i in range(offset):
            dummy_seq2.insert(i,fillvalue)
        #print(dummy_seq1)
        #print(dummy_seq2)
        result = tuple((v,dummy_seq2[x]) for x,v in enumerate(dummy_seq1))

    return result

if __name__ == "__main__":
    main()
