# BMI Kalkulačka
![mereni](https://github.com/user-attachments/assets/157343f5-380f-4d57-aceb-78e0e7ea6829)





Tento projekt je jednoduchá webová aplikace  je provozovan v CLOUDU na HEROKu https://bmi-calculate-77890143cb73.herokuapp.com/ a je  postavená na frameworku Django, která umožňuje uživatelům vypočítat svůj BMI index (Body Mass Index) na základě zadané hmotnosti a výšky. Projekt obsahuje základní funkčnost kalkulačky a ukázku testování aplikace pomocí Selenium.

##  AWS 
Bmi Kalkulacku lze samozrejme instalovat na i na **AWS**. Chtel sem predejit nakladum :-) Vice v sekci **Budoucí vylepšení**



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
- mozna implementace do AWS , postup:

 , nicmene postup bych volil tento:<br>
**1. Pripravime si :-)** <br> 
   Free tier 2<br>
        AMI: Ubuntu Server 20.04 LTS (free tier eligible).<br>
        Instance Type: t2.micro (free tier eligible).<br>
        Key Pair: Dam nový nebo použiju existující.<br>
        Security Groups: open ports **22 (SSH) a 80 (HTTP).**<br><br>
    

**2. Připojení k instanci**

    Použiju SSH k připojení:
```
    ssh -i "my-key.pem" ubuntu@<public-ip>
```
**3. Instalace závislostí**
```
sudo apt update
sudo apt install python3-pip python3-dev nginx 
pip3 install virtualenv
```
**4. Stažení aplikace**

    Naklonuju repo
```
git clone https://github.com/pajaspacenet/bmi_calculator.git
cd bmi_calculator
```

Vytvořeni virtuální prostředí a nainstalujte závislosti:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

**5. Spuštění aplikace pomocí Gunicorn**

Start Gunicorn:
```
gunicorn --workers 3 --bind 0.0.0.0:8000 bmi_calculator.wsgi:application
```

**6. Konfigurace Nginx**
```
sudo nano /etc/nginx/sites-available/bmi_calculator
```
Obsah konfigurace:

```
server {
    listen 80;
    server_name <public-ip>;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
Aktivuj konfiguraci:
```
    sudo ln -s /etc/nginx/sites-available/bmi_calculator /etc/nginx/sites-enabled
    sudo systemctl restart nginx
```

**7. Otevřu  aplikaci v prohlížeči /doufam :-)) /**

    

**Další možná vylepšení**
- Přidání dalších jazyků (multijazyčná podpora).
- Rozšíření o grafické zobrazení BMI výsledků.
- Implementace pokročilejších testů a CI/CD pipeline.
