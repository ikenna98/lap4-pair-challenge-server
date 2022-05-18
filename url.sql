DROP TABLE IF EXISTS shortURL;
CREATE TABLE shortURL (
    id integer PRIMARY KEY autoincrement,
    URL varchar(300) NOT NULL,
    shortURL varchar(50) NOT NULL,
);

