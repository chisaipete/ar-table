# ar-table
```bash
cd .
python -m venv flask
. flask/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -U https://github.com/eventlet/eventlet/archive/master.zip
# this dev version needs to be used on WSL in order to get around the SO_REUSEPORT bug until next PyPi Release (beyond 0.21.0)
./db_create.py
./db_upgrade.py
./run.py
```
