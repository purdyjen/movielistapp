from app import app

def test1():
    '''
    This function tests that the flask application has a correct response code when the application goes live.
    '''

    response = app.test_client().get('/')
    assert response.status_code == 200


def test2():
    response = app.test_client().get('/edit')
    assert response.status_code == 200


def test3():
    pass