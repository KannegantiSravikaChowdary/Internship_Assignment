# Mobius Strip Modelling and Analysis
##Assignment Task
Write a Python script that models a Mobius strip using parametric equations and computes key geometric properties.

1. Requirements
Define a MobiusStrip class that:
Accepts:
Radius R (distance from the center to the strip)
Width w (strip width)
Resolution n (number of points in the mesh)
Computes:
A 3D mesh/grid of (x, y, z) points on the surface
Surface area (numerically, using integration or approximation)
Edge length (numerically along the boundary)

2. Parametric Equation of Mobius Strip
Use the parametric equations:
x(u,v)=(R+v⋅cos⁡(u2))⋅cos⁡(u)
y(u,v)=(R+v⋅cos⁡(u2))⋅sin⁡(u)
z(u,v)=v⋅sin⁡(u2)
Where:
u∈[0,2π]
v∈[−w/2,w/2]

## Solution Overview 

### Code Structure  
- MobiusStrip class encapsulates all functionality  
- Constructor initializes parameters and generates mesh  
- Methods for computing surface area, edge length, and visualization  
- Code is modular and well-commented for clarity  

### Surface Area Approximation  
- Used numerical differentiation of parametric surface coordinates  
- Calculated the cross product of partial derivatives to find local area elements  
- Summed these local areas over the mesh to estimate total surface area  

### Challenges  
- Managing numerical stability in gradient calculations  
- Choosing optimal mesh resolution for balance between accuracy and performance  
- Rendering the Möbius strip smoothly in 3D plots  

## Usage  
- Run mobius_strip.py to see surface area, edge length output and 3D plot visualization  

## Output  
- Surface Area ≈  0.0001 
- Edge Length ≈  6.3150
- 3D plot displayed in a window  

## Files  
- mobius_strip.py — Python script implementing the solution  
- mobius_plot.png — Screenshot/image of the 3D Möbius strip visualization  

