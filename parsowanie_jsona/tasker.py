from src.App import App
from src.json.Importer import Importer
from src.json.Exporter import Exporter

# Inicjalizacja Importera i Exportera
filename = "taski.json"
importer = Importer(filename)
exporter = Exporter(filename)

print("Rozpoczynanie pracy aplikacji... \n")
application = App(importer,exporter,filename)

while application.is_active:
    application.print_data()
    application.get_input()
    application.execute_command()
del application

print("Do zobaczenia! \n")
