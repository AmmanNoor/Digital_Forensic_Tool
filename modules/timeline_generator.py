import os
from datetime import datetime


def extract_events(filepath):
    stats = os.stat(filepath)
    return [
        {"time": datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S"), "event": "File Created"},
        {"time": datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S"), "event": "File Modified"},
        {"time": datetime.fromtimestamp(stats.st_atime).strftime("%Y-%m-%d %H:%M:%S"), "event": "File Accessed"}
    ]

def generate_timeline(events):
    return sorted(events, key=lambda x: x['time'])