import requests
import json
import pandas as pd
import time
import os
import csv
from datetime import datetime

class CSVHandler:
    def __init__(self, csv_directory):
        self.csv_directory = csv_directory

    def create_csv_with_header(self, csv_file):
        if not os.path.exists(csv_file):
            with open(csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["timestamp", "value"])

    def update_csv(self, csv_file, timestamp, value):
        formatted_timestamp = timestamp
        new_data = {"timestamp": [formatted_timestamp], "value": [value]}
        df = pd.DataFrame(new_data)
        df.to_csv(csv_file, mode='a', header=False, index=False)


class DirHandler:
    def __init__(self, directory):
        self.directory = directory

    def create_directory(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

class DataFetcher:
    def __init__(self, api_url, query, csv_directory):
        self.api_url = api_url
        self.query = query
        self.csv_directory = csv_directory

    def fetch_and_save_data(self, interval=5):
        while True:
            timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%s")
            file_timesptamp = datetime.now().strftime("%d-%m-%Y")
            csv_file = os.path.join(self.csv_directory, f"{file_timesptamp}-dados-cpu.csv")
            csv_handler = CSVHandler(self.csv_directory)
            csv_handler.create_csv_with_header(csv_file)

            response = requests.get(self.api_url, params={'query': self.query})
            
            if response.status_code == 200:
                data = response.json()
                result = data["data"]["result"][0]
                value = result["value"][1]

                csv_handler.update_csv(csv_file, timestamp, value)

                print(f"Dados salvos em {csv_file}")

            time.sleep(interval)

if __name__ == "__main__":
    api_url = "http://192.168.158.250:9090/api/v1/query"
    query = 'container_cpu_usage_seconds_total{container="nginx-deploy-escalar",job="kubernetes-cadvisor",kubernetes_io_hostname="master",namespace="with-hpa"} * 100'
    csv_directory = "./data/"
    dir_handler = DirHandler(csv_directory)

    data_fetcher = DataFetcher(api_url, query, csv_directory)
    data_fetcher.fetch_and_save_data()
