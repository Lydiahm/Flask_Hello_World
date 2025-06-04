import pytest
import requests
import os

def test_routes_status_code():
    """Test que toutes les routes retournent un code 200"""
    
    ngrok_url = os.environ.get('NGROK_URL', '').rstrip('/')
    if not ngrok_url:
        pytest.fail("NGROK_URL non définie")
    
    routes_to_test = [
        "/",
        "/exercices/",
        "/contact/",
        "/calcul_carre/5",
        "/somme/10/15"
    ]
    
    for route in routes_to_test:
        url = f"{ngrok_url}{route}"
        print(f"🧪 Test de : {url}")
        
        try:
            response = requests.get(url, timeout=10)
            assert response.status_code == 200, f"Route {route} a retourné {response.status_code}"
            print(f"✅ {route} → 200 OK")
        except requests.exceptions.RequestException as e:
            pytest.fail(f"❌ Erreur sur {route}: {e}")

def test_content_verification():
    """Test que le contenu attendu est présent"""
    
    ngrok_url = os.environ.get('NGROK_URL', '').rstrip('/')
    if not ngrok_url:
        pytest.fail("NGROK_URL non définie")
    
    # Test page d'accueil
    response = requests.get(f"{ngrok_url}/")
    assert "Bonjour tout le monde" in response.text
    
    # Test calcul carré
    response = requests.get(f"{ngrok_url}/calcul_carre/5")
    assert "25" in response.text
    
    print("✅ Tous les contenus sont corrects")
