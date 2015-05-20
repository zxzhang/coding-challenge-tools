'''
Created on May 3, 2015

@author: Polarbear
'''
#!/usr/bin/python
import psycopg2
import urllib2
import xml.etree.ElementTree as ET
from SF_Movies.settings import DATABASES
 
def main():
    conn_string = "host='" + DATABASES['default']['HOST'] + "' dbname='" + DATABASES['default']["NAME"] + "' user='" + DATABASES['default']["USER"] + "' password='" + DATABASES['default']["PASSWORD"] + "'"
    # print the connection string we will use to connect
    print "Connecting to database\n    ->%s" % (conn_string)
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    with open("data/Film_Locations_in_San_Francisco.csv", "r") as ins:
        for line in ins:
            title, release_year, location, fun_facts, production_company, distributor, director, writer, actor1, actor2, actor3 = line.split('|')
            address = location.replace(" ", "+")
            address = address[1 : len(address) - 1] + ",+San+Francisco,+CA,+US"
            url = "https://maps.googleapis.com/maps/api/geocode/xml?address=%s&key=AIzaSyBEt9ozY7CfiRk_RQRAo6c0cAvjjT1mK3Q" % address
            fileToRead = urllib2.urlopen(url)
            data = fileToRead.read()
            fileToRead.close()
            root = ET.fromstring(data)
            child = root.find('result')
            if child is None or len(child) == 0:
                continue
            child = child.find('geometry')
            lat = child[0][0].text
            lng = child[0][1].text
            la, ln = float(lat), float(lng)
            if la < 37.697485 or la > 37.813662:
                continue
            if ln < -122.533645 or ln > -122.345504:
                continue
            sql = "INSERT INTO movies_movie(title,release_year,location,fun_facts,production_company,distributor,director,writer,actor1,actor2,actor3,latitude,longitude) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" \
                        % (title, release_year, location, fun_facts, production_company, distributor, director, writer, actor1, actor2, actor3, lat, lng)
            cursor.execute(sql)
    conn.commit()

    sql = "INSERT INTO movies_title (title) SELECT DISTINCT(title) FROM movies_movie"
    cursor.execute(sql)
    conn.commit()
    sql = "INSERT INTO movies_address (location) SELECT DISTINCT(location) FROM movies_movie"
    cursor.execute(sql)
    conn.commit()
    sql = "INSERT INTO movies_company (production_company) SELECT DISTINCT(production_company) FROM movies_movie" 
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
