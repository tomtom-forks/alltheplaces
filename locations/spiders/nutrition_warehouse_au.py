from locations.storefinders.stockinstore import StockInStoreSpider


class NutritionWarehouseAUSpider(StockInStoreSpider):
    name = "nutrition_warehouse_au"
    item_attributes = {"brand": "Nutrition Warehouse", "brand_wikidata": "Q117747424"}
    api_site_id = "10098"
    api_widget_id = "105"
    api_widget_type = "storelocator"
    api_origin = "https://www.nutritionwarehouse.com.au"
