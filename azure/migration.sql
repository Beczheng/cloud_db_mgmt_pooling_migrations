CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 86dd3688ee2b

ALTER TABLE patients DROP COLUMN contact_number;

INSERT INTO alembic_version (version_num) VALUES ('86dd3688ee2b');

-- Running upgrade 86dd3688ee2b -> 24866818c867

ALTER TABLE patients ADD COLUMN address VARCHAR(50) NOT NULL;

UPDATE alembic_version SET version_num='24866818c867' WHERE alembic_version.version_num = '86dd3688ee2b';

