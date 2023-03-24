from dataclasses import dataclass


@dataclass
class Elemento:

    nombre: str

    # isinstance: para comprobar si un objeto es una instancia de una determinada clase o de una subclase de esa clase.

    def __eq__(self, other):
        return self.nombre == other.nombre


class Conjunto:
    contador = 0

    # type(self): devuelve el tipo de la instancia actual, es decir, devuelve la clase a la que pertenece el objeto actual.
    # __id: Se consideran atributos "privados".

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.elementos = []
        self.__id = type(self).contador
        type(self).contador += 1

    # @property: Esto permite que se acceda al valor del atributo __id utilizando sintaxis de punto, pero no permite asignar un valor nuevo
    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        for busqueda in self.elementos:
            if busqueda.nombre == elemento.nombre:
                return True
            return False

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    # __add__: Crea un nuevo objeto de la clase Conjunto a partir de la concatenación de los nombres de los conjuntos que se están sumando.

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} O {otro_conjunto.nombre}")
        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1: 'Conjunto', conjunto2: 'Conjunto') -> 'Conjunto':
        elementos_comunes = [e for e in conjunto1.elementos if conjunto2.contiene(e)]
        nombre = f"{conjunto1.nombre} Intersectado {conjunto2.nombre}"
        return cls(elementos=elementos_comunes, nombre=nombre)

    def __str__(self):
        elementos_str = ", ".join([si.nombre for si in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"