F_list = [1,2,3,4,5]
I_list = [1]

n_d = 5
D = range(1,n_d + 1)
D = list(D)

n_r = 5
R = range(1,n_r + 1)
R = list(R)

n_l = 1
L = range(1, n_l + 1)
L = list(L)

nic = 1
P = range(1, nic + 1)
P = list(P)
c = 1

B = [1]

# F[(d,b)] = needed fertillizer for batch b on day d
F = {
    (1,1):1,
    (2,1):2,
    (3,1):3,
    (4,1):4,
    (5,1):5,       
}

# nc[(d,b)] = number of containers of batch b on day d
nc = {
    (1,1):1,
    (2,1):1,
    (3,1):1,
    (4,1):1,
    (5,1):1,       
}

# I[(d,b)] = needed irrigation for batch b on day d
I = {
    (1,1):1,
    (2,1):1,
    (3,1):1,
    (4,1):1,
    (5,1):1,  
}
