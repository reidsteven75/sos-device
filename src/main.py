from flask import Flask
from Hologram.HologramCloud import HologramCloud
credentials = {'devicekey': '12345a7b'}

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

    cloud = HologramCloud(dict(), network='cellular')
    print('HOLOGRAM')
    print cloud.version # Prints 0.7.0
    print cloud.network_type # Prints either 'Network Agnostic Mode' or 'Cellular'

    hologram = HologramCloud(credentials, network='cellular')

    print('sending message...')
    recv = cloud.sendMessage("hi there!", topics=["TOPIC1","TOPIC2"])

