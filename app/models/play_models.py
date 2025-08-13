import random
from dataclasses import dataclass
from typing import List, Dict, Optional


class Persona:
    def __init__(self, nombre: str, edad: int = None, sexo: str = None):
        self.nombre = nombre
        # if sexo not in ['H', 'M']:
        #     raise ValueError("Sexo puede ser 'H' o 'M'.")
        self.sexo = sexo
        # if edad is not None and edad < 10:
        #     raise ValueError("Has puesto una edad muy baja")
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"


class Jugador(Persona):
    def __init__(self, nombre: str, sexo: str = None, edad: int = None):
        super().__init__(nombre, edad, sexo)

    def __str__(self):
        return f"Jugador: {self.nombre}, sexo {'hombre' if self.sexo == 'H' else 'mujer'}, edad {self.edad}"


class Pregunta:
    def __init__(self, texto: str, categoria: str):
        self.texto = texto
        self.categoria = categoria

    def __str__(self):
        return f"Pregunta: {self.texto}, Categoría: {self.categoria}"


class BancoPreguntas:
    def __init__(self):
        self._por_categoria: Dict[str, List[Pregunta]] = {}

    def agregar(self, p: Pregunta):
        self._por_categoria.setdefault(p.categoria, []).append(p)

    def eliminar(self, texto: str) -> bool:
        for cat, lista in self._por_categoria.items():
            for i, p in enumerate(lista):
                if p.texto == texto:
                    del lista[i]
                    return True
        return False

    def categorias(self) -> List[str]:
        return sorted(self._por_categoria.keys())

    def aleatoria(self, categoria: Optional[str]) -> Optional[Pregunta]:
        # Filtra por categoría (o todas), edad y nivel
        candidatas = []
        cats = [categoria] if categoria else self.categorias()
        for cat in cats:
            for p in self._por_categoria.get(cat, []):
                # if (permitir_18 or not p.es_18) and p.intensidad <= max_intensidad:
                candidatas.append(p)
        return random.choice(candidatas) if candidatas else None




class Juego:
    def __init__(self, jugadores: list, banco: BancoPreguntas):
        self.jugadores = jugadores
        self.banco = banco
        self.turno = 0
        self.ultima_pregunta = None
        self.jugador_actual = None

    def siguiente_turno(self, categoria: Optional[str] = None) -> Optional[Pregunta]:
        self.jugador_actual = self.jugadores[self.turno % len(self.jugadores)]
        # otros = [j for j in self.jugadores if j != self.jugador_actual]
        # self.jugador_objetivo = random.choice(otros)

        pregunta = self.banco.aleatoria(categoria)
        self.ultima_pregunta = pregunta
        self.turno += 1
        return pregunta  # Devuelve la pregunta para mostrarla en Streamlit
        #
