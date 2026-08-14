import pandas as pd

sharpe = pd.read_csv("data/processed/sharpe_ratio.csv")
fund_master = pd.read_csv("data/processed/01_fund_master_cleaned.csv")

recommender = sharpe.merge(fund_master[["amfi_code","risk_category"]], on="amfi_code", how="left")

def recommend_funds(risk):
    result = recommender[recommender["risk_category"].str.lower() == risk.lower()]
    result = result.sort_values("Sharpe_Ratio", ascending=False)
    return result[["scheme_name","Sharpe_Ratio"]].head(3)

print("========== Mutual Fund Recommender ==========")
print("Available Risk Categories:")
print("1. Low")
print("2. Moderate")
print("3. Moderately High")
print("4. High")
print("5. Very High")

risk = input("\nEnter Risk Category: ")

recommendation = recommend_funds(risk)

if recommendation.empty:
    print("\nNo funds found.")
else:
    print("\nTop 3 Recommended Funds\n")

    for i, row in enumerate(recommendation.itertuples(index=False), start=1):
        print(f"{i}. {row.scheme_name}")
        print(f"   Sharpe Ratio : {row.Sharpe_Ratio:.3f}\n")