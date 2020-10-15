import os
import sys
import shutil

root = os.path.dirname(__file__)
sys.path.append(root + "/modules")

import read_json
import read_csv 
import db
import mail

db.init()

my_dir = '/trabajo/files/' #Corresponde al directorio a utilizar.

contenido = os.listdir(my_dir)
for fichero in contenido:
    if os.path.isfile(os.path.join(my_dir, fichero)) and fichero.endswith('.json'):
        read_json.read_file(my_dir+fichero);
        shutil.move(my_dir+fichero, my_dir+"procesados/"+fichero)
    if os.path.isfile(os.path.join(my_dir, fichero)) and fichero.endswith('.csv'):
        read_csv.read_file(my_dir+fichero);
        shutil.move(my_dir+fichero, my_dir+"procesados/"+fichero)

conn = db.create_connection(db.database)
if conn is not None:
    rows=db.select_all_tasks(conn)

    for row in rows:
        subject="Aprobación DB "+row[0]
        msg="Estimado(a) "+row[1]+" Favor su aprobación."
        print("Solicitud enviada (DB:" + row[0] + " - Usuario:" +  row[1] + " - Correo:" + row[2] + ")")
        mail.send_email(row[2],subject,msg)
        db.update_email_db_list(conn,row[0])

    conn.close() 

print("Proceso finalizado OK")
