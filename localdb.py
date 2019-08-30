import sqlite3 as lite
import logging
import sys

# Logging config
logging.basicConfig(filename='LocalDB.log', level=logging.ERROR, format='%(asctime)s %(levelname)s:%(message)s')

# DB Config
con = None
# path to Database
dbname = 'Substations.db'


# Get all Substations from the Database
def getLinkbyname(name):
    try:
        con = lite.connect(dbname)
        cur = con.cursor()
        querry = 'select name, google_link, waze_link from Substations where name like ?'
        cur.execute(querry, ['%'+str(name)+'%'])
        rows = cur.fetchall()
        if rows is not None:
            results = []
            for element in rows:
                entity = [element[0], str(element[1]).replace(" ", ""), element[2]]
                results.append(entity)
            return results
        else:
            logging.error("Oops! empty row  {}".format(name))
    except lite.Error:
        logging.error("Oops!", sys.exc_info()[0], "occured.")
    finally:
        if con:
            con.close()
