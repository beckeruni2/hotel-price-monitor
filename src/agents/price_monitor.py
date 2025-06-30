class PriceMonitor:
    def __init__(self, hotel_name, target_price):
        self.hotel_name = hotel_name
        self.target_price = target_price

    def check_price(self):
        # This method will call the scraper to get the current price
        current_price = scrape_price(self.hotel_name)
        return current_price

    def notify_user(self, current_price):
        if current_price < self.target_price:
            print(f"Price alert! The price for {self.hotel_name} has dropped to {current_price}.")