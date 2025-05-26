import json, toml
import sys
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Load config and secrets at the top-level
from config_secrets import load_config_and_secrets
env, local_secrets = load_config_and_secrets()

# Append the directory where db_utils.py is located
sys.path.append(os.path.abspath('C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Project2/Bird_Species_Observation'))


from db_utils import connect_to_postgres, connect_to_birdspecies

def setup_database_connection(env, local_secrets):
    # Step 1: Connect to the default 'postgres' database
    my_db_connection = connect_to_postgres(env, local_secrets)
    my_db_connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    mycursor = my_db_connection.cursor()

    # Step 2: Check if 'birdspecies' DB exists
    mycursor.execute("SELECT 1 FROM pg_database WHERE datname = 'birdspecies'")
    exists = mycursor.fetchone()

    if not exists:
        try:
            mycursor.execute("CREATE DATABASE birdspecies")
            print("✅ Database 'birdspecies' created successfully.")
        except Exception as e:
            print("❌ Failed to create database:", e)
    else:
        print("ℹ️ Database 'birdspecies' already exists.")

    mycursor.close()
    my_db_connection.close()

    # Step 3: Connect to 'birdspecies' DB
    conn = connect_to_birdspecies(env, local_secrets)
    cur = conn.cursor()
    print("🔗 Connected to 'birdspecies' database.")
    return conn, cur


setup_database_connection(env,local_secrets)