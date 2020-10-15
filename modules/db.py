import sqlite3
from sqlite3 import Error

database = r"db/db.db"

def init():

    sql_create_db_list_table = """ CREATE TABLE IF NOT EXISTS db_list (
                                        id integer PRIMARY KEY,
                                        nom_db text NOT NULL,
                                        user_id  text,
                                        classification  text,
                                        email_send   text
                                    ); """

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        user_id text NOT NULL,
                                        user_email   text NOT NULL,
                                        PRIMARY KEY (user_id)
                                    ); """

    sql_create_users_rel_table = """CREATE TABLE IF NOT EXISTS users_rel (
                                    id integer integer,
                                    user_id text NOT NULL,
                                    user_manager text NOT NULL,
                                    user_rel_state text NOT NULL,
                                    PRIMARY KEY (id),
                                    FOREIGN KEY (user_id) REFERENCES users (user_id),
                                    FOREIGN KEY (user_manager) REFERENCES users (user_id)                                  
                                );"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_db_list_table)
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_users_rel_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(create_table_sql)
        print(e)

def update_email_db_list(conn, id):
    """
    Update a user by user id
    :param conn:  Connection to the SQLite database
    :param id: id of the user
    :return:
    """
    try:
        sql = ''' UPDATE db_list SET email_send=?  WHERE nom_db=? '''
        cur = conn.cursor()
        cur.execute(sql, ('Y',id,))
        conn.commit()
    except Error as e:
        print(id)
        print(e)

def delete_db_list(conn, id):
    """
    Delete a user by user id
    :param conn:  Connection to the SQLite database
    :param id: id of the user
    :return:
    """
    sql = '''DELETE FROM db_list WHERE nom_db=? '''
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    
    
def create_db_list(conn, db_list):
    """
    Create a new database into the db_list table
    :param conn:
    :param db_list:
    :return: db_list id
    """
    try:
        sql = ''' INSERT INTO db_list(nom_db,user_id,classification,email_send)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, db_list)
        conn.commit()      
    except Error as e:
        conn.rollback()
        print(sql)
        print(e)
    finally:     
        return cur.lastrowid

def delete_users(conn, id):
    """
    Delete a user by user id
    :param conn:  Connection to the SQLite database
    :param id: id of the user
    :return:
    """
    sql = 'DELETE FROM users WHERE user_id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    
def create_users(conn, users):
    """
    Create a new database into the users table
    :param conn:
    :param users:
    :return: users id
    """
    try:
        sql = ''' INSERT INTO users(user_id,user_email)
                  VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, users)
        conn.commit()      
    except Error as e:
        conn.rollback()
        print(sql)
        print(e)
    finally:     
        return cur.lastrowid

def delete_users_rel(conn, id):
    """
    Delete a user by user id
    :param conn:  Connection to the SQLite database
    :param id: id of the user
    :return:
    """
    sql = 'DELETE FROM users_rel WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    
def create_users_rel(conn, users_rel):
    """
    Create a new database into the users table
    :param conn:
    :param users:
    :return: users id
    """
    try:
        sql = ''' INSERT INTO users_rel(id,user_id,user_manager,user_rel_state)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, users_rel)
        conn.commit()      
    except Error as e:
        conn.rollback()
        print(sql)
        print(e)
    finally:     
        return cur.lastrowid
        
        
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    try:
        cur = conn.cursor()
        cur.execute("SELECT db_list.nom_db,users.user_id,users.user_email FROM db_list,users,users_rel WHERE db_list.user_id=users_rel.user_id AND users_rel.user_manager=users.user_id AND db_list.classification='HIGH' AND db_list.email_send='N'")

        rows = cur.fetchall()
        return rows
            
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

