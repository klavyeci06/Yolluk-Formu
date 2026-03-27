import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hoca Bilgi Giriş Sistemi", page_icon="📝")

st.title("👨‍🏫 Eğitmen Bilgi ve Ödeme Formu")
st.info("Lütfen ödemelerinize esas teşkil edecek bilgileri eksiksiz doldurunuz.")

with st.form("hoca_bilgi_formu"):
    
    # 1. BÖLÜM: KİMLİK BİLGİLERİ
    st.subheader("🆔 Kimlik Bilgileri")
    col1, col2 = st.columns(2)
    with col1:
        tc_no = st.text_input("T.C. Kimlik No", max_chars=11)
        ad = st.text_input("Ad")
    with col2:
        soyad = st.text_input("Soyad")
        egitim_durumu = st.selectbox("Eğitim Durumu", ["Lisans", "Yüksek Lisans", "Doktora"])

    # 2. BÖLÜM: KURUMSAL VE EK DERS BİLGİLERİ
    st.subheader("💼 Kurumsal Bilgiler")
    c3, c4, c5 = st.columns(3)
    with c3:
        kadro_unvani = st.selectbox("Kadro Ünvanı", ["Profesör", "Doçent", "Dr. Öğr. Üyesi", "Öğr. Gör.", "Dış Ücretli"])
    with c4:
        ek_ders_unvani = st.selectbox("Ek Ders Ünvanı", ["Ünvan seçiniz...", "Doktora Derecesine Sahip", "Normal"])
    with c5:
        personel_tipi = st.selectbox("Personel Tipi", ["Kadrolu", "Sözleşmeli", "Kurum Dışı"])

    # 3. BÖLÜM: BANKA VE VERGİ BİLGİLERİ
    st.subheader("💰 Ödeme ve Vergi Bilgileri")
    iban = st.text_input("IBAN No", placeholder="TR00 0000...")
    
    col6, col7 = st.columns(2)
    with col6:
        banka_kod = st.selectbox("Banka Şb. Kodu", ["Ziraat", "Vakıfbank", "Halkbank", "Diğer"])
        toplam_matrah = st.number_input("Toplam Vergi Matrahı", min_value=0.0, step=0.01)
    with col7:
        raporlu_gun = st.number_input("Raporlu/İzinli Günler", min_value=0, max_value=31)
        kurum_disi = st.text_input("Kurum Dışı (Varsa Belirtiniz)")

    # GÖNDERME BUTONU
    submit = st.form_submit_button("Bilgilerimi Kaydet")

    if submit:
        # Burada verileri Google Sheets'e veya veri tabanına yazdıracağız
        st.success("Bilgileriniz başarıyla kaydedildi. Teşekkür ederiz.")
