import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# --- 1. CRIAR DADOS (Simulando Tráfego de Rede) ---
# Requisito do PDF: Pelo menos 100 tuplas [cite: 21]
data = {
    'porta': [80, 443, 22, 21, 3389, 8080, 53, 445, 80, 22],
    'tamanho_pacote': [500, 1200, 50, 60, 1500, 800, 120, 200, 450, 40],
    'protocolo': [1, 1, 0, 0, 1, 1, 2, 0, 1, 0], # 0=TCP, 1=HTTP, 2=DNS
    'classe': [0, 0, 1, 1, 1, 0, 0, 1, 0, 1] # 0 = Normal, 1 = Ataque
}

# Multiplicando os dados para ter 150 linhas
df = pd.DataFrame(data)
df = pd.concat([df]*15, ignore_index=True)

# --- 2. TREINAMENTO ---
# Separar dados e definir o alvo (classe)
X = df.drop('classe', axis=1)
y = df['classe']

# Dividir em Treino e Teste (Split) [cite: 25]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Criar o Modelo (Árvore de Decisão) [cite: 12]
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# --- 3. EXPORTAR ---
# Testar precisão
score = accuracy_score(y_test, modelo.predict(X_test))
print(f"Modelo treinado com sucesso! Acurácia: {score:.2f}")

# Salvar o arquivo para usar na API/Azure depois
joblib.dump(modelo, 'modelo.pkl')
print("Arquivo 'modelo.pkl' gerado na pasta!")