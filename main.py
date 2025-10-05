# main.py

import argparse
import os
from db import run_query

def load_sql_file(name):
    path = f"sql/{name}.sql"
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Query file '{path}' not found.")
    with open(path, "r") as f:
        return f.read()

def save_to_csv(rows, headers, filename):
    import csv
    os.makedirs("output", exist_ok=True)
    path = os.path.join("output", filename)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"✅ CSV exported to {path}")

def main():
    parser = argparse.ArgumentParser(description="🔧 Oracle CLI Tool")
    parser.add_argument("--query", help="Run a saved SQL file from sql/*.sql")
    parser.add_argument("--sql", help="Run an inline SQL string")
    parser.add_argument("--out", help="Export results to CSV (filename)")

    args = parser.parse_args()

    if args.sql:
        sql = args.sql
    elif args.query:
        sql = load_sql_file(args.query)
    else:
        print("❌ Provide --sql or --query")
        return

    rows, headers = run_query(sql)

    print("📋 Results:")
    for row in rows:
        print(row)

    if args.out:
        save_to_csv(rows, headers, args.out)

if __name__ == "__main__":
    main()
