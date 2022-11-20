import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5720354270:AAG2gBtnQVMPyMZJENVcYZGCtoMa3tEJX-M')
API_ID =  os.environ.get('api_id','15558101')
API_HASH = os.environ.get('api_hash','c2cbb2f07c44fe466076fbe65e3c00cc')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('Elnietodecacha')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','http://KFGGJJYGJKLHFKYEDIGDYJJEKEFKREEGLFDKLH'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')

space = {} #tabla de la base de datos de usario
space['Elnietodecacha'] = 0 #Tiene q ser valor 0, sino dará error