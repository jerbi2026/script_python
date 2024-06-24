import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime
import webbrowser


listener = sr.Recognizer()
engine = ttx.init()

voice = engine.getProperty('voices')

engine.setProperty('voice','french')


def parle(text):
    engine.say(text)
    engine.runAndWait()


def ecoute():
    try:
        with sr.Microphone() as source:
            print("parler")
            parle("parler")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
        
    except:
        pass
    return command

def assistant():
   
    global parler
    command=ecoute()
    print(command)
    if 'bonjour' in command:
        parle('Bonjour Guide pro est à votre service')
    elif 'liste des clients' in command:
        parle('tout de suite')
        webbrowser.open("https://guide-pro.netlify.app/#/clients")
    #elif 'mettez la chanson de ' in command:
        #chanteur  = command.replace('mettez la chanson de ','')
        #print(chanteur)
        #parle("tout de suite")
        #pywhatkit.playonyt(chanteur)
    elif 'gars' in command:
        
        print('les gains annuels 215000 dinars tunisiens et mensuels 10000 dinars tunisiens')
        parle('les gains annuels 215000 dinars tunisiens et mensuels 10000 dinars tunisiens')
    elif 'demande en attente' in command:
             parle("on a 18 demandes en attente") 
             print("on a 18 demandes en attente")
    elif 'heure' in command:
          heure= datetime.datetime.now().strftime('%H:%M')
          parle('il est '+heure)
    elif 'revenu' in command: 
         parle(' les Sources de revenus sont 30% directe 50% Sociale et 20% vente de produits')
    elif 'notification' in command:
         parle('12 octobre 2023 : Un nouveau rapport mensuel est prêt à être téléchargé !')
         parle('7 Octobre  2023 : L’équipe de communication a franchi la première étape')
         parle("2 septembre 2023: Votre projet a commencé aujourd'hui")
    elif 'message' in command:
         parle("Heythem Bahri : Salut! Je me demande si vous pouvez m'aider avec un problème que j'ai rencontré. " )
         parle("Ahmed Aziz Mhiri: J'ai terminé mon travail")
         parle("Mohamed ben ghozzi : J'ai du mal à diffuser des publicités")
         parle("Jerbi Ahmed : j'ai fini ma tâche")
    elif 'merci' in command:
         parle("merci pour l'interaction, bonne journée")
         parler=False
         
    
    else:
            pywhatkit.search(command)



#pp
parler = True
while (parler==True):
    assistant()
    if(parler==False):
         break