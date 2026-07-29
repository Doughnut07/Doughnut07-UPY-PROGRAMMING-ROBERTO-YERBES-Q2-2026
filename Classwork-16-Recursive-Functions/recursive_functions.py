# 1. Basic recursion example — recursiva(n)
def recursiva(n):
    """Cuenta regresiva desde n hasta 1 usando recursión."""
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n debe ser un número entero")
        if n < 0:
            raise ValueError("n no puede ser negativo")

        # Caso base
        if n == 0:
            return "Done!"

        # Caso recursivo
        print(n)
        return recursiva(n - 1)

    except (TypeError, ValueError) as e:
        print(f"Error en recursiva: {e}")
        return None


# 2. Fibonacci — fibonacci(n)
def fibonacci(n):
    """Regresa el n-ésimo número de la serie de Fibonacci."""
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n debe ser un número entero")
        if n < 0:
            raise ValueError("n no puede ser negativo")

        # Casos base
        if n == 0 or n == 1:
            return n

        # Caso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)

    except (TypeError, ValueError) as e:
        print(f"Error en fibonacci: {e}")
        return None


# 3. Factorial — factorial(n)
def factorial(n):
    """Regresa n! (n factorial) usando recursión."""
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n debe ser un número entero")
        if n < 0:
            raise ValueError("n no puede ser negativo")

        # Casos base
        if n == 0 or n == 1:
            return 1

        # Caso recursivo
        return factorial(n - 1) * n

    except (TypeError, ValueError) as e:
        print(f"Error en factorial: {e}")
        return None


# 4. Recursive multiplication — multiplicacion_recursiva(a, b)
def multiplicacion_recursiva(a, b):
    """Multiplica a * b usando únicamente sumas recursivas."""
    try:
        if (not isinstance(a, int) or isinstance(a, bool) or
                not isinstance(b, int) or isinstance(b, bool)):
            raise TypeError("a y b deben ser números enteros")
        
        if b < 0:
            raise ValueError("b no puede ser negativo")

        # Caso base
        if b == 0:
            return 0

        # Caso recursivo
        return multiplicacion_recursiva(a, b - 1) + a

    except (TypeError, ValueError) as e:
        print(f"Error en multiplicacion_recursiva: {e}")
        return None


# 5. Recursive integer division — division_entera_recursiva(dividendo, divisor)
def division_entera_recursiva(dividendo, divisor):
    """Regresa el cociente entero usando restas recursivas."""
    try:
        if (not isinstance(dividendo, int) or isinstance(dividendo, bool) or
                not isinstance(divisor, int) or isinstance(divisor, bool)):
            raise TypeError("dividendo y divisor deben ser números enteros")

        if divisor == 0:
            raise ZeroDivisionError("El divisor no puede ser 0")

        if dividendo < 0 or divisor < 0:
            raise ValueError("Esta función solo soporta valores positivos")

        # Caso base
        if dividendo - divisor < 0:
            return 0

        # Caso recursivo
        return division_entera_recursiva(dividendo - divisor, divisor) + 1

    except (TypeError, ZeroDivisionError, ValueError) as e:
        print(f"Error en division_entera_recursiva: {e}")
        return None


# 6. Power — potencia_recursiva(base, exponente)
def potencia_recursiva(base, exponente):
    """Regresa base elevado a exponente usando recursión."""
    try:
        if not isinstance(base, (int, float)) or isinstance(base, bool):
            raise TypeError("base debe ser un número")

        if not isinstance(exponente, int) or isinstance(exponente, bool):
            raise TypeError("exponente debe ser un número entero")

        if exponente < 0:
            raise ValueError("el exponente no puede ser negativo")

        # Caso base
        if exponente == 0:
            return 1

        # Caso recursivo
        return potencia_recursiva(base, exponente - 1) * base

    except (TypeError, ValueError) as e:
        print(f"Error en potencia_recursiva: {e}")
        return None


# 7. Collatz sequence — serie_collatz(n)
def serie_collatz(n):
    """Imprime la secuencia de Collatz hasta llegar a 1."""
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n debe ser un número entero")

        if n <= 0:
            raise ValueError("n debe ser un entero positivo mayor que 0")

        # Caso base
        if n == 1:
            print("END!")
            return 0

        # Caso recursivo
        if n % 2 == 0:
            print(n // 2)
            return serie_collatz(n // 2)
        else:
            print(3 * n + 1)
            return serie_collatz(3 * n + 1)

    except (TypeError, ValueError) as e:
        print(f"Error en serie_collatz: {e}")
        return None


# 8. Flattening a JSON — aplanar_json(diccionario, clave_padre, separador)
def aplanar_json(diccionario, clave_padre='', separador='.'):
    """Aplana un diccionario anidado en un diccionario de un solo nivel."""
    try:
        if not isinstance(diccionario, dict):
            raise AttributeError(
                f"aplanar_json solo acepta diccionarios, se recibió {type(diccionario).__name__}"
            )

        elementos = []

        for key, value in diccionario.items():
            nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else key

            if isinstance(value, dict):
                elementos.extend(
                    aplanar_json(value, nueva_llave, separador).items()
                )
            else:
                elementos.append((nueva_llave, value))

        return dict(elementos)

    except AttributeError as e:
        print(f"Error en aplanar_json: {e}")
        return {}

# TESTS 
if __name__ == "__main__":

    print("--- recursiva ---")
    print(recursiva(5))
    print(recursiva(0))
    print(recursiva(-3))
    print(recursiva(3.5))
    print(recursiva("5"))

    print("\n--- fibonacci ---")
    print(fibonacci(0))
    print(fibonacci(7))
    print(fibonacci(-1))

    print("\n--- factorial ---")
    print(factorial(5))
    print(factorial(0))
    print(factorial(-2))
    print(factorial(1.5))

    print("\n--- multiplicacion_recursiva ---")
    print(multiplicacion_recursiva(4, 3))
    print(multiplicacion_recursiva(7, 0))
    print(multiplicacion_recursiva(4, -3))
    print(multiplicacion_recursiva(4, "3"))

    print("\n--- division_entera_recursiva ---")
    print(division_entera_recursiva(17, 5))
    print(division_entera_recursiva(5, 5))
    print(division_entera_recursiva(10, 0))
    print(division_entera_recursiva(-10, 3))

    print("\n--- potencia_recursiva ---")
    print(potencia_recursiva(2, 5))
    print(potencia_recursiva(5, 0))
    print(potencia_recursiva(2, -2))

    print("\n--- serie_collatz ---")
    serie_collatz(6)
    serie_collatz(1)
    serie_collatz(0)
    serie_collatz(-6)

    print("\n--- aplanar_json ---")
    print(aplanar_json({"a": 1, "b": {"c": 2}}))
    print(aplanar_json({"a": {"b": {"c": 1}}}))
    print(aplanar_json(["a", "b", "c"]))
    print(aplanar_json({"tags": [1, 2, 3]}))
    print(aplanar_json({"a.b": 1, "a": {"b": 2}}))