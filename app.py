import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import time

st.set_page_config(page_title="Virtual Lab: Waktu & Jarak", layout="wide")

# --------------------------
# Fungsi perhitungan
# --------------------------
def compute_meeting_time(dist, v1, v2):
    if v1 + v2 == 0:
        return None
    return dist / (v1 + v2)

def pos_at_time(t, dist, v1, v2):
    x1 = v1 * t
    x2 = dist - v2 * t
    return x1, x2

# --------------------------
# Judul aplikasi
# --------------------------
st.title("🚗🧍 Virtual Lab Matematika — Waktu & Jarak (Pertemuan)")
st.write("Atur parameter lalu lihat animasinya! Cocok untuk pembelajaran jarak, waktu, dan kecepatan.")

# --------------------------
# Sidebar (Input)
# --------------------------
with st.sidebar:
    st.header("Parameter")
    dist = st.number_input("Jarak awal (meter)", min_value=1.0, value=100.0)
    v1 = st.number_input("Kecepatan A (m/s)", min_value=0.0, value=3.0)
    v2 = st.number_input("Kecepatan B (m/s)", min_value=0.0, value=4.0)

    autoplay = st.checkbox("Auto Play Animasi", value=False)
    speed = st.slider("Kecepatan animasi (x)", 0.2, 5.0, 1.0)

# --------------------------
# Hitung waktu pertemuan
# --------------------------
t_meet = compute_meeting_time(dist, v1, v2)

col1, col2 = st.columns([3,2])

# --------------------------
# Grafik animasi
# --------------------------
with col1:

    fig, ax = plt.subplots(figsize=(9,3))

    max_time = t_meet * 1.2 if t_meet else 20
    t = st.slider("Waktu (detik)", 0.0, float(max_time), 0.0, 0.1)

    x1, x2 = pos_at_time(t, dist, v1, v2)

    ax.set_xlim(0, dist)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])

    ax.hlines(0, 0, dist, linewidth=5, color="gray")

    # Objek A
    objA = Circle((x1, 0), radius=1, color="blue")
    ax.add_patch(objA)
    ax.text(x1, 0.3, "A 🧍", ha="center")

    # Objek B
    objB = Circle((x2, 0), radius=1, color="red")
    ax.add_patch(objB)
    ax.text(x2, 0.3, "B 🚗", ha="center")

    # Titik temu
    if t_meet and t >= t_meet:
        ax.scatter([v1*t_meet], [0], color="gold", s=150, marker="*", zorder=10)
        ax.text(v1*t_meet, -0.5, "Titik Temu ⭐", ha="center", fontsize=10)

    st.pyplot(fig)

    # Auto play
    if autoplay:
        place = st.empty()
        ct = 0
        while ct < max_time:
            fig, ax = plt.subplots(figsize=(9,3))
            x1, x2 = pos_at_time(ct, dist, v1, v2)

            ax.set_xlim(0, dist)
            ax.set_ylim(-1, 1)
            ax.set_yticks([])
            ax.hlines(0, 0, dist, linewidth=5, color="gray")

            ax.add_patch(Circle((x1,0), radius=1, color="blue"))
            ax.text(x1, 0.3, "A 🧍", ha="center")

            ax.add_patch(Circle((x2,0), radius=1, color="red"))
            ax.text(x2, 0.3, "B 🚗", ha="center")

            if t_meet and ct >= t_meet:
                ax.scatter([v1*t_meet], [0], color="gold", s=150, marker="*")
                ax.text(v1*t_meet, -0.5, "Titik Temu ⭐", ha="center")

            place.pyplot(fig)
            ct += 0.1 * speed
            time.sleep(0.05)

# --------------------------
# Perhitungan
# --------------------------
with col2:
    st.header("Hasil Perhitungan")

    if t_meet:
        st.success(f"Waktu pertemuan = **{t_meet:.2f} detik**")
        st.info(f"Mereka bertemu pada posisi **x = {v1*t_meet:.2f} meter** dari titik A.")
    else:
        st.error("Mereka tidak akan pernah bertemu (jumlah kecepatan = 0).")

    st.markdown("---")
    st.write("Rumus dasar bila bergerak saling mendekat:")
    st.latex(r"t = \frac{\text{jarak}}{v_1 + v_2}")
