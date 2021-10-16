import os, string
import searchdatabase as sd
import searchlogging as sl

def search_file_in_drives(filename, dirlist, logger):
    # Search in the history SQL table if there is an entry for the filename
    sql_statement = """SELECT 1 as dummy FROM search_results WHERE filename = '{}';""".format(str(filename))
    history_available = sd.execute_sql(sql_statement, "check_history_select", logger)

    # If there is no entry in the table then search in all the directories else show the result from the table
    if not history_available or history_available is None or history_available == '':
        filelist = []
        # search for the file in the directories
        for dirname in dirlist:
            dirname = dirname.upper() if ':' in dirname else dirname.upper() + ':'
            for dirpath, dirs, files in os.walk(dirname):
                for file in files:
                    if filename in os.path.join(dirpath, file):
                        filelist.append(os.path.join(dirpath, file))

        # write the results to the db
        filelist_str = ' || '.join(filelist)
        sql_statement = """INSERT INTO search_results (filename, searchresult, transaction_dt) VALUES('{}','{}', current_date);""".format(
            str(filename), str(filelist_str))
        sd.execute_sql(sql_statement, "write_recs_to_db", logger)
    else:
        # Retreive the search result from the table
        sql_statement = """SELECT searchresult FROM search_results WHERE filename = '{}';""".format(str(filename))
        table_data = sd.execute_sql(sql_statement, "select_recs_from_db", logger)
        for line in table_data:
            filelist = line

    if not filelist or ':' not in str(filelist):
        logger.info("There are no files present with the name '" + filename + "' in all the directories ")
    else:
        logger.info(
            "Please find below the list of search results for the file '" + filename + "' in all the directories:")
        logger.info(filelist)

    return filelist

if __name__ == '__main__':
    logger = sl.log_creation()
    sql_statement = """SELECT 1 as dummy FROM search_results;"""
    data = sd.execute_sql(sql_statement, "select_recs_from_db", logger)
    for line in data:
        filelist = line
    print(filelist)
    logger.info("search directory is working")
