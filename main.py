def fill_L(rules):
    '''Build dictionary for L(U)'''
    L = {}

    # step 1
    for key in rules:
        for elemInList in RULES[key]:
            if key in L:
                if elemInList[:1] not in L[key]:
                 L[key].append(elemInList[:1])
            else:
                L[key] = list(elemInList)[:1]

    # the remaining steps
    for key in L:
        for elemInList in L[key]:
            if elemInList != key and elemInList in NONTERM:
                for elem in L[elemInList]:
                    if elem not in L[key]:
                        L[key].append(elem)
    return L

def fill_R(rules):
    '''Build dictionary for R(U)'''
    R = {}

    # step 1
    for key in rules:
        for elemInList in RULES[key]:
            if key in R:
                if elemInList[-1:] not in R[key]:
                    R[key].append(elemInList[-1:])
            else:
                R[key] = list(elemInList)[-1:]

    # the remaining steps
    for key in R:
        for elemInList in R[key]:
            if elemInList != key and elemInList in NONTERM:
                for elem in R[elemInList]:
                    if elem not in R[key]:
                        R[key].append(elem)
    return R

def main():
    L = fill_L(RULES)
    R = fill_R(RULES)
    print (L)
    print (R)

if __name__ == '__main__':

    # initialization

    RULES = {'A' : ['!B!'], 'B' : ['B+T', 'T'], 'T' : ['T*M', 'M'], 'M' : ['I', '(B)']}
    # NUMBER_ALT = {'B': 2, 'T': 2, 'M': 2}
    TERM = {'!', '(', ')', '+', '*', 'a', 'b'}
    NONTERM = {'A', 'B', 'T', 'M'}
    First_PLACE_in_RULES = {'A' : 1, 'B': 2, 'T': 4, 'M': 6}

    STR = '!(a+b)*c!'

    main()
