import ipaddress
import requests
import pandas as pd

def bot_ip_addresses():
    bots_urls = {
        'google': 'https://developers.google.com/search/apis/ipranges/googlebot.json',
        'bing': 'https://www.bing.com/toolbox/bingbot.json'
    }
    ip_addresses = []
    for bot, url in bots_urls.items():
        bot_resp = requests.get(url)
        for iprange in bot_resp.json()['prefixes']:
            network = iprange.get('ipv4Prefix')
            if network:
                ip_list = [(bot, str(ip)) for ip in ipaddress.IPv4Network(network)]
                ip_addresses.extend(ip_list)
    df = pd.DataFrame(ip_addresses, columns=['bot_name', 'ip_address'])
    df.to_csv("Bot_ips.csv")
 
bot_ip_addresses()
