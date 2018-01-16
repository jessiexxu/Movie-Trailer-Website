import fresh_tomatoes
import media

benjamin_button = media.Movie(
						"The Curious Case of Benjamin Button",
						"Unusual adventures of an elderly man who ages in reverse",
						"https://images-na.ssl-images-amazon.com/images/I/91KxcLPgw5S._SL1500_.jpg",
						"https://www.youtube.com/watch?v=O6wP_LKA0DE")

#print(benjamin_button.storyline)
#benjamin_button.show_trailer()
#benjamin_button.show_poster()

invisible_guest = media.Movie(
						"The Invisible Guest",
						"A young businessman wakes up in a locked hotel room next to the body of his dead lover",
						"http://alein.org/torrentimg/be72d8fc62e31c53b4b0c978cac0571bf3d52185.jpg",
						"https://www.youtube.com/watch?v=epCg2RbyF80")


#invisible_guest.show_poster()

black_swan = media.Movie(
						"Black Swan",
						"The rivalry between two ballerinas transforms into a twisted friendship",
						"http://www.altfg.com/film/wp-content/uploads/images/2011/02/black-swan-poster-natalie-portman.jpg",
						"https://www.youtube.com/watch?v=5jaI1XOB-bs")

life_of_pie = media.Movie(
						"Life of Pi",
						"A young man who survives a disaster at sea is hurtled into an epic journey of adventure and discovery",
						"http://t2.gstatic.com/images?q=tbn:ANd9GcQLik2EaN6bm4GQBKTvI7uIlH4b5kQ29IhY1Tqh_nEoHkUsru82",
						"https://www.youtube.com/watch?v=j9Hjrs6WQ8M")

shawshank = media.Movie(
						"The Shawshank Redemption",
						"Framed for murder, upstanding banker Andy Dufresne begins a new life at the Shawshank prison",
						"http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
						"https://www.youtube.com/watch?v=K_tLp7T6U1c")


zootopia = media.Movie(
						"Zootopia",
						"The first rabbit in the police force proves herself by solving a mysterious case",
						"https://lumiere-a.akamaihd.net/v1/images/movie_poster_zootopia_866a1bf2.jpeg?region=0%2C0%2C300%2C450",
						"https://www.youtube.com/watch?v=g9lmhBYB11U")

#zootopia.show_trailer()

movies = [invisible_guest, black_swan, life_of_pie, shawshank, zootopia, benjamin_button]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__doc__)
