# WAP to ask the user to enter names of their 3 favourite movies & store them in a list 

movies = []
for i in range(3):
    movie = input("Enter your Favourite movies: ")
    movies.append(movie)
print("Your 3 favourite movies are:", movies)