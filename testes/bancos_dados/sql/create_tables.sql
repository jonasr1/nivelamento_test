CREATE TABLE demonstracoes_contabeis (
    id serial PRIMARY key, data DATE NOT NULL, reg_ans VARCHAR(10) NOT NULL, cd_conta_contabil VARCHAR(50) NOT NULL, 
    descricao TEXT NOT NULL, vl_saldo_inicial NUMERIC(18, 2), vl_saldo_final NUMERIC(18, 2),
    ano INT GENERATED ALWAYS AS (EXTRACT(YEAR FROM data)) STORED,
    trimestre INT GENERATED ALWAYS AS (EXTRACT(QUARTER FROM data)) STORED
);

CREATE TABLE operadoras_plano_saude_ativas (
    id SERIAL PRIMARY KEY, registro_ans VARCHAR(10) NOT NULL UNIQUE, cnpj VARCHAR(14) NOT NULL, razao_social TEXT NOT NULL,
    nome_fantasia TEXT, modalidade TEXT, logradouro TEXT, numero TEXT, complemento TEXT, bairro TEXT, cidade TEXT,
    uf VARCHAR(2), cep VARCHAR(8), ddd VARCHAR(3), telefone TEXT, fax VARCHAR(16), endereco_eletronico TEXT,
    representante TEXT, cargo_representante TEXT, regiao_comercializacao TEXT, data_regiao DATE
);