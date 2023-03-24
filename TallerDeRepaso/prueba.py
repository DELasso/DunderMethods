from dataclasses import dataclass
from typing import List


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre


@dataclass
class Conjunto:
    elementos: List[Elemento]
    nombre: str = None
    __contador: int = 0

    def __post_init__(self):
        Conjunto.__contador += 1
        self.__id = Conjunto.__contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return elemento in self.elementos

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro: 'Conjunto') -> 'Conjunto':
        nuevo = Conjunto(elementos=self.elementos.copy(), nombre=self.nombre)
        for elemento in otro.elementos:
            if not nuevo.contiene(elemento):
                nuevo.agregar_elemento(elemento)
        return nuevo

    def __add__(self, otro: 'Conjunto') -> 'Conjunto':
        return self.unir(otro)

    @classmethod
    def intersectar(cls, conjunto1: 'Conjunto', conjunto2: 'Conjunto') -> 'Conjunto':
        elementos_comunes = [e for e in conjunto1.elementos if conjunto2.contiene(e)]
        nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        return cls(elementos=elementos_comunes, nombre=nombre)

