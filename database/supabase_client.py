# database/supabase_client.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables from .env in the project root
load_dotenv()

# Fetch credentials safely
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Validate that keys exist
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "Supabase URL or Key not found. Make sure you have a .env file with SUPABASE_URL and SUPABASE_KEY"
    )

# Create a reusable Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Optional: simple test function to verify connection
def test_connection(table_name: str):
    """Fetch all rows from a table and print them."""
    response = supabase.table(table_name).select("*").execute()
    print(f"Data from '{table_name}':", response.data)
