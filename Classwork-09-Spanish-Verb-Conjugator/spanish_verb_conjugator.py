#INPUT
verbo = input("Ingresa verbo a conjugar: ")

#PROCESS
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}
stem = verbo[:-2]
terminacion = verbo[-2:]
lista_terminaciones = terminaciones[terminacion]

#OUTPUT
for index, pronombre in enumerate(pronombres):
    terminacion =lista_terminaciones[index]
    print(f"{pronombre} {stem}{terminacion}")
    