# Función que se usa para ingresar un número flotanteS
def ingresar_numero_flotante(mensaje, minimo=float("-Inf"), maximo=float("Inf")):    
    while True:
        try:
            num = float(input(mensaje))
            if minimo <= num <= maximo:
               return num
            else:
                print(f"\nPor favor, ingrese un número dentro del rango [{minimo},{maximo}]") 
        except ValueError:
            print("\nPor favor, ingrese un número válido.")


# Calcula el ìndice de masa corporal (IMC) y determina el estado de salud
def calcular_imc(peso, altura):
    if altura <= 0:
        return None     #Se evita la divisiòn por cero o altura negativa
    imc = peso / (altura ** 2)
    return round(imc, 2)   # Devuelve el resultado redondeando a 2 decimales
     