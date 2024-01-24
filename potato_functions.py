import json

def create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date):
        potato = {"owner_name": owner_name,"owner_discord_id": owner_discord_id,"name": name,"potato_type": potato_type,"price": price,"accomplishment": accomplishment,"date": date}
        return potato

def read_potatoes_by_discord_id(potatoes,owner_discord_id):
    # logic for how to find info here
    result_potatoes = []
    for potato in potatoes:
        if potato['owner_discord_id'] == owner_discord_id:
            result_potatoes.append(potato)

    return(result_potatoes)


def load_potatoes(save_filename):
    with open(save_filename, 'r') as file:
        loaded_potatoes = json.load(file)

    return (loaded_potatoes)
def save_potatoes(potatoes,save_filename):
    with open(save_filename, 'w') as file:
        json.dump(potatoes,file)

    return potatoes
def update_potato():

    # logic for how to find info here.
    pass

def delete_potato():
    # logic for how to find info here
    pass

import os

def file_exists(file_path):
    """
    Check if a file exists.

    Args:
    - file_path (str): The path to the file.

    Returns:
    - bool: True if the file exists, False otherwise.
    """
    return os.path.exists(file_path)


def format_achievements(achievements):
    owner_achievements = {}

    for achievement in achievements:
        owner_name = achievement['owner_name']

        if owner_name not in owner_achievements:
            owner_achievements[owner_name] = []

        owner_achievements[owner_name].append(achievement)

    formatted_output = ""

    for owner_name, achievements_list in owner_achievements.items():
        formatted_output += f"# {owner_name}\n"

        for achievement in achievements_list:
            formatted_output += f"- name: {achievement['name']}\n"
            formatted_output += f"- potato_type: {achievement['potato_type']}\n"
            formatted_output += f"- price: ${achievement['price']}\n"
            formatted_output += f"- accomplishment: {achievement['accomplishment']}\n"
            formatted_output += f"- date: {achievement['date']}\n\n"

    return formatted_output