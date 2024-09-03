 # match case

browser=input("Enter the name of the browser\n")
browser=browser.lower()
match browser:
    case "firefox":
        print("You have chosen firefox")
    case "edge":
        print("You have chosen edge")
    case "chrome":
        print("You have chosen chrome")
    case _:
        print("You have not chosen a valid browser")