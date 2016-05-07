# from django.conf import settings
# settings.configure()
def main():
    from ratings.models import Rating, Movie, Rater

    # Ratings
    with open('../ml-100k/u.data', 'r') as f:
        data = csv.reader(f, delimiter='\t')
        for row in data:
            rater = Rating.objects.get(user_id=row[0])
            movie = Rating.objects.get(movie_id=row[1])
            test = Rating(user_id=rater, movie_id=movie, rating=row[2])
            test.save()
        # obj, created = Rating.objects.get(user_id=row[0], movie_id=row[1], rating=row[2])
        #
        # test = Rating(user_id=rater, movie_id=movie, rating=row[2])


    # Movies
    # with open('../ml-100k/u.item', 'r') as f:
    #     data = csv.reader(f, delimiter='|')
    #     for row in data:
    #         print(row)
    #         obj, created = Movie.objects.get_or_create(id=row[0], title=row[1], release_date=row[2])

if __name__ == '__main__':
    import csv
    import django
    import os

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieratings.settings')

    django.setup()
    main()
