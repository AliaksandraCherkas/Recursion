# def palindrom(s):
#     if len(s) in (1,0):
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrom(s[1:-1])
# print(palindrom('sassas')) 


# def rec_string(s):
#     if len(s) < 3:
#         return s
#     return s[0] + '(' + rec_string(s[1:-1])+ ')'+ s[-1]
    
# print(rec_string('sasdfghjklzxcvbhnjkl'))

# def rec_star(s):
#     if len(s) ==1:
#         return s
#     return s[0] + '*' + rec_star(s[1:])
    
# print(rec_star('sasdfghjklzxcvbhnjkl'))


def rec_mirror(s):
    if len(s) ==1:
        return s if s != '(' else ')'
    return ')' + rec_mirror(s[:-1]) if s[-1] == '(' else s[-1] + rec_mirror(s[:-1])
    
# print(rec_mirror('(((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqo'))


def rec(x):
    if len(x)==1:
        if x!="(":
            return x+x
        return "()"
    if x[0]!="(":
        return x[0]+ rec(x[1:])+x[0]
    return "(" + rec(x[1:])+ ")"
x=input()
print(rec(x))