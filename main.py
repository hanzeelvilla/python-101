fighters_db = [
    {
        "name": "Sam 'The Warrior'",
        "stats": {
            "level": 4,
            "weight": 70
        }
    },
    {
        "name": "Dean 'The Iron'",
        "stats": {
            "level": 5,
            "weight": 85
        }
    },
    {
        "name": "Cas 'The Angel'",
        "stats": {
            "level": 2,
            "weight": 70}
        },
    {
        "name": "Crowley 'The Demon'",
        "stats": {
            "level": 5,
            "weight": 70
        }
    }
]

def match_fighters(fighters_list, target_name):
    target_fighter = None
    
    # Paso 1: Localizar al peleador objetivo
    for fighter in fighters_list:
        if fighter["name"] == target_name:
            target_fighter = fighter
            break
            
    if not target_fighter:
        return f"Error: El peleador '{target_name}' no existe en la base de datos."
        
    # Extraer variables de referencia
    target_lvl = target_fighter["stats"]["level"]
    target_wgt = target_fighter["stats"]["weight"]
    
    # Paso 2: Buscar rivales ideales que cumplan con los filtros de seguridad
    valid_opponents = []
    for fighter in fighters_list:
        if fighter["name"] == target_name:
            continue # No puede pelear contra sí mismo
            
        current_lvl = fighter["stats"]["level"]
        current_wgt = fighter["stats"]["weight"]
        
        # Calcular la diferencia absoluta de niveles usando la función nativa abs()
        lvl_diff = abs(target_lvl - current_lvl)
        
        if current_wgt == target_wgt and lvl_diff <= 1:
            valid_opponents.append(fighter["name"])
            
    return valid_opponents

print("Rivales seguros para Sam:")
print(match_fighters(fighters_db, "Dean 'The Warrior'"))