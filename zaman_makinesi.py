#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Gereksiz Zaman Makinesi
Sadece 1 saniye geleceğe gider. Ciddiye alın.
"""

import time
import random
import sys

def dramatik_anons():
    print("=" * 60)
    print("     EVRENİN EN GEREKSİZ ZAMAN MAKİNESİ v1.0")
    print("     Resmi NASA-ötesi Onaylı Dramatik Protokol")
    print("=" * 60)
    print()
    time.sleep(1)
    
    print("Sistem kontrol ediliyor...")
    time.sleep(0.8)
    print("Kuantum dolaşıklık durumu: Gereksiz ama stabil.")
    time.sleep(0.7)
    print("Enerji kaynağı: 1 adet time.sleep(1) fonksiyonu.")
    time.sleep(0.9)
    print("Hedef: Geleceğe tam 1 saniye.")
    time.sleep(0.5)
    print()
    
    print("UYARI: Bu makine geçmişe gidemez.")
    print("Geçmiş hataları düzeltmek için başka bir evren deneyin.")
    # Gizli not: Bazı yönetimler de geçmişi değiştiremez, sadece ileri bakar.
    time.sleep(1.2)
    
    print("\nBaşlatma sekansı başlıyor...")
    for i in range(3, 0, -1):
        print(f"  {i}...")
        time.sleep(0.6)
    print("  GİT!")
    print()

def zaman_yolculugu():
    print("Zaman-uzay sürekliliği bükülüyor...")
    time.sleep(0.5)
    print("1 saniye ileriye gidiliyor...")
    time.sleep(1)  # İşte o an. Bilim.
    print()
    print("*** YOLCULUK TAMAMLANDI ***")
    print("Artık 1 saniye gelecektesiniz.")
    print("Tebrikler. Hiçbir şey değişmedi. Ama resmi olarak gelecektesiniz.")
    print()
    print("Dönüş yok. Çünkü zaten sadece 1 saniye gittik.")
    print("Makineyi kapatmak için Ctrl+C yapın. Veya sonsuza kadar bekleyin.")

if __name__ == "__main__":
    try:
        dramatik_anons()
        zaman_yolculugu()
        print("\n[Damga] Gereksizlik Onaylandı.")
        print("[İmza] Kayyum Grok - Zaman Makinesi Operatörü")
        print("[Tarih] 13.10.2026")
        print("[Ciddiyet Seviyesi] %100 (ama biraz değil)")
    except KeyboardInterrupt:
        print("\nYolculuk iptal edildi. Hala şimdidesiniz. Üzgünüz.")
        sys.exit(0)
