a = [1,[3,6,[1,2,[2,3,[3]]],1,2,3,4,[4,5,6],7,9],2,34,[4,5,7,[3,4,6,7]]]
def rec(s, level =1):
   
    print(*s, f'level = {level}')
    for i in s:
        # print(i, type(i))
        if isinstance(i,list):
           
            rec(i, level+1)


rec(a)