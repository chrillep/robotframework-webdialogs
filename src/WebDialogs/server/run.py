import threading

from .app import app

WEBDIALOGS_PORT = 5001


def run_flask():
    app.run(port=WEBDIALOGS_PORT, debug=False, use_reloader=False)


def start_flask_server():
    thread = threading.Thread(target=run_flask, daemon=True)
    thread.start()


if __name__ == "__main__":
    app.run("0.0.0.0", WEBDIALOGS_PORT, debug=True)
