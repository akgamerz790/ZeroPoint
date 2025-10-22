{
  "server": {
    "port": 4444,
    "bind_address": "0.0.0.0",
    "max_clients": 50
  },
  "agent": {
    "reconnect_interval": 30,
    "heartbeat_interval": 30,
    "default_server": "127.0.0.1"
  },
  "security": {
    "encryption": True,
    "key_rotation": False
  },
  "logging": {
    "level": "INFO",
    "file": "zeropoint.log"
  }
}
