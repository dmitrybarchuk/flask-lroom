import local_settings
from app import app

if __name__ == '__main__':
    app.run(debug=local_settings.DEBUG)
