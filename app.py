import streamlit as st
from notion_client import Client

# Sayfa Ayarları
st.set_page_config(page_title="Personel Bildirim Formu", page_icon="📝")

# Secrets Bağlantısı
try:
    NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
    DATABASE_ID = st.secrets["DATABASE_ID"]
    notion = Client(auth=NOTION_TOKEN)
except:
    st.error("Lütfen Streamlit Secrets ayarlarını (TOKEN ve ID) yapın!")
    st.stop()

st.title("📝 Personel Yolluk ve Bildirim Formu")
st.write("Lütfen tüm bilgileri Notion tablosuna aktarılacak şekilde eksiksiz doldurunuz.")

with st.form("yolluk_formu", clear_on_submit=True):
    # Kişisel Bilgiler Bölümü
    col1, col2 = st.columns(2)
    with col1:
        ad = st.text_input("Adınız *")
        soyad = st.text_input("Soyadınız *")
        tc_no = st.text_input("T.C. Kimlik Numarası *")
        unvan = st.text_input("Unvanınız")
    with col2:
        telefon = st.text_input("Telefon (Başında 0 olmadan)")
        iban = st.text_input("IBAN (24 hane rakam) *")
        derece = st.text_input("Derece (Maks 1-15)")
        kademe = st.text_input("Kademe (Maks 1-4)")

    st.divider()
    
    # Görev Bilgileri
    col3, col4 = st.columns(2)
    with col3:
        gorev_yeri_ilce = st.text_input("Görev Yeri (İlçe) *")
        ek_gosterge = st.text_input("Ek Gösterge (3-4 Rakam)")
    with col4:
        seminer_adi = st.text_input("Seminer/Kurs Adı")
        sosyal_tesis = st.text_input("Akademi Sosyal Tesisleri Ödemesi")

    st.divider()
    
    # Ulaşım Bilgileri
    st.subheader("Ulaşım ve Bilet Bilgileri")
    c1, c2, c3 = st.columns(3)
    with c1:
        gidis_vasitasi = st.selectbox("Gidiş Vasıtası", ["Uçak", "Otobüs", "Özel Araç"])
        gidis_tutar = st.number_input("Gidiş Bileti Tutarı (₺)", min_value=0)
    with c2:
        donus_vasitasi = st.selectbox("Dönüş Vasıtası", ["Uçak", "Otobüs", "Özel Araç"])
        donus_tutar = st.number_input("Dönüş Bileti Tutarı (₺)", min_value=0)
    with c3:
        havaalani_ucret = st.number_input("Havaalanı - Seminer Yeri Ücreti", min_value=0)

    st.divider()
    submit = st.form_submit_button("🚀 Bilgileri Kaydet ve Notion'a Gönder")

    if submit:
        if not (ad and soyad and tc_no and iban):
            st.warning("Lütfen yıldızlı (*) alanları boş bırakmayın!")
        else:
            try:
                # NOTION SÜTUNLARI İLE EŞLEŞTİRME
                # Buradaki sol taraftaki isimler Notion'daki sütun başlıklarınla AYNI olmalı
                notion.pages.create(
                    parent={"database_id": DATABASE_ID},
                    properties={
                        "T.C. Kimlik Numarası *": {"title": [{"text": {"content": tc_no}}]},
                        "Adınız *": {"rich_text": [{"text": {"content": ad}}]},
                        "Soyadınız *": {"rich_text": [{"text": {"content": soyad}}]},
                        "Telefon (Başında 0 olmadan)": {"rich_text": [{"text": {"content": telefon}}]},
                        "IBAN (24 hane rakam) *": {"rich_text": [{"text": {"content": iban}}]},
                        "Unvanınız": {"rich_text": [{"text": {"content": unvan}}]},
                        "Görev Yeri (İlçe) *": {"rich_text": [{"text": {"content": gorev_yeri_ilce}}]},
                        "Gidiş Vasıtası": {"select": {"name": gidis_vasitasi}},
                        "Gidiş Bileti Tutarı (₺)": {"number": gidis_tutar},
                        "Dönüş Vasıtası": {"select": {"name": donus_vasitasi}},
                        "Dönüş Bileti Tutarı (₺)": {"number": donus_tutar},
                        "Havaalanı - Seminer Yeri Ücreti": {"number": havaalani_ucret},
                        "Akademi Sosyal Tesisleri Ödemesi": {"rich_text": [{"text": {"content": sosyal_tesis}}]},
                        "Seminer/Kurs Adı": {"rich_text": [{"text": {"content": seminer_adi}}]},
                        "Derece (Maks 1-15)": {"rich_text": [{"text": {"content": derece}}]},
                        "Kademe (Maks 1-4)": {"rich_text": [{"text": {"content": kademe}}]},
                        "Ek Gösterge (3-4 Rakam)": {"rich_text": [{"text": {"content": ek_gosterge}}]}
                    }
                )
                st.success("Tebrikler! Veriler Notion'a uçtu. Şimdi kahvenizi keyifle içebilirsiniz! ☕")
                st.balloons()
            except Exception as e:
                st.error(f"Eyvah, bir sütun ismi eşleşmedi sanırım: {e}")
