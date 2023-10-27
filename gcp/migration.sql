CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> da391babf012

ALTER TABLE patients DROP COLUMN contact_number;

INSERT INTO alembic_version (version_num) VALUES ('da391babf012');

-- Running upgrade da391babf012 -> b788106dc09a

ALTER TABLE patients ADD COLUMN address VARCHAR(50) NOT NULL;

UPDATE alembic_version SET version_num='b788106dc09a' WHERE alembic_version.version_num = 'da391babf012';

