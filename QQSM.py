import time
import turtle
from random import *
from random import sample
import random
from threading import Timer




#Declarar la pantalla

wn=turtle.Screen()
wn.setup(1000,600)
wn.colormode(255)
wn.bgcolor(0,0,10)
wn.title("Quien quiere ser millonario")



#Construyendo boxes
#C
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-450,-250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.color("blue")
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()    

#D
turtle.penup()
turtle.goto(25,-250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()    

#A
turtle.penup()
turtle.goto(-450, -75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()    

#B
turtle.penup()
turtle.goto(23,-75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()    

#Question box
turtle.penup()
turtle.goto(-450,100)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(625)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()

#Score
turtle.penup()
turtle.goto(225,100)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(225)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()

#Time
turtle.penup()
turtle.goto(-700,100)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(225)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()
    
#Creación de Pregunta
quest=turtle.Turtle()    
quest.speed(0)
quest.hideturtle()
quest.penup()
quest.goto(-425,150)

#Creación del Score
score1=turtle.Turtle()
score1.speed(0)
score1.hideturtle()
score1.penup()
score1.goto(250,125)

#Creación del TIMER

timeview=turtle.Turtle()
timeview.speed(0)
timeview.hideturtle()
timeview.penup()
timeview.goto(-620,160)



#Creación Boton de publico

tr = turtle.Turtle()
wn = turtle.Screen()
wn.addshape('people.gif')
tr.shape('people.gif')
tr.goto(-400,-300)

tr1 = turtle.Turtle()
wn1 = turtle.Screen()
wn1.addshape('5050.gif')
tr1.shape('5050.gif')
tr1.goto(0,-300)

tr3 = turtle.Turtle()
wn3 = turtle.Screen()
wn3.addshape('phone.gif')
tr3.shape('phone.gif')
tr3.goto(400,-300)

tr4 = turtle.Turtle()
wn4 = turtle.Screen()
wn4.addshape('1.gif')
tr4.shape('1.gif')
tr4.goto(700,0)

tr5= turtle.Turtle()
wn5=turtle.Screen()
wn5.addshape('time.gif')
tr5.shape('time.gif')
tr5.goto(-620,-200)



#Creación de respuestas

#A
A=turtle.Turtle()
A.speed(0)
A.hideturtle()
A.penup()
A.goto(-425,-50)

#B
B=turtle.Turtle()
B.speed(0)
B.hideturtle()
B.penup()
B.goto(50,-50)

#C
C=turtle.Turtle()
C.speed(0)
C.hideturtle()
C.penup()
C.goto(-425,-225)

#D
D=turtle.Turtle()
D.speed(0)
D.hideturtle()
D.penup()
D.goto(50,-225)

#Opening Credits
quest.write("Bienvenidos a Quien quiere ser millonario", font=("Verdana",15,"bold"))
time.sleep(2)
quest.clear()

quest.write("Presiona A B C D, para responder", font=("Verdana",15,"bold"))
time.sleep(2)
quest.clear()

quest.write("Presiona Z X V T, para elegir los comodines", font=("Verdana",15,"bold"))
time.sleep(2)
quest.clear()

quest.write("Buena suerte", font=("Verdana",15,"bold"))
time.sleep(2)
quest.clear()

#Numero de preguntas correctas
correctNow=0
score1.write("{}".format(correctNow),font=("Verdana",62,"bold"))

#Variables
CurrentQ=1

#TIMER FUNCIÓN
def contador():
    global rango
    for i in range(1,rango):
        time.sleep(1)
        timeview.clear()
        timeview.write(rango-i,font=("Verdana",40,"bold"))
    quest.clear()
    quest.write("Se acabo el tiempo vuelve a jugar",font=("Verdana",15,"bold"))
    time.sleep(5)
    turtle.bye()
     

#Key Funciones
def chooseAnswerA():
    global select
    select= 'A'
    evaluate()

def chooseAnswerB():
    global select
    select='B'
    evaluate()

def chooseAnswerC():
    global select
    select='C'
    evaluate()

def chooseAnswerD():
    global select
    select='D'
    evaluate()        

def incorrec1():
    incorrectn.clear()
    incorrectz.clear()
    trx = turtle.Turtle()
    wnx = turtle.Screen()
    wnx.addshape('5050x.gif')
    trx.shape('5050x.gif')
    trx.goto(0,-300)

def phonecall():
    global CurrentQ
    global correctNow
    tr3x = turtle.Turtle()
    wn3x = turtle.Screen()
    wn3x.addshape('Phonex.gif')
    tr3x.shape('Phonex.gif')
    tr3x.goto(400,-300)
    quest.clear()
    score1.clear()
    correctNow += 1
    clearimg()
    score1.write("{}".format(correctNow),font=("Verdana",62,"bold"))
    scoreimg()
    CurrentQ = randrange(2,68)
    clearBoard()
    GetQuestionNum()
    if correctNow ==15:
        win()
    
    

def cincuenta():
    incorrec1()

def moretime():
    global rango
    rango=rango+rango
    tr5x= turtle.Turtle()
    wn5x=turtle.Screen()
    wn5x.addshape('timex.gif')
    tr5x.shape('timex.gif')
    tr5x.goto(-620,-200)    

def publico():
    quest.clear()
    global metodo
    global questask
    quest.write(metodo,font=("Verdana",15,"bold"))
    time.sleep(1.2)
    quest.clear()
    quest.write(questask,font=("Verdana",15,"bold"))

    trxx = turtle.Turtle()
    wnxx = turtle.Screen()
    wnxx.addshape('peoplex.gif')
    trxx.shape('peoplex.gif')
    trxx.goto(-400,-300)

def scoreimg():
    if correctNow == 1:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('2.gif')
       tr41.shape('2.gif')
       tr41.goto(700,0)     
    if correctNow == 2:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture2.gif')
       tr41.shape('Picture2.gif')
       tr41.goto(700,0)  
    if correctNow == 3:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture3.gif')
       tr41.shape('Picture3.gif')
       tr41.goto(700,0)  
    if correctNow == 4:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture4.gif')
       tr41.shape('Picture4.gif')
       tr41.goto(700,0)  
    if correctNow == 5:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture5.gif')
       tr41.shape('Picture5.gif')
       tr41.goto(700,0)  
    if correctNow == 6:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture6.gif')
       tr41.shape('Picture6.gif')
       tr41.goto(700,0)  
    if correctNow == 7:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture7.gif')
       tr41.shape('Picture7.gif')
       tr41.goto(700,0)  
    if correctNow == 8:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture8.gif')
       tr41.shape('Picture8.gif')
       tr41.goto(700,0)  
    if correctNow == 9:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture9.gif')
       tr41.shape('Picture9.gif')
       tr41.goto(700,0)  
    if correctNow == 10:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture10.gif')
       tr41.shape('Picture10.gif')
       tr41.goto(700,0)  
    if correctNow == 11:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture11.gif')
       tr41.shape('Picture11.gif')
       tr41.goto(700,0)  
    if correctNow == 12:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture12.gif')
       tr41.shape('Picture12.gif')
       tr41.goto(700,0)  
    if correctNow == 13:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture13.gif')
       tr41.shape('Picture13.gif')
       tr41.goto(700,0)  
    if correctNow == 14:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture14.gif')
       tr41.shape('Picture14.gif')
       tr41.goto(700,0)  
    if correctNow == 15:
       tr41 = turtle.Turtle()
       wn41 = turtle.Screen()
       wn41.addshape('Picture15.gif')
       tr41.shape('Picture15.gif')
       tr41.goto(700,0)              

def win():
     if correctNow == 15:
           quest.clear()
           quest.write("Felicidades has ganado!",font=("Verdana",23,"bold"))
           time.sleep(1.2)
           turtle.bye()
                               

def evaluate():
    global correct
    global correctNow
    global CurrentQ
    if correct == select:
        quest.clear()
        quest.write("Correcto!",font=("Verdana",15,"bold"))
        time.sleep(1.2)
        score1.clear()
        correctNow += 1
        score1.write("{}".format(correctNow),font=("Verdana",62,"bold"))
        scoreimg()
        clearimg()
        if correctNow == 15:
           quest.clear()
           quest.write("Felicidades has ganado!",font=("Verdana",23,"bold"))
           time.sleep(1.2)
           turtle.bye()
    else:
        quest.clear()
        quest.write("Incorrecto, la respuesta era {}".format(correct),font=("Verdana",23,"bold"))
        time.sleep(1.2)
        quest.clear()
        quest.write("Juega pronto",font=("Verdana",23,"bold"))
        time.sleep(1.2)
        turtle.bye()
    CurrentQ = randrange(2,68)
    clearBoard()
    GetQuestionNum()

def clearimg():
    tr6.hideturtle()

def GetQuestionNum():
    if CurrentQ == 2:
        question2()
    if CurrentQ == 3:
        question3()    
    if CurrentQ == 4:
        question4()   
    if CurrentQ == 5:
        question5()   
    if CurrentQ == 6:
        question6()   
    if CurrentQ == 7:
        question7() 
    if CurrentQ == 8:
        question8() 
    if CurrentQ == 9:
        question9() 
    if CurrentQ == 10:
        question10()                             
    if CurrentQ == 11:
        question11()        
    if CurrentQ == 12:
        question12()    
    if CurrentQ == 13:
        question13()
    if CurrentQ == 14:
        question14()   
    if CurrentQ == 15:
        question15()
    if CurrentQ == 16:
        question16()
    if CurrentQ == 17:
        question17()                        
    if CurrentQ == 18:
        question18()
    if CurrentQ == 19:
        question19()
    if CurrentQ == 20:
        question20()
    if CurrentQ == 21:
        question21()         
    if CurrentQ == 22:
        question22() 
    if CurrentQ == 23:
        question23() 
    if CurrentQ == 24:
        question24() 
    if CurrentQ == 25:
        question25()
    if CurrentQ == 26:
        question26()   
    if CurrentQ == 27:
        question27()
    if CurrentQ == 28:
        question28()             
    if CurrentQ == 29:
        question29()
    if CurrentQ == 30:
        question30()      
    if CurrentQ == 31:
        question31()   
    if CurrentQ == 32:
        question30()   
    if CurrentQ == 33:
        question33()   
    if CurrentQ == 34:
        question34()   
    if CurrentQ == 35:
        question35()   
    if CurrentQ == 36:
        question36()   
    if CurrentQ == 37:
        question37()   
    if CurrentQ == 38:
        question38()   
    if CurrentQ == 39:
        question39()   
    if CurrentQ == 40:
        question40()   
    if CurrentQ == 41:
        question41()  
    if CurrentQ == 42:
        question42()  
    if CurrentQ == 43:
        question43()  
    if CurrentQ == 44:
        question44()  
    if CurrentQ == 45:
        question45()  
    if CurrentQ == 46:
        question46()  
    if CurrentQ == 47:
        question47()  
    if CurrentQ == 48:
        question48()  
    if CurrentQ == 49:
        question49()  
    if CurrentQ == 50:
        question50()  
    if CurrentQ == 51:
        question51()
    if CurrentQ == 52:
        question52()    
    if CurrentQ == 53:
        question53()
    if CurrentQ == 54:
        question54()
    if CurrentQ == 55:
        question55()
    if CurrentQ == 56:
        question56()
    if CurrentQ == 57:
        question57()
    if CurrentQ == 58:
        question58()
    if CurrentQ == 59:
        question59()
    if CurrentQ == 60:
        question60()
    if CurrentQ == 61:
        question61()
    if CurrentQ == 62:
        question62()
    if CurrentQ == 63:
        question63()
    if CurrentQ == 64:
        question64()
    if CurrentQ == 65:
        question65()
    if CurrentQ == 66:
        question66()
    if CurrentQ == 67:
        question67()
    if CurrentQ == 68:
        question68()  



def clearBoard():
    quest.clear()
    A.clear()
    B.clear()    
    C.clear()
    D.clear()

#--------------------------------------------------------------inicio de preguntas---------------------------------------------------------------------------------------------------------#    

def question1(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de {x2?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de {x2?")
    A.write("a. 5",font=("Verdana",23,"bold"))
    B.write("b. 2.34",font=("Verdana",23,"bold"))
    C.write("c. 29.49",font=("Verdana",23,"bold"))
    D.write("d. 8.123",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/1.gif')
    tr6.shape('Problema GIF/1.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= D
    rango=300
    metodo=("Matriz Cuadratica")
    correct='C'
    contador()
    

def question2(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de {x^2y?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de {x^2y?")
    A.write("a. 4.32",font=("Verdana",23,"bold"))
    B.write("b. 84.598",font=("Verdana",23,"bold"))
    C.write("c. 19.29",font=("Verdana",23,"bold"))
    D.write("d. 25.45",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/2.gif')
    tr6.shape('Problema GIF/2.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= C
    rango=300
    correct='B'
    metodo=("Matriz Cuadratica")
    contador()   
    

def question3(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de {x^4?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de {x^2y?")
    A.write("a. 6.78",font=("Verdana",23,"bold"))
    B.write("b. 10.23",font=("Verdana",23,"bold"))
    C.write("c. 219.2338",font=("Verdana",23,"bold"))
    D.write("d. 220.2338",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/3.gif')
    tr6.shape('Problema GIF/3.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= C
    rango=300
    metodo=("Matriz Cubica")    
    correct='D'
    contador()   
  
  
def question4(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de {x^2y?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de {x^2y?")
    A.write("a. 6.7070",font=("Verdana",23,"bold"))
    B.write("b. 700.6020",font=("Verdana",23,"bold"))
    C.write("c. 716.64274",font=("Verdana",23,"bold"))
    D.write("d. 23.123123",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/4.gif')
    tr6.shape('Problema GIF/4.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= B
    rango=300
    metodo=("Matriz Cubica")    
    correct='C'
    contador()   

def question5(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de {f(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de {f(x)?")
    A.write("a. -.1416043",font=("Verdana",23,"bold"))
    B.write("b. 7010.60",font=("Verdana",23,"bold"))
    C.write("c. 723.644274",font=("Verdana",23,"bold"))
    D.write("d. 232.43123",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/5.gif')
    tr6.shape('Problema GIF/5.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=300
    metodo=("Lineal con función")    
    correct='A'
    contador()      

def question6(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de {yf(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de {yf(x)?")
    A.write("a. -.14163443",font=("Verdana",23,"bold"))
    B.write("b. .3690062",font=("Verdana",23,"bold"))
    C.write("c. 23.22424",font=("Verdana",23,"bold"))
    D.write("d. 212.2323",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/6.gif')
    tr6.shape('Problema GIF/6.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=300
    metodo=("Lineal con función")    
    correct='B'
    contador()     

def question7(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de {f(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de {f(x)?")
    A.write("a. .59099133",font=("Verdana",23,"bold"))
    B.write("b. .3565",font=("Verdana",23,"bold"))
    C.write("c. 29.2224",font=("Verdana",23,"bold"))
    D.write("d. .23223323",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/7.gif')
    tr6.shape('Problema GIF/7.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= D
    rango=300
    metodo=("Cuadratica con función")    
    correct='A'
    contador()         

def question8(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de {x^2f(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de {x^2f(x)?")
    A.write("a. 4.1000234",font=("Verdana",23,"bold"))
    B.write("b. .23445",font=("Verdana",23,"bold"))
    C.write("c. 200.223",font=("Verdana",23,"bold"))
    D.write("d. 256.257",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/8.gif')
    tr6.shape('Problema GIF/8.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= C
    rango=300
    metodo=("Cuadratica con función")    
    correct='D'
    contador()       

def question9(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de c?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de c?")
    A.write("a. 66/87",font=("Verdana",23,"bold"))
    B.write("b. 32/87",font=("Verdana",23,"bold"))
    C.write("c. 12/87",font=("Verdana",23,"bold"))
    D.write("d. 10/87",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/9.gif')
    tr6.shape('Problema GIF/9.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= C
    rango=600
    metodo=("Metodo Montante")    
    correct='A'
    contador()     

def question10(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de A?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de A?")
    A.write("a. 800/216",font=("Verdana",23,"bold"))
    B.write("b. 5/78",font=("Verdana",23,"bold"))
    C.write("c. 801/215",font=("Verdana",23,"bold"))
    D.write("d. 10/200",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/10.gif')
    tr6.shape('Problema GIF/10.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= D
    rango=600
    metodo=("Metodo Montante")    
    correct='C'
    contador()        

def question11(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de A?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de A?")
    A.write("a. 545/87",font=("Verdana",23,"bold"))
    B.write("b. 600/800",font=("Verdana",23,"bold"))
    C.write("c. -681/91",font=("Verdana",23,"bold"))
    D.write("d. 681/91",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/11.gif')
    tr6.shape('Problema GIF/11.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= D
    rango=600
    metodo=("Gauss Jordan")    
    correct='C'
    contador()

def question12(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de B?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de B?")
    A.write("a. 2397/701",font=("Verdana",23,"bold"))
    B.write("b. 898/87",font=("Verdana",23,"bold"))
    C.write("c. -681/10",font=("Verdana",23,"bold"))
    D.write("d. 78/54",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/12.gif')
    tr6.shape('Problema GIF/12.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= D
    rango=600
    metodo=("Gauss Jordan")    
    correct='A'
    contador()    

   

def question13(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de A?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de A?")
    A.write("a. 23/24",font=("Verdana",23,"bold"))
    B.write("b. 54/16",font=("Verdana",23,"bold"))
    C.write("c. 800/176",font=("Verdana",23,"bold"))
    D.write("d. 977/176",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/13.gif')
    tr6.shape('Problema GIF/13.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= A
    rango=600
    metodo=("Eliminación Gaussiana")    
    correct='D'
    contador() 

           

def question14(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de B?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de B?")
    A.write("a. 23/87",font=("Verdana",23,"bold"))
    B.write("b. 100/87",font=("Verdana",23,"bold"))
    C.write("c. 285/34",font=("Verdana",23,"bold"))
    D.write("d. 977/87",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/14.gif')
    tr6.shape('Problema GIF/14.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= A
    rango=600
    metodo=("Eliminación Gaussiana")    
    correct='C'
    contador()  

def question15(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de A?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de A?")
    A.write("a. 1.350784375",font=("Verdana",23,"bold"))
    B.write("b. 1.5048564",font=("Verdana",23,"bold"))
    C.write("c. 5.22551848",font=("Verdana",23,"bold"))
    D.write("d. 54.254584",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/15.gif')
    tr6.shape('Problema GIF/15.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= D
    rango=600
    metodo=("Gauss-Seidel")    
    correct='A'
    contador() 

def question16(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de B?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de B?")
    A.write("a. 12.350784375",font=("Verdana",23,"bold"))
    B.write("b. 1.97364613",font=("Verdana",23,"bold"))
    C.write("c. 5.28585",font=("Verdana",23,"bold"))
    D.write("d. 5.344584",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/16.gif')
    tr6.shape('Problema GIF/16.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= D
    rango=600
    metodo=("Gauss-Seidel")    
    correct='B'
    contador()    

def question17(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de A?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de A?")
    A.write("a. 1.35095195",font=("Verdana",23,"bold"))
    B.write("b. 1.97364613",font=("Verdana",23,"bold"))
    C.write("c. 5.78542",font=("Verdana",23,"bold"))
    D.write("d. 5.344584",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/17.gif')
    tr6.shape('Problema GIF/17.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=600
    metodo=("Jacobi")    
    correct='A'
    contador()  

def question18(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de A?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de A?")
    A.write("a. 1.35095195",font=("Verdana",23,"bold"))
    B.write("b. -1.002862",font=("Verdana",23,"bold"))
    C.write("c. 5.78542",font=("Verdana",23,"bold"))
    D.write("d. 5.344584",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/18.gif')
    tr6.shape('Problema GIF/18.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=600
    metodo=("Jacobi")    
    correct='B'
    contador()      

def question19(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de I?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de I?")
    A.write("a. .142416952",font=("Verdana",23,"bold"))
    B.write("b. .2515124",font=("Verdana",23,"bold"))
    C.write("c. -.5428884",font=("Verdana",23,"bold"))
    D.write("d. .2412685",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/19.gif')
    tr6.shape('Problema GIF/19.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=500
    metodo=("Regla Trapezoidal")    
    correct='A'
    contador()     

def question20(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de I?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de I?")
    A.write("a. 2.142416952",font=("Verdana",23,"bold"))
    B.write("b. 1.387677424",font=("Verdana",23,"bold"))
    C.write("c. -3.5428884",font=("Verdana",23,"bold"))
    D.write("d. 4.2412685",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/20.gif')
    tr6.shape('Problema GIF/20.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=500
    metodo=("Regla Trapezoidal")    
    correct='B'
    contador()    

def question21(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de ln 3?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de ln 3?")
    A.write("a. 1.098612",font=("Verdana",23,"bold"))
    B.write("b. 1.38763",font=("Verdana",23,"bold"))
    C.write("c. 3.4548632",font=("Verdana",23,"bold"))
    D.write("d. 4.554847",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/21.gif')
    tr6.shape('Problema GIF/21.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=500
    metodo=("Interpolación Lineal")    
    correct='A'
    contador() 

def question22(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de ln 3?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de ln 3?")
    A.write("a. 1.098614",font=("Verdana",23,"bold"))
    B.write("b. 1.098612",font=("Verdana",23,"bold"))
    C.write("c. -3.4548632",font=("Verdana",23,"bold"))
    D.write("d. -4.554847",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/22.gif')
    tr6.shape('Problema GIF/22.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=300
    metodo=("Interpolación Lineal")    
    correct='B'
    contador() 

def question23(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de g(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de g(x)?")
    A.write("a. 48.21",font=("Verdana",23,"bold"))
    B.write("b. 5.21",font=("Verdana",23,"bold"))
    C.write("c. -9",font=("Verdana",23,"bold"))
    D.write("d. -7.554847",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/23.gif')
    tr6.shape('Problema GIF/23.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= D
    rango=600
    metodo=("Diferencias divididas")    
    correct='C'
    contador()      

def question24(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de g(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de g(x)?")
    A.write("a. 532",font=("Verdana",23,"bold"))
    B.write("b. 198",font=("Verdana",23,"bold"))
    C.write("c. -89",font=("Verdana",23,"bold"))
    D.write("d. 705",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/24.gif')
    tr6.shape('Problema GIF/24.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= D
    rango=600
    metodo=("Diferencias divididas")    
    correct='A'
    contador()  

def question25(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de g(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de g(x)?")
    A.write("a. 2.598",font=("Verdana",23,"bold"))
    B.write("b. 1.7056",font=("Verdana",23,"bold"))
    C.write("c. -5.245",font=("Verdana",23,"bold"))
    D.write("d. 3.1298",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/25.gif')
    tr6.shape('Problema GIF/25.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=500
    metodo=("Newton hacia adelante")    
    correct='B'
    contador()         

def question26(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de g(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de g(x)?")
    A.write("a. 29.598",font=("Verdana",23,"bold"))
    B.write("b. 30.7056",font=("Verdana",23,"bold"))
    C.write("c. 32.3898",font=("Verdana",23,"bold"))
    D.write("d. 32.1298",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/26.gif')
    tr6.shape('Problema GIF/26.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= D
    rango=500
    metodo=("Newton hacia adelante")    
    correct='C'
    contador()     

def question27(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de g(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de g(x)?")
    A.write("a. 2.598",font=("Verdana",23,"bold"))
    B.write("b. 3.7056",font=("Verdana",23,"bold"))
    C.write("c. 3.235",font=("Verdana",23,"bold"))
    D.write("d. 3.6879",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/27.gif')
    tr6.shape('Problema GIF/27.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= A
    rango=500
    metodo=("Newton hacia atras")    
    correct='D'
    contador()   

def question28(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de g(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de g(x)?")
    A.write("a. 32.39",font=("Verdana",23,"bold"))
    B.write("b. 30.38",font=("Verdana",23,"bold"))
    C.write("c. 31.35",font=("Verdana",23,"bold"))
    D.write("d. 3.849",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/28.gif')
    tr6.shape('Problema GIF/28.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= C
    rango=500
    metodo=("Newton hacia atras")    
    correct='A'
    contador()        

def question29(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de f(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de f(x)?")
    A.write("a. -80/24",font=("Verdana",23,"bold"))
    B.write("b. -1925/64",font=("Verdana",23,"bold"))
    C.write("c. 31/48",font=("Verdana",23,"bold"))
    D.write("d. 50/78",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/29.gif')
    tr6.shape('Problema GIF/29.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= C
    rango=600
    metodo=("Lagrange")    
    correct='B'
    contador()     

def question30(): 
    global tr6
    global questask
    quest.write("¿Cual es el valor de f(x)?",font=("Verdana",23,"bold"))
    questask=("¿Cual es el valor de f(x)?")
    A.write("a. -28",font=("Verdana",23,"bold"))
    B.write("b. -64",font=("Verdana",23,"bold"))
    C.write("c.  48",font=("Verdana",23,"bold"))
    D.write("d.  78",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/30.gif')
    tr6.shape('Problema GIF/30.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= C
    rango=600
    metodo=("Lagrange")    
    correct='A'
    contador()      

def question31(): 
    global tr6
    global questask
    quest.write("¿Sucesión donde el margen tiene 3 milesimas?",font=("Verdana",13,"bold"))
    questask=("¿Sucesión donde el margen tiene 3 milesimas?")
    A.write("a.  X2-X1",font=("Verdana",23,"bold"))
    B.write("b.  X5-X4",font=("Verdana",23,"bold"))
    C.write("c.  X8-X9",font=("Verdana",23,"bold"))
    D.write("d.  X6-X5",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/31.gif')
    tr6.shape('Problema GIF/31.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= B
    rango=600
    metodo=("Punto fijo")    
    correct='C'
    contador()      

def question32(): 
    global tr6
    global questask
    quest.write("¿Sucesión donde el margen tiene 3 milesimas?",font=("Verdana",13,"bold"))
    questask=("¿Sucesión donde el margen tiene 3 milesimas?")
    A.write("a.  X6-x5",font=("Verdana",23,"bold"))
    B.write("b.  X5-X4",font=("Verdana",23,"bold"))
    C.write("c.  X8-X9",font=("Verdana",23,"bold"))
    D.write("d.  X8-X7",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/32.gif')
    tr6.shape('Problema GIF/32.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= B
    rango=600
    metodo=("Punto fijo")    
    correct='A'
    contador()     

def question33(): 
    global tr6
    global questask
    quest.write("¿Iteración donde el margen tiene .000001?",font=("Verdana",13,"bold"))
    questask=("¿Iteración donde el margen tiene .000001?")
    A.write("a.  i=1",font=("Verdana",23,"bold"))
    B.write("b.  i=3",font=("Verdana",23,"bold"))
    C.write("c.  i=4",font=("Verdana",23,"bold"))
    D.write("d.  i=5",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/33.gif')
    tr6.shape('Problema GIF/33.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= C
    rango=600
    metodo=("Newton Raphson")    
    correct='B'
    contador()         

def question34(): 
    global tr6
    global questask
    quest.write("¿Iteración donde el margen tiene .000001?",font=("Verdana",13,"bold"))
    questask=("¿Iteración donde el margen tiene .000001?")
    A.write("a.  i=10",font=("Verdana",23,"bold"))
    B.write("b.  i=2",font=("Verdana",23,"bold"))
    C.write("c.  i=3",font=("Verdana",23,"bold"))
    D.write("d.  i=4",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/34.gif')
    tr6.shape('Problema GIF/34.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= C
    rango=600
    metodo=("Newton Raphson")    
    correct='D'
    contador() 

def question35(): 
    global tr6
    global questask
    quest.write("¿Iteración donde el margen tiene .000?",font=("Verdana",13,"bold"))
    questask=("¿Iteración donde el margen tiene .000?")
    A.write("a.  i=8",font=("Verdana",23,"bold"))
    B.write("b.  i=2",font=("Verdana",23,"bold"))
    C.write("c.  i=5",font=("Verdana",23,"bold"))
    D.write("d.  i=4",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/35.gif')
    tr6.shape('Problema GIF/35.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= B
    rango=600
    metodo=("Falsa Posición")    
    correct='C'
    contador()    

def question36(): 
    global tr6
    global questask
    quest.write("¿Iteración donde el margen tiene .000?",font=("Verdana",13,"bold"))
    questask=("¿Iteración donde el margen tiene .000?")
    A.write("a.  i=8",font=("Verdana",23,"bold"))
    B.write("b.  i=1",font=("Verdana",23,"bold"))
    C.write("c.  i=2",font=("Verdana",23,"bold"))
    D.write("d.  i=5",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/36.gif')
    tr6.shape('Problema GIF/36.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= B
    rango=600
    metodo=("Falsa Posición")    
    correct='A'
    contador()    

def question37(): 
    global tr6
    global questask
    quest.write("¿Iteración donde el margen tiene .000?",font=("Verdana",13,"bold"))
    questask=("¿Iteración donde el margen tiene .000?")
    A.write("a.  i=3",font=("Verdana",23,"bold"))
    B.write("b.  i=5",font=("Verdana",23,"bold"))
    C.write("c.  i=2",font=("Verdana",23,"bold"))
    D.write("d.  i=1",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/37.gif')
    tr6.shape('Problema GIF/37.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= A
    rango=600
    metodo=("Secante")    
    correct='B'
    contador()     

def question38(): 
    global tr6
    global questask
    quest.write("¿Iteración donde el margen tiene .000?",font=("Verdana",13,"bold"))
    questask=("¿Iteración donde el margen tiene .000?")
    A.write("a.  i=1",font=("Verdana",23,"bold"))
    B.write("b.  i=8",font=("Verdana",23,"bold"))
    C.write("c.  i=2",font=("Verdana",23,"bold"))
    D.write("d.  i=21",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/38.gif')
    tr6.shape('Problema GIF/38.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= A
    rango=600
    metodo=("Secante")    
    correct='C'
    contador()   

def question39(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de I",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de I")
    A.write("a.  .66666667",font=("Verdana",23,"bold"))
    B.write("b.  .3432143",font=("Verdana",23,"bold"))
    C.write("c.  .5566474",font=("Verdana",23,"bold"))
    D.write("d.  .3232532",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/39.gif')
    tr6.shape('Problema GIF/39.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= C
    rango=600
    metodo=("Newton-Cotes Cerradas")    
    correct='A'
    contador()

def question40(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de I",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de I")
    A.write("a.  2.2312435",font=("Verdana",23,"bold"))
    B.write("b.  1.458058354",font=("Verdana",23,"bold"))
    C.write("c.  4.2342351",font=("Verdana",23,"bold"))
    D.write("d.  2.34353",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/40.gif')
    tr6.shape('Problema GIF/40.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= C
    rango=600
    metodo=("Newton-Cotes Cerradas")    
    correct='B'
    contador()          

def question41(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de I",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de I")
    A.write("a.  2.2342",font=("Verdana",23,"bold"))
    B.write("b.  1.4233435",font=("Verdana",23,"bold"))
    C.write("c.  1.50349206",font=("Verdana",23,"bold"))
    D.write("d.  6.3423423",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/41.gif')
    tr6.shape('Problema GIF/41.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= B
    rango=600
    metodo=("Newton-Cotes Abiertas")    
    correct='C'
    contador()  

def question42(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de I",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de I")
    A.write("a.  12.34",font=("Verdana",23,"bold"))
    B.write("b.  5.65",font=("Verdana",23,"bold"))
    C.write("c.  10.23",font=("Verdana",23,"bold"))
    D.write("d.  -9.35",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/42.gif')
    tr6.shape('Problema GIF/42.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= B
    rango=600
    metodo=("Newton-Cotes Abiertas")    
    correct='D'
    contador() 

def question43(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de I",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de I")
    A.write("a.  1.49364",font=("Verdana",23,"bold"))
    B.write("b.  1.34",font=("Verdana",23,"bold"))
    C.write("c.  1.223",font=("Verdana",23,"bold"))
    D.write("d.  9.35",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/43.gif')
    tr6.shape('Problema GIF/43.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= B
    rango=600
    metodo=("Regla de 1/3 Simpson")    
    correct='A'
    contador()   

def question44(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de I",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de I")
    A.write("a.   1.4234",font=("Verdana",23,"bold"))
    B.write("b.  .14189715",font=("Verdana",23,"bold"))
    C.write("c.  1.12312",font=("Verdana",23,"bold"))
    D.write("d.  -9.35",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/44.gif')
    tr6.shape('Problema GIF/44.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= A
    rango=600
    metodo=("Regla de 1/3 Simpson")    
    correct='B'
    contador()    

def question45(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de I",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de I")
    A.write("a.  2.401154775",font=("Verdana",23,"bold"))
    B.write("b.  1.14189715",font=("Verdana",23,"bold"))
    C.write("c.  4.12312",font=("Verdana",23,"bold"))
    D.write("d.  8.35",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/45.gif')
    tr6.shape('Problema GIF/45.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= B
    rango=600
    metodo=("Regla de 3/8 Simpson")    
    correct='A'
    contador()       

def question46(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de I",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de I")
    A.write("a.  .501154775",font=("Verdana",23,"bold"))
    B.write("b.  .9580754183",font=("Verdana",23,"bold"))
    C.write("c.  .12312",font=("Verdana",23,"bold"))
    D.write("d.  .35",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/46.gif')
    tr6.shape('Problema GIF/46.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= A
    rango=600
    metodo=("Regla de 3/8 Simpson")    
    correct='B'
    contador()  

def question47(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y2",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y2")
    A.write("a.  50.1154775",font=("Verdana",23,"bold"))
    B.write("b.  32.1258",font=("Verdana",23,"bold"))
    C.write("c.  4.19777778",font=("Verdana",23,"bold"))
    D.write("d.  23.5",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/47.gif')
    tr6.shape('Problema GIF/47.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= B 
    incorrectz= A
    rango=600
    metodo=("Euler Hacia Adelante")    
    correct='C'
    contador()    

def question48(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y1",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y1")
    A.write("a.  5.23",font=("Verdana",23,"bold"))
    B.write("b.  4.7",font=("Verdana",23,"bold"))
    C.write("c.  4.24",font=("Verdana",23,"bold"))
    D.write("d.  21.23",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/48.gif')
    tr6.shape('Problema GIF/48.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= A
    rango=600
    metodo=("Euler Hacia Adelante")    
    correct='B'
    contador()       

def question49(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y1",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y1")
    A.write("a.  1.2005",font=("Verdana",23,"bold"))
    B.write("b.  2.7",font=("Verdana",23,"bold"))
    C.write("c.  3.24",font=("Verdana",23,"bold"))
    D.write("d.  1.23",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/49.gif')
    tr6.shape('Problema GIF/49.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= B
    rango=600
    metodo=("Euler Modificado")    
    correct='A'
    contador()  

def question50(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y2",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y2")
    A.write("a.  1.4305",font=("Verdana",23,"bold"))
    B.write("b.  .93181",font=("Verdana",23,"bold"))
    C.write("c.  3.234",font=("Verdana",23,"bold"))
    D.write("d.  1.2453",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/50.gif')
    tr6.shape('Problema GIF/50.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= C 
    incorrectz= D
    rango=600
    metodo=("Euler Modificado")    
    correct='B'
    contador()      

def question51(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y2",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y2")
    A.write("a.  23.4232305",font=("Verdana",23,"bold"))
    B.write("b.  .1293181",font=("Verdana",23,"bold"))
    C.write("c.  .6515326649",font=("Verdana",23,"bold"))
    D.write("d.  4.23242453",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/51.gif')
    tr6.shape('Problema GIF/51.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= D
    rango=600
    metodo=("Runge Kutta 2do Orden")    
    correct='C'
    contador()        

def question52(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y1",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y1")
    A.write("a.  2.305",font=("Verdana",23,"bold"))
    B.write("b.  1.98",font=("Verdana",23,"bold"))
    C.write("c.  2.26649",font=("Verdana",23,"bold"))
    D.write("d.  4.233",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/52.gif')
    tr6.shape('Problema GIF/52.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= D
    rango=600
    metodo=("Runge Kutta 2do Orden")    
    correct='B'
    contador()    

def question53(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y2",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y2")
    A.write("a.  2.23305",font=("Verdana",23,"bold"))
    B.write("b.  10.23298",font=("Verdana",23,"bold"))
    C.write("c.  .23226649",font=("Verdana",23,"bold"))
    D.write("d.  .178709886",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/53.gif')
    tr6.shape('Problema GIF/53.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= B
    rango=600
    metodo=("Runge Kutta 3er Orden")    
    correct='D'
    contador()            

def question54(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y2",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y2")
    A.write("a.  23.305",font=("Verdana",23,"bold"))
    B.write("b.  12.3298",font=("Verdana",23,"bold"))
    C.write("c.  32.26649",font=("Verdana",23,"bold"))
    D.write("d.  2.314767364",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/54.gif')
    tr6.shape('Problema GIF/54.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= A 
    incorrectz= B
    rango=600
    metodo=("Runge Kutta 3er Orden")    
    correct='D'
    contador()            

def question55(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y1",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y1")
    A.write("a.  1.996483333",font=("Verdana",23,"bold"))
    B.write("b.  1.233298",font=("Verdana",23,"bold"))
    C.write("c.  42.656649",font=("Verdana",23,"bold"))
    D.write("d.  1.4767364",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/55.gif')
    tr6.shape('Problema GIF/55.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= B
    rango=600
    metodo=("Runge Kutta 4to Orden 1/3 Simpson")    
    correct='A'
    contador() 

def question56(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y2",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y2")
    A.write("a.  .996483333",font=("Verdana",23,"bold"))
    B.write("b.  .60254868",font=("Verdana",23,"bold"))
    C.write("c.  .627654669",font=("Verdana",23,"bold"))
    D.write("d.  .454767364",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/56.gif')
    tr6.shape('Problema GIF/56.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= B
    rango=600
    metodo=("Runge Kutta 4to Orden 1/3 Simpson")    
    correct='C'
    contador()    

def question57(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y1",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y1")
    A.write("a.  .886483333",font=("Verdana",23,"bold"))
    B.write("b.  .552579996",font=("Verdana",23,"bold"))
    C.write("c.  .237654669",font=("Verdana",23,"bold"))
    D.write("d.  .114767364",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/57.gif')
    tr6.shape('Problema GIF/57.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= C
    rango=600
    metodo=("Runge Kutta 4to Orden 3/8 Simpson")    
    correct='B'
    contador()       

def question58(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y2",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y2")
    A.write("a.  3.886483333",font=("Verdana",23,"bold"))
    B.write("b.  5.552579996",font=("Verdana",23,"bold"))
    C.write("c.  1.899022614",font=("Verdana",23,"bold"))
    D.write("d.  2.114767364",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/58.gif')
    tr6.shape('Problema GIF/58.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= B
    rango=600
    metodo=("Runge Kutta 4to Orden 3/8 Simpson")    
    correct='C'
    contador()     

def question59(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y'1",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y'1")
    A.write("a.  3.3333",font=("Verdana",23,"bold"))
    B.write("b.  5.9996",font=("Verdana",23,"bold"))
    C.write("c.  3.0625",font=("Verdana",23,"bold"))
    D.write("d.  2.1147",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/59.gif')
    tr6.shape('Problema GIF/59.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= B
    rango=600
    metodo=("Runge Kutta Orden Superior")    
    correct='C'
    contador()      

def question60(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de y2",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de y2")
    A.write("a.  2.498956",font=("Verdana",23,"bold"))
    B.write("b.  1.4986416",font=("Verdana",23,"bold"))
    C.write("c.  4.124625",font=("Verdana",23,"bold"))
    D.write("d.  1545.1147",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/60.gif')
    tr6.shape('Problema GIF/60.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= A
    rango=600
    metodo=("Runge Kutta Orden Superior")    
    correct='B'
    contador()  

def question61(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de ambas x",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de ambas x")
    A.write("a.  -3 y -2",font=("Verdana",23,"bold"))
    B.write("b.  5 y 6",font=("Verdana",23,"bold"))
    C.write("c.  8 y 5",font=("Verdana",23,"bold"))
    D.write("d.  -12 y 5",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/61.gif')
    tr6.shape('Problema GIF/61.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= B
    rango=600
    metodo=("Raices Polinomiales")    
    correct='A'
    contador()      

def question62(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de ambas x",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de ambas x")
    A.write("a.  -3 y -2",font=("Verdana",23,"bold"))
    B.write("b.  3 y -1",font=("Verdana",23,"bold"))
    C.write("c.  4 y 25",font=("Verdana",23,"bold"))
    D.write("d.  -112 y 35",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/62.gif')
    tr6.shape('Problema GIF/62.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= A
    rango=600
    metodo=("Raices Polinomiales")    
    correct='B'
    contador()  

def question63(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de ambas a0",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de ambas a0")
    A.write("a.  2.008443615",font=("Verdana",23,"bold"))
    B.write("b.  3.232324",font=("Verdana",23,"bold"))
    C.write("c.  4.563001",font=("Verdana",23,"bold"))
    D.write("d.  -112",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/63.gif')
    tr6.shape('Problema GIF/63.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= C
    rango=600
    metodo=("Linea Recta")    
    correct='A'
    contador()           

def question64(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de ambas a1",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de ambas a1")
    A.write("a.  5.008443615",font=("Verdana",23,"bold"))
    B.write("b.  1.269377756",font=("Verdana",23,"bold"))
    C.write("c.  1.563001",font=("Verdana",23,"bold"))
    D.write("d.  -12.112",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/64.gif')
    tr6.shape('Problema GIF/64.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= C
    rango=600
    metodo=("Linea Recta")    
    correct='B'
    contador()  

def question65(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de  x",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de ambas x")
    A.write("a.  8.443615",font=("Verdana",23,"bold"))
    B.write("b.  1.26756",font=("Verdana",23,"bold"))
    C.write("c.  1.312138",font=("Verdana",23,"bold"))
    D.write("d.  2.112",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/65.gif')
    tr6.shape('Problema GIF/65.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= B
    rango=600
    metodo=("Grafico")    
    correct='C'
    contador() 

def question66(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de x",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de x")
    A.write("a.  4.43615",font=("Verdana",23,"bold"))
    B.write("b.  106.7777",font=("Verdana",23,"bold"))
    C.write("c.  3.12138",font=("Verdana",23,"bold"))
    D.write("d.  24.112",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/66.gif')
    tr6.shape('Problema GIF/66.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= C
    rango=600
    metodo=("Grafico")    
    correct='B'
    contador()     

def question67(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de  x",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de x")
    A.write("a.  .22086",font=("Verdana",23,"bold"))
    B.write("b.  10.77",font=("Verdana",23,"bold"))
    C.write("c.  32.138",font=("Verdana",23,"bold"))
    D.write("d.  241.12",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/67.gif')
    tr6.shape('Problema GIF/67.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= C
    rango=600
    metodo=("Bisectriz")    
    correct='A'
    contador()     

def question68(): 
    global tr6
    global questask
    quest.write("Encuentra el valor de x",font=("Verdana",23,"bold"))
    questask=("Encuentra el valor de x")
    A.write("a.  206",font=("Verdana",23,"bold"))
    B.write("b.  10",font=("Verdana",23,"bold"))
    C.write("c.  3",font=("Verdana",23,"bold"))
    D.write("d.  24",font=("Verdana",23,"bold"))
    tr6= turtle.Turtle()
    wn6=turtle.Screen()
    wn6.addshape('Problema GIF/68.gif')
    tr6.shape('Problema GIF/68.gif')
    tr6.goto(-650,-10)
    global correct
    global metodo
    global incorrectn
    global incorrectz
    global rango
    incorrectn= D 
    incorrectz= B
    rango=600
    metodo=("Bisectriz")    
    correct='C'
    contador()      
#--------------------------------------------------------------fin preguntas---------------------------------------------------------------------------------------------------------#    

#Key
wn.listen()
wn.onkeypress(chooseAnswerA,"a")
wn.onkeypress(chooseAnswerB,"b")
wn.onkeypress(chooseAnswerC,"c")
wn.onkeypress(chooseAnswerD,"d")
wn.onkeypress(cincuenta,"x")
wn.onkeypress(phonecall,"v")
wn.onkeypress(publico,"z")
wn.onkeypress(moretime,"t")
#Start
question1()

wn.mainloop()