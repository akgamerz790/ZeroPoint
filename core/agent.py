#!/usr/bin/env python3
"""ZeroPoint Agent - Educational Demo"""
# This is a simplified educational example of an agent that connects to a command server,
# sends periodic heartbeats, and can be extended to receive and execute commands.
# Note: This code is for educational purposes only.
import socket
import time
import json
from crypto import encrypt_data, decrypt_data

class Agent:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.connected = False
    
    def connect(self):
        """Connect to command server"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.server_ip, self.server_port))
            self.connected = True
            print(f"[+] Connected to {self.server_ip}:{self.server_port}")
        except Exception as e:
            print(f"[-] Connection failed: {e}")
    
    def send_heartbeat(self):
        """Send heartbeat to server"""
        data = {"type": "heartbeat", "timestamp": time.time()}
        encrypted = encrypt_data(json.dumps(data))
        self.sock.send(encrypted)
    
    def run(self):
        """Main agent loop"""
        while self.connected:
            try:
                self.send_heartbeat()
                time.sleep(30)
            except:
                self.connected = False
                break

if __name__ == "__main__":
    agent = Agent("127.0.0.1", 4444)
    agent.connect()
    agent.run()