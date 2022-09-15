from src import app, utils
from src.models import Models

if __name__ == '__main__':
    from os import environ
    models = Models()
    models.createModels()
    utils.readDbFile("src/data.sql", models)
    app.run(host='0.0.0.0', debug=False, port=environ.get("PORT", 5001))
