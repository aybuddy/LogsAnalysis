#!/usr/bin/env python

import psycopg2
import sys

DBNAME = "news"


# Most popular three articles

try:
    conn = psycopg2.connect(dbname=DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT articles.title, count(*) AS ques1
                FROM articles
                JOIN log ON log.path = '/article/' || articles.slug
                GROUP BY articles.title
                ORDER BY ques1 desc limit 3;""")
    rows = cur.fetchall()

    print
    print "Top 3 Article Views:"
    for title, views in rows:
        print('"{}" - {} views'.format(title, views))
    conn.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    sys.exit()


# Most popular article authors

try:
    conn = psycopg2.connect(dbname=DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT authors.name, count(*) as ques2
                FROM authors
                JOIN articles on authors.id = articles.author
                JOIN log on log.path = '/article/' || articles.slug
                GROUP BY authors.name
                ORDER BY ques2 desc limit 5;""")

    rows = cur.fetchall()

    print
    print "Author Rank by Article Views:"
    for author, views in rows:
        print('{0:<25} - {1:>8} views'.format(author, views))
    conn.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    sys.exit()


# Request errors

try:
    conn = psycopg2.connect(dbname=DBNAME)
    cur = conn.cursor()
    cur.execute("""WITH badReq AS (
                    SELECT time::date AS date, count(*) AS count
                    FROM log
                    WHERE status LIKE '4%'
                    GROUP BY date
                ), totalReq AS (
                    SELECT time::date AS date, count(*) AS count
                    FROM log
                    GROUP BY date
                )

                SELECT badReq.date, CAST(
                    badReq.count AS FLOAT
                ) / totalReq.count
                FROM badReq, totalReq
                WHERE badReq.date = totalReq.date
                AND cast(
                    badReq.count AS float
                ) / totalReq.count > 0.01
                """)
    rows = cur.fetchall()

    print
    print "Dates with More Than 1& Error Rate:"
    for date, error_rate in rows:
        print('{0:%B %d, %Y} - {1:.2%} errors'.format(date, error_rate))
    conn.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    sys.exit()
