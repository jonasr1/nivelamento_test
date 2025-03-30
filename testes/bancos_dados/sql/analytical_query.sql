-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

WITH despesas_trimestre AS (
    SELECT 
        d.reg_ans,
        SUM(d.vl_saldo_final) AS total_despesas
    FROM 
        demonstracoes_contabeis d
    WHERE 
        unaccent(regexp_replace(d.descricao, '\s+', ' ', 'g')) ILIKE 
        unaccent('%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%')
        AND d.trimestre = 4
        d.reg_ans
)
SELECT 
    o.registro_ans,
    o.razao_social,
    dt.total_despesas
FROM 
    despesas_trimestre dt
JOIN 
    operadoras_plano_saude_ativas o ON dt.reg_ans = o.registro_ans
ORDER BY 
    dt.total_despesas DESC
LIMIT 10;

--  Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

WITH despesas_ano AS (
    SELECT 
        d.reg_ans,
        SUM(d.vl_saldo_final) AS total_despesas
    FROM 
        demonstracoes_contabeis d
    WHERE 
        unaccent(regexp_replace(d.descricao, '\s+', ' ', 'g')) ILIKE 
        unaccent('%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%')
        AND d.ano = (SELECT MAX(ano) FROM demonstracoes_contabeis)
    GROUP BY 
        d.reg_ans
)
SELECT 
    o.registro_ans,
    o.razao_social,
    da.total_despesas
FROM 
    despesas_ano da
JOIN 
    operadoras_plano_saude_ativas o ON da.reg_ans = o.registro_ans
ORDER BY 
    da.total_despesas DESC
LIMIT 10;
