DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS politicians;
DROP TABLE IF EXISTS users_following_politicians;
DROP TABLE IF EXISTS users_following_count;
DROP TABLE IF EXISTS statuses;
DROP TABLE IF EXISTS final_users;
DROP TABLE IF EXISTS results;



CREATE TABLE users(
	id INTEGER,
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

CREATE TABLE users_following_politicians(
	id INTEGER,
	twitter_id INTEGER,
	politicians_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (politicians_id) REFERENCES politicians(id)
);

CREATE TABLE users_following_count(
	id INTEGER,
	users_id INTEGER,
	follow_count INTEGER,
	party STRING,
	PRIMARY KEY (id),
	FOREIGN KEY (users_id) REFERENCES users(id)
);

CREATE TABLE statuses(
	id INTEGER,
	users_id INTEGER,
	statuses STRING,
	PRIMARY KEY(id),
	FOREIGN KEY(users_id) REFERENCES users(id)
);

CREATE TABLE final_users(
	id INTEGER,
	users_id INTEGER,
	party STRING,
	PRIMARY KEY(id),
	FOREIGN KEY(users_id) REFERENCES users(id)
);

CREATE TABLE final_users_en(
	id INTEGER,
	users_id INTEGER,
	party STRING,
	PRIMARY KEY(id),
	FOREIGN KEY(users_id) REFERENCES users(id)
);

CREATE TABLE results(
	party String,
	correct integer,
	incorrect integer
);


	

.separator ","
.import candidates.csv politicians