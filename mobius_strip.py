import numpy as np
import matplotlib.pyplot as plt

class MobiusStrip:
    """
    Class to model a Möbius strip using parametric equations.
    Computes 3D mesh, surface area, edge length, and provides visualization.
    """
    def __init__(self, R=1.0, w=0.2, n=200):  # Fixed: __init__ not _init_
        self.R = R
        self.w = w
        self.n = n

        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w / 2, w / 2, n)
        )
        self.x, self.y, self.z = self._generate_mesh()

    def _generate_mesh(self):
        u, v = self.u, self.v
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_surface_area(self):
        dxu = np.gradient(self.x, axis=0)
        dxv = np.gradient(self.x, axis=1)
        dyu = np.gradient(self.y, axis=0)
        dyv = np.gradient(self.y, axis=1)
        dzu = np.gradient(self.z, axis=0)
        dzv = np.gradient(self.z, axis=1)

        cross_x = dyu * dzv - dzu * dyv
        cross_y = dzu * dxv - dxu * dzv
        cross_z = dxu * dyv - dyu * dxv

        # ✅ Fixed variable name: use square (`**2`) instead of undefined cross_y2 etc.
        dA = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)

        du = (2 * np.pi) / (self.n - 1)
        dv = self.w / (self.n - 1)
        return np.sum(dA) * du * dv

    def compute_edge_length(self):
        u = np.linspace(0, 2 * np.pi, self.n)
        v = self.w / 2
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)

        dx = np.diff(x)
        dy = np.diff(y)
        dz = np.diff(z)

        # ✅ Fixed variable name: dy**2, dz**2
        length = np.sum(np.sqrt(dx**2 + dy**2 + dz**2))
        return length

    def plot(self):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, cmap='viridis', edgecolor='none')
        ax.set_title('Möbius Strip')
        plt.tight_layout()
        plt.savefig("mobius_plot.png")
        plt.show()

if __name__ == "__main__":
    mobius = MobiusStrip(R=1.0, w=0.4, n=300)
    print(f"Surface Area ≈ {mobius.compute_surface_area():.4f}")
    print(f"Edge Length ≈ {mobius.compute_edge_length():.4f}")
    mobius.plot()
