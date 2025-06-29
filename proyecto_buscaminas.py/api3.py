import requests
import json  

class API_Configuracion:
    def __init__(self):
        self.base_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main"
        self.jugador = None
        self.dificultad = {
            "easy": "Fácil (10% minas)",
            "medium": "Medio (30% minas)", 
            "hard": "Difícil (60% minas)",
            "impossible": "Imposible (80% minas)"
        }

    def get_config(self, dificultad):
        """Obtiene configuración y calcula minas correctamente"""
        response = requests.get(f"{self.base_url}/config.json")
        response.raise_for_status()
        config = response.json()            
        if not all(key in config.get("global", {}) for key in ["board_size", "quantity_of_mines"]):
            raise ValueError("JSON inválido")
            
        tamaño = config["global"]["board_size"]
        porcentaje = config["global"]["quantity_of_mines"].get(dificultad)
            
        if porcentaje is None:
            raise ValueError(f"Dificultad '{dificultad}' no existe")
            
        total = tamaño[0] * tamaño[1]
        minas = max(1, int(total * porcentaje))

            
        return {
            "filas": tamaño[0],
            "columnas": tamaño[1],
            "minas": minas
            }
        

    def guardar_record(self, jugador, tiempo, config):
        """Guarda el record del jugador en records.json"""
        try:
            with open('records.json', 'r') as f:
                records = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            records = []
        
        # Separar nombre y apellido
        nombre, apellido = jugador.split(' ', 1) if ' ' in jugador else (jugador, '')
        
        nuevo_record = {
            "first_name": nombre,
            "last_name": apellido,
            "time": tiempo
        }
        
        records.append(nuevo_record)
        records = sorted(records, key=lambda x: x['time'])[:3]  # Top 3 por tiempo
        
        with open('records.json', 'w') as f:
            json.dump(records, f, indent=4)
        
        return records

    def obtener_top_records(self):
        """Obtiene los 3 mejores records"""
        try:
            with open('records.json', 'r') as f:
                records = json.load(f)
                return sorted(records, key=lambda x: x['tiempo'])[:3]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
