print("\033c")
contador_trabajadores = 0
total_sueldos_netos = 0
continuar = "s"

while continuar.lower() == "s":
   
    

    nombre = input("Nombre: ")
    horas = int(input("Horas trabajadas: "))
    sueldo_por_hora = float(input("Sueldo por hora: "))
    
    sueldo_base = horas * sueldo_por_hora
    aumento = 0
    
    
    if horas == 10:
        aumento = sueldo_base * 0.20
    elif horas == 15:
        aumento = sueldo_base * 0.30
    elif horas == 20:
        aumento = sueldo_base * 0.15
    elif horas > 25:
        aumento = sueldo_base * 0.08
    
    sueldo_neto = sueldo_base + aumento
    
    
    print("Aumento: $", aumento)
    print("Sueldo Neto: $", sueldo_neto)
    
    
    contador_trabajadores = contador_trabajadores + 1
    total_sueldos_netos = total_sueldos_netos + sueldo_neto
    
    
    continuar = input("¿Ingresar otro trabajador? (s/n): ")


print("\033c")

print("Trabajadores totales:", contador_trabajadores)
print("Monto total pagado: $", total_sueldos_netos)
