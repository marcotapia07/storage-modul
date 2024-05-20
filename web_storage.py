import json

localStorage = {}

def store_data(key, value):
    
    # Almacena un par clave-valor en el almacenamiento web.
    localStorage[key] = value

def retrieve_data(key):
    
    # Recupera el valor asociado a una clave del almacenamiento web.
    return localStorage.get(key, None)

def clear_storage():
    
    # Elimina todo el contenido del almacenamiento web.
    localStorage.clear()
