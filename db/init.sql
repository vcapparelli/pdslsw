CREATE TABLE IF NOT EXISTS programas (
	id SERIAL PRIMARY KEY,
	nome TEXT NOT NULL
);

INSERT INTO programas (nome) VALUES
('Debian GNU/Linux'),
('Docker'),
('Alpine Linux'),
('Postgres')
;
