
# data types in Python

from pyscript import display, document


# shop: resto name, owner, year

restaurant_name = ' Strawberry Clubhouse ✿' # string

owner_name = 'Harmony Yao' # string

year_established = 2025 # integer


# shop & menu

tax_rate = 0.05  # floating point

product_name = [
    'strawberry jam parfait', 
    'mixed berry yogurt', 
    'strawberry shortcake',
    'strawberry flan',
    'strawberry ice-cream bars', 
    'strawberry cream cheese cupcakes', 
    'strawberry cream sando'] # list

popular_item_price = [
    '₱180.00', 
    '₱170.00', 
    '₱150.00'] # list

menu_prices = [
'₱130.00',
'₱135.00',
'₱120.00',
'₱135.00'] #list

common_allergens = 'dairy, nuts, & egg' # string


# hours

has_delivery = True # boolean
business_hours = '7:00 am - 8:00pm'  # string



# display: shop
display(f'{restaurant_name}', target='name')
display(f'founded by {owner_name} | established on {year_established}', target='details')
display(f'tax rate: ₱{tax_rate}', target='tax')

# list
# best sellers
display(f'{product_name [0]}', target='desserts')
display(f'{product_name [1]}', target='desserts')
display(f'{product_name [2]}', target='desserts')

# desserts
display(f'{product_name [3]}', target='desserts')
display(f'{product_name [4]}', target='desserts')
display(f'{product_name [5]}', target='desserts')
display(f'{product_name [6]}', target='desserts')

display(f'{popular_item_price [0]}', target='price')
display(f'{popular_item_price [1]}', target='price')
display(f'{popular_item_price [2]}', target='price')
display(f'{menu_prices [0]}', target='price')
display(f'{menu_prices [1]}', target='price')
display(f'{menu_prices [2]}', target='price')
display(f'{menu_prices [3]}', target='price')

#allergens
display(f'CAUTION! ⚠️ food may contain: {common_allergens}', target='allergens')

#hours
display(f"⏰ Opening Hours: {business_hours}", target="hours")

# delivery: Boolean
if has_delivery:
    display("Delivery Available 🎂", target="hours")
else:
    display("Delivery Not Available 🍰", target="hours")
