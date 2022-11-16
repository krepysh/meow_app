from flask import Flask
import flask_config

app = Flask(__name__)
app.config.from_object(flask_config)


@app.route('/')
def hello_world():  # put application's code here
    return 'Meow!Meow!Meow!Meow!Meow!Meow!Meow!Meow!Meow!Meow!'


if __name__ == '__main__':
    app.run()
