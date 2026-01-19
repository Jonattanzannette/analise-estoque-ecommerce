--  Gerar calendário de datas
WITH datas AS (
    SELECT CAST('2025-10-01' AS DATE) AS data_referencia
    UNION ALL
    SELECT DATEADD(DAY, 1, data_referencia)
    FROM datas
    WHERE data_referencia < '2025-10-30'
),

-- Cruzar produtos com datas
estoque_base AS (
    SELECT
        p.produto_id,
        1 AS estoque_id,
        d.data_referencia,

        -- 3) Quantidade simulada (base + variação)
        CASE 
            WHEN (3 + p.produto_id + ABS(CHECKSUM(NEWID())) % 7 - 2) < 0 
                THEN 0
            ELSE (3 + p.produto_id + ABS(CHECKSUM(NEWID())) % 7 - 2)
        END AS quantidade

    FROM produtos p
    CROSS JOIN datas d
)

--  Inserir no estoque_atual
INSERT INTO estoque_atual (produto_id, estoque_id, quantidade, data_referencia)
SELECT
    produto_id,
    estoque_id,
    quantidade,
    data_referencia
FROM estoque_base
OPTION (MAXRECURSION 0);