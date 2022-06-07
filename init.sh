# Install requirements
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Execute continuous ping
python3 src/ping-plot.py