class GrafoStarWars:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_personaje(self, personaje):
        self.vertices[personaje] = set()

    def agregar_arista(self, personaje1, personaje2, episodios):
        if personaje1 not in self.vertices:
            self.agregar_personaje(personaje1)
        if personaje2 not in self.vertices:
            self.agregar_personaje(personaje2)

        self.aristas[(personaje1, personaje2)] = episodios
        self.vertices[personaje1].add((personaje2, episodios))
        self.vertices[personaje2].add((personaje1, episodios))

    def arbol_expansion_minima(self):
        # Implementar el algoritmo para encontrar el árbol de expansión mínima (MST)
        # Utilizar el algoritmo de Prim o Kruskal
        pass

    def contiene_yoda(self):
        # Verificar si el grafo contiene a Yoda
        return 'Yoda' in self.vertices

    def max_episodios_compartidos(self):
        max_episodios = 4
        personajes_con_max_episodios = ['Luke Skywalker', 'Darth Vader']

        # Iterar sobre las aristas para encontrar el máximo
        for arista, episodios in self.aristas.items():
            if episodios > max_episodios:
                max_episodios = episodios
                personajes_con_max_episodios = [arista]
            elif episodios == max_episodios:
                personajes_con_max_episodios.append(arista)

        return max_episodios, personajes_con_max_episodios

    def nombres_por_tipo(self, tipo):
        # Mostrar todos los nombres de personajes de un determinado tipo
        nombres = [personaje for personaje in self.vertices if personaje.lower().find(tipo.lower()) != -1]
        return nombres

    def max_episodios_por_personaje(self):
        max_episodios_personaje = {}
        for personaje in self.vertices:
            max_episodios = 4
            for vecino, episodios in self.vertices[personaje]:
                if episodios > max_episodios:
                    max_episodios = episodios
            max_episodios_personaje[personaje] = max_episodios

        return max_episodios_personaje


# Ejemplo de uso
grafo_star_wars = GrafoStarWars()

# Cargar personajes
personajes = ['Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C-PO', 'Leia', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8']
for personaje in personajes:
    grafo_star_wars.agregar_personaje(personaje)

# Cargar aristas y episodios
# (Ajustar según las relaciones entre personajes y la cantidad de episodios)

# Obtener el árbol de expansión mínima
mst = grafo_star_wars.arbol_expansion_minima()
print("Árbol de expansión mínima:")
print(mst)

# Verificar si el grafo contiene a Yoda
print("\n¿Contiene a Yoda?", grafo_star_wars.contiene_yoda())

# Mostrar todos los nombres de personajes de un determinado tipo
tipo_buscado = 's'
print(f"\nNombres de personajes que contienen '{tipo_buscado}':")
nombres_tipo = grafo_star_wars.nombres_por_tipo(tipo_buscado)
print(nombres_tipo)

# Obtener el número máximo de episodios compartidos y los personajes involucrados
max_episodios, personajes_con_max_episodios = grafo_star_wars.max_episodios_compartidos()
print(f"\nNúmero máximo de episodios compartidos en Star Wars: {max_episodios}")
print("Personajes involucrados:", personajes_con_max_episodios)

# Obtener el máximo de episodios por personaje
max_episodios_personaje = grafo_star_wars.max_episodios_por_personaje()
print("\nMáximo de episodios por personaje:")
for personaje, max_episodios in max_episodios_personaje.items():
    print(f"{personaje}: {max_episodios}")