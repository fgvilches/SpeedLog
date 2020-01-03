import json
import speedtest as st
import csv
import os, sys
import time
import traceback

from optparse import OptionParser
print("===========================================================")
print("SPEEDLOG V.0.2 - Felipe Gonzalez")
print("===========================================================")
print("INICIALIZANDO PRUEBAS Y CSV")
print("---------------------------")
print("UTILIZANDO SERVIDORES DE ISP ENTEL CHILE")
print("===========================================================")
start_time = time.time()
fecha = time.strftime("%x")
new_fecha = fecha.split("/")
fecha = new_fecha[0] + new_fecha[1] + new_fecha[2]
filename = "server_minimize.json"
test_type = ""
id_server = []

header = 'id country name sponsor download(mbps) upload(mbps) ping(ms) time_execute(s) hora'
header = header.split()

parser = OptionParser()

parser.add_option("-t", "--type", dest="test_type", default="multi")
parser.add_option("-l", "--list", dest="test_list", default="minimize")

(options, args) = parser.parse_args()

print(options.test_type)

if options.test_list == 'minimize':
    filename = 'server_minimize.json'
elif options.test_list == 'full':
    filename = 'server.json'
else:
    print("Argumento Invalido")
    sys.exit(0)

namefile = 'results_'+ fecha + '.csv'
file = open(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), namefile)), 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)

def speed_test_multi(server):
    s = st.Speedtest()
    s.get_servers(server)
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def speed_test_single(server):
    s = st.Speedtest()
    s.get_servers(server)
    s.download(threads=1)
    s.upload(threads=1)
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

hora_actual = time.strftime("%H:%M:%S")
hora_split = hora_actual.split(':')
hora_1 = int(hora_split[1]) - 15

while True:
    hora_actual = time.strftime("%H:%M:%S")
    hora_split = hora_actual.split(':')
    while int(hora_split[1]) == (int(hora_1) + 15):
        with open(filename, encoding="utf8", newline='') as json_f:
            data = json.load(json_f)
            for d in data['server']:
                print(f'Servidor de Prueba: {d["_name"]} en el pais: {d["_country"]}')
                s_time = time.time()
                server_to_test = [int(d['_id'])]
                    
                try:
                    if options.test_type == 'multi':
                        down ,up ,ping = speed_test_multi(server_to_test)
                    elif options.test_type == 'single':
                        down ,up ,ping = speed_test_single(server_to_test)
                    else:
                        raise Exception('Argumento Invalido')
                except Exception:
                    traceback.print_exc() 
                result_str = f'{d["_id"]}_{d["_country"]}_{d["_name"]}_{d["_sponsor"]}_{round(down/1000000, 2)} Mbps_{round(up/1000000,2)} Mbps_{round(ping,2)} ms_{round(time.time() - s_time, 2)} Seg_{hora_actual}'
                file = open(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), namefile)), 'a', newline='')
                with file:
                    writer = csv.writer(file)
                    writer.writerow(result_str.split("_"))

        hora_actual = time.strftime("%H:%M:%S")
        hora_split = hora_actual.split(':')
        hora_1= hora_split[1]
        print('Tiempo de ejecucion: {time.time() - start_time}')
        print("Esperando proxima prueba..")
