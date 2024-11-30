string='pranav you are best from best improve yourself regullary'

ele={}

for ch in string:
    if ch in ele:
        ele[ch]=ele[ch]+1
    else:
        ele[ch]=1

print(ele)
