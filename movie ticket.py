name = str(input("Enter your name: "))
movies = ["Licorice Pizza", "Top Gun: Maverick", "The Batman"]
print("Now Showing: ", movies)
movie = str(input("Enter the movie you want to watch: "))
if movie == movies[0]:
    time_lp = ["2:50 PM", "4:25 PM", "7:45 PM"]
    print("Timings for ", movie, ": ", time_lp)
elif movie == movies[1]:
    time_mvk = ["8:45 AM", "11:45 AM", "2:25 PM", "6:20 PM", "9:00 PM"]
    print("Timings for ", movie, ": ", time_mvk)
elif movie == movies[2]:
    time_btm = ["11:35 AM", "1:15 PM", "5:30 PM", "8:45 PM"]
    print("Timings for ", movie, ": ", time_btm)
time = input("Enter your preferred timings: ")
seat = input("Enter your preferred seating arrangement: ")

print("\nThank you for booking with us", name, "!")
print("\nYour ticket: ", "\n")
print(movie)
print(time)
print(seat)
print("\nHappy Viewing! Enjoy your time with us here at Indigo Theatres.")
