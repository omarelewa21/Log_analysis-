''' This file is working on a news database in the aim of
    doing some analysis on these data to obtain information.
    news database contains three tables of information as following:
    authors table: has 3 columns (name, bio, id)
    articles table: has 8 columns (authir, title, slug, lead, body, time, id)
    log table: has 6 columns (path, ip, method, status, time, id) '''

import psycopg2


DBNAME = "news"


def top_three_articles():
    """Prints the top three article on views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''create view counted_views as
                    select path, count(path) as top_counts from log
                    group by path
                    having path like '%candidate_is_jerk%' or
                            path like '%bears_love_berries%' or
                            path like '%bad_things_gone%' or
                            path like '%goats_eat_google%' or
                            path like '%trouble_for_trouble%' or
                            path like '%balloon_goons_doomed%' or
                            path like '%media_obsessed_with_bears%' or
                            path like '%so_many_bears%'
                    order by count(path) desc limit 8;
                    create view n_articles as
                        select *, ROW_NUMBER() over (order by title) as t_id
                        from articles;
                    create view n_counted_views as
                        select *, ROW_NUMBER() over (order by path) as t_id
                        from counted_views;
                    select n_articles.title, n_counted_views.top_counts
                    from n_articles inner join n_counted_views
                    on n_articles.t_id = n_counted_views.t_id
                    order by top_counts desc;''')

    posts = c.fetchall()
    db.close()
    counts = 0
    while counts < 3:
        print(posts[counts][0] + ', ' + str(posts[counts][1]) + ' views')
        counts += 1
    return None


def listed_authors():
    """Prints all authors in decending order based on views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''create view counted_views as
                    select path, count(path) as top_counts from log
                    group by path
                    having path like '%candidate_is_jerk%' or
                            path like '%bears_love_berries%' or
                            path like '%bad_things_gone%' or
                            path like '%goats_eat_google%' or
                            path like '%trouble_for_trouble%' or
                            path like '%balloon_goons_doomed%' or
                            path like '%media_obsessed_with_bears%' or
                            path like '%so_many_bears%'
                    order by count(path) desc limit 8;
                    create view n_articles as
                        select *, ROW_NUMBER() over (order by title) as t_id
                        from articles;
                    create view n_counted_views as
                        select *, ROW_NUMBER() over (order by path) as t_id
                        from counted_views;
                    create view joining_2ns as
                            select n_articles.title, n_articles.author,
                                n_counted_views.top_counts
                                from n_articles inner join n_counted_views
                                on n_articles.t_id = n_counted_views.t_id;
                select authors.name, sum(joining_2ns.top_counts)
                     as authors_views
                from authors
                inner join joining_2ns on
                    authors.id = joining_2ns.author
                group by authors.name
                order by authors_views desc;  ''')

    data = c.fetchall()
    db.close()
    for row in list(data):
        print(row[0] + ' -- ' + str(row[1]) + ' views')
    return None


def margin_one_percent():
    '''Prints days in which more than 1 percent of requests lead to error'''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    e = db.cursor()
    c.execute('''select count(status) as total_number from log
                        group by cast(log.time as date); ''')
    e.execute('''select count(status) as total_number from log
                        where status = '404 NOT FOUND'
                        group by cast(log.time as date); ''')
    total_data = c.fetchall()
    error_data = e.fetchall()
    counter = 0
    while counter < 31:
        error_percentage = error_data[counter][0]/total_data[counter][0] * 100
        if error_percentage > 1:
            print(
                "July " + str(counter+1) + ",2016 -- " +
                str(error_percentage) + "% errors"
                )
        counter += 1
    return None


def Answers():
    '''Displaying all above function in organized way'''
    print("Top three articles are:\n")
    top_three_articles()
    print("\n\nMost popular authors are:\n")
    listed_authors()
    print('''\n\nDays that have more than 1 percent of requests
             lead to errors are:\n''')
    margin_one_percent()

Answers()
