while True:

    number_1 = input('Por favor ingrese un numero:\n')
    number_2 = input('Por favor ingrese otro numero:\n')
    try:
        result = int(number_1)/int(number_2)
        print(f"El resultado es:{result}")
    except ValueError:
        print("Ingrese numeros o sos subnormal como camilo")
    except ZeroDivisionError:
        print("Subnormal no sabes como funcinan las matematicas")
    except Exception as e:
        print("Se produjo un error desconocido {e}")