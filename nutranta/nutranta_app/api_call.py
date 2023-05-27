import requests
from bs4 import BeautifulSoup


def dailycalorie(age,gender,height,weight,activitylevel):

    url = "https://fitness-calculator.p.rapidapi.com/dailycalorie"

    querystring = {"age":age,"gender":gender,"height":height,"weight":weight,"activitylevel":activitylevel}

    headers = {
        "X-RapidAPI-Key": "899b2f00b2msh6e93247fa1d82cfp1b890ajsnde30b850ad15",
        "X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    status_code = response.status_code
    data = response.json()

    # maintain weight
    main_tain = data['data']['goals']['maintain weight']

    # Mild weight loss
    mild_weight_loss = data['data']['goals']['Mild weight loss']
    mild_weight_loss_week = mild_weight_loss['loss weight']
    mild_weight_loss_cal = mild_weight_loss['calory']
    
    # Weight loss
    weight_loss = data['data']['goals']['Weight loss']
    weight_loss_week = weight_loss['loss weight']
    weight_loss_cal = weight_loss['calory']

    # Extreme weight loss
    extream = data['data']['goals']['Extreme weight loss']
    extream_calory = extream['calory']
    extream_loss_weight = extream['loss weight']

    return main_tain,mild_weight_loss_week,mild_weight_loss_cal,weight_loss_week,weight_loss_cal,extream_calory,extream_loss_weight



api_key = '9eef243de43f4a2cb8cc562b485a0f1a'
def get_diet_plan(diet):
    api_key = '9eef243de43f4a2cb8cc562b485a0f1a'
    url = f"https://api.spoonacular.com/mealplanner/generate?apiKey={api_key}&timeFrame=day&targetCalories=2000&diet={diet}"

    response = requests.get(url)
    status_code = response.status_code
    print("status_code: ",status_code)
    data = response.json()
    if data:
        breakfast_title = data['meals'][0]['title']
        lunch_title = data['meals'][1]['title']
        dinner_title = data['meals'][2]['title']
        breakfast_title_url = data['meals'][0]['sourceUrl']
        lunch_title_url = data['meals'][1]['sourceUrl']
        dinner_title_url = data['meals'][2]['sourceUrl']
        links = [breakfast_title_url,lunch_title_url,dinner_title_url]
        title_summary =[]
        for  meal in links:
            url_1 = f"https://spoonacular.com/{meal}"
            print(url_1)
            response = requests.get(url_1)
            soup = BeautifulSoup(response.content, 'html.parser')
            # finding by class
            # Get the recipe summary
            summary_elements = soup.find('p', class_='panel')
            summary = summary_elements.text
            title_summary.append(summary)
        return title_summary, breakfast_title, lunch_title, dinner_title 
    else:
        print("Failed to retrieve diet plan.")


