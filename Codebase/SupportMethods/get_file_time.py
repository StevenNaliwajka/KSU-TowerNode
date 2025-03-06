from datetime import datetime

def get_file_time():
    return datetime.now().strftime('%H-%M-%S')