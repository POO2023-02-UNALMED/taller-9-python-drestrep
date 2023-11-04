from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora Poo")
root.resizable(0,0)
root.geometry()

# Gestor de eventos para la calculadora

number1 = ""
number2 = ""
operator = ""
operadores = ["+","-","*","/"]
txt = ""
result = False
divZero = False
errortxt = ""

def Calcular(evento):
    cal = 0
    global errortxt
    global divZero
    global result
    global txt
    global number2
    global number1
    global operator
    
    if (divZero):
        pantalla.delete(0, len(errortxt))
        divZero = False
    else:
        pantalla.delete(0, len(txt))
    value = evento.widget.cget("text")
    
    
    if(value not in operadores and value != "="):
        if (result):
            number1 = ""
            number2 = ""
            operator = ""
    result = False
    
    if (value in operadores):
        if (operator == "" or number2 == ""):
            if (number1 == ""):
                number1 = "0"
        else:
            if (operator == "+"):
                cal = float(number1)+float(number2)
            if (operator == "-"):
                cal = float(number1)-float(number2)
            if (operator == "*"):
                cal = float(number1)*float(number2)
            if (operator == "/"):
                if (float(number2)*1 == 0):
                    divZero = True
                else:
                    cal = float(number1)/float(number2)
            number1 = str(cal)
            operator = ""
            number2 = ""
        operator = value    
    elif (value == "="):
        if (number1 == ""):
            number1 = "0"
        elif (number2 == ""):
            operator = ""
        else:
            if (operator == "+"):
                cal = float(number1)+float(number2)
            if (operator == "-"):
                cal = float(number1)-float(number2)
            if (operator == "*"):
                cal = float(number1)*float(number2)
            if (operator == "/"):
                if (float(number2)*1 == 0):
                    divZero = True
                else:
                    cal = float(number1)/float(number2)
            number1 = str(cal)
            operator = ""
            number2 = ""
        result = True
    elif (value == "."):
        if (operator == ""):
            if (number1 == ""):
                number1 = "0"
            if (number1[-1] != "." and number1.count(".")<1):   
                number1 += "."
        else:
            if (number2 == ""):
                number2 = "0"
            if (number2[-1] != "." and number2.count(".")<1):
                number2 += "."
    else:
        if (operator == ""):
           number1 += value
        else:
            number2 += value    
    if (number1 != ""):
        if (number1[-1] != "."):
            if (float(number1)-int(float(number1))== 0):
                number1 = f"{int(float(number1))}"

    if (number2 != ""):
        if (number2[-1] != "."):
            if (float(number2)-int(float(number2)) == 0):
                number2 = f"{int(float(number2))}"
    
    if (divZero):
        pantalla.delete(0, len(txt))
        errortxt = "No se puede dividir por cero. (Estudia matemáticas para más información"
        pantalla.insert(0, errortxt)
        number1 = ""
        number2 = ""
        operator = ""
    else:
        txt = f"{number1}{operator}{number2}"
        pantalla.insert(0,txt)
    
    
    
    
# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones (Tuve que separar el grid de la creación de los botones dado a que al juntarlos no deja que se le aplique bind())
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_1.bind("<Button-1>", Calcular)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_2.bind("<Button-1>", Calcular)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_3.bind("<Button-1>", Calcular)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_4.bind("<Button-1>", Calcular)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_5.bind("<Button-1>", Calcular)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_6.bind("<Button-1>", Calcular)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_7.bind("<Button-1>", Calcular)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_8.bind("<Button-1>", Calcular)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_9.bind("<Button-1>", Calcular)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_igual.bind("<Button-1>", Calcular)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_punto.bind("<Button-1>", Calcular)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_mas.bind("<Button-1>", Calcular)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_menos.bind("<Button-1>", Calcular)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_multiplicacion.bind("<Button-1>", Calcular)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)
boton_division.bind("<Button-1>", Calcular)

root.mainloop()