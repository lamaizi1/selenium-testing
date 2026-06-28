from datetime import datetime
import os

def take_screenshot(driver, test_name):
    """
    Prend une capture d'écran et l'enregistre dans le dossier screenshots.
    """

    # Crée le dossier screenshots s'il n'existe pas
    os.makedirs("screenshots", exist_ok=True)

    # Date et heure
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Nom du fichier
    filename = f"screenshots/{test_name}_{timestamp}.png"

    # Sauvegarder la capture
    driver.save_screenshot(filename)

    print(f"📸 Screenshot enregistrée : {filename}")