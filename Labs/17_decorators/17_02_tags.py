'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''

def decorator_function(arg1):
    def wrap(f):
        def wrapper(*args):
            print(f"{arg1} {f(*args)} {arg1}")
        return wrapper
    return wrap


@decorator_function("<head>")
def function_text(msg):
    return str(msg)

function_text("this will work")



# another way to do it with partial aka pseudo decorator (only two levels)

from functools import partial, wraps

def _pseudo_decor(fun, argument):
    # magic sauce to lift the name and doc of the function
    @wraps(fun)
    def ret_fun(*args):
        print(f"{argument} {fun(*args)} {argument}")
        return fun(*args)
    return ret_fun

real_decorator = partial(_pseudo_decor, argument="<head>")

@real_decorator
def bar(msg):
    return str(msg)

bar("this is a try")


# def decoratorFunctionWithArguments(arg1, arg2, arg3):
#     def wrap(f):
#         print ("Inside wrap()")
#         def wrapped_f(*args):
#             print ("Inside wrapped_f()")
#             print ("Decorator arguments:", arg1, arg2, arg3)
#             f(*args)
#             print ("After f(*args)")
#         return wrapped_f
#     return wrap
#
# @decoratorFunctionWithArguments("hello", "world", 42)
# def sayHello(a1, a2, a3, a4):
#     print ('sayHello arguments:', a1, a2, a3, a4)
#
# print ("After decoration")
#
# print ("Preparing to call sayHello()")
# sayHello("say", "hello", "argument", "list")
# print ("after first sayHello() call")
# sayHello("a", "different", "set of", "arguments")
# print ("after second sayHello() call")
# Here's the output:
#
# Inside wrap()
# After decoration
# Preparing to call sayHello()
# Inside wrapped_f()
# Decorator arguments: hello world 42
# sayHello arguments: say hello argument list
# After f(*args)
# after first sayHello() call
# Inside wrapped_f()
# Decorator arguments: hello world 42
# sayHello arguments: a different set of arguments
# After f(*args)
# after second sayHello() call


# another comment:

# @decorator
# def foo(*args, **kwargs):
#     pass
# translates to
# foo = decorator(foo)
#
# So if the decorator had arguments,
# @decorator_with_args(arg)
# def foo(*args, **kwargs):
#     pass
# translates to
# foo = decorator_with_args(arg)(foo)