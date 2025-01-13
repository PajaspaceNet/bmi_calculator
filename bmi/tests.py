from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializace Selenium WebDriveru
driver = webdriver.Chrome()  

# Spuštění testu
try:
    # Otevři Django aplikaci (lokální server)
    driver.get("http://127.0.0.1:8000/")

    # Najdi element na stránce (např. nadpis v šabloně)
    heading = driver.find_element(By.TAG_NAME, "h1")

    # Ověř obsah elementu
    assert heading.text == "BMI Kalkulačka"  #příklad testu

    print("Test úspěšný: Šablona se načetla správně.")

except AssertionError:
    print("Test neúspěšný: Obsah šablony neodpovídá.")
    print(f"Element text: '{heading.text}'")
except Exception as e:
    print(f"Chyba: {e}")

finally:
    # Zavři prohlížeč
    time.sleep(2)
    driver.quit()

