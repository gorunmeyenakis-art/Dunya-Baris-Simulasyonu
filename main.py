import time
import random
import sys

def yazi_yaz(metin, gecikme=0.03):
    """Metni daktilo efektiyle ekrana basar."""
    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def ana_simulasyon():
    # --- BASLANGIC VE ANALIZ ---
    print("\n" + "="*70)
    print("   TURK-ISLAM MERHAMETI VE ADALETI: DUNYA BARIS SIMULASYONU v4.0")
    print("="*70)
    
    yazi_yaz("[ANALIZ] Orta Dogu'daki gerilimler taranıyor...")
    time.sleep(1)
    yazi_yaz("[DURUM] Iran-Israil savas senaryosu sonlandirildi. Hakem: TURKIYE.")
    yazi_yaz("[HEDEF] Kudus ve dunya yonetiminin 'Adalet ve Hak' esasina gecisi.")
    
    # --- MODUL 1: EKONOMIK REFAH ---
    print("\n>>> [MODUL 1] Kuresel Refah ve Ekonomik Onarim")
    time.sleep(1)
    savas_hasari = random.randint(5, 15) # Adaletli yonetim hasari minimize eder
    refah_skoru = (100 - savas_hasari) * 1.5
    refah_skoru = min(refah_skoru, 100)
    yazi_yaz(f"[*] Kaynaklar adaletle dagitiliyor... Refah Puani: %{refah_skoru}")
    yazi_yaz("[*] Enflasyon ve aclik Turk-Islam merhametiyle sona erdirildi.")

    # --- MODUL 2: TEKNOLOJI VE KARDESLIK ---
    print("\n>>> [MODUL 2] Teknoloji Paylasimi ve Baris Muhafizlari")
    time.sleep(1)
    envanter = ["Merhamet IHA'lari", "Kuresel Siber Kalkan", "Yapay Zeka Adalet Terazisi"]
    for cihaz in envanter:
        yazi_yaz(f"    [+] {cihaz} tum dunya mazlumlari icin aktif edildi.")
    yazi_yaz("[*] Savunma sanayii artik 'Oldurmek' degil, 'Yasatmak' icin calisiyor.")

    # --- MODUL 3: GELECEK NESIL VE EGITIM ---
    print("\n>>> [MODUL 3] Yunus Emre & Mevlana Bilgelik Akustigi")
    time.sleep(1)
    yazi_yaz("[*] Dunyadaki tum yetimler 'Devlet-i Aliyye' gelenegiyle koruma altinda.")
    yazi_yaz("[*] Mufredat: Hak, Hukuk, Adalet ve Kardeslik dersleri eklendi.")

    # --- FINAL RAPORU ---
    time.sleep(2)
    print("\n" + "#"*70)
    print("                     SIMULASYON TAMAMLANDI")
    print("#"*70)
    yazi_yaz(f"FINAL DURUMU: Kudus huzurlu, Dunya adil, Turkiye lider.")
    yazi_yaz("SLOGAN: 'Insa Et, Yasat ve Adaleti Ustun Tut.'")
    print("#"*70 + "\n")

if __name__ == "__main__":
    ana_simulasyon()
