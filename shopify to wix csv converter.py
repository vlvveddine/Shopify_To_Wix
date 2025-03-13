import csv

def convert_shopify_to_wix(shopify_csv, wix_csv):
    with open(shopify_csv, mode='r', encoding='utf-8') as infile, open(wix_csv, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ["handleId", "fieldType", "name", "description", "price", "productImageUrl"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for index, row in enumerate(reader, start=1):  # Assign numeric handleId starting from 1
            writer.writerow({
                "handleId": index,
                "fieldType": "Product",  # Set fieldType to "Product"
                "name": row["Title"],
                "description": row["Body (HTML)"],
                "price": row["Variant Price"],
                "productImageUrl": row["Image Src"]
            })
    
    print(f"Conversion completed: {wix_csv}")

# Example usage
convert_shopify_to_wix("shopify_products.csv", "wix_products.csv")
