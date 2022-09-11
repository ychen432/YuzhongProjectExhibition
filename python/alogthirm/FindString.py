string1='abc'
string2='scdabchtbohqcbadh'
answer=[]
len
for i in range (len(string2)):
    if string2[i]==string1[0]:
        if string2[i:(i+len(string1))]==string1:
            answer.append(i)
    if string2[i]==string1[-1]:
        if string2[i:(i+len(string1))]==string1[::-1]:
            answer.append(i)

print(answer)

"find index of string1 in the string2 (abc and cba)"

    
                   
                   






