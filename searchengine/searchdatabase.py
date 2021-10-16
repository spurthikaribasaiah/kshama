from psycopg2 import connect, sql, Error
import searchlogging as sl

def execute_sql(statement, name, logger):
    try:
        # declare a new PostgreSQL connection object and instantiate a cursor object from the connection
        conn = connect(dbname="postgres", user="postgres", host="localhost", port="5433", password="admin")
        cursor = conn.cursor()
        # check if SQL statement/query end with a semi-colon
        if statement[-1] != ";":
            statement = statement + ";"
        # pass the psycopg2.sql.SQL object to execute() method
        cursor.execute(statement)
        if "select" in name:
            data = cursor.fetchall()
        else:
            data = 'NA'
        # print message if no exceptions were raised
        logger.info(f'execute_sql(): {name} FINISHED')
    except (Exception, Error) as err:
        logger.exception(f'execute_sql(): {name} ERROR', err)
        raise
    finally:
        if conn:
            # Committing the database transactions
            conn.commit()
            logger.info("committed the changes")
            # close the cursor object to avoid memory leaks
            cursor.close()
            # Closing the connection
            conn.close()
            logger.info("connection closed")

    return data

if __name__ == '__main__':
    statement = "SELECT 1 as dummy"
    name = "select 1 as dummy"
    logger = sl.log_creation()
    data = execute_sql(statement, name)
    print(data)
