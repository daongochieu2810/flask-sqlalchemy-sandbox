from src import app, utils
from src.models import Models

if __name__ == '__main__':
    models = Models()
    models.createModels()
    #utils.readDbFile("src/data.sql", models)
    app.run(debug=True)
