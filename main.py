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

def MOP():
    '''Using the dictionaries, L_t and R_t, construct the operator precedence matrix - mop{}'''
    mop = {}
    L_t = fill_L_t()
    R_t = fill_R_t()

    # fill =
    for leftInRules in RULES:
        for right in RULES[leftInRules]:
            if len(right) == 3 and right[0] in TERM and right[2] in TERM:
                mop[(right[0]), (right[2])] = '='

    # fill <
    for leftInRules in RULES:
        for right in RULES[leftInRules]:
            if len(right) >= 2:
                for i in range(len(right) - 1):
                    if right[i] in TERM and right[i+1] in NONTERM:
                        for elementInL_t in L_t[right[i+1]]:
                            mop[right[i], elementInL_t] = '<'

    # fill >
    for leftInRules in RULES:
        for right in RULES[leftInRules]:
            if len(right) >= 2:
                for i in range(len(right) - 1):
                    if right[i] in NONTERM and right[i + 1] in TERM:
                        for elementInR_t in R_t[right[i]]:
                            mop[elementInR_t, right[i + 1]] = '>'

    return mop

def main():
    L_t = fill_L_t()
    R_t = fill_R_t()
    print (L_t)
    print (R_t)
    mop = MOP()
    print(mop)

if __name__ == '__main__':

    # initialization

    RULES = {'A' : ['!B!'], 'B' : ['B+T', 'T'], 'T' : ['T*M', 'M'], 'M' : ['I', '(B)']}
    # NUMBER_ALT = {'B': 2, 'T': 2, 'M': 2}
    TERM = {'!', '(', ')', '+', '*', 'I'}
    NONTERM = {'A', 'B', 'T', 'M'}
    First_PLACE_in_RULES = {'A' : 1, 'B': 2, 'T': 4, 'M': 6}

    STR = '!(a+b)*c!'

    main()