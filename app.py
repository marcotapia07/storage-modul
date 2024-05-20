from ui import *
from web_storage import clear_storage, retrieve_data

# Punto de entrada de la aplicación
if __name__ == "__main__":
    # Iniciar la aplicación y manejar el flujo de ejecución
    clear_storage()
    handle_form_submission("bgcolor", "3CFF26")
    data = retrieve_data("bgcolor")
    display_data(data)
