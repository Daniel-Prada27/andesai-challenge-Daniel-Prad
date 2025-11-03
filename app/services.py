import pandas as pd
from database import load_items, load_orders, save_items, save_orders

from models import Item


def create_item(item):
    df = load_items()

    if (item.sku in df["sku"].values):
        raise ValueError(f"SKU {item.sku} already exists")

    new_item = pd.DataFrame([item.model_dump()])
    # new_item.head()

    df = pd.concat([df, new_item], ignore_index=True)
    save_items(df)
    return item.sku

