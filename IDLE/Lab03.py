#Nome: Yurih Santos de Oliveira
#DRE: 121056855

from math import*

#1a
def maximo(x,y,z):
    "função que acha o valor máximo dentre três; int,int,int -> int"
    return max(x,y,z)

def minimo(x,y,z):
    "função que acha o valor máximo dentre três; int,int,int -> int"
    return min(x,y,z)

#1b
def media(x,y,z):
    "função que calcula a média de três números; int,int,int -> float"
    return (x+y+z)/3

#1c
def media_max(x,y,z):
    "função que faz a diferença do termo maior termo com a média; int,int,int -> float"
    return max(x,y,z) - media(x,y,z)

#1d
def media_min(x,y,z):
    "função que faz a soma do maior termo com a média; int,int,int -> float"
    return max(x,y,z) + media(x,y,z)

#2a
def delta(a,b,c):
    "função que calcula o discriminante de uma equação do segundo grau; int,int,int -> int"
    return b**2 - 4*a*c

#2b
def raiz_x1(a,b,c):
    "função que calcula a raiz positiva de uma equação do segundo grau; int,int,int -> float"
    return (-b + sqrt(delta(a,b,c)))/(2*a)

#2c
def raiz_x2(a,b,c):
    "função que calcula a raiz negativa de uma equação do segundo grau; int,int,int ->float"
    return (-b - sqrt(delta(a,b,c)))/(2*a)

#3b
def PA(a1,n,r):
    "função que define o termo geral de uma P.A; int,int,int -> int"
    return a1+(n-1)*r

#3c
def PA_soma(a1,an,n):
    "função que define a soma dos termos de uma PA; int,int,int -> float"
    return ((a1+an)*n)/2

#4a
def distancia(x1,y1,x2,y2):
    "calcula a distância entre dois pontos, A(x1,y1) e B(x2,y2); int,int,int,int -> float"
    return sqrt((x2-x1)**2+(y2-y1)**2)

#4b
def perimetro_tri(A,B):
    "calcula o perímetro de um triângulo reto dados dois catetos; int,int -> float"
    return A+B+sqrt(A**2 + B**2)

#4c
def rel_fun(x):
    "calcula a relação fundamental da trigonometria; int -> int"
    return sin(x)**2 +cos(x)**2

#5
def setorc(r,a=2*pi):
    "calcula a área de um setor circular dados o ângulo e o raio da circunferência; int,float ->float"
    return (a*r**2)/2