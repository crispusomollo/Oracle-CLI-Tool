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
    parser = argparse.ArgumentParser(description="Oracle DB CLI Tool")
    parser.add_argument("--sql", help="Run raw SQL string")
    parser.add_argument("--query", help="Run SQL from file in sql/")
    parser.add_argument("--out", help="Output CSV filename")
    parser.add_argument("--params", nargs='*', help="Parameters for SQL in key=value format")

    # ✅ These two must be added:
    parser.add_argument("--insert-csv", help="Path to CSV file to insert into DB")
    parser.add_argument("--table", help="Table to insert CSV rows into")

    #parser = argparse.ArgumentParser(description="🔧 Oracle CLI Tool")
    #parser.add_argument("--query", help="Run a saved SQL file from sql/*.sql")
    #parser.add_argument("--sql", help="Run an inline SQL string")
    #parser.add_argument("--out", help="Export results to CSV (filename)")
    #parser.add_argument("--insert-csv", help="Path to CSV file to insert into DB")
    #parser.add_argument("--table", help="Table to insert CSV rows into")


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


    if args.insert_csv and args.table:
        import csv

        with open(args.insert_csv, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Assumes header row exists

            placeholders = ','.join([f":{i+1}" for i in range(len(headers))])
            sql = f"INSERT INTO {args.table} ({', '.join(headers)}) VALUES ({placeholders})"

            rows = list(reader)

        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.executemany(sql, rows)
            conn.commit()
        print(f"✅ Inserted {len(rows)} rows into {args.table}")
        return


if __name__ == "__main__":
    main()
