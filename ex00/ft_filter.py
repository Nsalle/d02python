def ft_filter(funct, inputs):
    rep = []
    for i in inputs:
        if funct(i) is True:
            rep.append(i)
    return rep

# def is_even(nb):
#     if nb % 2 == 0:
#         return True
#     else:
#         return False

# lst = [1, 2, 4, 8, 7, 6, 11, 12, 99, 69, 42]
# print(ft_filter(is_even, lst))
