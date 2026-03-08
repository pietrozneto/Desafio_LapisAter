import csv
import os
from datetime import datetime

LOG_FILE = "data/logs.csv"

os.makedirs("data", exist_ok=True)

def log_request(data, audio_file):

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "age_range",
                "mood",
                "context",
                "style",
                "length",
                "audio_file"
            ])

        writer.writerow([
            datetime.now(),
            data["age_range"],
            data["mood"],
            data["context"],
            data["style"],
            data["length"],
            audio_file
        ])