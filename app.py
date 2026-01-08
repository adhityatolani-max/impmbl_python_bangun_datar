import streamlit as st

# ================================
# KONFIGURASI HALAMAN (WAJIB)
# ================================
st.set_page_config(
    page_title="IMPMBL Bangun Datar",
    layout="centered"
)

# ================================
# JUDUL APLIKASI
# ================================
st.title("IMPMBL")
st.subheader("Aplikasi Hitung Luas dan Keliling Bangun Datar")

st.markdown(
    """
    **Ikatan Montolutusan Pemuda Mahasiswa Banggai Laut (IMPMBL)**  
    Aplikasi ini digunakan untuk menghitung **luas** dan **keliling**
    beberapa bangun datar yang diperlukan untuk membangun ASRAMA BANGGAI LAUT.
    """
)

st.markdown("---")

# ================================
# FUNGSI LUAS
# ================================
def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# ================================
# FUNGSI KELILING
# ================================
def keliling_persegi(sisi):
    return 4 * sisi

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def keliling_segitiga(sisi):
    return 3 * sisi

# ================================
# PILIH JENIS PERHITUNGAN
# ================================
st.markdown("### Pilih Jenis Perhitungan")
jenis = st.radio(
    "Jenis Perhitungan",
    ["Luas", "Keliling"]
)

st.markdown("### Pilih Bangun Datar")
bangun = st.selectbox(
    "Bangun Datar",
    ["Persegi", "Persegi Panjang", "Segitiga"]
)

st.markdown("---")

# ================================
# INPUT & PROSES
# ================================
if bangun == "Persegi":
    sisi = st.number_input("Masukkan panjang sisi", min_value=0.0)

    if st.button("Hitung"):
        if jenis == "Luas":
            hasil = luas_persegi(sisi)
        else:
            hasil = keliling_persegi(sisi)

        st.success(f"Hasil {jenis} Persegi = {hasil}")

elif bangun == "Persegi Panjang":
    panjang = st.number_input("Masukkan panjang", min_value=0.0)
    lebar = st.number_input("Masukkan lebar", min_value=0.0)

    if st.button("Hitung"):
        if jenis == "Luas":
            hasil = luas_persegi_panjang(panjang, lebar)
        else:
            hasil = keliling_persegi_panjang(panjang, lebar)

        st.success(f"Hasil {jenis} Persegi Panjang = {hasil}")

elif bangun == "Segitiga":
    if jenis == "Luas":
        alas = st.number_input("Masukkan alas", min_value=0.0)
        tinggi = st.number_input("Masukkan tinggi", min_value=0.0)

        if st.button("Hitung"):
            hasil = luas_segitiga(alas, tinggi)
            st.success(f"Hasil Luas Segitiga = {hasil}")
    else:
        sisi = st.number_input("Masukkan panjang sisi", min_value=0.0)

        if st.button("Hitung"):
            hasil = keliling_segitiga(sisi)
            st.success(f"Hasil Keliling Segitiga = {hasil}")

# ================================
# FOOTER
# ================================
st.markdown("---")
st.markdown("© 2026 **IMPMBL**")
