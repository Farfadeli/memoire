from world_simulation import World
import pandas as pd

def save_xlsx_file(world : World ,  file_path : str) :
    countries = world.get_countries_list().get_country()
    
    with pd.ExcelWriter(f"./results/{file_path}.xlsx") as writer:
        for country in countries :
            data = {'name' : [] , 'sexuality' : [], 'birth' : []}
            for human in world.get_human_list() :
                if human.get_country().get_country_name() == country.get_country_name() :
                    data['name'].append(human.get_name())
                    data['sexuality' ].append( human.get_sexuality())
                    data['birth'].append(human.get_birth_date())
                    
            pd.DataFrame(data).to_excel(writer, sheet_name=f"{country.get_country_name()}", index=False)
            
    print(f"✅ Fichier excels créer avec succès dans : ./results/{file_path}.xlsx")
