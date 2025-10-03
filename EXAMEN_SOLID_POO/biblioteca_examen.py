
# LUIS FERNANDO FERNANDEZ GARCIA

"""
EXAMEN PRINCIPIOS SOLID - 2 HORAS
Sistema de Mini-Biblioteca
INSTRUCCIONES:
1. NO modifiques este archivo
2. Crea archivos nuevos para tus refactorizaciones
3. Asegúrate que el código siga funcionando
CÓDIGO BASE CON VIOLACIONES DELIBERADAS DE SOLID
"""

from abc import ABC, abstractmethod

#EJERCICIO 1:
#Esta es la clase abstracta que usare para generar estrategias de busqueda
class BusquedaStrategy(ABC):
    @abstractmethod
    def buscar(self, libros, valor):
        pass


#Estrategias que usare para buscar aqui es por titulo
class BusquedaPorTitulo(BusquedaStrategy):
    def buscar(self, libros, valor):
        return [libro for libro in libros if valor.lower() in libro.titulo.lower()]

#Estrategias que usare para buscar aqui es por autor
class BusquedaPorAutor(BusquedaStrategy):
    def buscar(self, libros, valor):
        return [libro for libro in libros if valor.lower() in libro.autor.lower()]

#Estrategias que usare para buscar aqui es por ISBN
class BusquedaPorISBN(BusquedaStrategy):
    def buscar(self, libros, valor):
        return [libro for libro in libros if libro.isbn == valor]


#Este es la busqueda por disponibilidad para que encuentre los que estan disponibles
class BusquedaPorDisponibilidad(BusquedaStrategy):
    def buscar(self, libros, valor):
        disponible = valor.lower() == "true"
        return [libro for libro in libros if libro.disponible == disponible]
#EJERCICIO1

#EJERCICIO2
class ValidadorBiblioteca:
    def validar_libro(self, titulo, autor, isbn):
        if not titulo or len(titulo) < 2:
            return "Error: Título inválido"
        if not autor or len(autor) < 3:
            return "Error: Autor inválido"
        if not isbn or len(isbn) < 10:
            return "Error: ISBN inválido"
        return None
    
    def validar_usuario(self, usuario):
        if not usuario or len(usuario) < 3:
            return "Error: Nombre de usuario inválido"
        return None
    
class RepositorioBiblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self.archivo = archivo

    def guardar(self, libros, prestamos):
        with open(self.archivo, "w") as f:
            f.write(f"Libros: {len(libros)}\n")
            f.write(f"Préstamos: {len(prestamos)}\n")

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                return f.read()
        except FileNotFoundError:
            return None
        
class ServicioNotificaciones:
    def enviar(self, usuario, libro):
        print(f"[NOTIFICACIÓN] {usuario}: Préstamo de '{libro}'")
#EJERCICIO 2

#EJERICIO 3
#La clase abstracta de repositorio con sus metodos
class IRepositorio(ABC):
    @abstractmethod
    def guardar(self, libros, prestamos):
        pass

    @abstractmethod
    def cargar(self):
        pass

#Esta clase ahora hereda de la interfaz de repositorio y es la que maneja archivos 
# y sustituira a repositorio biblioteca
class RepositorioArchivo(IRepositorio):
    def __init__(self, archivo="biblioteca.txt"):
        self.archivo = archivo

    def guardar(self, libros, prestamos):
        with open(self.archivo, "w") as f:
            f.write(f"Libros: {len(libros)}\n")
            f.write(f"Préstamos: {len(prestamos)}\n")

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                return f.read()
        except FileNotFoundError:
            return None
#EJERCICIO3

class Libro:
    def __init__(self, id, titulo, autor, isbn, disponible=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
class Prestamo:
    def __init__(self, id, libro_id, usuario, fecha):
        self.id = libro_id
        self.libro_id = libro_id
        self.usuario = usuario
        self.fecha = fecha
        self.devuelto = False

# VIOLACIÓN: Esta clase hace DEMASIADAS cosas (SRP)
# VIOLACIÓN: Búsqueda con if/elif (OCP)
# VIOLACIÓN: Dependencia directa de implementación (DIP)
class SistemaBiblioteca:
    #aqui en el constructor se reciben las nuevas clases que hemos creado
    def __init__(self,validador,repositorio,notificador):
        self.libros = []
        self.prestamos = []
        self.contador_libro = 1
        self.contador_prestamo = 1
        self.archivo = "biblioteca.txt"

        #Aquí inyecto las nuevas clases que haran la parte de validar, cargar y notificar
        self.validador = validador
        self.repositorio = repositorio
        self.notificador = notificador

    
    # VIOLACIÓN SRP: Mezcla validación + lógica de negocio + persistencia
    def agregar_libro(self, titulo, autor, isbn):
        # Validación inline
        # if not titulo or len(titulo) < 2:
        #     return "Error: Título inválido"
        # if not autor or len(autor) < 3:
        #     return "Error: Autor inválido"
        # if not isbn or len(isbn) < 10:
        #     return "Error: ISBN inválido"

        #EJERCICIO 2
        #Nueva validacion:
        error = self.validador.validar_libro(titulo,autor,isbn) 
        if error: #En caso de que un if de la antigua validacion llegara a ocurrir
                return error #Se devuelve aca
        
        # Lógica de negocio
        libro = Libro(self.contador_libro, titulo, autor, isbn)
        self.libros.append(libro)
        self.contador_libro += 1
    
        #EJERCICIO 2
        # Cambiamos la persistencia por la funcion de la clase repositorio
        self.repositorio.guardar(self.libros, self.prestamos)

        # Antigua persistencia self._guardar_en_archivo()
        
        return f"Libro '{titulo}' agregado exitosamente"
    
    #Este es el metodo que antes tenia muchos if anidados, lo cual hacia que si querias que implementara nuevas formas tuvieras que programarlo, por lo que ahora se le inyecta una clase
    def buscar_libro(self, estrategia: BusquedaStrategy, valor):
        return estrategia.buscar(self.libros, valor)
    
    # VIOLACIÓN SRP: Mezcla validación + lógica + persistencia
    def realizar_prestamo(self, libro_id, usuario):
        # Validación: La modificamos para que use la nueva validacion
        error = self.validador.validar_usuario(usuario)
        if error:
            return error
        
        #ANTIGUA VALIDACION
        # if not usuario or len(usuario) < 3:
        #     return "Error: Nombre de usuario inválido"
        
        # Buscar libro
        libro = None
        for l in self.libros:
            if l.id == libro_id:
                libro = l
                break
        
        if not libro:
            return "Error: Libro no encontrado"
        
        if not libro.disponible:
            return "Error: Libro no disponible"
        
        # Lógica de negocio
        from datetime import datetime
        prestamo = Prestamo(
            self.contador_prestamo,
            libro_id,
            usuario,
            datetime.now().strftime("%Y-%m-%d")
        )
        
        self.prestamos.append(prestamo)
        self.contador_prestamo += 1
        libro.disponible = False
        
        # Persistencia: Cambiamos por la nueva funcion de la clase creada
        self.repositorio.guardar(self.libros, self.prestamos)
        # self._guardar_en_archivo()
        
        # Notificación la cambiamos tambien por la nueva funcion de la clase creada
        self.notificador.enviar(usuario, libro.titulo)
        #self._enviar_notificacion(usuario, libro.titulo)
        
        return f"Préstamo realizado a {usuario}"
    
    def devolver_libro(self, prestamo_id):
        prestamo = None
        for p in self.prestamos:
            if p.id == prestamo_id:
                prestamo = p
                break
        
        if not prestamo:
            return "Error: Préstamo no encontrado"
        
        if prestamo.devuelto:
            return "Error: Libro ya devuelto"
        
        for libro in self.libros:
            if libro.id == prestamo.libro_id:
                libro.disponible = True
                break
        
        prestamo.devuelto = True

        #Usamso el nuevo metodo que creamos 
        self.repositorio.guardar(self.libros, self.prestamos)

        
        return "Libro devuelto exitosamente"
    
    def obtener_todos_libros(self):
        return self.libros
    
    def obtener_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]
    
    def obtener_prestamos_activos(self):
        return [p for p in self.prestamos if not p.devuelto]
    
    # VIOLACIÓN SRP: Persistencia mezclada
    def _guardar_en_archivo(self):
        with open(self.archivo, 'w') as f:
            f.write(f"Libros: {len(self.libros)}\n")
            f.write(f"Préstamos: {len(self.prestamos)}\n")
    
    def _cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r') as f:
                data = f.read()
            return True
        except:
            return False
    
    # VIOLACIÓN SRP: Notificación es otra responsabilidad
    def _enviar_notificacion(self, usuario, libro):
        print(f"[NOTIFICACIÓN] {usuario}: Préstamo de '{libro}'")
# VIOLACIÓN DIP: Dependencia directa de implementación
def main():
    validador = ValidadorBiblioteca()
    #repositorio = RepositorioBiblioteca() La antigua clase que se encargaba de Repositorio
    repositorio = RepositorioArchivo() #La nueva clase que se encarga del repositorio que ademas hereda de la interfaz
    notificador = ServicioNotificaciones()

    sistema = SistemaBiblioteca(validador, repositorio, notificador)
    
    print("=== AGREGANDO LIBROS ===")
    print(sistema.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", "9780060883287"))
    print(sistema.agregar_libro("El Principito", "Antoine de Saint-Exupéry", "9780156012195"))
    print(sistema.agregar_libro("1984", "George Orwell", "9780451524935"))
    
    print("\n=== BÚSQUEDA POR AUTOR ===") #EJERCICIO 1
    resultados = sistema.buscar_libro(BusquedaPorAutor(), "Gabriel García Márquez")#Aqui ahora se le inyecta la nueva estrategia, busqueda pro autor que implementamos
    for libro in resultados:
        print(f"- {libro.titulo} por {libro.autor}")

    print("\n=== BÚSQUEDA POR TITULO ===")#EJERCICIO 1
    resultados = sistema.buscar_libro(BusquedaPorTitulo(),"El Principito") #Aquí estoy probando que funcione el metodo buscar por titulo
    for libro in resultados:
        print(f"- {libro.titulo} por {libro.autor}")
    
    print("\n=== BÚSQUEDA POR DISPONIBILIDAD ===")#EJERCICIO 1
    resultados = sistema.buscar_libro(BusquedaPorDisponibilidad(),"true") #Aquí estoy probando que funcione el metodo buscar por disponibilidad
    for libro in resultados:
        print(f"- {libro.titulo} por {libro.autor}")
    
    print("\n=== REALIZAR PRÉSTAMO ===")
    print(sistema.realizar_prestamo(1, "Juan Pérez"))
    
    print("\n=== LIBROS DISPONIBLES ===")
    disponibles = sistema.buscar_libro(BusquedaPorDisponibilidad(),"true") #Aquí cambie para que use el metodo de disponibilidad mejor y si funciona correctamente despues del prestamo
    for libro in disponibles:
        print(f"- {libro.titulo} por {libro.autor}")
    
    print("\n=== DEVOLVER LIBRO ===")
    print(sistema.devolver_libro(1))
    
    print("\n=== PRÉSTAMOS ACTIVOS ===")
    activos = sistema.obtener_prestamos_activos()
    print(f"Total de préstamos activos: {len(activos)}")
if __name__ == "__main__":
    main()
