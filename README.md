# StockSentry
A website used to manage investment portfolio


## Installation

```bash
conda create --name stocksentry python -y
conda activate stocksentry
pip install -r requirements.txt
```

```bash
django-admin startproject stocksentry
python manage.py startapp users
python manage.py migrate
python manage.py createsuperuser
```