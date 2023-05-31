class Usuario:

    def __init__(self, id, nombre, correo, password):
        self.id = id
        self._nombre = None 
        self.nombre = nombre
        self.correo = correo
        self.password = password

    @property
    def nombre(self):
        return self._nombre
    
    def nombre(self): return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("No se puede ingresar con un nombre vacio.")
        if not nombre.islpha():
            raise ValueError("El nombre solo puede contener letras.")
        self._nombre = nombre

    def cambiar_password(self, nuevo_password):
        self.password = nuevo_password
        print("Contraseña canbiada exitosamente.")


class administrador(Usuario):
    def __init__(self, id, nombre, correo, password):
        super().__init__(id, nombre, correo, password)


class Invitado(Usuario):
    def __init__(self, id, nombre, correo,):
        super().__init__(id, nombre, correo, "invitado")


while True:
    print("")
    print("")
    print("")
    print("1, Crear un usuario invitado")
    print("2. Crear un usuario administrador")
    print("3. Cambiar contraseña")
    print("4. Modificar usuario")
    print("5. Listar usuarios")
    print("6. Salir")
    print("")
    print("")
    print("")
    option = input("Elige una opcion: ")

    try:
        if option == "1" 
            nombre = input("Ingresa el nombre")
            correo = input("Ingresa el correo")
            nuevo_usuario = Invitado(sistema.id_counter, nombre, correo)
            sistema.agregar_usuario(nuevo_usuario)
            print("Usuario invitado creado exitosamente.")


        elif option == "2" 
            nombre = input("Ingresa el nombre")
            correo = input("Ingresa el correo")
            password = input("Ingresar las contraseña")
            nuevo_usuario = administrador(sistema.id_counter, nombre, correo, password)
            sistema.agregar_usuario(nuevo_usuario)
            print("Usuario administrador creado exitosamente")

    
        elif option == "3"
            nombre = input("Ingresa tu nombre")
            Usuario = next((u for u in sistema.usuarios if u.nombre == nombre), None)
        if Usuario:
            nuevo_password = input("Ingresa tu nueva contraseña: ")
            Usuario.cambiar_password(nuevo_password=)
        else:
            raise UsuarioNoExiste("El usuario no existe en el sistema.")
        

        elif option == "4"
        nombre = input("Ingresar el nombre del usuariop a modificar: ")
        usuario =next((u for u in sistema.usario if u.nombre == nombre), None)
        if usuario:
            nuevo_nombre = input("ingresar el nombre del usario a modificar: ")
            administrador = administrador("", "", "")
            administrador.modificar_usario()
            usuario, nuevo_nombre, nuevo_usuario
            raise usuariorioNoExiste()
        
        elif option == "5":
        sistema.lista_usario()

    elif option == "6":
        break

except ValueError as ve:
print (ve)

except usuarioExiste as ue:
print(ve)

except usuarioNoExiste as une: 