
stranger=input("Enter admin, manager, guest\n")
stranger=stranger.lower()
match stranger:
    case "admin"|"manager":
        print("Hello Sir")
    case "guest":
        print("Hello, guest")
    case _:
        print("Hello")