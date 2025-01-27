def countvowelsndconsonant(a):
    v="aeiou"
    vc=0 #vowelscount
    cc=0 #consonantcount
    for i in a.lower():
        if i.isalpha():
            #if i is letter then
           if i in v:
               #if vowel add 1 or add consonant 1
                vc+=1
           else:
                cc +=1
    print(f'vowels : {vc}')
    print(f'consonants : {cc}')
countvowelsndconsonant("aaaaa")
