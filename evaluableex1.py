# Defino la variable para poder calcular el peso en otros planetas
def calcular_peso (aceleración,masa):
    peso = masa * aceleración 
    return peso
# Pido el peso y la elección del planeta/satélite
peso = float(input("Introduzca el peso que quiere cacular en el cuerpo celeste:")) 
planeta = str(input("Introduzca un cuerpo celeste a elegir de los propuestos dentro del paréntesis (mercurio, venus, la tierra, marte, júpiter, saturno, urano, neptuno, plutón, luna, el sol):"))
# Se saca la masa del peso propuesto teniendo en cuenta que es el de la tierra
masa = peso / 9.8
# se calcula el peso en función de la masa y del planeta a elegir
if planeta == "mercurio":
    aceleración == (6.67 * (10 ** -11) * 3.285 * (10 ** 23))/(2440000 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "venus":
    aceleración = (6.67 * (10 ** -11) * 4.867 * (10 ** 24))/(6051800 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "la tierra":
    aceleración = (6.67 * (10 ** -11) * 5.972 * (10 ** 24))/(6371000 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "marte":
    aceleración = (6.67 * (10 ** -11) * 6.39 * (10 ** 23))/(3389500 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "júpiter":
    aceleración = (6.67 * (10 ** -11) * 1898130 * (10 ** 21))/(69911000 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "saturno":
    aceleración = (6.67 * (10 ** -11) * 5.688 * (10 ** 26))/(58232000 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "urano":
    aceleración = (6.67 * (10 ** -11) * 86.816 * (10 ** 24))/(25362000 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "neptuno":
    aceleración = (6.67 * (10 ** -11) * 1.024 * (10 ** 26))/(24622000 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "plutón":
    aceleración = (6.67 * (10 ** -11) * 1.3 * (10 ** 22))/(1188300 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "luna":
    aceleración = (6.67 * (10 ** -11) * 7.34 * (10 ** 22))/(1740000 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
elif planeta == "el sol":
    aceleración = (6.67 * (10 ** -11) * 1.989 * (10 ** 30))/(696000000 ** 2)
    peso_calculado = calcular_peso(aceleración,masa)
    print(f"Su peso en {planeta} es:", peso_calculado, "kg.")
else:
    print("Vuelva a repetir el proceso.")