#!/usr/bin/python3

MENU = """
Menu:
1. About Me
2. Resume/CV
3. Contact
4. Exit
"""

ABOUT_ME = """
About Me:
- I can meow pretty well
- I am a programming co-captain on Spartronics
- I like sleeping
- I can almost make a steak that doesn't suck
"""

RESUME = """
Resume:
- Contact Information
  - Troy Edwards
  - 555-555-5555
  - edwartro000@frogrock.org

- Education
  - Bainbridge High School, 2020-present

- Extracurricular Activities
  - Programming co-captain on Spartronics

- Work Experience
  - Grounds crew at Wing Point (2022)
    - Watered grass and raked bunkers

- Skills
  - Programming
    - Java
    - R
    - Rust (some)
    - HTML/CSS (a little bit)
    - Haskell (a little bit)
    - Python (a little bit)
  - Math
    - Calculus
    - Statistics
  - Communication
    - Gmail
    - Discord? idk im just trying to come up with stuff to put on here

- Achievements
  - Honestly not much
"""

CONTACT = """
Contact Me:
Email: edwartro000@frogrock.org
"""

def display_menu():
    print(MENU)

def display_about_me():
    print(ABOUT_ME)

def display_resume():
    print(RESUME)

def display_contact():
    print(CONTACT)

if __name__ == "__main__":
    while True:
        display_menu()
        match input("Enter your selection (1-4): "):
            case "1": display_about_me()
            case "2": display_resume()
            case "3": display_contact()
            case "4": break
            case _: print("Invalid input. Please try again.")

        match input("Press enter to continue or type q to exit: "):
            case "q": break
            case _: continue
    print("Exiting...")