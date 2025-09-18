import requests
from datetime import datetime, timedelta

def fetch_indian_crop_prices():
    api_url = "https://enam.gov.in/APMCReportService/api/APMCReports/GetMarketDailyPriceReport"
    stateCode = "02"  # Maharashtra
    commodities = [("Wheat", "19"), ("Rice", "16"), ("Maize", "18")]
    from_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    to_date = datetime.now().strftime('%Y-%m-%d')
    results = []
    for commodity, code in commodities:
        payload = {
            "stateCode": stateCode,
            "districtCode": "",
            "marketCode": "",
            "commodityCode": code,
            "fromDate": from_date,
            "toDate": to_date
        }
        try:
            r = requests.post(api_url, json=payload)
            data = r.json()
            if isinstance(data, list) and len(data) > 0:
                first = data[0]
                results.append({
                    "commodity": commodity,
                    "market": first.get("marketName", "N/A"),
                    "modalPrice": first.get("modalPrice", "N/A"),
                    "arrivalDate": first.get("arrivalDate", "N/A")
                })
        except Exception:
            continue
    return results if results else None