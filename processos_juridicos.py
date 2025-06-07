import pandas as pd
import random
from faker import Faker
from datetime import timedelta, date

# Inicialização
fake = Faker('pt_BR')
random.seed(42)
Faker.seed(42)

# --- Parâmetros de Geração ---
n_processos = 2000 # Aumentado para mais dados
n_clientes = 200 # Novo parâmetro para o número de clientes
n_responsaveis = 25 # Aumentado o número de responsáveis
n_empresas_clientes = 100 # Número de empresas que podem ser clientes
n_pessoas_clientes = 100 # Número de pessoas físicas que podem ser clientes
n_escritorios = 10 # Número de escritórios/filiais

tipos_processo = [
    'Execução', 'Monitória', 'Conhecimento', 'Cautelar', 'Ação Popular',
    'Ação Civil Pública', 'Mandado de Segurança', 'Inventário', 'Divórcio',
    'Usucapião', 'Revisão Contratual', 'Recuperação Judicial', 'Falência'
]
areas_juridicas = [
    'Direito Civil', 'Direito do Trabalho', 'Direito Tributário',
    'Direito Empresarial', 'Direito Administrativo', 'Direito Ambiental',
    'Direito de Família', 'Direito do Consumidor', 'Direito Penal',
    'Direito Imobiliário', 'Direito Previdenciário'
]
fases = [
    'Petição Inicial', 'Contestação', 'Réplica', 'Saneamento', 'Instrução Probatória',
    'Alegações Finais', 'Sentença', 'Recurso de Apelação', 'Recurso Especial',
    'Recurso Extraordinário', 'Execução', 'Encerrado', 'Suspenso'
]
status_processo = ['Ativo', 'Encerrado', 'Suspenso', 'Arquivado']
decisoes = [
    'Procedente', 'Improcedente', 'Parcialmente Procedente', 'Acordo Homologado',
    'Extinto sem Resolução de Mérito', 'Extinto com Resolução de Mérito',
    'Prejudicado', 'Recurso Provido', 'Recurso Improvido'
]
tribunais = [
    'TJSP', 'TRF1', 'TRF2', 'TRF3', 'TRF4', 'TRF5', 'TJMG', 'TJRJ', 'TJRS',
    'TJPR', 'TJSC', 'TJBA', 'TJDF', 'STJ', 'STF', 'TST', 'TRT1', 'TRT2', 'TRT3'
]
comarcas = [
    'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre',
    'Curitiba', 'Salvador', 'Brasília', 'Recife', 'Fortaleza', 'Campinas',
    'Ribeirão Preto', 'Florianópolis', 'Vitória', 'Goiânia'
]
instancias = ['1ª Instância', '2ª Instância', 'STJ', 'STF', 'TST']
uf_br = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS',
         'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

# Geração de listas de entidades
responsaveis = [fake.name() for _ in range(n_responsaveis)]
escritorios_responsaveis = [f"{fake.company()} Advogados" for _ in range(n_escritorios)]

# Geração de Clientes
clientes_data = []
for i in range(1, n_clientes + 1):
    tipo_cliente = random.choice(['Pessoa Física', 'Pessoa Jurídica'])
    if tipo_cliente == 'Pessoa Física':
        nome_cliente = fake.name()
    else:
        nome_cliente = fake.company()
    clientes_data.append({
        'id_cliente': i,
        'nome_cliente': nome_cliente,
        'tipo_cliente': tipo_cliente,
        'uf_cliente': random.choice(uf_br)
    })
df_clientes = pd.DataFrame(clientes_data)
df_clientes.to_csv('clientes.csv', index=False)
print("Arquivo 'clientes.csv' criado com sucesso!")

# --- Geração dos Dados de Processos ---
dados_processos = []

for i in range(1, n_processos + 1):
    # Geração de número de processo simulado (formato XXXXX-XX.XXXX.X.XX.XXXX)
    numero_processo = f"{random.randint(10000, 99999)}-{random.randint(0, 99):02d}.{random.randint(1990, 2024):04d}.{random.randint(1, 9)}.{random.randint(1, 99):02d}.{random.randint(1000, 9999)}"

    # Escolha de clientes para polo ativo e passivo
    cliente_polo_ativo = random.choice(df_clientes['nome_cliente'].tolist())
    cliente_polo_passivo = random.choice(df_clientes['nome_cliente'].tolist())
    while cliente_polo_ativo == cliente_polo_passivo: # Garante que não sejam a mesma entidade
        cliente_polo_passivo = random.choice(df_clientes['nome_cliente'].tolist())

    tipo = random.choice(tipos_processo)
    area = random.choice(areas_juridicas)
    responsavel = random.choice(responsaveis)
    escritorio = random.choice(escritorios_responsaveis)
    tribunal = random.choice(tribunais)
    comarca = random.choice(comarcas)
    instancia = random.choice(instancias)
    uf_processo = random.choice(uf_br)

    valor = round(random.uniform(1000, 1000000), 2)
    custo = round(valor * random.uniform(0.01, 0.15), 2)
    honorarios = round(valor * random.uniform(0.05, 0.25), 2) if random.random() < 0.8 else 0 # Nem todo processo tem honorários na simulação
    provisao_risco = round(valor * random.uniform(0.1, 0.9), 2) if random.random() < 0.7 else 0 # Provisão de risco

    data_abertura = fake.date_between(start_date='-5y', end_date='-60d')
    
    # Simulação de status e datas
    status = random.choice(status_processo)
    
    data_encerramento = None
    tempo_dias = None
    decisao = None
    fase = 'Petição Inicial' # Fase inicial padrão

    if status == 'Encerrado' or status == 'Arquivado':
        data_encerramento = data_abertura + timedelta(days=random.randint(90, 1800))
        if data_encerramento > date.today(): # Garante que a data de encerramento não seja no futuro
            data_encerramento = date.today() - timedelta(days=random.randint(1, 30))
        tempo_dias = (data_encerramento - data_abertura).days
        decisao = random.choice(decisoes)
        fase = 'Encerrado' if status == 'Encerrado' else 'Arquivado'
    else: # Processos Ativos ou Suspensos
        fase = random.choice([f for f in fases if f not in ['Encerrado', 'Arquivado']])
        if status == 'Suspenso':
            fase = 'Suspenso'
    
    data_ultima_movimentacao = data_abertura + timedelta(days=random.randint(1, (date.today() - data_abertura).days if data_abertura < date.today() else 1))
    if data_ultima_movimentacao > date.today():
        data_ultima_movimentacao = date.today()

    # Geração de movimentações/eventos do processo
    movimentacoes = []
    num_movimentacoes = random.randint(1, 15) if status != 'Encerrado' and status != 'Arquivado' else random.randint(5, 25)
    current_date = data_abertura
    for _ in range(num_movimentacoes):
        if current_date > date.today():
            break
        mov_date = current_date + timedelta(days=random.randint(15, 90))
        if mov_date > date.today():
            mov_date = date.today()
        mov_descricao = fake.sentence(nb_words=8)
        movimentacoes.append(f"{mov_date.strftime('%Y-%m-%d')}: {mov_descricao}")
        current_date = mov_date
        if current_date > data_ultima_movimentacao:
            data_ultima_movimentacao = current_date
        
    dados_processos.append({
        'id_processo': i,
        'numero_processo': numero_processo,
        'polo_ativo': cliente_polo_ativo,
        'polo_passivo': cliente_polo_passivo,
        'tipo_processo': tipo,
        'area_juridica': area,
        'valor_causa': valor,
        'custo_total': custo,
        'honorarios_advogado': honorarios,
        'provisao_risco': provisao_risco,
        'fase_atual': fase,
        'status_processo': status,
        'data_abertura': data_abertura,
        'data_ultima_movimentacao': data_ultima_movimentacao,
        'data_encerramento': data_encerramento,
        'tempo_tramitacao_dias': tempo_dias,
        'decisao_final': decisao,
        'responsavel': responsavel,
        'escritorio_responsavel': escritorio,
        'tribunal_responsavel': tribunal,
        'comarca': comarca,
        'instancia': instancia,
        'uf_processo': uf_processo,
        'descricao_processo': fake.paragraph(nb_sentences=2),
        'movimentacoes': movimentacoes # Lista de strings para simular eventos
    })

# Criação do DataFrame e exportação
df_processos = pd.DataFrame(dados_processos)
df_processos.to_csv('processos_juridicos_complexo.csv', index=False)
print("Arquivo 'processos_juridicos_complexo.csv' criado com sucesso!")