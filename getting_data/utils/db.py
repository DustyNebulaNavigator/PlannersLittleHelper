from decouple import config
import psycopg2
from typing import List, Optional
from datetime import datetime

DATABASE_NAME = config('DATABASE_NAME')
DATABASE_USER = config('DATABASE_USER')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')
DATABASE_HOST = config('DATABASE_HOST')
DATABASE_TABLE_IMPULSES = config('DATABASE_TABLE_IMPULSES')
DATABASE_TABLE_MACHINES = config('DATABASE_TABLE_MACHINES')


class Database:
    def __init__(self, machine_names: List[str]):
        self.conn = psycopg2.connect(dbname=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST)
        self.table_name_machines = DATABASE_TABLE_MACHINES
        self.table_name_impulses = DATABASE_TABLE_IMPULSES
        self.cursor = self.conn.cursor()
    

    def add_record(self, machine_name: str, counter:int, timestamp:int, product_name: str="Missing"):
        self.cursor.execute(f'''
            INSERT INTO {self.table_name_impulses} (machine_name, sensor_counter, sensor_timestamp, created_at) VALUES (%s, %s, %s, %s);
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
    
    def update_machine_status(self, machine_name:str, status: str):
        """
        Database has unique constraint on machine_name.
        If there is no machine name, row is created.
        If there is machine name, then row status is updated.
        """
        self.cursor.execute(f"""
        INSERT INTO {self.table_name_machines} (machine_name, status) 
        VALUES (%s, %s) 
        ON CONFLICT (machine_name) 
        DO UPDATE SET status = EXCLUDED.status;
        """, (machine_name, status))

        self.conn.commit()
