# This is a sample Python script.
from stockx import StockXAPI

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settin

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def print_supreme():
    stockx = StockXAPI()
    search_term = "adidas yeezy"
    item_id = "adidas-yeezy-450-cloud-white"

    products = stockx.search_items(search_term=search_term, output_data=['name', 'id', ['market', 'lastSale']],
                                   page=1,
                                   max_searches=10)
    for product in products:
        print(product)

    item_info = stockx.get_item_data(
        item_id=item_id,
        output_data=[
            'name',
            ['market', 'lastSale'],
            ['market', 'lowestAsk'],
            ['market', 'highestBid']
        ])
    print('\n', item_info)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_supreme()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
