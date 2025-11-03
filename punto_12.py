contraseña= "contraseña"
contraseña_2= input("ingrese la contraseña: ")
contraseña_3= contraseña_2.lower()
if str(contraseña) == str(contraseña_3):
    print("la contraseña es correcta")
else:
    print("la contraseña es incorrecta")
input()