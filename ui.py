from web_storage import store_data, retrieve_data, clear_storage

def handle_form_submission(key, value):
    # Maneja el envío del formulario y llama a las funciones del módulo de Almacenamiento Web.
    store_data(key, value)
    data = retrieve_data(key)
    display_data(data)

def display_data(data):
    # Muestra los datos almacenados en la página web.
    print(f"Datos almacenados: {data}")

