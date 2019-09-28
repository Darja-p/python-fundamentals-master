'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def daily_menu(**kwargs):
    print("Today's menu: ")
    for i,n in kwargs.items():
        print(f"{i:<10}: {n:<30}")
daily_menu(starter= "ceviche", soup= "carrot with ginger", main_dish= "bulgur with grilled vegetables ", dessert="chocolate cake")



