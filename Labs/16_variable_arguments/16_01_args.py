'''
Write a script with a function that demonstrates the use of *args.

'''

def today_menu(*args):
    print("We have these flavors today:")
    for k in args:
        print(f"* {k}")

today_menu("chocolate", "vanilla", "lemon", "strawberry")