from django.urls import path
from .views import inicio, login_inicio, login_view, logout_view, singup_view, modificar_p, producto_cocina, producto_libreros, producto_muebles, contacto, eliminar_producto, carrito, muestra_producto, perfil, form_agregar, editar_usuario, cambiar_contrasena, menu_admin, checkout, registrar_p, lista_usuarios, modificar_producto, registro_ventas, actualizarProducto, procesarCompra,post_editar_usuario

urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login_inicio, name='login_inicio'), 
    path('logout/', logout_view, name='logout'), 
    path('login_view/', login_view, name='login_view'), 
    path('registro/', singup_view, name="registro"),
    path('cocina/', producto_cocina, name="cocina"),
    path('libreros/', producto_libreros, name="libreros"),
    path('muebles/', producto_muebles, name="muebles"),
    path('contacto/', contacto, name="contacto"),
    path('carrito/', carrito, name="carrito"),
    path('checkout/', checkout, name="checkout"),
    path('muestra_producto/<int:id>', muestra_producto, name="muestra_producto"),
    path('perfil/', perfil, name="perfil"),
    path('editar_perfil/', editar_usuario, name="editar_perfil"),
    path('cambiar_contrasena/', cambiar_contrasena, name="cambiar_contrasena"),
    path('menu_admin/', menu_admin, name="menu_admin"),
    path('form_agregar/', form_agregar, name="form_agregar"),
    path('registrar_p/', registrar_p, name="registrar_p"),
    path('lista_usuarios/', lista_usuarios, name="lista_usuarios"),
    path('modificar_producto/<int:id>', modificar_producto, name="modificar_producto"),
    path('modificar_p/', modificar_p, name="modificar_p"),
    path('eliminar_producto/<int:id>', eliminar_producto, name="eliminar_producto"),
    path('ventas/', registro_ventas, name="registro_ventas"),
    path('actualizar_producto/', actualizarProducto, name="actualizarProducto"),
    path('procesar_compra/', procesarCompra, name="procesarCompra"),
    path('post_editar_usuario/', post_editar_usuario, name="post_editar_usuario"),
]