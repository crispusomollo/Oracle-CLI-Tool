# 🐍 Oracle CLI Tool (Python)

A lightweight command-line tool to connect to an Oracle database, run SQL queries (inline or from file), and export results to CSV — using Python and the `oracledb` driver.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Oracle DB](https://img.shields.io/badge/Oracle%20DB-Supported-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## ✅ Features

- Connects to Oracle DB (thin mode, no Instant Client required)
- Run SQL from `.sql` files or inline strings
- Export query results to CSV
- Safe, clean, and easy to extend or integrate into scripts and pipelines
- Test-covered and modular

---

## 📦 Requirements

- Python 3.7+
- Oracle database (local or remote)
- Python package: `oracledb`

---

## 🚀 Setup

1. **Clone the repo**

```bash
git clone https://github.com/crispusomollo/oracle-cli-tool.git
cd oracle-cli-tool
```

2. **Create virtual environment**
```bash
python3 -m venv oracledb-env
source oracledb-env/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Edit config.py to match your Oracle DB credentials:**
```bash
DB_CONFIG = {
    "user": "your_user",
    "password": "your_password",
    "dsn": "your_host:1521/your_service_name"
}
```



## 🖥️ Usage

▶️ Run a saved SQL file
```bash
python main.py --query sample_query
```
 
(Reads sql/sample query.sql)



▶️ Run an inline SQL query
```bash
python main.py --sql "SELECT * FROM employees"
```

💾 Export query to CSV
```bash
python main.py --query sample_query --out result.csv
```

CSV is saved to output/result.csv


🧪 Run Tests
python3 -m unittest discover tests


## 📁 File Structure

```bash
oracle-cli-tool/
├── main.py          # CLI entry point
├── db.py            # DB functions
├── config.py        # Connection details
├── sql/             # Folder for saved queries
│   └── sample_query.sql
├── output/          # CSV exports go here
├── requirements.txt
└── README.md
```

## 🧠 Tips

- Place your queries inside sql/ as .sql files.
- Refer to them by name (without .sql) using --query.
- All CSVs are exported to the output/ folder.



## 📦 Install Notes

Install dependencies manually if needed:

```bash 
pip install oracledb
```


## 🤝 License

MIT — free to use and modify.


📦 Coming Soon

 Docker support

 Insert from CSV

 JSON output

 GitHub Actions CI

