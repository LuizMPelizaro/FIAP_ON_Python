import getpass
from datetime import datetime

print(f"Usuario........:{getpass.getuser()}\n"
      f"Data Completa..:{datetime.now()}\n"
      f"Dia............:{datetime.now().day}\n"
      f"Mês............:{datetime.now().month}\n"
      f"Ano............:{datetime.now().year}\n"
      f"Hora...........:{datetime.now().hour}\n"
      f"Minuto.........:{datetime.now().minute}\n"
      f"Segundo........:{datetime.now().second}")
