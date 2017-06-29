# ar-table
```bash
cd .
python -m venv flask
. flask/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
# this dev version needs to be used on WSL in order to get around 
# the SO_REUSEPORT bug until next PyPi Release (beyond 0.21.0)
pip install -U https://github.com/eventlet/eventlet/archive/master.zip
pip install -U https://github.com/benoitc/gunicorn/archive/master.zip
./db_create.py
./db_upgrade.py
# ./run.py
gunicorn --worker-class eventlet -w 1 --certfile cert.pem --keyfile key.pem -b 0.0.0.0:5500 app:app```
