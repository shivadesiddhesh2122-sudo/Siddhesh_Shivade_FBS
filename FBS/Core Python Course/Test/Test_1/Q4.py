NUM_EXTERIOR_WALLS = 7
NUM_INTERIOR_WALLS = 8

area_one_wall = float(input("Enter the area of one wall: "))
cost_per_sq_interior = float(input("Enter the cost per unit area for INTERIOR wall: "))
cost_per_sq_exterior = float(input("Enter the cost per unit area for EXTERIOR wall: "))



# 1. Exterior Cost
total_exterior_area = NUM_EXTERIOR_WALLS * area_one_wall
exterior_painting_cost = total_exterior_area * cost_per_sq_exterior

# 2. Interior Cost
total_interior_area = NUM_INTERIOR_WALLS * area_one_wall
interior_painting_cost = total_interior_area * cost_per_sq_interior

# 3. Total Cost
total_painting_cost = exterior_painting_cost + interior_painting_cost

# Output
print("Assumed Exterior Walls:", NUM_EXTERIOR_WALLS)
print("Assumed Interior Walls:", NUM_INTERIOR_WALLS)
print("Cost for Exterior Walls:", exterior_painting_cost)
print("Cost for Interior Walls:", interior_painting_cost)
print("TOTAL PAINTING COST:", total_painting_cost)
