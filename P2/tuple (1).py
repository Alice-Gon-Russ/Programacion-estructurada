"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
paises=["México","Brasil","Canada","Español"]

pais1 = {
    "nombre": "México",
    "capital": "Ciudad de México",
    "poblacion": "126000000",
    "idioma": "español",
    "status": True
}

pais2 = {
    "nombre": "Brasil",
    "capital": "Brasilia",
    "poblacion": "214000000",
    "idioma": "portugués",
    "status": True
}

pais3 = {
    "nombre": "Canadá",
    "capital": "Ottawa",
    "poblacion": "38000000",
    "idioma": ["inglés", "francés"],
    "status": True
}

print(pais1)
for i in pais1:
    print(f"{i}={pais1[i]}")

#Agregar un atributo de un item o atributo que ya exista 
pais1.update({"altitud":2500})
for i in pais1:
    print(f"{i}={pais1[i]}")

#Quitar el ultimo atributo de un objeto
pais1.popitem()
for i in pais1:
    print(f"{i}={pais1[i]}")

#Quitar un atributo en especifico de un objeto
pais1.pop("status")
for i in pais1:
    print(f"{i}={pais1[i]}")