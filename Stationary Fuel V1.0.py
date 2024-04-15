def calculate_emissions(fuel_type, fuel_consumption, emission_factor):
    emissions = fuel_consumption * emission_factor
    return emissions

# Dummy data for a sub-sector (e.g., Residential buildings)
fuel_type = "Natural gas"
fuel_consumption = 1000  # GJ
emission_factor = 56  # kg CO2e/GJ

# Calculate emissions for the sub-sector
emissions = calculate_emissions(fuel_type, fuel_consumption, emission_factor)

print(f"Emissions from {fuel_type}: {emissions} kg CO2e")
