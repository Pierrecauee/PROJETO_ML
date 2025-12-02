import requests
import json

# Endereço da sua API (que está rodando no outro terminal)
url = 'http://127.0.0.1:5000/predict'

# --- TESTE 1: Simulação de Tráfego Normal (Navegação Web) ---
pacote_normal = {
    'porta': 443,           # HTTPS
    'tamanho_pacote': 1200, # Tamanho comum
    'protocolo': 1          # HTTP/UDP
}

# --- TESTE 2: Simulação de Ataque (Brute Force SSH) ---
pacote_ataque = {
    'porta': 22,            # SSH
    'tamanho_pacote': 50,   # Pacote pequeno (tentativa de login)
    'protocolo': 0          # TCP
}

print("--- Enviando Teste 1 (Normal) ---")
response = requests.post(url, json=pacote_normal)
print("Resposta do Servidor:", response.json())

print("\n--- Enviando Teste 2 (Suspeito) ---")
response = requests.post(url, json=pacote_ataque)
print("Resposta do Servidor:", response.json())
