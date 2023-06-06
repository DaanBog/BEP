F_list = [1,2,3]
I_list = [1,2]

n_d = 5
D = range(1,n_d + 1)
D = list(D)

n_r = 8
R = range(1,n_r + 1)
R = list(R)

n_l = 6
L = range(1, n_l + 1)
L = list(L)

nic = 2
P = range(1, nic + 1)
P = list(P)
c = 15

B = [1,2]

# F[(d,b)] = needed fertillizer for batch b on day d
F = {
    (1,1):1,
    (2,1):1,
    (3,1):2,
    (4,1):2,
    (5,1):3,    
    
    (1,2):1,
    (2,2):1,
    (3,2):2,
    (4,2):3,
    (5,2):3,
}

# nc[(d,b)] = number of containers of batch b on day d
nc = {
    (1,1):1,
    (2,1):1,
    (3,1):2,
    (4,1):2,
    (5,1):3,    
    
    (1,2):1,
    (2,2):1,
    (3,2):2,
    (4,2):3,
    (5,2):3,
}

# I[(d,b)] = needed irrigation for batch b on day d
I = {
    (1,1):1,
    (2,1):1,
    (3,1):2,
    (4,1):2,
    (5,1):2,    
    
    (1,2):1,
    (2,2):1,
    (3,2):2,
    (4,2):2,
    (5,2):2,
}
