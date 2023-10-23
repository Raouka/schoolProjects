# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

order1 = ('manan', 'holyoke', 'FLAT3', 'chicken', 'white', 'pinto', False, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream')
order2 = ('allison', 'greenfield', 'MAGIC', 'veggies', 'brown', 'black', True, 'cheese', 'fajita veggies', 'sour cream', 'guacamole', 'tomato salsa')


prices = {
    'protein': {
        'chicken': 2.5,
        'steak': 3.5,
        'barbacoa': 3.5,
        'carnitas': 3.0,
        'veggies': 2.5,
    },
    
    'toppings': {
        'guacamole': 2.75,
        'tomato salsa': 2.5,
        'chili corn salsa': 1.75,
        'tomatillo green chili salsa': 2.0,
        'sour cream': 2.5,
        'fajita veggies': 2.5,
        'cheese': 2.0,
        'queso blanco': 2.75,
    },
    
    'discounts': {
        'MAGIC': .95,
        'SUNDAYFUNDAY': .9,
        'FLAT3': 3,
    },
    
    'locations': {
        'amherst' : 15,
        'north amherst': 15,
        'south amherst': 15,
        'hadley': 15,
        'northampton': 30,
        'south hadley': 30,
        'belchertown': 30,
        'sunderland': 30,
        'holyoke': 45,
        'greenfield': 45,
        'deerfield': 45,
        'springfield' : 45,
    },
    
    'else': 0.0,
    
}


    
def get_protein(order):
    orderDetail = order[3]
    checklist = prices['protein']
    price = 0
    for i, v in enumerate(checklist):
        if orderDetail == v:
            price += checklist[v]
        else:
            price += prices['else']
    return price
    
def get_rice(order):
    orderDetail = order[4]
    price = 0
    if orderDetail == 'white':
        price += 2.5
    elif orderDetail == 'brown':
        price += 3.5
    else:
        price = 0.0
    return price

def get_beans(order):
    orderDetail = order[5]
    price = 2.5 if orderDetail == 'pinto' or orderDetail == 'black' else 0.0
    return price

def get_burrito(order):
    orderDetail = order[6]
    boolean = 2.0 if orderDetail == True else 0.0
    return boolean

def assort_toppings(order):
    assortment = []
    for orde in range(7, len(order)):
        assortment.append(order[orde])
    return assortment
def get_toppings(order):
    orderDetails = assort_toppings(order)
    price = 0
    checklist = prices['toppings']
    
    if order[3] == 'veggies':
        checklist['fajita veggies'] = 0.0
        checklist['guacamole'] = 0.0
    
    for i, v in enumerate(checklist):
        for ord in orderDetails:
            if ord == v:
                price+= checklist[v]
            else:
                price += prices['else']
    
    checklist['fajita veggies'] = 2.5
    checklist['guacamole'] = 2.75
    return price

def calculate_total(order):
    total = get_protein(order) + get_beans(order) + get_burrito(order) + get_rice(order) + get_toppings(order)
    return total

def apply_discount(order, total):
    orderDetail = order[2]
    checklist = prices['discounts']
    
    for i, v in enumerate(checklist):
        if orderDetail == v:
            discount = checklist[v]
            if type(discount) == int:
                total -= discount
            elif type(discount) == float:
                total *= discount
            else:
                total += prices['else'] 
    
    return total   
    
def approximate_time(order):
    orderDetail = order[1]
    checklist = prices['locations']
    time = 0
    
    for i, v in enumerate(checklist):
        if orderDetail == v:
            time+= checklist[v]
        else:
            time+= prices['else']
    
    return int(time)        
    

def generate_invoice(order):
    
    y_n = 'Yes' if order[6] == True else 'No'
    top = assort_toppings(order)
    toppings = ""
    for v in range(0, len(top)):
        if v == len(top)-1:
            toppings += top[v]
        else:
            toppings += top[v] + ', '
    invoice = f'Welcome to Chipotle Mexican Grill Hadley, {order[0]}.\nYour invoice is displayed below:\nProtein: {order[3]} - ${get_protein(order)}\nRice: {order[4]} rice - ${get_rice(order)}\nBeans: {order[5]} beans - ${get_beans(order)}\nBurrito: {y_n} - ${int(get_burrito(order))}\nToppings: {toppings} - ${get_toppings(order)}\nSubtotal: ${calculate_total(order)}\nDiscount Code: {order[2]}\nTotal: ${apply_discount(order, calculate_total(order))}\nYou Save: ${calculate_total(order) - apply_discount(order, calculate_total(order))}\nYour order will be ready in {approximate_time(order)} minutes.\nEnjoy your meal and have a good day!'
    print(invoice)



generate_invoice(order1)
generate_invoice(order2)

