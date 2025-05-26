import psycopg2

# --- Function to connect to the default 'postgres' database ---
def connect_to_postgres(env, local_secrets):
    if env == "local":
        return psycopg2.connect(
            host=local_secrets["host"],
            user=local_secrets["user"],
            password=local_secrets["password"],
            database="postgres"
        )
    else:
        raise ValueError(f"Unknown environment: {env}")



# --- Function to connect to the actual 'birdspecies' database ---
def connect_to_birdspecies(env, local_secrets):
    if env == "local":
        return psycopg2.connect(
            host=local_secrets["host"],
            user=local_secrets["user"],
            password=local_secrets["password"],
            database=local_secrets["database"]
        )
    else:
        raise ValueError(f"Unknown environment: {env}")
