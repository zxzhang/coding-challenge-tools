'''
Created on May 3, 2015

@author: Polarbear
'''
#!/usr/bin/python
import psycopg2
 
def main():
    conn_string = "host='contrib-postgres.club.cc.cmu.edu' dbname='contrib_zhengxiz' user='zhengxiz' password='zhengxiong'"
    # print the connection string we will use to connect
    # print "Connecting to database\n    ->%s" % (conn_string)
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    
    with open("data/Film_Locations_in_San_Francisco.csv", "r") as ins:
        for line in ins:
            title, release_year, location, fun_facts, production_company, distributor, director, writer, actor1, actor2, actor3 = line.split('|')
            sql = "INSERT INTO movies_movies(title,release_year,location,fun_facts,production_company,distributor,director,writer,actor1,actor2,actor3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" \
                        % (title, release_year, location, fun_facts, production_company, distributor, director, writer, actor1, actor2, actor3)
            cursor.execute(sql)
    conn.commit()
    # execute our Query
    # cursor.execute("SELECT * FROM movies_movies")
 
    # retrieve the records from the database
    # records = cursor.fetchall()
 
    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    # pprint.pprint(records)
 
if __name__ == "__main__":
    main()