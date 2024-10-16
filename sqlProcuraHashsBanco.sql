SELECT nomearqlocal
FROM processoanexo
WHERE idprocesso = (
    SELECT idprocesso
    FROM processo
    WHERE codigo = 111
    AND exercicio = 2024
);