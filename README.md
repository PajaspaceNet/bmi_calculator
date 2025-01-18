# BMI Kalkulačka
![mereni](https://github.com/user-attachments/assets/157343f5-380f-4d57-aceb-78e0e7ea6829)





Tento projekt je jednoduchá webová aplikace postavená na frameworku Django, která umožňuje uživatelům vypočítat svůj BMI index (Body Mass Index) na základě zadané hmotnosti a výšky. Projekt obsahuje základní funkčnost kalkulačky a ukázku testování aplikace pomocí Selenium.
Tento projekt je provozovan v CLOUDU na HEROKu https://bmi-calculate-77890143cb73.herokuapp.com/

## Funkce

- Vstupní pole pro zadání:
  - Hmotnosti (v kilogramech).
  - Výšky (v centimetrech).
- Výpočet BMI na základě zadaných hodnot:


- Klasifikace výsledku BMI (např. podváha, normální váha, nadváha, obezita).

## Požadavky

- Python 3.8+.
- Django 4.x+.
- Selenium (pro testování).
- Webový ovladač (např. ChromeDriver pro prohlížeč Google Chrome).

## Instalace

1. Naklonujte tento repozitář:
   ```bash
   git clone https://github.com/username/bmi_calculator.git
   cd bmi_calculator
   ```

2. Vytvořte a aktivujte virtuální prostředí:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Na Windows: .venv\Scripts\activate
   ```

3. Nainstalujte závislosti:
   ```bash
   pip install -r requirements.txt
   ```

4. Spusťte server:
   ```bash
   python manage.py runserver
   ```

5. Otevřete aplikaci v prohlížeči: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Testování pomocí Selenium , jednoduchy vzor je take v folderu ... bmi/tests
- je mozno primo spustit

### Požadavky
- Nainstalujte Selenium:
  ```bash
  pip install selenium
  ```
- Stáhněte odpovídající WebDriver pro váš prohlížeč (např. [ChromeDriver](https://sites.google.com/chromium.org/driver/)).

### Ukázkový test

Níže je ukázka jednoduchého testu, který ověřuje načtení hlavní stránky a přítomnost BMI kalkulačky:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_bmi_calculator():
    # Inicializace prohlížeče (upravte cestu k driveru, pokud není v PATH)
    driver = webdriver.Chrome()

    try:
        # Otevřete aplikaci
        driver.get("http://127.0.0.1:8000/")

        # Ověřte přítomnost nadpisu na stránce
        heading = driver.find_element(By.TAG_NAME, "h1")
        assert heading.text == "BMI Kalkulačka"

        # Vyplňte vstupní pole
        weight_input = driver.find_element(By.ID, "weight")
        height_input = driver.find_element(By.ID, "height")
        calculate_button = driver.find_element(By.ID, "calculate")

        weight_input.send_keys("70")
        height_input.send_keys("170")
        calculate_button.click()

        # Ověřte výsledek
        result = driver.find_element(By.ID, "result")
        assert "Vaše BMI je" in result.text

        print("Test úspěšný: Aplikace funguje správně.")
    except Exception as e:
        print(f"Test selhal: {e}")
    finally:
        time.sleep(2)
        driver.quit()

# Spusťte test
if __name__ == "__main__":
    test_bmi_calculator()
```




## Budoucí vylepšení

- Přidání dalších jazyků (multijazyčná podpora).
- Rozšíření o grafické zobrazení BMI výsledků.
- Implementace pokročilejších testů a CI/CD pipeline.
