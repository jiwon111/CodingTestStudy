def solution(s, n):
    answer = ''
    for i in range(0, len(s)):
        if s[i] == ' ':
            answer+= ' '
        else:
            if ord(s[i])+n>ord('Z') and ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'):
                answer += chr(ord('A')+n-(ord('Z')-ord(s[i]))-1)
            elif ord(s[i])+n>ord('z') and ord(s[i])>=ord('a') and ord(s[i])<=ord('z'):
                answer += chr(ord('a')+n-(ord('z')-ord(s[i]))-1)
            else:
                answer += chr(ord(s[i])+n)
    return answer