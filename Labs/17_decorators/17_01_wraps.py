'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''




def decorator_function( original_function ):
    def wrapper( *args, **kwargs ):
        print(f"<p> {original_function(*args, **kwargs)} <p>")
        return f"<p> {original_function(*args, **kwargs)} <p>"

    return wrapper


@decorator_function
def function_text(msg):
    return  msg


function_text("this will not work")
print(function_text("this should be ptinted twice"))
