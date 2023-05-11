# BitPin Task Project

## .env
```bash
vim .env
```
```
DB_NAME=bitpin
DB_USER=bitpin
DB_PASSWORD=bitpin
DB_HOST=localhost
DB_PORT=
```

## PostgreSQL
```bash
sudo -u postgres psql
postgres=# CREATE DATABASE [your db name];
postgres=# CREATE USER [your db user] WITH PASSWORD [your db password];
postgres=# ALTER ROLE [your db user] SET client_encoding TO 'utf8';
postgres=# ALTER ROLE [your db user] SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE [your db user] SET timezone TO 'UTC';
postgres=# GRANT ALL PRIVILEGES ON DATABASE [your db name] TO [your db user];
postgres=# \q
```