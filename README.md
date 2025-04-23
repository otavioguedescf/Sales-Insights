# Sales Insights

**Análise exploratória, visualizações e modelagem preditiva de vendas**

Este projeto simula um pipeline completo de Data Science aplicado a um conjunto de vendas fictício, com o objetivo de exercitar habilidades desde a preparação de dados até a criação de modelos preditivos e uso de LLMs.

---

## 💡 Objetivo

Realizar uma análise detalhada de vendas utilizando:

- Análise Exploratória (EDA)
- Visualizações com matplotlib, seaborn e plotly
- Modelagem preditiva com árvores, XGBoost e redes neurais
- NLP com campanhas e descrições
- Geração de relatórios com LLMs (OpenAI)
- Testes A/B
- MLOps (pipeline, deploy e versionamento)

---

## 📊 Dados simulados

A base de dados `df_vendas` foi gerada com 10.000 registros contendo:

- Data da venda  
- Descrição do produto  
- Cor do item  
- Quantidade e Valor  
- Situação de pagamento  
- Cliente ID  
- Categoria de produto  
- Canal de venda  
- Região  
- Campanha de marketing  
- Valor final com desconto

---

## 🔁 Pipeline do projeto

### 📁 1. Preparação dos Dados

- Carregamento da base
- Tratamento de nulos e conversão de tipos
- Criação de colunas derivadas: `Valor_Final`, `Ticket_Médio`, `Categoria_Produto`

### 📊 2. Análise Exploratória de Dados (EDA)

- Estatísticas descritivas
- Histogramas com média, mediana e std
- Séries temporais com média móvel
- Agrupamentos por produto, cliente, canal, campanha
- Detecção de outliers (IQR e Z-score)

### 🔢 3. Visualização de Dados

- Matplotlib + Seaborn + Plotly
- Heatmap de correlação
- Gráficos interativos e dashboard com Streamlit

### 🤖 4. Modelagem Preditiva

- X_train / X_test, Scaling, Correlação
- Modelos: Árvore de Decisão, Random Forest, XGBoost, Redes Neurais (TensorFlow/PyTorch)
- Avaliação com RMSE, R², F1-score
- Cross-validation + GridSearchCV

### 💬 5. NLP

- TF-IDF nas descrições e campanhas
- Clusterização e classificação

### 🧠 6. LLMs e RAG

- Geração de relatórios com OpenAI
- RAG com embeddings de texto
- Criação de chatbot de insights

### 🧪 7. Testes A/B

- Simulação de campanhas
- Testes de significância (t-test, p-value)

### ⚙️ 8. MLOps

- Pipelines com scikit-learn
- Serialização com joblib/pickle
- Deploy com Flask, FastAPI ou Streamlit
- Versionamento com Git e GitHub

---

## 📂 Estrutura de pastas

```bash
sales-insights/
├── data/               # Arquivos de dados simulados/tratados
├── notebooks/          # Jupyter Notebooks com as análises
├── reports/            # Markdown, relatórios e PDFs
├── app/                # Código de deploy (Streamlit, Flask etc.)
├── README.md           # Descrição geral do projeto
├── requirements.txt    # Dependências do projeto
```
---

## 🚀 Status
Etapas concluídas: 1.0 e 2.0

Em andamento: 2.4 Agrupamentos + Documentação para GitHub

## 📅 Autor
Otávio Guedes
Cientista de Dados em transição de carreira, focado em projetos práticos de ponta a ponta.

Acesse o [meu perfil no LinkedIn](https://www.linkedin.com/in/otaviomendesguedes/)

