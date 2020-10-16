CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    brukernavn VARCHAR(255) UNIQUE,
    epost VARCHAR(255) UNIQUE,
    passord VARCHAR(255)
);