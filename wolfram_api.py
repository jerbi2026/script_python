import wolframalpha

def wolfram_alpha_query(query, app_id):
    # Initialiser le client Wolfram Alpha avec votre clé d'API
    client = wolframalpha.Client(app_id)
    
    try:
        # Envoyer la requête à Wolfram Alpha
        result = client.query(query)
        
        # Afficher les résultats
        for pod in result.pods:
            for sub in pod.subpods:
                print(sub.plaintext)
    
    except wolframalpha.WolframAlphaError as e:
        print(f"Une erreur s'est produite : {e}")


while True:
    wolfram_api_key = "WXEJUX-L8R4K57TVU"
    user_query = input("Entrez votre requête pour Wolfram Alpha : ")
    wolfram_alpha_query(user_query, wolfram_api_key)
  
    
   
