# Define the Multi-Level BOM structure
BOM = {
    "Assembly A": {"Sub-Assembly B": 2, "Sub-Assembly C": 1, "Part D": 3},
    "Assembly H": {"Sub-Assembly C": 1, "Part E": 2, "Part F": 1},
    "Sub-Assembly B": {"Part E": 2, "Part G": 1},
    "Sub-Assembly C": {"Part D": 2, "Part H": 1},
}
raw_materials = {"Part D": 0, "Part E": 0, "Part F": 0, "Part G": 0, "Part H": 0}
def calculate_materials(bom, assembly, quantity, material_count):
    if assembly in bom:
        for component, qty in bom[assembly].items():
            calculate_materials(bom, component, quantity * qty, material_count)
    else:
        material_count[assembly] += quantity
material_requirements = raw_materials.copy()
calculate_materials(BOM, "Assembly A", 10, material_requirements)
calculate_materials(BOM, "Assembly H", 5, material_requirements)

print("Total Raw Material Requirements:")
for material, qty in material_requirements.items():
    print(f"{material}: {qty}")

def bulk_analysis(quantities):
    bulk_results = {material: 0 for material in raw_materials}
    for assembly, qty in quantities.items():
        calculate_materials(BOM, assembly, qty, bulk_results)
    return bulk_results
bulk_quantities = {"Assembly A": 15, "Assembly H": 8}
bulk_results = bulk_analysis(bulk_quantities)
print("\nBulk Analysis Results:")
for material, qty in bulk_results.items():
    print(f"{material}: {qty}")
