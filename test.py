#!/usr/bin/env python3
import os
import sys
from time import sleep
from funciones import *

class TerminalMenu:
    def __init__(self):
        # Configuración de colores
        self.RED = '\033[91m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.BLUE = '\033[94m'
        self.PURPLE = '\033[95m'
        self.CYAN = '\033[96m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self, title):
        print(f"\n{self.YELLOW}{'='*50}{self.ENDC}")
        print(f"{self.GREEN}{self.BOLD}{title.center(50)}{self.ENDC}")
        print(f"{self.YELLOW}{'='*50}{self.ENDC}\n")


    def display_decorator1(self):
        print(f"\n{self.GREEN}{"="*59}{self.ENDC}\n")
    
    def display_decorator2(self):
        print(f"\n{self.GREEN}{"="*20}{"ESCANEO COMPLETADO"}{"="*20}{self.ENDC}\n")

    def display_decorator3(self):
        print(f"\n{self.RED}{"="*59}{self.ENDC}\n")
    
    def display_decorator4(self):
        print(f"\n{self.RED}{"="*27}{"ERROR"}{"="*28}{self.ENDC}\n")

    def main_menu(self):
        while True:
            self.clear_screen()
            self.display_header("MENÚ PRINCIPAL - LogAnalyzer")
            
            print(f"{self.BLUE}1.{self.ENDC} Analisis General")
            print(f"{self.BLUE}2.{self.ENDC} Filtrar por Fecha especifica")
            print(f"{self.BLUE}3.{self.ENDC} Mostrar Logs de latencia elevada")
            print(f"{self.BLUE}4.{self.ENDC} Filtrar por Metodo")
            print(f"{self.BLUE}5.{self.ENDC} Filtrar por Endpoint especifico")
            print(f"{self.RED}6.{self.ENDC} Salir")
            
            choice = input(f"\n{self.YELLOW}Seleccione una opción [1-4]: {self.ENDC}")

            if choice == '1':
                logFile = input("Ingresa la ruta del archivo de log (por ejemplo ./prueba.log): ").strip()
                if os.path.exists(logFile):
                    with open(logFile, 'r', encoding='utf-8', errors='ignore') as log:
                        readerLog = log.readlines()
                        resultado = AnalisisGeneral(readerLog)
                        self.display_decorator2()
                        print(resultado)
                        self.display_decorator1()
                        input("pulsa cualquier tecla para continuar...")
                else:
                    self.display_decorator4()
                    print("Error: El archivo no existe o la ruta es incorrecta.")
                    self.display_decorator3()
                    input("pulsa cualquier tecla para continuar...")


            elif choice == '2':
                logFile = input("Ingresa la ruta del archivo de log (por ejemplo ./prueba.log): ").strip()
                if os.path.exists(logFile):
                    with open(logFile, 'r', encoding='utf-8', errors='ignore') as log:
                        readerLog = log.readlines()
                        resultado = AnalisisFecha(readerLog)
                        self.display_decorator2()
                        print(resultado)
                        self.display_decorator1()
                        input("pulsa cualquier tecla para continuar...")
                else:
                    self.display_decorator4()
                    print("Error: El archivo no existe o la ruta es incorrecta.")
                    self.display_decorator3()
                    input("pulsa cualquier tecla para continuar...")



            elif choice == '3':
                logFile = input("Ingresa la ruta del archivo de log (por ejemplo ./prueba.log): ").strip()
                if os.path.exists(logFile):
                    with open(logFile, 'r', encoding='utf-8', errors='ignore') as log:
                        readerLog = log.readlines()
                        resultado = AnalisisStatus(readerLog)
                        self.display_decorator2()
                        print(resultado)
                        self.display_decorator1()
                        input("pulsa cualquier tecla para continuar...")
                else:
                    self.display_decorator4()
                    print("Error: El archivo no existe o la ruta es incorrecta.")
                    self.display_decorator3()
                    input("pulsa cualquier tecla para continuar...")

            
            elif choice == '4':
                logFile = input("Ingresa la ruta del archivo de log (por ejemplo ./prueba.log): ").strip()
                if os.path.exists(logFile):
                    with open(logFile, 'r', encoding='utf-8', errors='ignore') as log:
                        readerLog = log.readlines()
                        resultado = AnalisisMetodo(readerLog)
                        self.display_decorator2()
                        print(resultado)
                        self.display_decorator1()
                        input("pulsa cualquier tecla para continuar...")
                else:
                    self.display_decorator4()
                    print("Error: El archivo no existe o la ruta es incorrecta.")
                    self.display_decorator3()
                    input("pulsa cualquier tecla para continuar...")


            elif choice == '5':
                logFile = input("Ingresa la ruta del archivo de log (por ejemplo ./prueba.log): ").strip()
                if os.path.exists(logFile):
                    with open(logFile, 'r', encoding='utf-8', errors='ignore') as log:
                        readerLog = log.readlines()
                        resultado = AnalisisEnd(readerLog)
                        self.display_decorator2()
                        print(resultado)
                        self.display_decorator1()
                        input("pulsa cualquier tecla para continuar...")
                else:
                    self.display_decorator4()
                    print("Error: El archivo no existe o la ruta es incorrecta.")
                    self.display_decorator3()
                    input("pulsa cualquier tecla para continuar...")




    def run(self):
        try:
            self.main_menu()
        except KeyboardInterrupt:
            print(f"\n{self.RED}\nInterrupción recibida. Saliendo...{self.ENDC}")
            sys.exit(1)

if __name__ == "__main__":
    menu = TerminalMenu()
    menu.run()