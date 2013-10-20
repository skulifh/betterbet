DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS politicians;
DROP TABLE IF EXISTS users_politicians;

CREATE TABLE users(
	id INTEGER,
	twitter_id INTEGER,
	PRIMARY KEY (id)
);

CREATE TABLE politicians(
	id INTEGER,
	name STRING,
	screenname STRING,
	party STRING,
	followers INTEGER,
	PRIMARY KEY (id)
);

CREATE TABLE users_politicians(
	id INTEGER,
	users_id INTEGER,
	politicians_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (users_id) REFERENCES users(id),
	FOREIGN KEY (politicians_id) REFERENCES politicians(id)
);

.separator ","
.import candidates.csv politicians