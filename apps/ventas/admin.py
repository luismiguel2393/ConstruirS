from django.contrib import admin
from .models import Cliente, Producto, Venta, Factura, CategoriaProducto, Proveedor, Inventario, Pago, ItemVenta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'correo')  # Campos a mostrar en la lista de registros
    search_fields = ('nombre', 'direccion', 'telefono', 'correo')  # Campos por los que se puede buscar

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'cantidad_stock')  # Campos a mostrar en la lista de registros
    search_fields = ('nombre', 'descripcion')  # Campos por los que se puede buscar

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_venta', 'monto_total')  # Campos a mostrar en la lista de registros
    list_filter = ('cliente', 'fecha_venta')  # Filtros laterales basados en campos

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'numero_factura', 'fecha_emision')  # Campos a mostrar en la lista de registros
    search_fields = ('numero_factura',)  # Campos por los que se puede buscar

@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # Campos a mostrar en la lista de registros
    search_fields = ('nombre', 'descripcion')  # Campos por los que se puede buscar

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'correo')  # Campos a mostrar en la lista de registros
    search_fields = ('nombre', 'direccion', 'telefono', 'correo')  # Campos por los que se puede buscar

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad_disponible')  # Campos a mostrar en la lista de registros

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('venta', 'monto', 'fecha_pago', 'metodo_pago')  # Campos a mostrar en la lista de registros
    list_filter = ('fecha_pago',)  # Filtros laterales basados en campos

@admin.register(ItemVenta)
class ItemVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'subtotal')  # Campos a mostrar en la lista de registros
