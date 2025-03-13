CREATE TABLE IF NOT EXISTS task (
t_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
t_name TEXT NOT NULL,
t_priority INTEGER NOT NULL,
u_id_fk INTEGER NOT NULL,
FOREIGN KEY(u_id_fk) REFERENCES user(u_id)
);