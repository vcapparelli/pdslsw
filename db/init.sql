CREATE TABLE IF NOT EXISTS softwares (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

INSERT INTO softwares (name) VALUES
('Debian GNU/Linux'),
('Podman'),
('Alpine Linux'),
('Postgres'),
('Python'),
('FastAPI'),
('Uvicorn'),
('asyncpg')
;
