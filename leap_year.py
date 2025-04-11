def leap_year():
    año = int(input("Ingrese un año: "))
    result = "es"

    if año % 400 == 0:
        result = "es"
    elif año % 100 != 0 and año % 4 == 0:
        result = "es"
    else:
        result = "no es"

    print(f"El año {año} {result} bisiesto")