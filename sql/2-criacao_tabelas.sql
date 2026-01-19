-- TABELA PRODUTOS CHAVE PRIMARIA produto_id
CREATE TABLE produtos( 
produto_id INT PRIMARY KEY, 
sku VARCHAR(50), nome_produto VARCHAR(255), 
marca VARCHAR(100), categoria VARCHAR(100), 
preco DECIMAL(10,2) ); 

-- TABELA ESTOQUES CHAVE PRIMARIA estoques_id
CREATE TABLE estoques ( 
estoque_id INT IDENTITY (1,1) PRIMARY KEY, 
descricao VARCHAR (50) NOT NULL ); 

-- TABELA ESTOQUE_ ATUAL 
CREATE TABLE estoque_atual ( 
produto_id INT NOT NULL, 
estoque_id INT NOT NULL, 
quantidade INT NOT NULL, 
data_referencia DATE NOT NULL, 

CONSTRAINT pk_estoque_atual 
	PRIMARY KEY (produto_id, estoque_id, data_referencia), 
CONSTRAINT fk_estoque_atual_produto 
	FOREIGN KEY (produto_id) REFERENCES produtos(produto_id), 
CONSTRAINT fk_estoque_atual_estoque 
	FOREIGN KEY (estoque_id) REFERENCES estoques(estoque_id) ); 