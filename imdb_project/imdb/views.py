from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie,Cast,Actor,Director
from .utils import execute_sql_query
from collections import defaultdict
from datetime import date 
 
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def home(request):
    movie_list=Movie.objects.all()
    context={'movie_list':movie_list}
    return render(request,'imdb_home.html',context)

def movie(request,movie_id):
    movie_obj=Movie.objects.get(movie_id=movie_id)
    cast_list=Cast.objects.filter(movie=movie_obj)
    actor_list=movie_obj.actors.all().distinct()
    context={'movie_obj':movie_obj,'cast_list':cast_list,'actor_role_list':actor_list}
    return render(request,'imdb_movie.html',context)

def actor(request,actor_id):
    actor_obj=Actor.objects.get(actor_id=actor_id)
    cast_list=Cast.objects.filter(actor=actor_obj)
    context={'actor_obj':actor_obj,'cast_list':cast_list}
    return render(request,'imdb_actor.html',context)

def director(request,director_id):
    director_obj=Director.objects.get(id=director_id)
    movie_list=Movie.objects.filter(director=director_obj)
    context={'director_obj':director_obj,'movie_list':movie_list}
    return render(request,'imdb_director.html',context)

def delete(request,movie_id):
    Movie.objects.get(movie_id=movie_id).delete()
    return render(request,'imdb_home.html')

def analytics(request):
    data1=get_one_bar_plot_data_of_movies_count_per_year()
    data2=get_multi_line_plot_data_of_count_movies_per_year_and_genre()
    data3=get_two_bar_plot_data_of_hero_and_heroine_avg_remuneration_per_year()
    data4=get_area_plot_data_of_avg_collections_of_movie_per_year()
    data5=get_radar_chart_data_of_avg_age_of_all_actors_acted_in_all_movies_per_year()
    data1.update(data2)
    data1.update(data3)
    data1.update(data4)
    data1.update(data5)
    return render(request,'analytics.html',data1)

def analytics1(request):
    from .utils import get_area_plot_data,get_radar_chart_data,get_doughnut_chart_data,get_one_bar_plot_data
    from .utils import get_multi_line_plot_with_area_data,get_pie_chart_data,get_multi_line_plot_data
    from .utils import get_one_bar_plot_data,get_two_bar_plot_data,get_multi_line_plot_data,get_two_bar_plot_data
    data1=get_area_plot_data()
    data5=get_radar_chart_data() 
    data6=get_doughnut_chart_data()
    data7=get_multi_line_plot_with_area_data()
    data8=get_pie_chart_data()
    data2=get_one_bar_plot_data()
    data3=get_two_bar_plot_data()
    data4=get_multi_line_plot_data()
    data1.update(data5)
    data1.update(data6)
    data1.update(data7)
    data1.update(data8)
    data1.update(data2)
    data1.update(data3)
    data1.update(data4)
    return render(request,'analytics.html',data1)


def get_radar_chart_data_of_avg_age_of_all_actors_acted_in_all_movies_per_year():
    import json
    sql_query='''
    SELECT gender_age.mo_year,
        AVG(gender_age.ac_age)
    FROM (SELECT strftime("%Y",year_gender.rel_date) as mo_year,
            year_gender.gender as ac_gender,
            (
            year_gender.rel_date-year_gender.dob
            ) as ac_age
        FROM (SELECT ca.movie_id as mo_id,
                (SELECT m.release_date
                FROM imdb_movie as m
                WHERE m.movie_id=ca.movie_id
                ) as rel_date,
                ca.actor_id as ac_id,
                (SELECT a.gender
                FROM imdb_actor as a
                WHERE a.actor_id=ca.actor_id
                ) as gender,
                (SELECT a.date_of_birth
                FROM imdb_actor as a
                WHERE a.actor_id=ca.actor_id
                ) as dob
            FROM imdb_cast ca
            ) as year_gender
            WHERE year_gender.gender='male'
        ) as gender_age
    GROUP BY gender_age.mo_year
    '''
    male_year_age_list=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        male_year_age_list[movie[0]]=movie[1]

    sql_query='''
    SELECT gender_age.mo_year,
        AVG(gender_age.ac_age)
    FROM (SELECT strftime("%Y",year_gender.rel_date) as mo_year,
            year_gender.gender as ac_gender,
            (
            year_gender.rel_date-year_gender.dob
            ) as ac_age
        FROM (SELECT ca.movie_id as mo_id,
                (SELECT m.release_date
                FROM imdb_movie as m
                WHERE m.movie_id=ca.movie_id
                ) as rel_date,
                ca.actor_id as ac_id,
                (SELECT a.gender
                FROM imdb_actor as a
                WHERE a.actor_id=ca.actor_id
                ) as gender,
                (SELECT a.date_of_birth
                FROM imdb_actor as a
                WHERE a.actor_id=ca.actor_id
                ) as dob
            FROM imdb_cast ca
            ) as year_gender
            WHERE year_gender.gender='female'
        ) as gender_age
    GROUP BY gender_age.mo_year
    '''
    female_year_age_list=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        female_year_age_list[movie[0]]=movie[1]

    radar_chart_data = {
        "labels": ["2015","2016","2017","2018","2019","2020"],
        "defaultFontFamily": 'Poppins',
        "datasets": [
            {
                "label": "Male Actors",
                "data": [
                    male_year_age_list["2015"],
                    male_year_age_list["2016"],
                    male_year_age_list["2017"],
                    male_year_age_list["2018"],
                    male_year_age_list["2019"],
                    male_year_age_list["2020"]
                ],
                "borderColor": "rgba(0, 123, 255, 0.6)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.4)"
            },
            {
                "label": "Female Actors",
                "data": [
                    female_year_age_list["2015"],
                    female_year_age_list["2016"],
                    female_year_age_list["2017"],
                    female_year_age_list["2018"],
                    female_year_age_list["2019"],
                    female_year_age_list["2020"]
                ],
                "borderColor": "rgba(0, 123, 255, 0.7",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'radar_chart_data_one': json.dumps(radar_chart_data),
        'radar_chart_data_one_title': 'Average Age Of Actors In All Movies Per Year'
    }

def get_area_plot_data_of_avg_collections_of_movie_per_year():
    import json
    sql_query='''
    SELECT strftime('%Y',im_mo.release_date) as year,
        AVG(im_mo.box_office_collection_in_crores) as avg_collection
    FROM imdb_movie as im_mo
    GROUP BY strftime('%Y',im_mo.release_date)
    '''
    avg_movie_collection_list_per_year=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        avg_movie_collection_list_per_year[movie[0]]=movie[1]

    area_plot_data = {
        "labels": ["2015", "2016", "2017", "2018", "2019", "2020"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": [avg_movie_collection_list_per_year["2015"], 
                    avg_movie_collection_list_per_year["2016"], 
                    avg_movie_collection_list_per_year["2017"],
                    avg_movie_collection_list_per_year["2018"], 
                    avg_movie_collection_list_per_year["2019"], 
                    avg_movie_collection_list_per_year["2020"]
                    ],
            "label": "Avg Collections",
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
        'area_plot_data_one_title': 'Average Collections Of Movies Per Year'
    }

def get_two_bar_plot_data_of_hero_and_heroine_avg_remuneration_per_year():
    import json

    sql_query='''
    SELECT hero_table.year,
        AVG(hero_table.a_remuneration) as avg_remuneration
    FROM (SELECT im_ca.actor_id as a_id,
            im_ca.remuneration a_remuneration,
            (SELECT strftime('%Y',m.release_date)
            FROM imdb_movie as m
            WHERE m.movie_id=im_ca.movie_id) as year
        FROM imdb_cast as im_ca
        WHERE im_ca.role='hero') as hero_table
    GROUP BY hero_table.year
    '''
    hero_avg_rem_list=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        hero_avg_rem_list[movie[0]]=movie[1]
    
    sql_query='''
    SELECT heroine_table.year,
        AVG(heroine_table.a_remuneration) as avg_remuneration
    FROM (SELECT im_ca.actor_id as a_id,
            im_ca.remuneration a_remuneration,
            (SELECT strftime('%Y',m.release_date)
            FROM imdb_movie as m
            WHERE m.movie_id=im_ca.movie_id) as year
        FROM imdb_cast as im_ca
        WHERE im_ca.role='heroine') as heroine_table
    GROUP BY heroine_table.year
    '''
    heroine_avg_rem_list=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        heroine_avg_rem_list[movie[0]]=movie[1]

    multi_bar_plot_data = {
        "labels": ["2015","2016","2017","2018","2019","2020"],
        "datasets": [
            {
                "label": "Heros",
                "data": [hero_avg_rem_list['2015'],
                        hero_avg_rem_list['2016'],
                        hero_avg_rem_list['2017'], 
                        hero_avg_rem_list['2018'], 
                        hero_avg_rem_list['2019'], 
                        hero_avg_rem_list['2020']
                        ],
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "Heroines",
                "data": [heroine_avg_rem_list['2015'],
                        heroine_avg_rem_list['2016'],
                        heroine_avg_rem_list['2017'], 
                        heroine_avg_rem_list['2018'], 
                        heroine_avg_rem_list['2019'], 
                        heroine_avg_rem_list['2020']
                        ],
                "borderColor": "rgba(0,0,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,0,0,0.07)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Average Remuneration Per Year'
    }

def get_one_bar_plot_data_of_movies_count_per_year():
    import json
    sql_query='''
    SELECT strftime('%Y',im_mo.release_date) as year,
        COUNT(*)
    FROM imdb_movie as im_mo
    GROUP BY strftime('%Y',im_mo.release_date)
    '''
    movies_count_per_year_list=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        movies_count_per_year_list[movie[0]]=movie[1]
    single_bar_chart_data = {
        "labels": ["2015", "2016", "2017", "2018", "2019", "2020"],
        "datasets": [
            {
                "data": [movies_count_per_year_list['2015'], 
                    movies_count_per_year_list['2016'],
                    movies_count_per_year_list['2017'], 
                    movies_count_per_year_list['2018'], 
                    movies_count_per_year_list['2019'], 
                    movies_count_per_year_list['2020'],
                    ],
                "name": "Single Bar Chart",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "border_width": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "label":"movies count"
            }       

        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Movies Count Per Year'
    }


def get_multi_line_plot_data_of_count_movies_per_year_and_genre():
    import json
    sql_query='''
    SELECT strftime('%Y',m.release_date)
    FROM imdb_movie as m
    GROUP BY strftime('%Y',m.release_date)
    '''
    sql_query='''
    SELECT comedy_movie_table.year,COUNT(*)
    FROM   (SELECT strftime('%Y',imdb_movie.release_date) as year,imdb_movie.movie_id as id
            FROM imdb_movie
            WHERE imdb_movie.genre='comedy'  ) as comedy_movie_table
    GROUP BY comedy_movie_table.year
    '''
    comedy_movie_list=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        comedy_movie_list[movie[0]]=movie[1]
    
    sql_query='''
    SELECT movie_table.year,COUNT(*)
    FROM   (SELECT strftime('%Y',imdb_movie.release_date) as year,imdb_movie.movie_id as id
            FROM imdb_movie
            WHERE imdb_movie.genre='horror'  ) as movie_table
    GROUP BY movie_table.year
    '''
    horror_movie_list=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        horror_movie_list[movie[0]]=movie[1]

    sql_query='''
    SELECT movie_table.year,COUNT(*)
    FROM   (SELECT strftime('%Y',imdb_movie.release_date) as year,imdb_movie.movie_id as id
            FROM imdb_movie
            WHERE imdb_movie.genre='action_adventure'  ) as movie_table
    GROUP BY movie_table.year
    '''
    action_adventure_movie_list=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        action_adventure_movie_list[movie[0]]=movie[1]

    sql_query='''
    SELECT movie_table.year,COUNT(*)
    FROM   (SELECT strftime('%Y',imdb_movie.release_date) as year,imdb_movie.movie_id as id
            FROM imdb_movie
            WHERE imdb_movie.genre='science_fiction'  ) as movie_table
    GROUP BY movie_table.year
    '''
    science_fiction_movie_list=defaultdict(int)
    for movie in execute_sql_query(sql_query):
        science_fiction_movie_list[movie[0]]=movie[1]


    multi_line_plot_data = {
        "labels": ["2015", "2016", "2017", "2018", "2019", "2020"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "Comedy",
            "data": [comedy_movie_list['2015'], 
                    comedy_movie_list['2016'],
                    comedy_movie_list['2017'], 
                    comedy_movie_list['2018'], 
                    comedy_movie_list['2019'], 
                    comedy_movie_list['2020'],
                    ],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "Horror",
            "data":[horror_movie_list['2015'], 
                    horror_movie_list['2016'],
                    horror_movie_list['2017'], 
                    horror_movie_list['2018'], 
                    horror_movie_list['2019'], 
                    horror_movie_list['2020'],
                    ],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        },{
            "label": "Action Adventure",
            "data":[action_adventure_movie_list['2015'], 
                    action_adventure_movie_list['2016'],
                    action_adventure_movie_list['2017'], 
                    action_adventure_movie_list['2018'], 
                    action_adventure_movie_list['2019'], 
                    action_adventure_movie_list['2020'],
                    ],
            "backgroundColor": 'transparent',
            "borderColor": 'rgb(255, 255, 0)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgb(255, 255, 0)',
        },{
            "label": "Science Fiction",
            "data":[science_fiction_movie_list['2015'], 
                    science_fiction_movie_list['2016'],
                    science_fiction_movie_list['2017'], 
                    science_fiction_movie_list['2018'], 
                    science_fiction_movie_list['2019'], 
                    science_fiction_movie_list['2020'],
                    ],
            "backgroundColor": 'transparent',
            "borderColor": 'rgb(0, 64, 255)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgb(0, 64, 255)',
        }
        
        ]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': 'Genres count per year'
    }


