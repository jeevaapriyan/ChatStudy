import socket             
s = socket.socket()         
print ("Socket successfully created")
port = 12345                
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
s.listen(5)     
print ("socket is listening")    
c, addr = s.accept()         
while True: 
  message = c.recv(1024).decode()
  print("Client:", message)
  if message.lower() == "exit":
    break
  reply = input("Server: ")
  c.send(reply.encode())
c.close()