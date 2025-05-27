from src.data.load.create_table import create_table
from src.data.load.load_data import load_data
from src.data.load.read_db import read_db


def main():    
    create_table()
    load_data()
    read_db()