def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200


# ENDPOINT: /revenues ---------------------------------------------------------
def test_revenue_correct(app, client):
    res = client.get('/revenues/11661/1999')
    assert res.status_code == 200


def test_revenue_wrong_year(app, client):
    res = client.get('/revenues/11661/3000')
    assert res.status_code == 200


def test_revenue_wrong_company(app, client):
    res = client.get('/revenues/0/1999')
    assert res.status_code == 200


def test_revenue_wrong_year_company(app, client):
    res = client.get('/revenues/0/0')
    assert res.status_code == 200


# ENDPOINT: /budgets ----------------------------------------------------------
def test_budget_correct(app, client):
    res = client.get('/budgets/11661/1999')
    assert res.status_code == 200


def test_budget_wrong_year(app, client):
    res = client.get('/budgets/11661/3000')
    assert res.status_code == 200


def test_budget_wrong_company(app, client):
    res = client.get('/budgets/0/1999')
    assert res.status_code == 200


def test_budget_wrong_year_company(app, client):
    res = client.get('/budgets/0/0')
    assert res.status_code == 200
    
# ENDPOINT: /genres -----------------------------------------------------------
def test_genre_correct(app, client):
    res = client.get('/genres/1999')
    assert res.status_code == 200


def test_genre_wrong_year(app, client):
    res = client.get('/genres/3000')
    assert res.status_code == 200
