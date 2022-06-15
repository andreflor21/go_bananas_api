# Api Go-bananas &#174;

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/andreflor21/go_bananas_api)](https://github.com/andreflor21/api-go-bananas/blob/main/LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andreflor21/go_bananas_api?include_prereleases)](https://GitHub.com/andreflor21/api-go-bananas/releases/)

## Run Dev server

-   **Dev server run on**: <code>https://localhost:5000</code>

```shell
flask run
```

---

## Requirements

### Install requirements

```shell
pip install -r requirements.txt
```

### Update requirements

```shell
pip freeze > requirements.txt
```

---

## Migrations

### New migrations

```shell
flask db migrate -m 'Creation - Table Car'
```

### Make migrations

```shell
flask db upgrade
```
