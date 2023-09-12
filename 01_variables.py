#############
# Variables #
#############

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 3
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

#Concatenación de variables de distintos tipos en un mismo print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

# Este type no dice nada porque tiene varios tipos
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable)))

#########################
# Funciones del sistema #
#########################

#len es abreviado de Lenght, lo que hace es contar los caracteres
print(len(my_int_to_str_variable)) #1, porque es número entero
print(len(my_string_variable)) #18, porque es una cadena de texto

###############################
# Variables en una sola línea #
###############################

name, surname, alias, edad = "Pepe", "Lirio", "PepeLirio", 37
print("Me llamo:",name,". Mi primer apellido es:",surname,". Tengo", edad, "años.","Y mi usuario en GitHub es:", alias)

# Input para recoger datos. No se suele usar mucho.
# Solo cuando se usa en terminal.
"""
    name = input("What's your name?: ")
    age = input("How old are you?: ")

    print(name) # La variable name ya existía y tenía valor pero con el input reasignamos el valor.
    print(age) 
"""

#Cambiamos el tipo de la variable
name = 37
age = "Pepe"

print(name)
print(age) 

# ¿Forzamos el tipo?
address: str = "Mi dirección"
print(address)
print(type(address))

address = 32
print(address)
print(type(address))


