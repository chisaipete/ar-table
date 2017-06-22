# ar-table
cd .
python -m venv flask
flask\Scripts\pip install -r requirements.txt
./db_create.py
./db_upgrade.py
./run.py
