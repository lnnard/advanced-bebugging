import argparse
import math

def calculate_cone_properties(radius, height, scale):
    """
    Calculate the volume and surface area of a cone.
    
    Args:
        radius (float): The radius of the cone's base.
        height (float): The height of the cone.
        scale (float): An optional scale factor to resize the cone.
        
    Returns:
        tuple: Scaled volume and surface area of the cone.
    """
    # Apply scale factor
    radius *= scale
    height *= scale
    
    # Calculate volume and surface area
    volume = (1/3) * math.pi * radius**2 * height
    slant_height = math.sqrt(radius**2 + height**2)
    surface_area = math.pi * radius * (radius + slant_height)
    
    return volume, surface_area

def main():
    # calculate_cone_properties here

    # radius
    radius = 2
    # height
    height = 10
    # scale
    scale = 2.2
    
    # Calculate properties
    volume, surface_area = calculate_cone_properties(radius, scale)
    
    # Output results
    print(f"Scaled Cone Properties:")
    print(f" - Volume: {volume:.2f} cubic units")
    print(f" - Surface Area: {surface_area:.2f} square units")

if __name__ == "__main__":
    main()
