import logging

def log_def(name, file):
    game_history = logging.Logger(name, level=logging.INFO)
    f = logging.FileHandler(file)
    myformat = logging.Formatter(" %(asctime)s - %(name)s — %(message)s")
    f.setFormatter(myformat)
    game_history.addHandler(f)
    return game_history