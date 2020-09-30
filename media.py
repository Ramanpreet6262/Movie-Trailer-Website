import project
import fresh_tomatoes
mr_Robot = project.movie("Mr.Robot","https://c.wallhere.com/photos/96/13/Mr_Robot_Rami_Malek-1412613.jpg!d","https://www.youtube.com/watch?v=4yKsIdr_PNU","2015","6","24")
gots01e01 = project.movie("Game Of Thrones","https://mcdn.wallpapersafari.com/medium/90/93/sni2zH.jpg","https://www.youtube.com/watch?v=BpJYNVhGf1s","2011","4","17")
three_idiots = project.movie("3 idiots","https://fanart.tv/fanart/movies/20453/moviethumb/3-idiots-56dbe7b229ce5.jpg","https://www.youtube.com/watch?v=xvszmNXdM4w","2009","8.4")
fandf7 = project.movie("Furious 7","https://2.bp.blogspot.com/-KCErRWJaS40/VYKwVVkoG1I/AAAAAAAAAD8/EV3SUyi4vIQ/s1600/Fast-and-Furious-7-Poster.jpg","https://www.youtube.com/watch?v=Skpu5HaVkOc","2015","7.2")
fandf8 = project.movie("Fast 8", "http://www.fotolip.com/wp-content/uploads/2016/05/Fast-And-Furious-8-1.jpg", "https://www.youtube.com/watch?v=uisBaTkQAEs","2017","9.0")
inters = project.movie("Interstellar","http://www.movienewz.com/img/gallery/interstellar/posters/interstellar_movie_poster_4.jpg","https://www.youtube.com/watch?v=0vxOhd4qlnA","2014","8.6")
darkknight = project.movie("The Dark Knight","https://akalol.files.wordpress.com/2008/08/new-joker-poster-for-the-dark-knight.jpg","https://www.youtube.com/watch?v=_PZpmTj1Q8Q","2008","9.0")
nysm = project.movie("Now You See Me","https://image.tmdb.org/t/p/original/hGsi9bPp4PEQANCUxswQDLymJag.jpg","https://www.youtube.com/watch?v=4OtM9j2lcUA","2013","7.3")
movies = [three_idiots, fandf7, fandf8, inters, darkknight, nysm]
movies=sorted(movies, key=lambda movie:movie.name)
fresh_tomatoes.open_movies_page(movies)

#code ends
