import pathlib
import json, toml
import sys
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def load_config_and_secrets():
# Load environment
 try:
    with open("C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Project2/Bird_Species_Observation/config.json", "r") as f:
        config = json.load(f)

    env = config["environment"] # 'local' currently using only local or 'cloud'
 except FileNotFoundError:
    raise FileNotFoundError("⚠️ 'config.json' not found. Please check the path.")
 except json.JSONDecodeError:
    raise ValueError("⚠️ 'config.json' is not a valid JSON file.")
 except KeyError:
    raise KeyError("⚠️ 'environment' key not found in config.json.")

 # Load secrets from your custom toml file
 local_secrets = toml.load("C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Project2/Bird_Species_Observation/.pwd/password.toml")


 return env, local_secrets
