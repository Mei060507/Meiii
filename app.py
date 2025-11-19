import streamlit as st
import datetime

# Ambil tahun saat ini secara dinamis
TAHUN_SEKARANG = datetime.date.today().year

def hitung_usia(tahun_lahir, tahun_sekarang=TAHUN_SEKARANG):
    """Menghitung usia (hanya tahun) berdasarkan tahun lahir."""
    
    # Pastikan input adalah integer sebelum perhitungan
    try:
        tahun_lahir = int(tahun_lahir)
    except ValueError:
        return "Error: Tahun lahir harus berupa angka."
        
    usia = tahun_sekarang - tahun_lahir
    return usia

# --- Tampilan Streamlit ---

st.set_page_config(
    page_title="Kalkulator Usia Sederhana",
    layout="centered"
)

st.title("🎂 Kalkulator Usia Sederhana")
st.markdown(f"*(Tahun sekarang disetel ke **{TAHUN_SEKARANG}**)*")

# Widget input Streamlit (Teks input untuk tahun lahir)
tahun_lahir_input = st.number_input(
    "Masukkan Tahun Lahir Anda:",
    min_value=1900,
    max_value=TAHUN_SEKARANG,
    value=2000, # Nilai default
    step=1,
    format="%d" # Pastikan input berupa integer
)

# Tombol untuk memicu perhitungan
if st.button("Hitung Usia"):
    if tahun_lahir_input:
        # Panggil fungsi
        usia_hasil = hitung_usia(tahun_lahir_input)
        
        # Tampilkan hasil
        st.balloons() # Efek visual 
        st.success(
            f"Jika Anda lahir tahun **{tahun_lahir_input}** dan sekarang adalah tahun **{TAHUN_SEKARANG}**, "
            f"usia Anda adalah: **{usia_hasil} tahun**"
        )
    else:
        st.warning("Mohon masukkan tahun lahir terlebih dahulu.")

st.sidebar.info("Aplikasi sederhana yang dibuat dengan Streamlit.")