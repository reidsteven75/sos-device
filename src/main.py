from Hologram.HologramCloud import HologramCloud
credentials = {'devicekey': '12345a7b'}

if __name__ == '__main__':

    cloud = HologramCloud(dict(), network='cellular')
    print('HOLOGRAM')
    print cloud.version # Prints 0.7.0
    print cloud.network_type # Prints either 'Network Agnostic Mode' or 'Cellular'

    hologram = HologramCloud(credentials, network='cellular')

    print('sending message...')
    recv = cloud.sendMessage("hi there!", topics=["TOPIC1","TOPIC2"])

