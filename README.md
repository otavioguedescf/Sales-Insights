# 📊 Sales Insights – Projeto de Ciência de Dados

**Análise exploratória, visualizações e modelagem preditiva de vendas com dados simulados**

Este projeto simula um pipeline completo de Data Science, com foco em análise prática, aprendizado técnico e preparação de portfólio para oportunidades na área de ciência de dados.

---

## 💡 Objetivo

Realizar uma análise detalhada de vendas simuladas, passando por todas as etapas de um projeto de ciência de dados:

- 📁 Preparação e limpeza de dados
- 📊 Análise Exploratória (EDA)
- 📈 Visualizações com matplotlib, seaborn e plotly
- 🧠 Modelagem preditiva com Decision Trees, Random Forest, XGBoost e Redes Neurais

---

## 📦 Base de Dados

A base `df_vendas.csv` contém **10.000 registros simulados**, com as seguintes colunas:

- `Data` – Data da venda  
- `Descrição` – Descrição do produto  
- `Cor` – Cor do item  
- `Quantidade` – Itens vendidos  
- `Valor` – Valor unitário  
- `Valor_Final` – Valor total com desconto aplicado  
- `Ticket_Medio` – Valor por item  
- `Situação` – Situação do pagamento  
- `Cliente_ID`, `Categoria`, `Canal`, `Região`, `Campanha`

---

## 🔁 Pipeline do Projeto

### 📁 1. Preparação dos Dados
1.1 Carregamento dos dados:  
• Importação do `.csv`  
• Verificação da estrutura do DataFrame  

1.2 Tratamento de valores nulos:  
• Identificação e decisão de tratamento (remoção/preenchimento)  

1.3 Conversão de tipos de dados:  
• Ajustes de colunas (ex: datas, inteiros, floats)  

1.4 Criação de colunas derivadas:  
• `Valor_Final`, `Ticket_Medio`, variáveis de data  

1.5 Organização do DataFrame:  
• Renomeação de colunas e padronização de categorias  

---

### 📊 2. Análise Exploratória de Dados (EDA)
2.1 Visão Geral:  
• `.info()`, `.describe()`, valores únicos, nulos  

2.2 Distribuições:  
• Histogramas, análise de outliers e proporção de categorias  

2.3 Séries Temporais:  
• Evolução de vendas, ticket médio, campanhas  

2.4 Agrupamentos:  
• Por categoria, cliente, canal, situação de venda  

2.5 Outliers:  
• Detecção via Z-Score e IQR  
• Comparação entre métodos  

---

### 📈 3. Visualização de Dados
3.1 Gráficos de distribuição:  
• Histogramas, skewness  

3.2 Séries temporais:  
• Evolução mensal de vendas e sazonalidades  

3.3 Comparações categóricas:  
• Gráficos de barras horizontais, destaque por canal e campanha  

3.4 Correlação:  
• Heatmap elegante com máscara triangular  
• Análise de multicolinearidade  

---

### 🧠 4. Modelagem Preditiva
4.1 Separação dos dados:  
• `X_train`, `X_test`, `y_train`, `y_test`  

4.2 Feature Scaling:  
• Padronização com `StandardScaler`  

4.3 Seleção de variáveis importantes  

4.4 Construção e avaliação de modelos:  
• Árvore de Decisão  
• Random Forest  
• XGBoost  
• Rede Neural Simples (implementada com TensorFlow/Keras)

4.5 Feature Engineering e avaliações:  
• Novas variáveis (ex: `Valor x Quantidade`, faixas de valor)  

4.6 Validação Cruzada:  
• K-Fold (10 folds) com F1-Score  

4.7 Escolha do melhor modelo:  
• Modelo final: **XGBoost**, por melhor performance e estabilidade  

> 🔧 Decidimos encerrar este módulo com uma entrega sólida e bem documentada. Melhorias como ajuste fino de hiperparâmetros, Curva ROC e análise de importância ficam registradas para evolução futura.

---

## 📂 Estrutura de Pastas

```bash
sales-insights/
├── data/               # Arquivos base
├── notebooks/          # Jupyter Notebooks
├── reports/            # Relatórios e gráficos
├── app/                # Código de deploy
├── README.md           # Este arquivo
├── requirements.txt    # Bibliotecas necessárias

```
---

## 📅 Autor
Otávio Guedes
Cientista de Dados em transição de carreira, focado em projetos práticos de ponta a ponta.

Acesse o [meu perfil no LinkedIn](https://www.linkedin.com/in/otaviomendesguedes/)

