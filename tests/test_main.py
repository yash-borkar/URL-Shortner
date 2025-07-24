import pytest
from app.main import app, url_store

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_shorten_valid_url(client):
    res = client.post('/api/shorten', json={'url': 'https://example.com'})
    assert res.status_code == 201
    data = res.get_json()
    assert 'short_code' in data
    assert 'short_url' in data

def test_shorten_invalid_url(client):
    res = client.post('/api/shorten', json={'url': 'not-a-url'})
    assert res.status_code == 400

def test_redirect_and_stats(client):
    res = client.post('/api/shorten', json={'url': 'https://example.com'})
    code = res.get_json()['short_code']

    for _ in range(3):
        client.get(f'/{code}')

    stats = client.get(f'/api/stats/{code}')
    data = stats.get_json()
    assert data['url'] == 'https://example.com'
    assert data['clicks'] == 3

def test_redirect_404(client):
    res = client.get('/nonexistent')
    assert res.status_code == 404

def test_stats_404(client):
    res = client.get('/api/stats/bad123')
    assert res.status_code == 404
