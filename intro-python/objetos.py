class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self):
        print("Hola mi nombre es:", self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print("Hola, me llamo", self.nombre,"y soy administrador")


# usuario = Usuario("Felipe", "Feliz")
# #usuario2 = Usuario("Chanchito", "Feliz")

# #print(usuario.nombre,usuario.apellido,usuario2.nombre,usuario.apellido)



# usuario.saludo()
# usuario.nombre = "Chanchito"
# usuario.saludo()
# #del usuario.nombre()
# #usuario.saludo()
# #del usuario
# #print(usuario)

# admin = Admin("Super", "Feliz")
# admin.saludo()
# admin.superSaludo()
# usuario.superSaludo()

class Animal:
        def __init__(self, nombre, onomatopeya):
            self.nombre = nombre
            self.onomatopeya = onomatopeya
        def saludo(self):
            print("Hola, soy un", self.tipo, "y mi sonido es", self.onomatopeya)


class Gato(Animal):
    tipo = "gato"
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print("Hola, soy un gato extendido")

class Perro(Animal):
    tipo = "perro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("instanciando un perro")

class Canario(Animal):
    tipo = "ave"

gato = Gato("Fluffy", "maullido")
gato.saludo()

perro = Perro("Firulais", "ladrido")
perro.saludo()

canario = Canario("Piolín", "trino")
canario.saludo()