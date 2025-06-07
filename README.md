
# 🧠 Simulação Jurídica com Dados Sintéticos Realistas para Data Science

Este projeto foi desenvolvido para gerar um **dataset jurídico sintético**, com estrutura detalhada e realista, visando aplicações em **análise de dados, visualização e modelagem preditiva** na área do Direito.

## 📌 Objetivo

Criar um conjunto robusto de dados falsos (mas verossímeis) com milhares de processos judiciais, partes envolvidas e movimentações processuais. Ideal para treinamentos, estudos e demonstrações de portfólio em Data Science e Business Intelligence.

---

## 🛠️ Tecnologias Utilizadas

- **Python** – Linguagem principal
- **Pandas** – Manipulação e exportação de dados
- **Faker** – Geração de dados fictícios realistas
- **Datetime & Random** – Controle temporal e aleatoriedade

---

## 🧰 Funcionalidades

✔️ Geração de 2000 processos jurídicos  
✔️ 200 clientes únicos (PF e PJ)  
✔️ Distribuição por UFs, tribunais, áreas jurídicas e tipos de ação  
✔️ Fases e status processuais com datas realistas  
✔️ Honorários, valores de causa, custos e provisão de risco  
✔️ Registro de movimentações judiciais com descrição  
✔️ Exportação em `.csv` para uso em Power BI, Excel ou Python

---

## 📊 Estrutura dos Arquivos Gerados

### `clientes.csv`

| Campo         | Descrição                         |
|---------------|-----------------------------------|
| id_cliente    | ID único do cliente               |
| nome_cliente  | Nome do cliente                   |
| tipo_cliente  | Pessoa Física ou Jurídica         |
| uf_cliente    | Unidade Federativa                |

---

### `processos_juridicos_complexo_fake.csv`

| Campo                     | Descrição                                           |
|--------------------------|-----------------------------------------------------|
| numero_processo          | Identificador simulado no padrão jurídico brasileiro |
| polo_ativo/passivo       | Partes envolvidas                                   |
| tipo_processo            | Ex: Ação Popular, Mandado de Segurança              |
| area_juridica            | Ex: Direito Civil, Penal, Ambiental                 |
| valor_causa              | Valor monetário da causa                           |
| custo_total              | Estimativa de custos                               |
| honorarios_advogado      | Honorários do advogado                             |
| provisao_risco           | Valor provisionado baseado no risco estimado       |
| fase_atual               | Fase processual atual                              |
| status_processo          | Ativo, Encerrado, Suspenso, Arquivado              |
| data_abertura            | Data inicial do processo                           |
| data_ultima_movimentacao | Última movimentação registrada                      |
| data_encerramento        | Data de encerramento (se aplicável)                |
| tempo_tramitacao_dias    | Duração do processo em dias                        |
| decisao_final            | Resultado final (se aplicável)                     |
| responsavel              | Nome do advogado responsável                       |
| escritorio_responsavel   | Escritório fictício                                 |
| tribunal, comarca, instancia, uf_processo | Dados de localização judicial     |
| movimentacoes            | Lista textual com eventos simulados                |
| descricao_processo       | Texto resumido sobre o processo                    |

---

## 🖼️ Banner do Projeto

![Banner](./A_digital_graphic_design_banner_titled_"Simulação_.png)

---

## 🎯 Casos de Uso

- Análise estatística e exploratória de processos judiciais
- Treinamento de modelos de predição de decisões judiciais
- Desenvolvimento de dashboards de indicadores jurídicos
- Simulações internas para departamentos jurídicos empresariais

---

## 🧪 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/simulacao-dados-juridicos.git
   ```

2. Execute o script Python:
   ```bash
   python gerar_dados.py
   ```

3. Os arquivos `clientes.csv` e `processos_juridicos_complexo.csv` serão salvos no mesmo diretório.

---

## ⚠️ Aviso Legal

> Os dados gerados por este projeto são **inteiramente fictícios**. Qualquer semelhança com nomes, empresas, processos ou instituições reais é mera coincidência. Utilização segura para fins de estudo, portfólio ou demonstração.

---

## 👨‍💼 Autor

**Kelvin Santos Andrade**  
Analista de Dados | Business Intelligence | Portfólio de Projetos  
🔗 [LinkedIn](https://www.linkedin.com/in/kelvinandradeworks/)  
🔗 [Portfólio](https://ksaworks.github.io/portfolio_projetos/)
