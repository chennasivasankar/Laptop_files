def get_one_bar_plot_data():
    import json
    single_bar_chart_data = {
        "labels": ["Sun", "Mon", "Tu", "Wed", "Th", "Fri", "Sat"],
        "datasets": [
            {
                "data": [40, 55, 75, 81, 56, 55, 40],
                "name": "Single Bar Chart",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "border_width": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }       

        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Title'
    }


def get_two_bar_plot_data():
    import json
    multi_bar_plot_data = {
        "labels": ["January", "February", "March", "April", "May", "June",
                   "July"],
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 80, 81, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "My Second dataset",
                "data": [28, 48, 40, 19, 86, 27, 90],
                "borderColor": "rgba(0,0,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,0,0,0.07)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Title'
    }


def get_multi_line_plot_data():
    import json
    multi_line_plot_data = {
        "labels": ["2010", "2011", "2012", "2013", "2014", "2015", "2016"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "Foods",
            "data": [0, 30, 10, 120, 50, 63, 10],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "Electronics",
            "data": [0, 50, 40, 80, 40, 79, 120],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        }]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': 'Title'
    }


def get_area_plot_data():
    import json
    area_plot_data = {
        "labels": ["2010", "2011", "2012", "2013", "2014", "2015", "2016"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": [0, 7, 3, 5, 2, 10, 7],
            "label": "Expense",
            "backgroundColor": 'rgba(0,103,255,.15)',
            "borderColor": 'rgba(0,103,255,0.5)',
            "borderWidth": 3.5,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(0,103,255,0.5)',
        }, ]
    }
    return {
        'area_plot_data_one': json.dumps(area_plot_data),
        'area_plot_data_one_title': 'Title'
    }


def get_radar_chart_data():
    import json
    radar_chart_data = {
        "labels": [["Eating", "Dinner"], ["Drinking", "Water"], "Sleeping",
                   ["Designing", "Graphics"], "Coding", "Cycling", "Running"],
        "defaultFontFamily": 'Poppins',
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 66, 45, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.6)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.4)"
            },
            {
                "label": "My Second dataset",
                "data": [28, 12, 40, 19, 63, 27, 87],
                "borderColor": "rgba(0, 123, 255, 0.7",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'radar_chart_data_one': json.dumps(radar_chart_data),
        'radar_chart_data_one_title': 'Title'
    }


def get_doughnut_chart_data():
    import json
    doughnut_graph_data = {
        "datasets": [{
            "data": [45, 25, 20, 10],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4"
        ]
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': 'Title'
    }


def get_multi_line_plot_with_area_data():
    import json
    multi_line_plot_with_area_data = {
        "labels": [
            "January", "February", "March", "April", "May", "June",
            "July"],
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label": "My First dataset",
                "borderColor": "rgba(0,0,0,.09)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0,0,0,.07)",
                "data": [22, 44, 67, 43, 76, 45, 12]
            },
            {
                "label": "My Second dataset",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": [16, 32, 18, 26, 42, 33, 44]
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': 'Title'
    }


def get_pie_chart_data():
    import json

    pie_chart_data = {
        "datasets": [{
            "data": [45, 25, 20, 10],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": [
            "Green",
            "Green",
            "Green"
        ]
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'Title'
    }


def get_polar_chart_data():
    import json

    polar_chart_data = {
        "datasets": [{
            "data": [15, 18, 9, 6, 19],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.8)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0,0,0,0.2)",
                "rgba(0, 123, 255,0.5)"
            ]

        }],
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4",
            "Green5"
        ]
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Title'
    }


def execute_sql_query(sql_query):
    """
    Executes sql query and return data in the form of lists (
        This function is similar to what you have learnt earlier. Here we are
        using `cursor` from django instead of sqlite3 library
    )
    :param sql_query: a sql as string
    :return:
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    return rows

def calculate_age(birth_date,today_date): 
    today=today_date
    days_in_year = 365.2425    
    age = int((today - birth_date).days / days_in_year) 
    if(age<0):
        age=0
    return age 





import random
import time
from datetime import datetime
import requests
import re
from bs4 import BeautifulSoup

def get_story_line_of_movie(url):
    page=requests.get(url)
    movie_soup=BeautifulSoup(page.content,'html.parser')
    try:
        movie_story_line=movie_soup.find('div',class_='inline canwrap').p.span.text
        return movie_story_line
    except:
        return "No Description"

def get_image_url_of_movie(url):
    page=requests.get(url)
    movie_soup=BeautifulSoup(page.content,'html.parser')
    try:
        image_url=movie_soup.img.attrs['src']
        return(image_url)
    except:
        return '#'


def populate_database(actors_list=[], 
                    movies_list=[], 
                    directors_list=[]):
    from .models import Actor,Director,Movie,Cast
    from .utils import get_story_line_of_movie,get_image_url_of_movie
    import json
    '''
    file=open("actors_100.json",'rb')
    actors_list=json.loads(file.read())
    file=open("directors_100.json",'rb')
    directors_list=json.loads(file.read())
    '''
    file=open("movies_100.json",'rb')
    movies_list=json.loads(file.read())
    for actor in actors_list:
        Actor.objects.create(
            actor_id=actor['actor_id'],
            name=actor['name'],
            gender=actor['gender'],
            fb_likes=actor["fb_likes"],
            date_of_birth=datetime.strptime(random_date("1/1/1990", "1/1/2000", random.random()),
                                    "%m/%d/%Y"
                                    ).date()
            )
        
    for director in directors_list:
        Director.objects.create(
            name=director['name'],
            gender=director['gender'],
            no_of_facebook_likes=director["no_of_facebook_likes"],

        )
    
    for movie in movies_list:
        imdb_link=movie['imdb_link']
        story_line=get_story_line_of_movie(imdb_link)
        image_url=get_image_url_of_movie(imdb_link)
        movie_obj=Movie.objects.create(movie_id=movie['movie_id'],
                                        name=movie['name'],    
                                        box_office_collection_in_crores=movie['box_office_collection_in_crores'],
                                        director=Director.objects.get(name=movie['director_name']),
                                        rating=movie['average_rating'],
                                        release_date=datetime.strptime(random_date("1/1/2005", "12/31/2020", random.random()),
                                                                                                                "%m/%d/%Y"
                                                                                                                ).date(),
                                        genre=random.choice([
                                            'action_adventure',
                                            'horror',
                                            'comedy',
                                            'science_fiction'
                                        ]),
                                        movie_story_line=story_line,
                                        movie_image_url=image_url
                                        )
        cast_list=movie['actors']
        for cast_item in cast_list:
                Cast.objects.create(
                    actor=Actor.objects.get(actor_id=cast_item['actor_id']),
                    movie=movie_obj,
                    is_debut_movie=cast_item['is_debut_movie'],
                    role=random.choice([
                            'hero',
                            'heroine',
                            'vilan',
                            'side_actor'
                        ]),
                    remuneration=random.choice([1,2,3,4,5,7,10,12,14,18,20])
                    )
              
def populate():
    from .utils import get_story_line_of_movie,get_image_url_of_movie
    story_line=get_story_line_of_movie("http://www.imdb.com/title/tt5289954/?ref_=fn_tt_tt_1")
    image=get_image_url_f_movie("http://www.imdb.com/title/tt5289954/?ref_=fn_tt_tt_1")
    print(story_line)
    print(image)

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)

    #print(random_date("1/1/2008", "1/1/2009", random.random()))
#Task 3
def get_no_of_distinct_movies_actor_acted(actor_id):
    return Movie.objects.all().filter(actors__actor_id=actor_id).distinct().count()
    
#Task 4    
def get_movies_directed_by_director(director_obj):
    return Movie.objects.filter(director=director_obj)

#Task 5
def get_average_rating_of_movie(movie_obj):
    try:
        movie_rating=Rating.objects.get(movie=movie_obj)
        return (movie_rating.rating_one_count+movie_rating.rating_two_count*2+
                movie_rating.rating_three_count*3+movie_rating.rating_four_count*4+
                movie_rating.rating_five_count*5)/(movie_rating.rating_one_count+movie_rating.rating_two_count+
                movie_rating.rating_three_count+movie_rating.rating_four_count+
                movie_rating.rating_five_count)
    except:
        return 0
        
#Task 6
def delete_movie_rating(movie_obj):
    Rating.objects.get(movie=movie_obj).delete()

#Task 7
def get_all_actor_objects_acted_in_given_movies(movie_objs):
    return Actor.objects.filter(movie__in=movie_objs).distinct()
    
    
#Task 8
def update_director_for_given_movie(movie_obj, director_obj):
    movie_obj.director=director_obj
    movie_obj.save()

#Task 9
def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    return Movie.objects.filter(actors__name__contains='john').distinct()

#Task 10
def remove_all_actors_from_given_movie(movie_obj):
    #Cast.objects.get(movie=movie_obj).delete()
    movie_obj.actors.clear()

#Task 11
def get_all_rating_objects_for_given_movies(movie_objs):
    return Rating.objects.filter(movie__in=movie_objs)
    
def get_all_distinct_actors_for_given_movie(movie_obj):
    return movie_obj.actors.distinct()
