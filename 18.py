l = [[1,2,3],['a','b','c',],[True,False]]
def combination(o_comb, index):
    if index==len(l):
        print(o_comb,)
        return
    for lis in l[index]:
        new_comb = o_comb + [lis]
        combination(new_comb,index+1)
combination([],0)

