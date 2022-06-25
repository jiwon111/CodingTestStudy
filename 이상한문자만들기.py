def solution(s):
    answer = ''
    idx = 0
    for i in range(len(s)):
        if s[i]!=' ' and (i-idx)%2==0:
            answer+=s[i].upper()
        elif s[i]!=' ' and (i-idx)%2==1:
            answer+=s[i].lower()
        elif s[i]==' ':
            answer+=' '
            idx=i+1
    return answer
s = 'abc abc  abc   abc'
solution(s)