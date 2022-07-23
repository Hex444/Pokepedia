from xml.dom import NotFoundErr
import requests,json

def getstats(pokemon):

    link = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon = pokemon
    link += pokemon

    try:
        res = requests.get(link)
        jsondata = json.loads(res.text)
    except Exception as nopokemon:
        return NotFoundErr

    name = jsondata['name']
    baseexp = jsondata['base_experience']
    height = jsondata['height']
    weight = jsondata['weight']
    type1 = jsondata['types'][0]['type']['name']

    try:
        type2 = jsondata['types'][1]['type']['name']
    except Exception as one_type:
        pass

    stats = {   
                jsondata['stats'][0]['stat']['name']:jsondata['stats'][0]['base_stat'],
                jsondata['stats'][1]['stat']['name']:jsondata['stats'][1]['base_stat'],
                jsondata['stats'][2]['stat']['name']:jsondata['stats'][2]['base_stat'],
                jsondata['stats'][3]['stat']['name']:jsondata['stats'][3]['base_stat'],
                jsondata['stats'][4]['stat']['name']:jsondata['stats'][4]['base_stat'],
                jsondata['stats'][5]['stat']['name']:jsondata['stats'][5]['base_stat'],
            }

    pfp = jsondata['sprites']['official-artwork']['front_default']

    try:
        icon = jsondata['sprites']['versions']['generation-viii']['icons']['front_default']
    except Exception as noicon:
        icon = jsondata['sprites']['front_default'] 
