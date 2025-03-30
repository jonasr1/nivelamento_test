# Documentação do Processo de Importação de Dados

Este repositório contém um conjunto de arquivos CSV que serão importados para o banco de dados PostgreSQL. Durante o processo de importação, foi necessário ajustar os dados numéricos nos arquivos para garantir que fossem interpretados corretamente pelo PostgreSQL.

## Problema

Os arquivos CSV estavam utilizando vírgulas (`,`) como separadores decimais para números (ex: `168042,38`), enquanto o PostgreSQL espera o ponto (`.`) como separador decimal para valores numéricos.

### Solução

Para resolver este problema, foi utilizado o comando `sed` para substituir todas as vírgulas por pontos nos arquivos CSV, garantindo que os valores numéricos fossem compatíveis com o formato esperado pelo PostgreSQL.

## Comando Executado

Exemplo:

```bash
sed -i 's/,/./g' /home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2023/1T2023.csv
```

## Criação do Banco de Dados

Para criar o banco de dados, execute o comando:

```bash
psql -U postgres
CREATE DATABASE test_db;
```

## Criação das Tabelas

Após criar o banco de dados, as seguintes tabelas foram criadas para armazenar os dados importados:

### Tabela demonstracoes_contabeis

```sql
CREATE TABLE demonstracoes_contabeis (
    id serial PRIMARY key, data DATE NOT NULL, reg_ans VARCHAR(10) NOT NULL, cd_conta_contabil VARCHAR(50) NOT NULL, 
    descricao TEXT NOT NULL, vl_saldo_inicial NUMERIC(18, 2), vl_saldo_final NUMERIC(18, 2),
    ano INT GENERATED ALWAYS AS (EXTRACT(YEAR FROM data)) STORED,
    trimestre INT GENERATED ALWAYS AS (EXTRACT(QUARTER FROM data)) STORED
);
```

### Tabela operadoras_plano_saude_ativas

```sql
CREATE TABLE operadoras_plano_saude_ativas (
    id SERIAL PRIMARY KEY, registro_ans VARCHAR(10) NOT NULL UNIQUE, cnpj VARCHAR(14) NOT NULL, razao_social TEXT NOT NULL,
    nome_fantasia TEXT, modalidade TEXT, logradouro TEXT, numero TEXT, complemento TEXT, bairro TEXT, cidade TEXT,
    uf VARCHAR(2), cep VARCHAR(8), ddd VARCHAR(3), telefone TEXT, fax VARCHAR(16), endereco_eletronico TEXT,
    representante TEXT, cargo_representante TEXT, regiao_comercializacao TEXT, data_regiao DATE
);
```

## Importação dos Dados

Após a criação das tabelas, os dados foram importados dos arquivos CSV para as tabelas no banco de dados. Para cada tabela, o comando \copy foi utilizado no PostgreSQL para importar os dados de cada arquivo CSV.

Exemplo para a tabela demonstracoes_contabeis:

```sql
\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2023/1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';

```

## Uso de unaccent e regexp_replace

Durante a importação de dados, foi necessário aplicar algumas transformações nas colunas de texto para garantir que a busca e comparação de dados fossem realizadas corretamente. Para isso, foram utilizados dois métodos: o unaccent e o regexp_replace. Aqui está o motivo para cada um:

### 1. Uso do unaccent

Objetivo: Remover acentos das palavras.

Motivo: O PostgreSQL, por padrão, considera acentos ao realizar comparações de texto. Isso pode gerar inconsistências nos resultados das consultas, especialmente se houver variações na forma de acentuação dos dados de entrada. Utilizando o unaccent, conseguimos remover os acentos das palavras e realizar comparações mais flexíveis.

Exemplo:

```sql
SELECT * FROM demonstracoes_contabeis WHERE unaccent(descricao) ILIKE '%assistencia%';
```

Com isso, a busca não será afetada por caracteres acentuados como á ou ã.

### 2. Uso do regexp_replace

Objetivo: Substituir múltiplos espaços consecutivos por um único espaço.

Motivo: Os dados importados podem conter espaços extras entre as palavras ou entre palavras e pontuação. Isso pode causar inconsistências nas consultas, já que o PostgreSQL considera espaços extras como parte do texto. Utilizando o regexp_replace, garantimos que qualquer ocorrência de múltiplos espaços seja substituída por um único espaço, normalizando o texto para buscas e comparações mais precisas.

Exemplo:

```sql
SELECT * FROM demonstracoes_contabeis WHERE regexp_replace(descricao, '\s+', ' ', 'g') ILIKE '%assistencia%';
```

Isso assegura que espaços adicionais não interferirão nas comparações de texto.
