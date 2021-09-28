def pitagoras():
    a= int(input('cateto:'))
    b=int(input('cateto:'))
    h = ((a**2)+ (b**2))**(1/2)
    print(h)

def egrau():
    a=int(input('valor de a:'))
    b=int(input('valor de b:'))
    c=int(input('valor de c:'))
    if c==0:
        r= -(b/a)
        print(f'x1= 0 e x2= {r:.2f}')
    elif b==0:
        r=(-c/a)**(1/2)
        print(f' x=+/- {r:.2f} ')
    else:
        d=b**2-(4*a*c)
        if d>0:
            r1= (-b+((d)**(1/2)))/(2*a)
            r2= (-b-((d)**(1/2)))/(2*a)
            print(f'x1= {r1} e x2= {r2}')
        else:
            print('n possui raiz')

def soma(a, b):
    return (a+b)
a=5
b=5
egrau()
