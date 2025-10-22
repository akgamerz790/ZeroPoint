#!/usr/bin/env python3

import socket
import threading
import json
from crypto import encrypt_data, decrypt_data

class Server:
    def __init__(self, port=4444):
        self.port = port
        self.clients = []
        self.running = False
    
    def start(self):
        """Start the server"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('0.0.0.0', self.port))
        self.sock.listen(5)
        self.running = True
        print(f"[+] Server listening on port {self.port}")
        
        while self.running:
            try:
                client, addr = self.sock.accept()
                print(f"[+] New connection from {addr}")
                thread = threading.Thread(target=self.handle_client, args=(client, addr))
                thread.start()
            except:
                break
    
    def handle_client(self, client, addr):
        """Handle individual client connections"""
        while True:
            try:
                data = client.recv(1024)
                if not data:
                    break
                decrypted = decrypt_data(data)
                print(f"[*] Received from {addr}: {decrypted}")
            except:
                break
        client.close()
    
    def stop(self):
        """Stop the server"""
        self.running = False
        self.sock.close()

if __name__ == "__main__":
    server = Server()
    server.start()