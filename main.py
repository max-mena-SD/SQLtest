from config.database_config import DatabaseConfig
from extraction.json_manipulation import JsonManipulation

from services.customers_crud import CustomerCrud
from services.applications_crud import ApplicationCrud
from services.marketing_crud import MarketingCrud
from services.store_crud import StoreCrud

import pandas as pd
import time


db_config = DatabaseConfig(DATABASE_URL="sqlite:///datasnap.db")

# Get a database session
db_session = db_config.get_session()

json_manipulation = JsonManipulation("datasnap.json")
df_datasnap = json_manipulation.load_file()

customer = df_datasnap["customers"]

cust = CustomerCrud(db_session)

start_time = time.time()
for data in customer:
    # loop over
    print(f"Inserting... {data['customer_id']}", end="\r", flush=True)

    result = cust.create_customer(
        customer_id=data["customer_id"],  # Column(Integer, primary_key=True)
        DOB=pd.to_datetime(data["DOB"]),
        first_name=data["first_name"],  # Column(String)
        last_name=data["last_name"],  # Column(String)
        email=data["email"],  # Column(String)
        phone_number=data["phone_number"],  # Column(String)
        language=data["language"],  # Column(String)
        income=data["income"],  # Column(Integer)
        title=data["title"],  # Column(String)
        campaign=data["campaign"],  # Column(String)
    )
end_time = time.time()
print(f"customer loop finished {(end_time - start_time):.6f} seconds")


application = df_datasnap["applications"]

app = ApplicationCrud(db_session)
start_time = time.time()
for data in application:
    print(f"Inserting... {data['application_id']}", end="\r", flush=True)

    result = app.create_application(
        application_id=data["application_id"],
        customer_id=data["customer_id"],
        store=data["store"],
        submit_date=pd.to_datetime(data["submit_date"]),  # .dt.date(),
        approved=data["approved"],
        approved_date=pd.to_datetime(data["approved_date"]),  # .dt.date(),
        approved_amount=data["approved_amount"],
        dollars_used=data["dollars_used"],
        lease_grade=data["lease_grade"],
    )
end_time = time.time()
print(f"application loop finished {(end_time - start_time):.6f} seconds")

stores = df_datasnap["stores"]

stor = StoreCrud(db_session)
start_time = time.time()
for data in stores:
    print(f"Inserting... {data['store']}", end="\r", flush=True)

    result = stor.create_store(
        store=data["store"],  ## Column(String, primary_key=True)
        start_dt=pd.to_datetime(data["start_dt"]),  ## Column(Date)
        state=data["state"],  ## Column(String)
        size=data["size"],
        industry=data["industry"],  ## Column(String)
    )
end_time = time.time()
print(f"stores loop finished {(end_time - start_time):.6f} seconds")

marketing = df_datasnap["marketing"]

market = MarketingCrud(db_session)
start_time = time.time()
for data in marketing:
    print(f"Inserting... {data['id']}", end="\r", flush=True)

    result = market.create_marketing_campaign(
        id=data["id"],  ##: int,
        name=data["name"],  ##: str,
        spend=data["spend"],  ##: float,
        start_date=pd.to_datetime(data["start_date"]),  ##: date,
        end_date=pd.to_datetime(data["end_date"]),  ##: date
    )
end_time = time.time()
print(f"marketing loop finished {(end_time - start_time):.6f} seconds")

# ['applications', 'customers', 'stores', 'marketing']
