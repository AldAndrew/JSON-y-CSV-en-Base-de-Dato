import json
import db


def read_file(my_json):
    with open(my_json) as file:
        data = json.load(file)
        for row in data:
            conn = db.create_connection(db.database)
            if conn is not None:
                db_list = (row['nom_db'] , row['user_owner'], row['classification'], "N")
                
                db.delete_db_list(conn, row['nom_db'])
                 
                create_db_list_id = db.create_db_list(conn, db_list)
                
                conn.close()            


