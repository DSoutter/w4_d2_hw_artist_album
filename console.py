import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

# Start of additions:

artist1=Artist("Born Ruffians")
artist2=Artist("The Strokes")

album1=Album("Pulp", "Indie", artist1)
album2=Album("Is this is", "rock", artist2)
album3=Album("Squeeze", "Indie", artist1)
album4=Album("Juice", "Indie", artist1)
album5=Album("Red, Yellow & Blue", "Indie", artist1)

artist_repository.save(artist1)
artist_repository.save(artist2)

album_repository.save(album1)
album_repository.save(album2)
album_repository.save(album3)
album_repository.save(album4)
album_repository.save(album5)

artist_repository.update(artist1)



# for album in album_repository.select_all():
#     print(album.__dict__)

pdb.set_trace()
