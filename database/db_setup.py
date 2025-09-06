import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "ecoops.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("PRAGMA foreign_keys = ON;")

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS organizations(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL UNIQUE,
      created_at TEXT DEFAULT (datetime('now'))
    );

    CREATE TABLE IF NOT EXISTS users(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      org_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
      name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      role TEXT CHECK(role IN ('admin','manager','viewer')) DEFAULT 'viewer',
      created_at TEXT DEFAULT (datetime('now'))
    );

    CREATE TABLE IF NOT EXISTS energy_usage(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      org_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
      asset_name TEXT,
      period_start TEXT NOT NULL,
      period_end TEXT NOT NULL,
      kwh REAL NOT NULL CHECK(kwh >= 0),
      cost_inr REAL CHECK(cost_inr >= 0),
      created_at TEXT DEFAULT (datetime('now'))
    );

    CREATE TABLE IF NOT EXISTS water_usage(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      org_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
      asset_name TEXT,
      period_start TEXT NOT NULL,
      period_end TEXT NOT NULL,
      kl REAL NOT NULL CHECK(kl >= 0),
      cost_inr REAL CHECK(cost_inr >= 0),
      created_at TEXT DEFAULT (datetime('now'))
    );

    CREATE TABLE IF NOT EXISTS transport_logs(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      org_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
      date TEXT NOT NULL,
      mode TEXT CHECK(mode IN ('car','bus','rail','flight','other')) NOT NULL,
      distance_km REAL NOT NULL CHECK(distance_km >= 0),
      passengers INTEGER DEFAULT 1,
      fuel_type TEXT,
      created_at TEXT DEFAULT (datetime('now'))
    );
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized at", DB_PATH)

if __name__ == "__main__":
    init_db()
