
import pandas as pd
import os

RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"

os.makedirs(PROCESSED_PATH, exist_ok=True)

def clean_fund_master():

    print("Cleaning fund_master...")

    df = pd.read_csv(f"{RAW_PATH}/01_fund_master.csv")
    df = df.drop_duplicates()
    df = df.dropna(subset=["amfi_code"])
    df["amfi_code"] = df["amfi_code"].astype(int)
    text_columns = df.select_dtypes(include=["object", "string"]).columns
    for col in text_columns:
        df[col] = df[col].str.strip()
    df.to_csv(
        f"{PROCESSED_PATH}/01_fund_master_cleaned.csv",
        index=False
    )

    print("✓ fund_master cleaned")


def clean_nav_history():
    print("Cleaning nav_history data...")
    df = pd.read_csv(f"{RAW_PATH}02_nav_history.csv")
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["amfi_code", "date"])
    df["nav"] = df.groupby("amfi_code")["nav"].ffill()
    df = df.drop_duplicates()
    df = df[df["nav"] > 0]
    df.to_csv(
        f"{PROCESSED_PATH}/02_nav_history_cleaned.csv",
        index=False
    )

    print("✓ nav_history cleaned")



def clean_aum_by_fund_house():

    print("Cleaning aum_by_fund_house...")

    df = pd.read_csv(f"{RAW_PATH}/03_aum_by_fund_house.csv")

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows where fund_house is missing
    df = df.dropna(subset=["fund_house"])

    # Remove extra spaces
    df["fund_house"] = df["fund_house"].str.strip()

    # Validate numeric columns
    df = df[
        (df["aum_lakh_crore"] > 0) &
        (df["aum_crore"] > 0) &
        (df["num_schemes"] > 0)
    ]

    # Sort
    df = df.sort_values(["date", "fund_house"])

    # Save
    df.to_csv(
        f"{PROCESSED_PATH}/03_aum_by_fund_house_cleaned.csv",
        index=False
    )

    print("✓ aum_by_fund_house cleaned")


def clean_monthly_sip_inflows():

    print("Cleaning monthly_sip_inflows...")

    df = pd.read_csv(f"{RAW_PATH}/04_monthly_sip_inflows.csv")

    # Convert month to datetime
    df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows with missing month
    df = df.dropna(subset=["month"])

    # Validate numeric columns
    df = df[
        (df["sip_inflow_crore"] > 0) &
        (df["active_sip_accounts_crore"] > 0) &
        (df["new_sip_accounts_lakh"] > 0) &
        (df["sip_aum_lakh_crore"] > 0)
    ]

    # Sort by month
    df = df.sort_values("month")

    # Save cleaned file
    df.to_csv(
        f"{PROCESSED_PATH}/04_monthly_sip_inflows_cleaned.csv",
        index=False
    )

    print("✓ monthly_sip_inflows cleaned")



# df = pd.read_csv(f"{RAW_PATH}/05_category_inflows.csv")

# print(df.columns)
# print(df.dtypes)
# print(df.head())
# print(df.shape)

def clean_category_inflows():

    print("Cleaning category_inflows...")

    df = pd.read_csv(f"{RAW_PATH}/05_category_inflows.csv")

    # Convert month to datetime
    df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows where category is missing
    df = df.dropna(subset=["category"])

    # Remove extra spaces
    df["category"] = df["category"].str.strip()

    # Validate inflow values
    df = df[df["net_inflow_crore"].notna()]

    # Sort data
    df = df.sort_values(["month", "category"])

    # Save cleaned file
    df.to_csv(
        f"{PROCESSED_PATH}/05_category_inflows_cleaned.csv",
        index=False
    )

    print("✓ category_inflows cleaned")

# df = pd.read_csv(f"{RAW_PATH}/06_industry_folio_count.csv")

# print(df.columns)
# print(df.dtypes)
# print(df.head())
# print(df.shape)

def clean_industry_folio_count():

    print("Cleaning industry_folio_count...")

    df = pd.read_csv(f"{RAW_PATH}/06_industry_folio_count.csv")

    # Convert month to datetime
    df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows where month is missing
    df = df.dropna(subset=["month"])

    # Validate folio counts
    df = df[
        (df["total_folios_crore"] > 0) &
        (df["equity_folios_crore"] > 0) &
        (df["debt_folios_crore"] > 0) &
        (df["hybrid_folios_crore"] > 0) &
        (df["others_folios_crore"] > 0)
    ]

    # Sort by month
    df = df.sort_values("month")

    # Save cleaned file
    df.to_csv(
        f"{PROCESSED_PATH}/06_industry_folio_count_cleaned.csv",
        index=False
    )

    print("✓ industry_folio_count cleaned")

# df = pd.read_csv(f"{RAW_PATH}/07_scheme_performance.csv")

# print(df.columns)
# print(df.dtypes)
# print(df.head())
# print(df.shape)

def clean_scheme_performance():

    print("Cleaning scheme_performance...")

    df = pd.read_csv(f"{RAW_PATH}/07_scheme_performance.csv")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows where AMFI code is missing
    df = df.dropna(subset=["amfi_code"])

    # Convert return columns to numeric
    return_columns = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "expense_ratio_pct"
    ]

    for col in return_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove rows with missing return values
    df = df.dropna(subset=return_columns)

    # Validate expense ratio
    df = df[
        (df["expense_ratio_pct"] >= 0.1) &
        (df["expense_ratio_pct"] <= 2.5)
    ]

    # Remove extra spaces from text columns
    text_columns = df.select_dtypes(include=["object", "string"]).columns

    for col in text_columns:
        df[col] = df[col].str.strip()

    # Sort data
    df = df.sort_values(["fund_house", "scheme_name"])

    # Save cleaned file
    df.to_csv(
        f"{PROCESSED_PATH}/07_scheme_performance_cleaned.csv",
        index=False
    )

    print("✓ scheme_performance cleaned")

# df = pd.read_csv(f"{RAW_PATH}/08_investor_transactions.csv")

# print(df.columns)
# print(df.dtypes)
# print(df.head())
# print(df.shape)


def clean_investor_transactions():

    print("Cleaning investor_transactions...")

    df = pd.read_csv(f"{RAW_PATH}/08_investor_transactions.csv")

    # Convert transaction date to datetime
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Standardize transaction type
    df["transaction_type"] = (
        df["transaction_type"]
        .str.strip()
        .str.title()
    )

    # Keep only valid transaction types
    valid_types = ["Sip", "Lumpsum", "Redemption"]
    df = df[df["transaction_type"].isin(valid_types)]

    # Validate amount
    df = df[df["amount_inr"] > 0]

    # Standardize KYC status
    df["kyc_status"] = (
        df["kyc_status"]
        .str.strip()
        .str.title()
    )

    # Keep only valid KYC values
    valid_kyc = ["Verified", "Pending", "Rejected"]
    df = df[df["kyc_status"].isin(valid_kyc)]

    # Remove extra spaces from text columns
    text_columns = df.select_dtypes(include=["object", "string"]).columns

    for col in text_columns:
        df[col] = df[col].str.strip()

    # Sort data
    df = df.sort_values(["transaction_date", "investor_id"])

    # Save cleaned file
    df.to_csv(
        f"{PROCESSED_PATH}/08_investor_transactions_cleaned.csv",
        index=False
    )

    print("✓ investor_transactions cleaned")

# df = pd.read_csv(f"{RAW_PATH}/09_portfolio_holdings.csv")

# print(df.columns)
# print(df.dtypes)
# print(df.head())
# print(df.shape)

def clean_portfolio_holdings():

    print("Cleaning portfolio_holdings...")

    df = pd.read_csv(f"{RAW_PATH}/09_portfolio_holdings.csv")

    # Convert portfolio date to datetime
    df["portfolio_date"] = pd.to_datetime(df["portfolio_date"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows where AMFI code is missing
    df = df.dropna(subset=["amfi_code"])

    # Remove extra spaces from text columns
    text_columns = df.select_dtypes(include=["object", "string"]).columns

    for col in text_columns:
        df[col] = df[col].str.strip()

    # Validate numeric columns
    df = df[
        (df["weight_pct"] > 0) &
        (df["market_value_cr"] > 0) &
        (df["current_price_inr"] > 0)
    ]

    # Sort data
    df = df.sort_values(["amfi_code", "portfolio_date", "stock_name"])

    # Save cleaned file
    df.to_csv(
        f"{PROCESSED_PATH}/09_portfolio_holdings_cleaned.csv",
        index=False
    )

    print("✓ portfolio_holdings cleaned")

# df = pd.read_csv(f"{RAW_PATH}/10_benchmark_indices.csv")

# print(df.columns)
# print(df.dtypes)
# print(df.head())
# print(df.shape)

def clean_benchmark_indices():

    print("Cleaning benchmark_indices...")

    df = pd.read_csv(f"{RAW_PATH}/10_benchmark_indices.csv")

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows where date or index_name is missing
    df = df.dropna(subset=["date", "index_name"])

    # Remove extra spaces
    df["index_name"] = df["index_name"].str.strip()

    # Validate close value
    df = df[df["close_value"] > 0]

    # Sort data
    df = df.sort_values(["index_name", "date"])

    # Save cleaned file
    df.to_csv(
        f"{PROCESSED_PATH}/10_benchmark_indices_cleaned.csv",
        index=False
    )

    print("✓ benchmark_indices cleaned")

# ==========================
# Run All Cleaning Functions
# ==========================

clean_fund_master()
clean_nav_history()
clean_aum_by_fund_house()
clean_monthly_sip_inflows()
clean_category_inflows()
clean_industry_folio_count()
clean_scheme_performance()
clean_investor_transactions()
clean_portfolio_holdings()
clean_benchmark_indices()

print("\n🎉 All datasets cleaned successfully!")