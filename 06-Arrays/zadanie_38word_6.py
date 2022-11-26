def create_2d_arr(x,y):
    #b=[[ , , ],[ , , ],[ , , ],[ , , ],[ , , ]]
    z=[]
    s=[]
    for i in range(x):
        z.append(0)
    for j in range(y):
        s.append(z)
    return s   
            
            





print(create_2d_arr(3,5))