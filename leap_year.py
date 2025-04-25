def leap_year():
    año = int(input("Ingrese un año: "))

    if (año % 400 == 0) or (año % 100 != 0 and año % 4 == 0):
        result = "es"
    else:
        result = "no es"

    print(f"El año {año} {result} bisiesto")