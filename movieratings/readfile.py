import csv

from django.conf import settings
settings.configure()



from ratings.models import Rating, Movie, Rater

# Ratings
with open('../ml-100k/u.data', 'r') as f:
    data = csv.reader(f, delimiter='\t')
    for row in data:
        obj, created = Rating.objects.get(user_id=row[0], movie_id=row[1], rating=row[2])

# Movies
# with open('../ml-100k/u.item', 'r') as f:
#     data = csv.reader(f, delimiter='|')
#     for row in data:
#         print(row)
#         # obj, created = Rating.objects.get_or_create(title=row[1], release_date=row[2])
