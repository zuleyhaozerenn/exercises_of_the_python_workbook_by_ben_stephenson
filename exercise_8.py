"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
"""
widget = 75
gizmo = 112

widget_sayısı = int(input("The number of widget: "))
gizmo_sayısı = int(input("The number of gizmo: "))

total_weight = (widget * widget_sayısı) + (gizmo_sayısı * gizmo)

print("The total weight of your order: {} gram".format(total_weight))