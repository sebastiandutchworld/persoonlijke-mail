# CHANGES TO THIS DIRECTORY 
<hr>

#### Ticket #2006  
#### Date: 17/05/2022 
#### By: Frannie

1. Add a new column to show "Total Delivered" for pdf sale report only if status is "Order"
2. Decrease font size of column header for a better fit
3. Include translation for this column in DE and NL to "Insgesamt Gelieferd" and "Aantal Geleverd"\
4. Change "Hoeveelheid" to "Aantal", "Quantity" to "Qty"
5. Omit in the generated sale_report any cancelled product that reflects a qty of 0.

#### Working Directories:
1. dws_gascontrol
   * i18n
     * de.po
     * nl.po
   * views
     * report_sale.xml

#### Work:
Task 1 & 3
@views - report_sales.xml
Insert a "Total Delivered" table header/column  with a conditional at line 119
Insert table row/data with conditional at line 162 to 166
@i18n - de.po 
Insert new block of translation for "Insgesamt Geliefert" at line 81 - 84 
@i18n - nl.po
Insert new block of translation for "Aantal Geleverd" at line 454 - 457

Note: if msgstr will grab an existing msgid, so attention needs to be given if naming contains part of another msgid. eg. "Qty" "Menge".  Naming "Qty Delivered" with translation "Insgesamt Geliefert" produced a "Menge Geliefert".

Task 2
@views - report_sales.xml
Change Quantity to Qty
Reduced font-size of Qty, Total Delivered, Unit Price, Discount to 0.9rem
Gave Unit Price a small left-right padding of 0.5rem

Task 4 
@i18n - nl.po
Change NL translation "Hoeveelheid" to "Aantal"

Task 5
@views -report_sales.xml
Add conditional to line 142 factoring in if product quantity is 0, it will not render in the report.

<hr>

#### Ticket #1726 
#### Date: 18/05/2022 
#### By: Frannie

Product description from vendor in the view for WH/IN (Receipts) should be Vendor Product Name

#### Working Directories:
1. dws_gascontrol
   * views
     * stock_picking_views.xml
     
#### Work:
1. Add new code block at lines 23-32 that pulls Vendor Product Code + Vendor Product Name in new column "Vendor Description"

Note: if Vendor Product Name is empty, only Vendor Product Code will render.

<hr>
