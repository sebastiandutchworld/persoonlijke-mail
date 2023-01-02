# CHANGES TO THIS DIRECTORY 
<hr>

#### Ticket #2336 
#### Date: 2/06/2022 
#### By: Frannie

Remove 
1. New Order and Cancel Selected
2. New Order and Delete Selected 
in merging of PO from module. 
These options cause the printout to render a different description as it creates an entirely new PO.

Copy 
Copy the bi_merge_purchase_order folder and renamed it to dws_po_merge

#### Working Directories:
1. dws_po_merge
   * security
     * ir.model.access.csv
   * wizard
     * order_merge_wiz.py
   * __ manifest __.py

#### Work:
@ ir.model.access.csv
change model_id:id to dws_po_merge

@ order_merge_wiz.py
Line 37:
deleted - ('new', 'New Order and Cancel Selected'), ('exist', 'New order and Delete all selected order')
change - default="exist_1"

Line 86 - 149:
removed conditional for "new", "exist"

@ __ manifest __.py
changed - 'name': 'DWS Purchase Order Merge'

Uninstalled bi_merge_purchase and installed dws_po_merge

<hr>
