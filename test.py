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


def jobs_test():
    print('Jobs_Api')
    print('Correct requests:')
    print()
    print(get('http://localhost:5000/api/v2/jobs').json())
    print()
    print(post('http://localhost:5000/api/v2/jobs', json={'id': 3,
                                                          'title_of_activity': 'TEst',
                                                          'team_leader': 'TEstLeadert',
                                                          'collaborators': 'TESTer1 and Tester 2',
                                                          'is_finished': True,
                                                          'work_size': 15,
                                                          'user_id': 1
                                                          }).json())
    print()
    print(get('http://localhost:5000/api/v2/jobs/3').json())
    print()
    print(delete('http://localhost:5000/api/v2/jobs/3').json())
    print()
    print('Not correct requests:')
    print()
    print(get('http://localhost:5000/api/v2/jobs/99').json())
    print(post('http://localhost:5000/api/v2/jobs', json={'id': -10,
                                                          'name': 'TEst',
                                                          'hashed_password': 'swdf1223213gsdfgfdsds'}).json())
    print(delete('http://localhost:5000/api/v2/jobs/299').json())


if __name__ == '__main__':
    users_test()
    print()
    jobs_test()
