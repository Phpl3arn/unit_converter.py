# Katkıda Bulunma Rehberi

Bu projeye katkıda bulunduğunuz için teşekkür ederiz! Her türlü katkı (hata düzeltmeleri, yeni özellikler, dokümantasyon iyileştirmeleri vb.) büyük takdirle karşılanır.

## 🚀 Başlamadan Önce

1.  **Hata Raporu/Özellik İsteği:** Bir hata bulduysanız veya yeni bir özellik önermek istiyorsanız, lütfen öncelikle bir [Issue](https://github.com/KullaniciAdiniz/unit-converter-python/issues) açın. Böylece aynı iş üzerinde birden fazla kişinin çalışmasını engellemiş oluruz ve tartışma için bir platform oluştururuz.
    (Yukarıdaki linki kendi deponuzun issues sayfasına göre düzenleyin.)

2.  **Kod Stili:** Lütfen Python'ın PEP 8 kodlama standartlarına uymaya çalışın.

## ✨ Katkıda Bulunma Adımları

1.  **Depoyu Çatallayın (Fork edin):**
    Projenin GitHub sayfasında sağ üstteki "Fork" butonuna tıklayarak projenin kendi kopyanızı oluşturun.

2.  **Projeyi Klonlayın:**
    Terminalinizde veya komut istemcinizde aşağıdaki komutu kullanarak projeyi yerel bilgisayarınıza klonlayın:
    ```bash
    git clone [https://github.com/Phpl3arn/unit-converter-python.git](https://github.com/Phpl3arn/unit-converter-python.git)
    ```
3.  **Yeni Bir Dal (Branch) Oluşturun:**
    Değişikliklerinizi yapmak için ana (master/main) daldan ayrı yeni bir dal oluşturun. Dal adları genellikle yapılan işi yansıtmalıdır (örn: `feature/new-unit-type`, `bugfix/temperature-error`).
    ```bash
    git checkout -b ozellik/yeni-birim-tipi
    ```

4.  **Değişikliklerinizi Yapın:**
    Kodu geliştirin, hata düzeltmelerini yapın veya yeni özellikleri ekleyin.

5.  **Değişikliklerinizi Taahhüt Edin (Commit):**
    Yaptığınız değişiklikleri açıklayan anlamlı ve kısa commit mesajları kullanın.
    ```bash
    git add .
    git commit -m "feat: yeni birim tipi (alan) eklendi"
    ```
    (Commit mesajları için "feat:", "fix:", "docs:", "style:" gibi ön ekler kullanmak iyi bir pratiktir.)

6.  **Değişiklikleri Uzak Depoya Gönderin (Push):**
    Kendi çatallanmış deponuzdaki yeni dala değişiklikleri gönderin:
    ```bash
    git push origin ozellik/yeni-birim-tipi
    ```

7.  **Çekme İsteği (Pull Request - PR) Oluşturun:**
    GitHub'daki kendi deponuza gidin. `ozellik/yeni-birim-tipi` dalınızda bir Pull Request oluşturma seçeneğini göreceksiniz. Açıklayıcı bir başlık ve detaylı bir açıklama ile Pull Request'i oluşturun.

Proje sahibi/bakımcısı PR'nizi inceleyecek ve uygun gördüğü takdirde ana depoya birleştirecektir.

Tekrar teşekkürler!
