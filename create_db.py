import peewee as pw
import pandas as pd
from database import database
from models import User, Instructions, Machine

def create_tables():
    with database:
        database.create_tables([User, Instructions, Machine])


if __name__ == '__main__':
    create_tables()
    df_user = pd.read_csv("users.csv", encoding="ansi", delimiter="\t")

    print("Adding users")
    for i, a_row in df_user.iterrows():
        a_user = User.create(surname=a_row["surname"], group=a_row["group"])
        a_user.save()
        print(f"added user: {a_user.surname}")

    print("Adding machines")
    df_machine = pd.read_csv("machines.csv", encoding="ansi", delimiter="\t")
    for i, a_row in df_machine.iterrows():
        a_machine = Machine.create(name=a_row["name"])
        a_machine.save()
        print(f"added user: {a_machine.name}")