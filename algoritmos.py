import secrets

# Credenciales hardcodeadas (Exposición de datos sensibles)
CONTRASENA_ADMIN = "contrasena123"

def verificar_contrasena(contrasena):
    if contrasena == CONTRASENA_ADMIN:
        return True
    return False

def juego():
    numero = secrets.randbelow(100) + 1  # Genera un número aleatorio entre 1 y 100
    intentos = 0
    print("¡Bienvenido al Juego de Adivinanzas!")
    print("Intenta adivinar el número entre 1 y 100")

    while True:
        # Problema de validación de entrada (Entrada no validada)
        adivinanza = int(input("Ingresa tu adivinanza: "))

        # Problema de manejo de errores (Excepción general)
        try:
            if adivinanza < numero:
                print("¡Demasiado bajo!")
            elif adivinanza > numero:
                print("¡Demasiado alto!")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except Exception as e:
            print("Ocurrió un error: ", e)

        intentos += 1

def main():
    print("Ingresa la contraseña de administrador para iniciar el juego:")
    contrasena = input()

    # Verificación de contraseña insegura
    if verificar_contrasena(contrasena):
        juego()
    else:
        print("Contraseña inválida. Acceso denegado.")

if __name__ == "__main__":
    main()
