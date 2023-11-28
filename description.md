# Description of The Package

Group 3: Han Chen, Jade Yu

## Package

package name: superman

establish a management system that can be used by both the customers and the supermarket.

## Subpackage

two subpackage: customer, admin

### `customer` subpackage

include two modules, namely `members.py` and `transactions.py`.

the module `members.py` mainly stores the membership information inputs, including personal information such as name, email, phone number etc. It can also stores information like account credits, total consumption amount etc.

the module `tranaction.py` records every order made by customers, providing detail information like transaction time, shopped items etc. It also enables customers to return, reorder goods, write reviews etc.

### `admin` subpackage

include two modules, namely `account.py` and `inventory.py`.

the module `account.py` can access customer information and give promotions.

the module `inventory.py` can access the supermarket inventory records and manage the inventory including updating the quantity of items, calculating the expected profit, deciding clearance goods, removing items etc. 
