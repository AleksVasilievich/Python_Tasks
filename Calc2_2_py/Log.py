from pathlib import Path


class Log:
    LOG_PATH = Path(__file__).parent / "calc2_2.txt"

    @staticmethod
    def log(text):
        print(text)
        with open(Log.LOG_PATH, 'a', encoding='utf_8') as file:
            file.write(text + "\n")