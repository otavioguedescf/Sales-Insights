# 📊 Sales Insights – Projeto de Ciência de Dados

**Análise exploratória, visualizações e modelagem preditiva de vendas com dados simulados**

Este projeto simula um pipeline completo de Data Science, com foco em análise prática, aprendizado técnico e preparação de portfólio para oportunidades na área de dados.

---

## 💡 Objetivo

Realizar uma análise detalhada de vendas simuladas, passando por todas as etapas de um projeto de ciência de dados:

- 📁 Preparação e limpeza de dados
- 📊 Análise Exploratória (EDA)
- 📈 Visualizações com matplotlib, seaborn e plotly
- 🧠 Modelagem preditiva com Decision Trees, Random Forest, XGBoost e Redes Neurais
- 💬 NLP com campanhas e descrições
- 🤖 Geração de relatórios com LLMs (OpenAI)
- 🧪 Testes A/B
- ⚙️ MLOps: pipeline, deploy e versionamento

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

4.4 Construção de modelos:  
• Árvore de Decisão  
• Random Forest  
• XGBoost  
• Rede Neural Simples

4.5 Feature Engineering:  
• Novas variáveis (ex: `Valor x Quantidade`, faixas de valor)  

4.6 Avaliação:  
• Acurácia, Precisão, Recall, F1-Score, Matriz de Confusão  

4.7 Validação Cruzada:  
• K-Fold (10 folds) com F1-Score  

4.8 Escolha do melhor modelo:  
• Modelo final: **XGBoost**, por melhor performance e estabilidade  

> 🔧 Decidimos encerrar este módulo com uma entrega sólida e bem documentada. Melhorias como ajuste fino de hiperparâmetros, Curva ROC e análise de importância ficam registradas para evolução futura.

---

### 💬 5. NLP – Processamento de Linguagem Natural
5.1 Pré-processamento:  
• Limpeza, tokenização, stopwords  

5.2 Vetorização:  
• TF-IDF, Bag of Words (opcional)  

5.3 Exploração textual:  
• Palavras mais frequentes, wordcloud  

5.4 Clusterização:  
• KMeans ou DBSCAN sobre vetores  

5.5 Classificação textual (bônus):  
• Classificação da descrição do produto  

---

### 🤖 6. LLMs e RAG – Large Language Models e Recuperação de Contexto

6.1 Criação de embeddings a partir dos textos:  
• Geração de vetores de contexto usando modelos como `Sentence Transformers`  

6.2 Construção de base vetorizada para recuperação:  
• Uso de ferramentas como `FAISS` ou `Chroma` para indexação semântica  

6.3 Implementação de um pequeno RAG (Retrieval-Augmented Generation):  
• Usuário faz perguntas sobre vendas  
• O sistema recupera trechos relevantes + gera resposta com LLM (ex: GPT)  

6.4 (Bônus) Integração com modelos open-source:  
• Hugging Face Transformers, GPT-4-All, OpenAssistant, entre outros  

---

### 🧪 7. Testes A/B – Validação de Impacto Estatístico

7.1 Planejamento de Testes A/B em vendas:  
• Como montar um experimento entre Campanha A vs Campanha B  

7.2 Simulação prática de Teste A/B:  
• Uso de dados simulados ou reais de campanhas para testes de performance  

7.3 Análise Estatística:  
• Teste de hipóteses com `T-Test` e `Mann-Whitney`  
• Cálculo e interpretação de p-valor  

7.4 Conclusão do teste:  
• Tomada de decisão com base em evidência estatística sólida  

---

### ⚙️ 8. MLOps – Operacionalização de Modelos

8.1 Pipeline de Machine Learning estruturado:  
• Separação clara entre: Pré-processamento → Treinamento → Avaliação → Deploy  

8.2 Serialização do modelo:  
• Exportação com `pickle`, `joblib` ou formato interoperável como `ONNX`  

8.3 Criação de API para o modelo:  
• Backend com `FastAPI`, simples e moderno para servir o modelo  

8.4 Deploy simples e escalável:  
• Com `Streamlit`, `Render`, `Hugging Face Spaces`, ou servidores locais  

8.5 Controle de versão e documentação:  
• Repositório versionado com `Git` + `GitHub`  
• `README.md` completo e estruturado para portfólio e contratação    

---

## 📂 Estrutura de Pastas

```bash
sales-insights/
├── data/               # Arquivos simulados e tratados
├── notebooks/          # Jupyter Notebooks
├── reports/            # Relatórios e PDFs
├── app/                # Código de deploy
├── README.md           # Este arquivo
├── requirements.txt    # Dependências

```
---

## 🚀 Status
Etapas concluídas: 1.0 à 4.0

Em andamento: 5.1 Pré-processamento + Documentação para GitHub

## 📅 Autor
Otávio Guedes
Cientista de Dados em transição de carreira, focado em projetos práticos de ponta a ponta.

Acesse o [meu perfil no LinkedIn](https://www.linkedin.com/in/otaviomendesguedes/)

