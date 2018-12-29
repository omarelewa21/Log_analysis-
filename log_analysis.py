#!/usr/bin/env python3
'''This file is working on a news database in the aim of
    doing some analysis on these data to obtain information.
    news database contains three tables of information as following:
    authors table: has 3 columns (name, bio, id)
    articles table: has 8 columns (authir, title, slug, lead, body, time, id)
    log table: has 6 columns (path, ip, method, status, time, id) '''

import psycopg2


DBNAME = "news"


def top_three_articles(cur):
    """Prints the top three article on views"""
    cur.execute('''select articles.title, counted_views.top_counts
                        from articles
                        inner join (select path, count(path) as top_counts
                                    from log
                                    group by path
                                    order by count(path) desc limit 9)
                                        as counted_views
                        on counted_views.path =
                            concat('/article/', articles.slug)
                        order by top_counts desc limit 3;''')

    data = cur.fetchall()
    for row in data:
        print(row[0] + ' -- ' + str(row[1]) + ' views')
    return None


def listed_authors(cur):
    """Prints all authors in decending order based on views"""
    cur.execute('''select authors.name, count(log_articles.path) as popular
                        from authors
                        inner join (select articles.author, log.path
                                    from articles
                                    inner join log
                                    on log.path =
                                        concat('/article/', articles.slug))
                                        as log_articles
                            on authors.id = log_articles.author
                    group by authors.name
                    order by popular desc;
                    ''')

    data = cur.fetchall()
    for row in (data):
        print(row[0] + ' -- ' + str(row[1]) + ' views')
    return None


def margin_one_percent(cur):
    '''Prints days in which more than 1 percent of requests lead to error'''
    cur.execute('''select date, error_percentage from
                (select A1.date,
                    (100 / (ROUND(A1.total_number / A2.error_number, 2)))
                        as error_percentage
                    from
                        (select cast(log.time as date) as date, count(status)
                        as total_number from log
                        group by cast(log.time as date)) as A1
                    inner join
                        (select cast(log.time as date) as date, count(status)
                        as error_number from log
                        where status = '404 NOT FOUND'
                        group by cast(log.time as date)) as A2
                        on A1.date = A2.date) as A
                    where error_percentage > 1''')
    data = cur.fetchall()
    for row in data:
        print(str(row[0]) + ' -- ' + str(row[1]))
    return None


if __name__ == "__main__":
    '''Print data in an organized manner'''
    db = psycopg2.connect('dbname=news')
    cur = db.cursor()
    cur2 = db.cursor()
    print("Top three articles are:")
    top_three_articles(cur)
    print("\n\nMost popular authors are:")
    listed_authors(cur)
    print(
        "\n\nDays that have more than 1 percent of requests " +
        "lead to errors are: ")
    margin_one_percent(cur)
