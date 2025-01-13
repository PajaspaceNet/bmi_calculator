from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    category = None

    if request.method == 'POST':
        try:
            height = float(request.POST.get('height')) / 100  # Převeď cm na metry
            weight = float(request.POST.get('weight'))
            bmi = round(weight / (height ** 2), 2)  # BMI výpočet

            # Kategorie BMI
            if bmi < 18.5:
                category = "Podváha"
            elif 18.5 <= bmi < 24.9:
                category = "Normální váha"
            elif 25 <= bmi < 29.9:
                category = "Nadváha"
            else:
                category = "Obezita"
        except (ValueError, ZeroDivisionError):
            bmi = "Chyba ve vstupních datech"

    return render(request, 'bmi_calculator/index.html', {'bmi': bmi, 'category': category})