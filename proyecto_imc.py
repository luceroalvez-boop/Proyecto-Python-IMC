def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: Este campo no puede estar vacio.")
        
def pedir_numero(mensaje, tipo=float):
            while True:
                entrada = input(mensaje).strip()
                try:
                    return tipo(entrada)
                except ValueError:
                    print("Error: Por favor, introduce un numero valido.")
print(" CALCULADORA DE INDICE DE MASA CORPORAL (IMC) ")
nombre = pedir_texto("Ingresa tu nombre: ")
apellido_paterno = pedir_texto("Ingresa tu apellido paterno: ")
apellido_materno = pedir_texto("Ingresa tu apellido materno: ")
edad = pedir_numero("Ingresa tu edad: ", tipo=int)
peso = pedir_numero("Ingresa tu peso en kg: ", tipo=float)
estatura = pedir_numero("Ingresa tu estatura en metros (ej. 1.65): ", tipo=float)

#Clculo del IMC
imc = peso / (estatura ** 2)

#Despligue de resultados
print("\n--- DATOS DEL USUARIO --- ")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"Tu Indice de Masa Corporal (IMC)es: {imc:.2f}")
