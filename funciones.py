import re
import pandas as pd
from datetime import *
import sys

RED = '\033[91m'
ENDC = '\033[0m'




# funcion para clasificar el estado segun el ms
def statusMs(ms):
    if ms < 300:
        return "Óptimo"
    elif ms < 700:
        return "Lento"
    else:
        return "Crítico"



def AnalisisGeneral(readerLog):
    timeLog = re.compile(r"\[(.*?)\]\s+INFO:\s+(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s+(\S+)\s+[-–]\s+(\d+)ms")
    records = []
    for line in readerLog:
        match = timeLog.search(line)
        if match:
            timestamp, method,endpoint, duration = match.groups()
            records.append({
                "TIMESTAMP": pd.to_datetime(timestamp),
                    "METHOD": method,
                    "ENDPOINT": endpoint,
                    "LATENCY": f"{int(duration)}ms",
                    "STATUS" : statusMs(int(duration))
            })
    df = pd.DataFrame(records)
    return df

def AnalisisStatus(readerLog):
    timeLog = re.compile(r"\[(.*?)\]\s+INFO:\s+(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s+(\S+)\s+[-–]\s+(\d+)ms")
    records = []
    for line in readerLog:
        match = timeLog.search(line)
        if match:
            timestamp, method,endpoint, duration = match.groups()
            if int(duration) >= 500:
                records.append({
                    "TIMESTAMP": pd.to_datetime(timestamp),
                    "METHOD": method,
                    "ENDPOINT": endpoint,
                    "LATENCY": f"{int(duration)}ms",
                    "STATUS" : statusMs(int(duration))
                })
    df = pd.DataFrame(records)
    return df

def AnalisisFecha(readerLog):
    timeLog = re.compile(r"\[(.*?)\]\s+INFO:\s+(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s+(\S+)\s+[-–]\s+(\d+)ms")
    records = []
    filtro = input(f"Ingrese La fecha que desea filtrar en formato (2025-01-01)")
    try:
        fecha_filtrada = datetime.strptime(filtro, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de fecha inválido. Use YYYY-MM-DD.")

    for line in readerLog:
        match = timeLog.search(line)
        if match:
            timestamp_str, method,endpoint, duration = match.groups()
            timestamp = pd.to_datetime(timestamp_str)
            if timestamp.date() == fecha_filtrada:
                records.append({
                    "TIMESTAMP": pd.to_datetime(timestamp),
                    "METHOD": method,
                    "ENDPOINT": endpoint,
                    "LATENCY": f"{int(duration)}ms",
                    "STATUS" : statusMs(int(duration))
                })
    df = pd.DataFrame(records)
    return df

def AnalisisMetodo(readerLog):
    metodos_validos = {"GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"}
    timeLog = re.compile(r"\[(.*?)\]\s+INFO:\s+(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s+(\S+)\s+[-–]\s+(\d+)ms")
    records = []    
    while True:
        filtro = input("Ingrese el nombre del método por el cual quiere filtrar (POST, GET, PUT, etc...): ").strip().upper()
        if filtro in metodos_validos:
            for line in readerLog:
                match = timeLog.search(line)
                if match:
                    timestamp, method,endpoint, duration = match.groups()
                    if method == filtro:
                        records.append({
                            "TIMESTAMP": pd.to_datetime(timestamp),
                            "METHOD": method,
                            "ENDPOINT": endpoint,
                            "LATENCY": f"{int(duration)}ms",
                            "STATUS" : statusMs(int(duration))
                        })
                df = pd.DataFrame(records)
            return df
        else:
            print(f"{RED}{"="*27}{"ERROR"}{"="*28}{ENDC}\n")
            print(f"{RED}Método inválido. Intenta nuevamente.{ENDC} ")
            print(f"\n{RED}{"="*59}{ENDC}\n")

        

            




           

    

def AnalisisEnd(readerLog):
    timeLog = re.compile(r"\[(.*?)\]\s+INFO:\s+(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s+(\S+)\s+[-–]\s+(\d+)ms")
    records = []
    filtro = input(f"Ingrese la ruta por la cual quiere filtrar (/login , /checkout, /payment, etc...)").strip().lower()
    # try:
    #     fecha_filtrada = datetime.strptime(filtro, "%Y-%m-%d").date()
    # except ValueError:
    #     print("Formato de fecha inválido. Use YYYY-MM-DD.")

    for line in readerLog:
        match = timeLog.search(line)
        if match:
            timestamp, method,endpoint, duration = match.groups()
            if endpoint == filtro:
                records.append({
                    "TIMESTAMP": pd.to_datetime(timestamp),
                    "METHOD": method,
                    "ENDPOINT": endpoint,
                    "LATENCY": f"{int(duration)}ms",
                    "STATUS" : statusMs(int(duration))
                })
    df = pd.DataFrame(records)
    return df


