# Ghost Blog Data Sanitizer

![Python](https://img.shields.io/badge/Python-v3.7-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v1.0.2-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![PyMySQL](https://img.shields.io/badge/PyMySQL-v0.9.3-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Google Cloud Functions](https://img.shields.io/badge/Google--Cloud--Functions-v93-blue.svg?longCache=true&logo=google&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/ghost-sql-sanitation.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/ghost-sql-sanitation/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/ghost-sql-sanitation.svg?style=flat-square8&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/ghost-sql-sanitation/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/ghost-sql-sanitation.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/ghost-sql-sanitation/network)

Executes various SQL queries for blog maintenance. Looks in **/queries** folder for SQL queries and executes all of them.

## Getting Started

Installation is recommended with Pipenv:

```shell
$ git clone https://github.com/hackersandslackers/ghost-sql-sanitation.git
$ cd ghost-sql-sanitation
$ pipenv shell
$ pipenv update
$ python3 main.py
```

Alternatively, try installing via `setup.py`:

```shell
$ git clone https://github.com/hackersandslackers/ghost-sql-sanitation.git
$ cd ghost-sql-sanitation
$ python3 setup.py run
```

The following environment variables are required to run this script:

* `DATABASE_USERNAME`: User with access to your Ghost blog's database.
* `DATABASE_PASSWORD`: Password for the above user.
* `DATABASE_HOST`: The host name where your database lives (either a managed DB, or publicly accessible local DB)
* `DATABASE_NAME`: The name of the database/schema where your Ghost tables live.
* `DATABASE_PORT`: The port.
* `DATABASE_CERT` _(optional)_: Path to SSL certificate for protected databases.
* `DATABASE_PEM` _(optional)_: See above.
* `DATABASE_KEY` _(optional)_: See above.
* `SQL_FOLDER`: The local folder (in this repo) where your SQL files live.


-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
