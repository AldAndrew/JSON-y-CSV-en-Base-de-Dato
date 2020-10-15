import csv
import db

def read_file(my_csv):
    with open(my_csv, newline='') as File:  
        reader = csv.DictReader(File, delimiter=';')
        for row in reader:
            conn = db.create_connection(db.database)
            if conn is not None:
                users = (row['user_id'] , row['user_email'])
                
                db.delete_users(conn, row['user_id'])
                
                create_users_id = db.create_users(conn, users)                
                
                users_rel = (row['row_id'] , row['user_id'], row['user_manager'], row['user_state'])

                db.delete_users_rel(conn, row['row_id'])
                
                create_users_rel_id = db.create_users_rel(conn, users_rel)
                
                conn.close()   