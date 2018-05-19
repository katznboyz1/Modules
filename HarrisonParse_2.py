class __parser__():
    def __count__(string, letter):
        v1 = 0
        for i in letter: v1 += 1
        if v1 != 1: raise SyntaxError('[arg] must be a singular character.')
        v2 = -1
        for i in string: v2 += 1
        v3 = 0
        for i in range(v2):
            if string[i] == letter: v3 += 1
        return  v3
    def __deletelast__(string):
        old = string
        new = ''
        v1 = -1
        for i in old: v1 += 1
        for i in range(v1): new = str(new) + old[i]
        return new
    def __lower__(string):
        old = string
        new = ''
        uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        v1 = 26
        for a in old:
            for b in range(26):
                if a == uppers[(b - 1)]: new = str(new) + lowers[(b - 1)]
                if a == lowers[(b - 1)]: new = str(new) + lowers[(b - 1)]
        return new
    def __capitalize__(string):
        old = string
        new = ''
        uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        v1 = 26
        try:
            for a in range(26):
                if old[0] == lowers[(a - 1)]: new = str(new) + uppers[(a - 1)]
            v2 = 2
            for b in old: v2 += 1
            for c in range(v2): new = str(new) + old[(c + 1)]
        except IndexError: None
        return new
    def __reversecase__(string):
        old = string
        new = ''
        uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        v1 = 0
        for a in old:
            for b in range(26):
                if a == lowers[(b - 1)]:
                    new = str(new) + uppers[(b - 1)]
                    v1 += 1
                elif a == uppers[(b - 1)]:
                    new = str(new) + lowers[(b - 1)]
                    v1 += 1
            if a not in uppers and a not in lowers:
                new = str(new) + str(a)
                v1 += 1
        return new

