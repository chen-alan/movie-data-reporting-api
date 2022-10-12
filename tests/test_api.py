import ast

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200


# ENDPOINT: /revenues ---------------------------------------------------------
def test_revenue_correct(app, client):
    res = client.get('/revenues/11661/1997')
    assert res.status_code == 200
    assert '237770259\n' == res.get_data(as_text=True)


def test_revenue_wrong_year(app, client):
    res = client.get('/revenues/11661/3000')
    assert res.status_code == 200
    assert '0\n' == res.get_data(as_text=True)


def test_revenue_wrong_company(app, client):
    res = client.get('/revenues/0/1999')
    assert res.status_code == 200
    assert '0\n' == res.get_data(as_text=True)


def test_revenue_wrong_year_company(app, client):
    res = client.get('/revenues/0/0')
    assert res.status_code == 200
    assert '0\n' == res.get_data(as_text=True)


# ENDPOINT: /budgets ----------------------------------------------------------
def test_budget_correct(app, client):
    res = client.get('/budgets/11661/1997')
    assert res.status_code == 200
    assert '215000000\n' == res.get_data(as_text=True)


def test_budget_wrong_year(app, client):
    res = client.get('/budgets/11661/3000')
    assert res.status_code == 200
    assert '0\n' == res.get_data(as_text=True)


def test_budget_wrong_company(app, client):
    res = client.get('/budgets/0/1999')
    assert res.status_code == 200
    assert '0\n' == res.get_data(as_text=True)


def test_budget_wrong_year_company(app, client):
    res = client.get('/budgets/0/0')
    assert res.status_code == 200
    assert '0\n' == res.get_data(as_text=True)


# ENDPOINT: /genres -----------------------------------------------------------
def test_genre_correct(app, client):
    res = client.get('/genres/1999')
    assert res.status_code == 200
    expected = {'Drama': 18}
    assert expected == ast.literal_eval(res.get_data(as_text=True))


def test_genre_wrong_year(app, client):
    res = client.get('/genres/3000')
    assert res.status_code == 200
    expected = {}
    assert expected == ast.literal_eval(res.get_data(as_text=True))
