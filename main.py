import os
import argparse
import pandas as pd
from world_simulation import World
from tools.save import save_xlsx_file

def create_result_dir() -> None :
    if os.path.exists("./results") == False :
        os.mkdir("./results")
    
def get_args() -> argparse.Namespace:
    """Argument a passer en ligne de commande pour modifier la simulation"""
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--file", type=str , help="File name to store data of world")
    parser.add_argument("--humans", type=int, help="Number of human at the start of simulation")
    parser.add_argument("--countries", type=int, help="Set the number of countries in world simulation")
    parser.add_argument("--gap", type=int, help="number of days between each loop")
    parser.add_argument("--limit", type=int, help="Limit years of simulation")
    
    args = parser.parse_args()
    return args
    
def set_error(error_text : str) -> None:
    print(error_text)
    exit(1)

if __name__ == "__main__" :
    # Création du fichier de résultat (./results) dans lequelle seront stocker tout les resultats de simulation
    create_result_dir()
    
    GAP = 0
    LIMIT = 0
    
    # Récupérer les arguments passer en ligne de commande et gérer les erreurs en cas de manque d'arguments
    args = get_args()
    if args.file == None : set_error("La varible '--file' n'a pas été défini")
    if args.humans == None : set_error("La variable '--humans' n'a pas été défini")
    if args.countries == None or args.countries > 9 : set_error("La variable '--countries' n'a pas été défini, ou sa valeur est supérieur à 9")
    if args.gap == None : GAP =1
    else : GAP = args.gap
    if args.limit == None : LIMIT = 1
    else : LIMIT = args.limit
    
    # Phase de simulation du monde
    world = World(args.humans, args.countries, gap=GAP, limit=LIMIT)
    
    # Sauvegarde du fichier de résultat dans les dossier results avec les nom de fichier passer par l'argument '--file'
    save_xlsx_file(world, args.file)

    