"""
Script to seed the database with sample data.
Run this script after creating the database and tables.

Usage:
    python seed_database.py
"""

import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:binhnguyen1208@localhost:5432/omnichat_db")

# Parse the database URL
def parse_db_url(db_url):
    """Parse PostgreSQL connection URL"""
    # Format: postgresql://user:password@host:port/database
    from urllib.parse import urlparse
    parsed = urlparse(db_url)
    
    return {
        'host': parsed.hostname or 'localhost',
        'port': parsed.port or 5432,
        'database': parsed.path.lstrip('/'),
        'user': parsed.username,
        'password': parsed.password
    }

def seed_database():
    """Execute all seed SQL files"""
    try:
        # Parse connection details
        db_params = parse_db_url(DATABASE_URL)
        
        # Connect to database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        
        # Get the data directory
        data_dir = os.path.dirname(os.path.abspath(__file__))
        
        # List of seed files in order (respecting foreign key constraints)
        seed_files = [
            'seed_departments.sql',
            'seed_users.sql',
            'seed_customers.sql',
            'seed_keywords.sql',
            'seed_shifts.sql',
            'seed_kpis.sql',
            'seed_messages.sql',
            'seed_message_assignments.sql',
            'seed_requests.sql',
            'seed_user_shifts.sql',
            'seed_notifications.sql',
        ]
        
        print("🌱 Starting database seeding...")
        print("-" * 50)
        
        for filename in seed_files:
            filepath = os.path.join(data_dir, filename)
            
            if not os.path.exists(filepath):
                print(f"⚠️  File not found: {filename}")
                continue
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    sql_script = f.read()
                
                cursor.execute(sql_script)
                conn.commit()
                print(f"✅ Executed: {filename}")
                
            except psycopg2.Error as e:
                conn.rollback()
                print(f"❌ Error executing {filename}: {str(e)}")
                continue
        
        cursor.close()
        conn.close()
        
        print("-" * 50)
        print("✨ Database seeding completed!")
        
    except psycopg2.Error as e:
        print(f"❌ Database connection error: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    seed_database()
