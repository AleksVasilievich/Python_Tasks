def is_one_away(word1, word2):
    count = 0
    ind = -1
    
    if len(txt1) != len(txt2) or txt1 == txt2:
        return False
    else:
        len_txt = len(txt1)
        while len_txt != 0:
            ind +=1
            if txt1[ind] != txt2[ind]:
                count +=1
                # ind +=1
            len_txt = len_txt - 1

        if count < 2:
            return True
        else:
            return False
    

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))