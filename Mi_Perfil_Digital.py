#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Jean Paul Mejia angarita"
edad = 14
estatura = 1.62
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("Jean2012M", "00_jean")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Aló Aló", "artista": "LuisRa", "duracion": "3:22"},
{"titulo": "Habla Claro", "artista": "LuisRa", "duracion": "3:55"},
{"titulo": "La María", "artista": "Luister La Voz", "duracion": "3:38"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
