import pytest
import os

@pytest.fixture
def ngrok_url():
    """Récupère l'URL ngrok depuis les variables d'environnement"""
    url = os.environ.get('NGROK_URL')
    if not url:
        pytest.skip("NGROK_URL not found")
    return url.rstrip('/')
