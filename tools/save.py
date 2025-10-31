from world_simulation import World
import pandas as pd

def save_xlsx_file(world : World ,  file_path : str) :
    countries = world.get_countries_list().get_country()
    result = {}
    with pd.ExcelWriter(f"./results/{file_path}.xlsx") as writer:
            for key,value in world.get_human_list().items() :
                result = {'name' : [] , 'sexuality'  : [], 'born country' : []}
                for human in value : 
                    result['name'].append(human.get_name())
                    result['sexuality'].append(human.get_sexuality())
                    result['born country'].append(human.get_born_country().get_country_name())
                pd.DataFrame(result).to_excel(writer, sheet_name=f"{key}", index=False)
            
    print(f"✅ Fichier excels créer avec succès dans : ./results/{file_path}.xlsx")
