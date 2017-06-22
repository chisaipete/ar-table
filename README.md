# ar-table
cd .
python -m venv flask
. flask/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
./db_create.py
./db_upgrade.py
./run.py
