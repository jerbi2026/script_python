import requests

app_id = 'WXEJUX-L8R4K57TVU'





def resolve_equation(equation):
    base_url = 'http://api.wolframalpha.com/v2/query'
    
    params = {
        'input': equation,
        'format': 'plaintext',
        'output': 'JSON',
        'appid': app_id
    }

    response = requests.get(base_url, params=params)
    result = response.json()

   

    try:
        pods = result['queryresult']['pods']
        for pod in pods:
            if pod['title'] == 'Result':
                solutions = pod['subpods'][0]['plaintext']
                return solutions
    except KeyError as e:
        return 'Pas de solution trouvée'




equation_to_solve = '4x+y=0'

solution = resolve_equation('solve '+equation_to_solve)
print(f'Solution: {solution}')
