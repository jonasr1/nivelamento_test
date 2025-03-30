\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2023/1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2023/2T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2023/3T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2023/4T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';


\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2024/1T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2024/2T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2024/3T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';

\copy demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/demonstracoes_contabeis/2024/4T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';

\copy operadoras_plano_saude_ativas(
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade,logradouro, numero, complemento, bairro, cidade, uf, cep,
    ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_comercializacao, data_regiao
    )
FROM '/home/jonas/Projects/nivelamento_test/testes/bancos_dados/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF-8' NULL '';
