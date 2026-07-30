import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_FILE = BASE_DIR / "UseCase__002_.xlsx"

def read_users(sheet_name):

    # Read Excel sheet
    df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_name)

    # Keep only active users
    df = df[df["IsActive"] == "Yes"]

    return df

def read_email_template(environment):

    # Read the Email Format sheet
    df = pd.read_excel(EXCEL_FILE, sheet_name="Email Format")

    # Find the required template
    template = df[df["Subject"] == f"{environment} Update"].iloc[0]

    subject = template["Subject"]
    body = template["Body"]

    return subject, body