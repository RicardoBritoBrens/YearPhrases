import requests
import json
from datetime import datetime
import calendar
from bs4 import BeautifulSoup

current_date = datetime.now()

def get_motivational_quotes(month):
    url = f"https://365frasesmotivadoras.com/{month}/"
    response = requests.get(url)
    return response.text

def get_current_month_name():    
    month_name = current_date.strftime("%B")  # Obtiene el nombre del mes actual      
    return month_name

def get_month_days_range():
   return calendar.monthrange(current_date.year, current_date.month) # Obtiene el numero de días del mes actual  
   

def save_to_json(data):
    with open("monthData.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":    
    month_name = get_current_month_name()    
    modified_quotes = get_motivational_quotes(month_name.lower())     
    soup = BeautifulSoup(modified_quotes, 'html.parser')              
    to_save_data = soup.find_all("span")    
    saved_success = save_to_json({"motivational_quotes": soup.find_all('span')})
    print("Datos guardados en monthData.json")

