password = "contraseña"

password_del_usuario = input("Introduce la contraseña o te reviento: ")
password_del_usuario = password_del_usuario.lower()

if(password == password_del_usuario):
    print("Joder loco es igual que crack eres!")
else:
    print("Pues va a ser que no :-)")