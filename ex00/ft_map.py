def ft_map(funct, inputs):
    rep = []
    for i in inputs:
        rep.append(funct(i))
    return rep

# def testf(tomult):
#     return tomult * 3

# lst = [2, 6, 12, 42, 69]
# print(ft_map(testf, lst))
