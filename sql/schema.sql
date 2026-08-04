-- ============================
-- Dimension Table : Fund
-- ============================

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT NOT NULL,

    scheme_name TEXT NOT NULL,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    launch_date DATE,

    benchmark TEXT,

    expense_ratio_pct REAL,

    exit_load_pct REAL,

    min_sip_amount REAL,

    min_lumpsum_amount REAL,

    fund_manager TEXT,

    risk_category TEXT,

    sebi_category_code TEXT

);

-- ============================
-- Dimension Table : Date
-- ============================

CREATE TABLE dim_date (

    date_id INTEGER PRIMARY KEY AUTOINCREMENT,

    full_date DATE NOT NULL,

    day INTEGER,

    month INTEGER,

    month_name TEXT,

    quarter INTEGER,

    year INTEGER

);

-- ============================
-- Fact Table : NAV
-- ============================

CREATE TABLE fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER NOT NULL,

    full_date DATE NOT NULL,

    nav REAL NOT NULL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);

-- ============================
-- Fact Table : Transactions
-- ============================

CREATE TABLE fact_transactions (

    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    investor_id TEXT NOT NULL,

    amfi_code INTEGER NOT NULL,

    full_date DATE NOT NULL,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);