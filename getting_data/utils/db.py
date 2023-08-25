from decouple import config
import psycopg2
from typing import List, Optional
from datetime import datetime

DATABASE_NAME = config('DATABASE_NAME')
DATABASE_TABLE_NAME = config('DATABASE_TABLE_NAME')
DATABASE_USER = config('DATABASE_USER')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')
DATABASE_HOST = config('DATABASE_HOST')


class Database:
    def __init__(self, machine_names: List[str]):
        self.conn = psycopg2.connect(dbname=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST)
        self.table_name = DATABASE_TABLE_NAME
        self.cursor = self.conn.cursor()
        #self.create_table(machine_names)
    
    """
    def create_table(self, machine_names: List[str]):
        # Each machine has its own table
        for machine in machine_names:
            self.cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {machine} (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    counter INTEGER,
                    timestamp INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                ''')
            self.conn.commit()
    """
    def add_record(self, machine_name: str, counter:int, timestamp:int, product_name: str="Missing"):
        self.cursor.execute(f'''
            INSERT INTO {self.table_name} (machine_name, sensor_counter, sensor_timestamp, created_at) VALUES (%s, %s, %s, %s);
            ''', (machine_name, counter, timestamp, datetime.now()))
        self.conn.commit()

    def get_latest_counter_value(self, machine_name:str) -> int:
        """
        If there is no values in table, N
        Returns:
            int: If there is record in database table, then counter value as integer. If there is not, then 0.
        """
        try:
            query_string = f"""
                SELECT sensor_counter 
                FROM machine_integrations_impulses 
                WHERE machine_name = '{machine_name}'
                ORDER BY id DESC 
                LIMIT 1;
                """
            self.cursor.execute(query_string)
            value = self.cursor.fetchone()[0]
        except psycopg2.errors.UndefinedTable:
            # Table with machine name does not exist.
            # This should not happen because tabels are created (if not present) when program starts
            value = None
        except TypeError:
            # There are no records in database table
            value = 0

        return value
    
    def drop_tables(self, machine_names: List[str]):
        """Drops all tables with given names """
        for machine in machine_names:
            self.cursor.execute(f"DROP TABLE IF EXISTS {machine};")
            self.conn.commit()
