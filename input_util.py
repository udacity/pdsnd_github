
def get_user_input(message, user_list):
    """
    An utility function to obtain user specific input value
    Args:
        (str) message - an information message for a particular request
    Returns:
        (str) user_data - requested data from user
    """

    while True:
        user_data = input(message).lower()
        if user_data in user_list:
            break
        if user_data == 'all':
            break
    
    return user_data