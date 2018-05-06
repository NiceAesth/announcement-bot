import requests, discord, os
from time import sleep
from bottle import run, post, request, route
from discord import Webhook, RequestsWebhookAdapter, File

@route('/')
def index():
    return 'Status: OK' 

webhook = Webhook.partial(os.environ['webhookID'], os.environ['token'],\
 adapter=RequestsWebhookAdapter())

while(1):
	webhook.send("Aveți un play impresionant care întrece majoritatea din osu!ro și vreți să fie postat pe YouTube ca alte playuri impresionante? Puteți da submit la play aici <https://goo.gl/forms/F0U5HVHh3ToLrlwn2> și vă vom contacta dacă play-ul e acceptat sau nu cât mai repede posibil.")
	webhook.send("Play-ul nu pare impresionant decât pentru cei de categoria ta de skill zici? Poți participa aici:<https://goo.gl/forms/6czwXikmsS0uWH9o2> la plays of the month unde, câștigătorii vor fi anunțați într-un video pe canalul nostru de youtube: <https://www.youtube.com/c/osuro> primind un anumit grad de recunoaștere din partea comunității românești de osu! și nu numai!")
	sleep(7200)

run(server='gevent', port=int(os.environ.get('PORT', 5000)), host='0.0.0.0')