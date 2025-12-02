from flask import Flask, request, jsonify
from flask_cors import CORS  # <--- Nova linha
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app) # <--- Libera o acesso para o Frontend

# Carregar modelo
try:
    modelo = joblib.load('modelo.pkl')
    print("Modelo carregado!")
except:
    print("Erro no modelo!")

@app.route('/predict', methods=['POST'])
def predict():
    dados = request.json
    
    # Cria o dataframe
    df_input = pd.DataFrame([dados], columns=['porta', 'tamanho_pacote', 'protocolo'])
    
    # Previsão
    previsao = modelo.predict(df_input)
    probabilidade = modelo.predict_proba(df_input).max() * 100
    
    # Lógica de Resposta
    if previsao[0] == 1:
        resultado = "PERIGO: ATAQUE DETECTADO"
        cor = "red"
    else:
        resultado = "TRÁFEGO NORMAL"
        cor = "green"
    
    return jsonify({
        'mensagem': resultado,
        'confianca': f"{probabilidade:.1f}%",
        'cor': cor
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)