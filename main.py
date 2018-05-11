def fill_L():
    '''Build dictionary for L(U)'''
    L = {}

    # step 1
    for key in RULES:
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

def fill_R():
    '''Build dictionary for R(U)'''
    R = {}

    # step 1
    for key in RULES:
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

def fill_L_t():
    '''Build dictionary for L_t (U)'''
    L = fill_L()
    L_t = {}

    # step 1
    for key in RULES:
        for elemInList in RULES[key]:
            if key in L_t:
                for symbol in elemInList:
                    if symbol in TERM:
                        L_t[key].append(symbol)
                        break
            else:
                for symbol in elemInList:
                    if symbol in TERM:
                        L_t[key] = list(symbol)
                        break

    # step 2
    for key in L_t:
        for elemInList in L[key]:
            if elemInList in NONTERM and elemInList != key:
                for i in L_t[elemInList]:
                    if i not in L_t[key]:
                        L_t[key].append(i)
    return L_t

def fill_R_t():
    '''Build dictionary for R_t (U)'''
    R = fill_R()
    R_t = {}

    # step 1
    for key in RULES:
        for elemInList in RULES[key]:
            if key in R_t:
                for symbol in reversed(elemInList):
                    if symbol in TERM:
                        R_t[key].append(symbol)
                        break
            else:
                for symbol in elemInList:
                    if symbol in TERM:
                        R_t[key] = list(symbol)
                        break

    # step 2
    for key in R_t:
        for elemInList in R[key]:
            if elemInList in NONTERM and elemInList != key:
                for i in R_t[elemInList]:
                    if i not in R_t[key]:
                        R_t[key].append(i)
    return R_t

def main():
    L_t = fill_L_t()
    R_t = fill_R_t()
    print (L_t)
    print (R_t)

if __name__ == '__main__':

    # initialization

    RULES = {'A' : ['!B!'], 'B' : ['B+T', 'T'], 'T' : ['T*M', 'M'], 'M' : ['I', '(B)']}
    # NUMBER_ALT = {'B': 2, 'T': 2, 'M': 2}
    TERM = {'!', '(', ')', '+', '*', 'I'}
    NONTERM = {'A', 'B', 'T', 'M'}
    First_PLACE_in_RULES = {'A' : 1, 'B': 2, 'T': 4, 'M': 6}

    STR = '!(a+b)*c!'

    main()