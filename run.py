from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
python -m venv venv
source venv/bin/activate     # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py

