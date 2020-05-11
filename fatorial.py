
#Script que calcula o fatoria de um número
  


def fact1(n):
    assert n >= 0 
    
    f=1
    for i in range(1,n+1): 
        f = f * i 
    return f

def fact2(n):
    assert n >= 0 
    
    f=1
    for i in range(1,n+1): 
        f = f * i 
    return f

def fatorial(n):

    assert n >= 0 

    if(n>0):
        f = n*fatorial(n-1)
    else:
        f = 1 
    return f 

def fatorial(n):

    assert n >= 0 

    if(n>0):
        f = n*fatorial(n-1)
    else:
        f = 1 
    return f 
    


def main():
    for i in range(0,20):
        print('Fatorial de '+str(i) +' é ' + str(fact1(i)) + ', e também deve ser '+ str(fatorial(i)))



if __name__ == "__main__":
    main()




