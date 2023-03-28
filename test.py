from requests import post, get, delete


def users_test():
    print('Users_Api')
    print('Correct requests:')
    print()
    print(get('http://localhost:5000/api/v2/users').json())
    print()
    print(post('http://localhost:5000/api/v2/users', json={'id': 2,
                                                        'name': 'TEst',
                                                        "about": 'TEst_USers_Put_About',
                                                        'email': 'TEST@mail.ru',
                                                        'hashed_password': 'swdf1223213gsdfgfdsds'}).json())
    print()
    print(get('http://localhost:5000/api/v2/users/2').json())
    print()
    print(delete('http://localhost:5000/api/v2/users/2').json())
    print()
    print('Not correct requests:')
    print()
    print(get('http://localhost:5000/api/v2/users/99').json())
    print(post('http://localhost:5000/api/v2/users', json={'id': -10,
                                                        'name': 'TEst',
                                                        'hashed_password': 'swdf1223213gsdfgfdsds'}).json())
    print(delete('http://localhost:5000/api/v2/users/299').json())


if __name__ == '__main__':
    users_test()

