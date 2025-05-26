import numpy as np
import matplotlib.pyplot as plt

class MobiusStrip:
    """
    Class to model a Möbius strip using parametric equations.
    Computes 3D mesh, surface area, edge length, and provides visualization.
    """
    def _init_(self, R=1.0, w=0.2, n=200):
        """
        Initialize parameters and generate mesh grid.

        Args:
            R (float): Radius from center to strip.
            w (float): Width of the strip.
            n (int): Resolution of mesh grid.
        """
        self.R = R
        self.w = w
        self.n = n
        
        # Parameter ranges: u in [0, 2π], v in [-w/2, w/2]
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w / 2, w / 2, n)
        )
        self.x, self.y, self.z = self._generate_mesh()

    def _generate_mesh(self):
        """
        Generate 3D coordinates (x, y, z) using parametric equations.

        Returns:
            tuple: Mesh grids for x, y, z coordinates.
        """
        u, v = self.u, self.v
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_surface_area(self):
        """
        Approximate the surface area of the Möbius strip numerically.

        Uses partial derivatives with respect to parameters u and v,
        calculates the cross product norm, then sums over the mesh grid.

        Returns:
            float: Approximate surface area.
        """
        # Compute partial derivatives
        dxu = np.gradient(self.x, axis=0)
        dxv = np.gradient(self.x, axis=1)
        dyu = np.gradient(self.y, axis=0)
        dyv = np.gradient(self.y, axis=1)
        dzu = np.gradient(self.z, axis=0)
        dzv = np.gradient(self.z, axis=1)

        # Cross product components of the tangent vectors
        cross_x = dyu * dzv - dzu * dyv
        cross_y = dzu * dxv - dxu * dzv
        cross_z = dxu * dyv - dyu * dxv

        # Differential area element magnitude
        dA = np.sqrt(cross_x*2 + cross_y2 + cross_z*2)

        # Numerical integration over u and v
        du = (2 * np.pi) / (self.n - 1)
        dv = self.w / (self.n - 1)
        area = np.sum(dA) * du * dv
        return area

    def compute_edge_length(self):
        """
        Approximate the length of the Möbius strip boundary edge numerically.

        Returns:
            float: Approximate edge length.
        """
        u = np.linspace(0, 2 * np.pi, self.n)
        v = self.w / 2  # Top edge boundary
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)

        # Compute distance between consecutive points
        dx = np.diff(x)
        dy = np.diff(y)
        dz = np.diff(z)
        length = np.sum(np.sqrt(dx*2 + dy2 + dz*2))
        return length

    def plot(self):
        """
        Visualize the Möbius strip as a 3D surface plot.
        Saves the plot as 'mobius_plot.png'.
        """
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, cmap='viridis', edgecolor='none')
        ax.set_title('Möbius Strip')
        plt.tight_layout()
        plt.savefig("mobius_plot.png")  # Save image for report
        plt.show()

if _name_ == "_main_":
    # Instantiate MobiusStrip with desired parameters
    mobius = MobiusStrip(R=1.0, w=0.4, n=300)
    
    # Compute and print surface area and edge length
    print(f"Surface Area ≈ {mobius.compute_surface_area():.4f}")
    print(f"Edge Length ≈ {mobius.compute_edge_length():.4f}")
    
    # Plot the Möbius strip
    mobius.plot()