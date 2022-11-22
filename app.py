from flask import Flask
import flask_config
from flask_feature_flag import flag

app = Flask(__name__)
app.config.from_object(flask_config)


@app.route("/")
def hello_world():  # put application's code here
    if flag("hello_world"):
        return "Hello, World!"
    return "Meow!Meow!Meow!Meow!Meow!Meow!Meow!Meow!Meow!Meow!"


if __name__ == "__main__":
    app.run()
