import pytest
import requests
import time

def test_routes_status_code(ngrok_url):
    """Test que toutes les routes retournent un code 200"""
    
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

def test_content_verification(ngrok_url):
    """Test que le contenu attendu est présent"""
    
    # Test page d'accueil
    response = requests.get(f"{ngrok_url}/")
    assert "Bonjour tout le monde" in response.text
    
    # Test page exercices
    response = requests.get(f"{ngrok_url}/exercices/")
    assert "Bienvenue sur votre Framework Flask" in response.text
    
    # Test calcul carré
    response = requests.get(f"{ngrok_url}/calcul_carre/5")
    assert "25" in response.text
    
    print("✅ Tous les contenus sont corrects")
