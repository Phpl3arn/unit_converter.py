def convert_length(value, from_unit, to_unit):
    #uzunluk birimlerinin standart birime (metre) dönüştürme katsayıları
    # ve sonra istenen birime geri dönüştürme
    conversion_factors = {
        "milimetre": 0.001,
        "santimetre": 0.01,
        "metre": 1.0,
        "kilometre": 1000.0,
        "inç": 0.0254,
        "foot": 0.3048,
        "yarda": 0.9144,
        "mil": 1609.34
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Geçersiz birimler."
    
    #Değeri standart birime (metre) dönüştür
    value_in_meters = value * conversion_factors[from_unit]

    # Standart birimden istenen birime dönüştür
    converted_value = value_in_meters / conversion_factors[to_unit]

    return converted_value

def convert_weight(value, from_unit, to_unit):
    # Ağırlık birimlerinin standart birime (kilogram) dönüştürme katsayıları
    conversion_factors = {
        "miligram": 0.000001,
        "gram": 0.001,
        "kilogram": 1.0,
        "pound": 0.453592,
        "ons": 0.0283495
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Geçersiz birimler."
    
    #Değeri standart birime (kilogram dönüştür)
    value_in_kg = value * conversion_factors[from_unit]

    # Standart birimden istenen birime dönüştür
    converted_value = value_in_kg / conversion_factors[to_unit]

    return converted_value

def convert_temperature(value, from_unit, to_unit):
    #Sıcaklık dönüşümleri daha karmaşık olduğu için ayrı ele alınır
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
        elif to_unit == "celsius":
            return value
    elif from_unit == "fahrenheit": # Bu elif bloğu, yukarıdaki if bloğunun dışına taşındı
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        elif to_unit == "fahrenheit":
            return value
    elif from_unit == "kelvin": # Bu elif bloğu da yukarıdaki if bloğunun dışına taşındı
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
        elif to_unit == "kelvin":
            return value
    else:
        return "Geçersiz birimler."
        
def main():
    print("✨ Python Birim Dönüştürücüye Hoş Geldiniz! ✨")
    print("Desteklenen dönüştürücü türleri: uzunluk, ağırlık, sıcaklık")

    while True:
        try:
            converter_type = input("\nDönüştürücünün türünü girin (uzunluk, ağırlık, sıcaklık) veya çıkmak için 'q' yazın: ").lower()

            if converter_type == 'q':
                print("Çıkılıyor... Güle güle !!!")
                break
            
            if converter_type not in ["uzunluk", "ağırlık", "sıcaklık"]:
                print("! Geçersiz dönüştürücü türü, Lütfen 'uzunluk', 'ağırlık' veya 'sıcaklık' girin.")
                continue

            value = float(input("Dönüştürülecek değeri giriniz: "))
            from_unit = input(f"Dönüştürülecek birimi girin (örn: {'metre, inç, foot' if converter_type == 'uzunluk' else 'kilogram, pound, gram' if converter_type == 'ağırlık' else 'celsius, fahrenheit, kelvin'}): ").lower()
            to_unit = input(f"Hangi birime dönüştürülsün (örn: {'santimetre, kilometre, mil' if converter_type == 'uzunluk' else 'miligram, ons' if converter_type == 'ağırlık' else 'kelvin, celsius'}): ").lower() # Parantez kapatma eksikti

            result = None
            if converter_type == "uzunluk":
                result = convert_length(value, from_unit, to_unit)
            elif converter_type == "ağırlık":
                result = convert_weight(value, from_unit, to_unit)
            elif converter_type == "sıcaklık":
                result = convert_temperature(value, from_unit, to_unit)

            if isinstance(result, str):
                print(f"Hata: {result}")
            else:
                print(f"Sonuç: {value} {from_unit} = {result:.2f} {to_unit}")

        except ValueError:
            print("! Geçersiz giriş. Lütfen geçerli bir sayı girin.")
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
