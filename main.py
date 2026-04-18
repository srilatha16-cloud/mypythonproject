from db_utils import create_database, create_table

db_name = input("Enter database name (with .db): ")

create_database(db_name)
create_table(db_name)