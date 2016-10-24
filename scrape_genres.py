import requests
import json


def get_game_genres(game_id):
    base_url = "http://www.giantbomb.com/api/game/3030-" + str(game_id)
    with open('api_keys.json', 'r') as f:
        api_key = json.load(f)['giant_bomb']
    headers = {'User-agent': 'Python'}
    params = {
        'api_key': api_key,
        'format': 'json',
        'field_list': 'genres'
    }
    results = requests.get(base_url, headers=headers, params=params).json()
    try:
        return results['results']['genres']
    except:
        print results

if __name__ == '__main__':
    with open('scraped_games.json') as f:
        games = json.load(f)
    for idx, g in enumerate(games):
        ascii_title = g['title'].encode('ascii', 'ignore')
        print "({0}/{1}) Searching for: {2}".format(idx + 1,
                                                    len(games),
                                                    ascii_title)
        g['data']['genres'] = get_game_genres(g['data']['id'])
    with open('scraped_games_with_genres.json', 'w+') as f:
        json.dump(games, f)
