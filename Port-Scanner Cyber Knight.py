print("""    
╭━━━╮╱╱╱╱╭╮╱╱╭━━━╮
┃╭━╮┃╱╱╱╭╯╰╮╱┃╭━╮┃
┃╰━╯┣━━┳┻╮╭╯╱┃╰━━┳━━┳━━┳━╮╭━╮╭━━┳━╮
┃╭━━┫╭╮┃╭┫┣━━╋━━╮┃╭━┫╭╮┃╭╮┫╭╮┫┃━┫╭╯
┃┃╱╱┃╰╯┃┃┃╰┳━┫╰━╯┃╰━┫╭╮┃┃┃┃┃┃┃┃━┫┃
╰╯╱╱╰━━┻╯╰━╯╱╰━━━┻━━┻╯╰┻╯╰┻╯╰┻━━┻╯
            \x1b[91m                  Created By Cyber Knight""")
print("📡PORT SCANNER📡")
import socket,sys,threading
print('\n> Python Port Scanner By xRO & Jocker & Cyber Knight \x1b[93m\n  '+'='*50+'\n')
if len(sys.argv) > 1: target = socket.gethostbyname(sys.argv[1])
else: target = socket.gethostbyname(input('> \x1b[93m Enter Target Ip: '))
# Scan ports - arguments: target + port
def scanPort(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c = s.connect_ex((target, port))
    if c == 0: print ('  ' + target + ' ~ Port %d \t[open]' % (port,))
    s.close()
# Here we define range of ports to scan
for i in range(1, 5000):
    scan = threading.Thread(target=scanPort, args=(target, i))
    scan.start()