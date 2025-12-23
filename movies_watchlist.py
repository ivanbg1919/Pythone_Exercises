movies = []

while True:
    print("\n--- MOVIE WATCHLIST ---")
    print("1. Add movie")
    print("2. Show movies")
    print("3. Delete movie")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        movie = input("Enter movie title: ")
        movies.append(movie)
        print("Movie added to watchlist.")

    elif choice == "2":
        if not movies:
            print("The movie list is empty.")
        else:
            print("\nMovies to watch:")
            for index, movie in enumerate(movies, start=1):
                print(f"{index}. {movie}")

    elif choice == "3":
        if not movies:
            print("No movies to delete.")
        else:
            for index, movie in enumerate(movies, start=1):
                print(f"{index}. {movie}")

            try:
                delete_movie = int(input("Enter the movie number to delete: "))
                if 1 <= delete_movie <= len(movies):
                    removed = movies.pop(delete_movie - 1)
                    print(f"Deleted movie: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("You must enter a number.")

    elif choice == "4":
        print("Exiting program. ")
        break

    else:
        print("Unknown option.")
