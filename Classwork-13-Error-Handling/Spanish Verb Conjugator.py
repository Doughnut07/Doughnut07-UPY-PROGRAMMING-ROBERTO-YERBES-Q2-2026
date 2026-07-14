#INPUT
verbo = input("Ingrese verbo: ")

#PROCESS
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

try:
    
    if verbo == "":
        raise ValueError("El verbo debe terminar en ar, er o ir")

    
    if not verbo.isalpha():
        raise TypeError("El verbo debe terminar en ar, er o ir")

    
    if verbo != verbo.lower():
        raise NameError("El verbo debe escribirse en minúsculas")


    if len(verbo) < 2:
        raise IndexError

    raiz = verbo[:-2]
    final = verbo[-2:]

    lista_de_terminaciones = terminaciones[final]

except KeyError:
    print("El verbo debe terminar en ar, er o ir")
    raise SystemExit

except IndexError:
    print("El verbo debe terminar en ar, er o ir")
    raise SystemExit

except ValueError as e:
    print(e)
    raise SystemExit

except TypeError as e:
    print(e)
    raise SystemExit

except NameError as e:
    print(e)
    raise SystemExit

else:
    #OUTPUT
    for index, pronombre in enumerate(pronombres):
        terminacion = lista_de_terminaciones[index]
        print(f"{pronombre} {raiz}{terminacion}")