# class myError(NotImplementedError):
#     pass

# raise myError("This is an error")
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid.')
    finally:
        n_square = n ** 2
        return n_square