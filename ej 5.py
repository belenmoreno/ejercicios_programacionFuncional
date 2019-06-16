def alumno(diccionario):
    diccionario_mayusculas = {}

    for key in diccionario:
        aux = key.upper()
        diccionario_mayusculas[aux] = diccionario[key]
    return diccionario_mayusculas

def main():
    estudiante = {}
    while 1:
        asignatura = input("introduce la asignatura: ")
        nota = float(input("introduce la nota: "))
        estudiante[asignatura] = nota
        salir = input("Introduce salir para salir para no añadir más asignatuas.")
        salir = salir.upper()
        if salir == 'SALIR':
            resultado = alumno(estudiante)
            break #break sale del bucle y return sale de la funcion

    print(resultado)



[1,3]
[2,3]

[6,15]

if __name__ == "__main__":
    main()