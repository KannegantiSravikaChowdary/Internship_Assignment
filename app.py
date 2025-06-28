import streamlit as st
from mobius_strip import MobiusStrip
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🌀 Möbius Strip Visualizer")

R = st.slider("Radius (R)", 0.5, 2.0, 1.0)
w = st.slider("Width (w)", 0.1, 1.0, 0.4)
n = st.slider("Resolution (n)", 100, 500, 300)

mobius = MobiusStrip(R=R, w=w, n=n)

st.subheader("🔢 Computed Properties")
st.write(f"• Surface Area ≈ `{mobius.compute_surface_area():.4f}`")
st.write(f"• Edge Length ≈ `{mobius.compute_edge_length():.4f}`")

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(mobius.x, mobius.y, mobius.z, cmap='viridis', edgecolor='none')
ax.set_title("Möbius Strip (3D)")
st.pyplot(fig)
