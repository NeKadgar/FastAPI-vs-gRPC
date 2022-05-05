import logging
import time

from flask import Flask, jsonify

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

count = 0
start_time = time.time()


@app.route("/hello/<name>")
def hello_name(name):
    global count, start_time
    count += 1
    if count % 1000 == 0:
        print(f"1000 responses in {time.time() - start_time} sec")
        start_time = time.time()
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    app.run(port=8000)
