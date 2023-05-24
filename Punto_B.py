diccionario = {
    "humanos": {
        "clases": {
            "guerrero": {
                "id": "01",
                "vida": "400 %",
                "ataque": "Golpe celestial",
                "defensa": "Escudero",
                "poder magico": "Invisibilidad"
            },
            "jinete": {
                "id": "02",
                "vida": "300 %" ,
                "ataque": "Spirit Bom",
                "defensa": "Reinhardt",
                "poder magico": "Bola de fuego"
            },
            "mago": {
                "id": "03",
                "vida": "700 %",
                "ataque": "Danza de las sombras",
                "defensa": "Orisa",
                "poder magico": "Teletransportación"
            },
            "recolector": {
                "id": "04",
                "vida": "800 %",
                "ataque": "Onda de choque",
                "defensa": "Mei",
                "poder magico": "Escudo de piedra"
            },
            "observador": {
                "id": "05",
                "vida": "500 %",
                "ataque": "Corte mortal",
                "defensa": "Tracer",
                "poder magico": "ilusión óptica"
            }
        }
    },
    "orcos": {
        "clases": {
            "guerrero": {
                "id": "06",
                "vida": "500 %",
                "ataque": "Lluvia de flechas",
                "defensa": "Rook",
                "poder magico": "Escudo Arcano"
            },
            "chaman": {
                "id": "07",
                "vida": "800 %",
                "ataque": "Golpe de trueno",
                "defensa": "Garen",
                "poder magico": "Control mental"
            },
            "jinete": {
                "id": "08",
                "vida": "800 %",
                "ataque": "Martillo de la justicia",
                "defensa": "Braum",
                "poder magico": "Telequinesis"
            }
        }
    }
}



def depurar(diccionario):
    # Iterar sobre cada raza en el diccionario
    for raza, info_raza in diccionario.items():
        print(f"Raza: {raza}")  # Imprimir el nombre de la raza

        # Iterar sobre cada clase dentro de la raza
        for clase, info_clase in info_raza["clases"].items():
            print(f"Clase: {clase}")  # Imprimir el nombre de la clase

            # Iterar sobre cada atributo dentro de la clase
            for atributo, valor in info_clase.items():
                print(f"{atributo}: {valor}")  # Imprimir el atributo y su valor

            print("----")  # Imprimir línea de separación entre clases

        print("====")  # Imprimir línea de separación entre razas

# Llamada a la función
depurar(diccionario)
