def ft_reduce(funct, inputs):
    rep = inputs[0]
    for i in inputs[1:]:
        rep = funct(rep, i)
    return rep

def addboth(nb1, nb2):
    return (nb1 + nb2)

lst = [1, 1, 1, 42, 1, 1, 1]
print(ft_reduce(addboth, lst))
