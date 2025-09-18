def get_chemical_price(chemical, region):
    # Use local agri market API or dummy data
    # In real app, fetch from market data provider
    prices = {
        "Urea": {"Delhi": 6, "Maharashtra": 7, "Punjab": 5, "Odisha": 8},
        "Carbendazim": {"Delhi": 120, "Maharashtra": 130, "Punjab": 110, "Odisha": 125},
    }
    return prices.get(chemical, {}).get(region, "N/A")