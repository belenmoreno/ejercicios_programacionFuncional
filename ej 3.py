def main():
    diccionario = {}
    frase = input("introduce una frase: ")
    frase1 = frase.split(' ') #frase1 es palabra
    # i = 0
    # longitud = len(frase1)
    # while i < longitud:
    #     diccionario[frase1[i]] = len(frase1[i])
    #     i += 1

    for palabra in frase1:
        diccionario[palabra] = len(palabra)

    print(diccionario)








if __name__ == "__main__":
    main()