
#<img src="{{ image.image.url }}" class="image-preview">


'''
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




'''
Table Director as D {
  director_id int [pk]
  name varchar
  gender varchar
  no_of_facebook_likes varchar
}

Table Actor as A {
  actor_id int [pk]
  name varchar
  gender varchar
  fb_likes varchar
  date_of_birth timestamp
}

Table Movie as M {
  movie_id varchar[pk]
  name varchar
  box_of_collection_in_crores float
  rating float
  release_date timestamp
  genre varchar
  director_id int [ref: > D.director_id]
}

Table Cast as C {
  actor_id int [ref: > A.actor_id]
  movie_id int [ref: > M.movie_id]
  is_debut_movie boolean
  role varchar
  remuneration varchar
}
'''
 

 '''
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
    '''

'''
import json
    file=open("actors_5000.json",'rb')
    actors_list=json.loads(file.read())
    file=open("directors_5000.json",'rb')
    directors_list=file.read()
'''
'''
for actor in actors_list:
        Actor.objects.create(
            actor_id=actor['actor_id'],
            name=actor['name'],
            date_of_birth=actor['date_of_birth'],
            gender=actor['gender']
            )
    
    for director in directors_list:
        Director.objects.create(name=director)
    
    for movie in movies_list:
        movie_obj=Movie.objects.create(movie_id=movie['movie_id'],
                                        name=movie['name'],    
                                        box_office_collection_in_crores=movie['box_office_collection_in_crores'],
                                        release_date=movie['release_date'],
                                        director=Director.objects.get(name=movie['director_name']),
                                        genre=movie['genre'],
                                        rating=movie['rating']
                                        )
        cast_list=movie['actors']
        for cast_item in cast_list:
                Cast.objects.create(
                    actor=Actor.objects.get(actor_id=cast_item['actor_id']),
                    movie=movie_obj,
                    role=cast_item['role'],
                    is_debut_movie=cast_item['is_debut_movie'],
                    remuneration=cast_item['remuneration']
                    )
'''

'''
populate_database(
    actors_list=[
        {
            'actor_id':1,
            'name':'Actor-1',
            'date_of_birth':'2020-03-17',
            'gender':'M'
        },
        {
            'actor_id':2,
            'name':'Actor-2',
            'date_of_birth':'2020-03-17',
            'gender':'F'
        },
        {
            'actor_id':3,
            'name':'Actor-3',
            'date_of_birth':'2020-03-17',
            'gender':'F'
        },
        {
            'actor_id':4,
            'name':'Actor-5',
            'date_of_birth':'2020-03-17',
            'gender':'M'
        },
        {
            'actor_id':5,
            'name':'Actor-5',
            'date_of_birth':'2020-03-17',
            'gender':'M'
        },
    ]
)
'''

'''
populate_database(
    directors_list=[
        'Director-1','Director-2','Director-3','Director-4','Director-5'
    ]
)
'''

'''
populate_database(
    movies_list=[


'''

'''
movies_list= [
        {
            "movie_id": "1",
            "name": "Movie-1",
            "actors": [
                {
                    "actor_id": 1,
                    "role": "hero",
                    "is_debut_movie": False,
                    "remuneration":20
                }
            ],
            "box_office_collection_in_crores": "12.3",
            "release_date": "2020-3-3",
            "director_name": "Director-1",
            'genre':'comedy',
            'rating':2.0
        },
        {
            "movie_id": "2",
            "name": "Movie-2",
            "actors": [
                {
                    "actor_id": 1,
                    "role": "hero",
                    "is_debut_movie": False,
                    "remuneration":10
                },
                {
                    "actor_id": 2,
                    "role": "heroine",
                    "is_debut_movie": False,
                    "remuneration":5
                },
                {
                    "actor_id": 3,
                    "role": "Vilan",
                    "is_debut_movie": False,
                    "remuneration":2
                },
                {
                    "actor_id": 4,
                    "role": "side-actor",
                    "is_debut_movie": False,
                    "remuneration":1
                }
            ],
            "box_office_collection_in_crores": "20",
            "release_date": "2020-3-3",
            "director_name": "Director-2",
            'genre':'horror',
            'rating':3.0
        },
        {
            "movie_id": "3",
            "name": "Movie-3",
            "actors": [
                {
                    "actor_id": 3,
                    "role": "hero",
                    "is_debut_movie": False,
                    "remuneration":7
                },
                {
                    "actor_id": 1,
                    "role": "heroine",
                    "is_debut_movie": False,
                    "remuneration":4
                },
                {
                    "actor_id": 2,
                    "role": "Vilan",
                    "is_debut_movie": False,
                    "remuneration":1
                },
                {
                    "actor_id": 4,
                    "role": "side-actor",
                    "is_debut_movie": False,
                    "remuneration":1
                }
            ],
            "box_office_collection_in_crores": "40",
            "release_date": "2020-3-3",
            "director_name": "Director-3",
            'genre':'action_adventure',
            'rating':2.5
        },
        {
            "movie_id": "4",
            "name": "Movie-4",
            "actors": [
                {
                    "actor_id": 5,
                    "role": "hero",
                    "is_debut_movie": False,
                    "remuneration":20
                },
                {
                    "actor_id": 2,
                    "role": "heroine",
                    "is_debut_movie": False,
                    "remuneration":7
                },
                {
                    "actor_id": 1,
                    "role": "Vilan",
                    "is_debut_movie": False,
                    "remuneration":4
                },
                {
                    "actor_id": 4,
                    "role": "side-actor",
                    "is_debut_movie": False,
                    "remuneration":1
                }
            ],
            "box_office_collection_in_crores": "10",
            "release_date": "2020-3-3",
            "director_name": "Director-4",
            'genre':'science_fiction',
            'rating':1.0
        },
        {
            "movie_id": "5",
            "name": "Movie-5",
            "actors": [
                {
                    "actor_id": 3,
                    "role": "hero",
                    "is_debut_movie": False,
                    "remuneration":12
                },
                {
                    "actor_id": 2,
                    "role": "heroine",
                    "is_debut_movie": False,
                    "remuneration":6
                },
                {
                    "actor_id": 1,
                    "role": "Vilan",
                    "is_debut_movie": False,
                    "remuneration":4
                },
                {
                    "actor_id": 5,
                    "role": "side-actor",
                    "is_debut_movie": False,
                    "remuneration":1
                }
            ],
            "box_office_collection_in_crores": "5",
            "release_date": "2020-3-3",
            "director_name": "Director-5",
            'genre':'comedy',
            'rating':2.7
        }
    ]
'''