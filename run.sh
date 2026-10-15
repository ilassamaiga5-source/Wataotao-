#!/bin/bash
while true; do
  pkill -f "5000:localhost"
  tmux kill-session -t watao 2>/dev/null
  tmux new -d -s watao 'python3 ~/WATAOTAO/app.py'
  echo "WATAOTAO lancé, curl test:"
  sleep 3
  curl -s -o /dev/null -w "%{http_code} /client = %{url_effective}\n" http://localhost:5000/client
  echo "Lancement tunnel..."
  autossh -M 0 -R 80:localhost:5000 serveo.net
  echo "Tunnel coupé, relance dans 3 sec..."
  sleep 3
done
