str = "bababaabaabaaabbbaaababbbbabbaaabaaababbababbbabbbaaabbabbbaabbabaabaababbbaababaabaaababbababbabbbababbababbbaabbbaaaaaaaabaababaaabaabaaabbabbbbaabbaabbbaabaababbbbaabaaabaaaaababaaabaabaabaabbbabbbababaaabaabbaaababbaabbbabaaabaaabbbabbbabaaabaabababbbbaaababbbbababbabaaabaaabaabaaaaaaaabbbaaaaaaabbabaabbaabbabbabbbbabbbabababababaabababababbababaabababaabbababbbababaababbbababaababbabbabaababababbababbababaabaaababbabbabbabbababababaabababbabaababbabbaabaababababaababababaabaababbabababababbababababbbababbabababbabaabaababbababaabbabababbaabaabbabbaabaabbaabaabababababbababababaababababaabaababababaabbababababbaabaabaababaabababbabaabababbaabaababaabababaababbaababababaabbabbabababababbababababababababbaabababaabbababaabaabbbaaabaabababbabbababababaabababaabababbaababababababababababababaabbabbababbabababbaababababbabaabbbabbababababababababaabbabababaababbbabaababababbabababaabbabaababbaabababaabaababababbababababaabababbaabababaabaabababaababbababaabaababababbabababababababbabbabaababababaabaabbabaabaabaababaabababababaabababaababababbbababababbabababababbabababababbabababbabbababbabababbabaababbababaabaabababababaababababbaabbabaabbbabbabbababbaababaabaababababaabbaabababababaababaabbabbaababababaabababababababbabababababbaababababbabababbabbabababbaabaababaabababbabbaababbaababaabaabababababaabababbabababbaabababababaabababbaababaababababbababbabababbabbaabbabbababbabbabaabaababababbbababaabababaabbabaabaababbababab"
cnt = 0
unit = ""
list = []
text = ""
for i in str:
    if cnt >= 5:
        list.append(unit)
        cnt = 0
        unit = ""
    cnt += 1
    unit += i

for i in list:
    if i=='aaaaa':
        text+='a'
    elif i=='aaaab':
        text+='b'
    elif i=='aaaba':
        text+='c'
    elif i=='aaabb':
        text+='d'
    elif i=='aabaa':
        text+='e'
    elif i=='aabab':
        text+='f'
    elif i=='aabba':
        text+='g'
    elif i=='aabbb':
        text+='h'
    elif i=='abaaa':
        text+='i'
    elif i=='abaab':
        text+='j'
    elif i=='ababa':
        text+='k'
    elif i=='ababb':
        text+='l'
    elif i=='abbaa':
        text+='m'
    elif i=='abbab':
        text+='n'
    elif i=='abbba':
        text+='o'
    elif i=='abbbb':
        text+='p'
    elif i=='baaaa':
        text+='q'
    elif i=='baaab':
        text+='r'
    elif i=='baaab':
        text+='s'
    elif i=='baabb':
        text+='t'
    elif i=='babaa':
        text+='u'
    elif i=='babab':
        text+='v'
    elif i=='babba':
        text+='w'
    elif i=='babbb':
        text+=' ' #x
    elif i=='bbaaa':
        text+='y'
    elif i=='bbaab':
        text+='z'
    else:
        print(i)

print(text)
