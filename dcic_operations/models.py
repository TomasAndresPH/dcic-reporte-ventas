from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone  
    
class TarifaMercadoLibre(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Tarifa Mercado Libre")
    limite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Límite de la Tarifa")
    valor = models.IntegerField(verbose_name="Valor de la Tarifa (en CLP)")
    
    class Meta:
        verbose_name = "Tarifa Mercado Libre"
        verbose_name_plural = "Tarifas Mercado Libre"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} - Límite: {self.limite} CLP - Valor: {self.valor} CLP"
    
class TarifaRipley(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=100, unique=False, verbose_name="Nombre de la Tarifa Ripley")
    clase_logistica = models.CharField(max_length=100, null=True, blank=True, verbose_name="Clase Logística (Ripley)")
    medida_limite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Límite de la Tarifa")
    valor = models.IntegerField(verbose_name="Valor de la Tarifa (en CLP)")
    tramo_limite = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tramo de la Tarifa (en CLP)")
    
    class Meta:
        verbose_name = "Tarifa Ripley"
        verbose_name_plural = "Tarifas Ripley"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} - Límite: {self.limite} CLP - Valor: {self.valor} CLP"

class TarifaWalmart(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=100, unique=False, verbose_name="Nombre de la Tarifa Walmart")
    medida_limite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Límite de la Tarifa")
    tramo_limite = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tramo de la Tarifa (en CLP)")
    valor = models.IntegerField(verbose_name="Valor de la Tarifa (en CLP)")
    
    class Meta:
        verbose_name = "Tarifa Walmart"
        verbose_name_plural = "Tarifas Walmart"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} - Tramo Límite: {self.tramo_limite} CLP - Valor: {self.valor} CLP"
    
class TarifaParisOld(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=150, null=True, blank=True, verbose_name="Nombre de la Clase Logística")
    medida_limite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Límite de la Tarifa")
    reputacion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Reputación (Paris)")
    tramo_limite = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tramo de la Tarifa (en CLP)")
    valor = models.IntegerField(verbose_name="Valor de la Tarifa (en CLP)")
    
    class Meta:
        verbose_name = "Tarifa Paris"
        verbose_name_plural = "Tarifas Paris"
        ordering = ['medida_limite']
    
    def __str__(self):
        return f"{self.nombre} - Límite: {self.limite} CLP - Valor: {self.valor} CLP"
    
class TarifaParisNew(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=150, null=True, blank=True, verbose_name="Nombre de la Clase Logística")
    medida_limite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Límite de la Tarifa")
    reputacion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Reputación (Paris)")
    tramo_limite = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tramo de la Tarifa (en CLP)")
    valor = models.IntegerField(verbose_name="Valor de la Tarifa (en CLP)")
    
    class Meta:
        verbose_name = "Tarifa Paris"
        verbose_name_plural = "Tarifas Paris"
        ordering = ['medida_limite']
    
    def __str__(self):
        return f"{self.nombre} - Límite: {self.limite} CLP - Valor: {self.valor} CLP"
    
class TarifaFalabella(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=100, unique=False, verbose_name="Nombre de la Tarifa Falabella")
    clase_logistica = models.CharField(max_length=100, null=True, blank=True, verbose_name="Clase Logística (Falabella)")
    kg = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Límite de la Tarifa (en kg)")
    m3 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Límite de la Tarifa (en m³)")
    cm = models.IntegerField(verbose_name="Límite de la Tarifa (en cm)")
    tramo_limite = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tramo de la Tarifa (en CLP)")
    reputacion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Reputación (Falabella)")
    valor = models.IntegerField(verbose_name="Valor de la Tarifa (en CLP)")
    
    class Meta:
        verbose_name = "Tarifa Falabella"
        verbose_name_plural = "Tarifas Falabella"
        ordering = ['clase_logistica'] # Importante para la lógica de selección
    
    def __str__(self):
        return f"{self.nombre} (Clase: {self.clase_logistica}) - Kg: {self.kg}, m3: {self.m3}, cm: {self.cm}"
    
class TarifaFalabellaNew(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=100, unique=False, verbose_name="Nombre de la Tarifa Falabella")
    clase_logistica = models.CharField(max_length=100, null=True, blank=True, verbose_name="Clase Logística (Falabella)")
    kg = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Límite de la Tarifa (en kg)")
    m3 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Límite de la Tarifa (en m³)")
    cm = models.IntegerField(verbose_name="Límite de la Tarifa (en cm)")
    tramo_limite = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tramo de la Tarifa (en CLP)")
    reputacion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Reputación (Falabella)")
    valor = models.IntegerField(verbose_name="Valor de la Tarifa (en CLP)")
    
    class Meta:
        verbose_name = "Tarifa Falabella"
        verbose_name_plural = "Tarifas Falabella"
        ordering = ['clase_logistica'] # Importante para la lógica de selección
    
    def __str__(self):
        return f"{self.nombre} (Clase: {self.clase_logistica}) - Kg: {self.kg}, m3: {self.m3}, cm: {self.cm}"

class TarifaFalabellaFull(models.Model):
    
    nombre = models.CharField(
        max_length=20,
        verbose_name="Nombre del Tramo de Peso",
        help_text="Ej: '0-1kg', '1-2kg', etc."
    )
    clase_logistica = models.IntegerField(
        verbose_name="Clase Logística (1-21)"
    )
    kg_limite = models.DecimalField(
        max_digits=8, decimal_places=2,
        verbose_name="Límite Superior en kg",
        help_text="Ej: 1, 2, 3, 6, 10..."
    )
    tramo_limite = models.CharField(
        max_length=20,
        choices=[('Tramo Menor', 'Menor a $19.990'), ('Tramo Mayor', 'Mayor o igual a $19.990')],
        verbose_name="Tramo de Precio de Venta"
    )
    reputacion = models.CharField(
        max_length=5,
        choices=[('5', '5/5'), ('4', '4/5'), ('3', '3/5'), ('2', '2/5')],
        verbose_name="Reputación del Seller"
    )
    valor = models.IntegerField(
        verbose_name="Valor de la Tarifa (en CLP)"
    )

    class Meta:
        verbose_name = "Tarifa Falabella Full (Fulfillment)"
        verbose_name_plural = "Tarifas Falabella Full (Fulfillment)"
        ordering = ['clase_logistica', 'tramo_limite', 'reputacion']
        unique_together = [['clase_logistica', 'tramo_limite', 'reputacion']]

    def __str__(self):
        return f"{self.nombre} (Clase {self.clase_logistica}) | {self.tramo_limite} | Rep {self.reputacion}/5 → ${self.valor}"
        
class TarifaFalabellaColecta(models.Model):
    
    nombre = models.CharField(
        max_length=20,
        verbose_name="Nombre del Tramo de Peso",
        help_text="Ej: '0-1kg', '1-2kg', etc."
    )
    clase_logistica = models.IntegerField(
        verbose_name="Clase Logística (1-21)"
    )
    kg_limite = models.DecimalField(
        max_digits=8, decimal_places=2,
        verbose_name="Límite Superior en kg",
        help_text="Ej: 1, 2, 3, 6, 10..."
    )
    tramo_limite = models.CharField(
        max_length=20,
        choices=[('Tramo Menor', 'Menor a $19.990'), ('Tramo Mayor', 'Mayor o igual a $19.990')],
        verbose_name="Tramo de Precio de Venta"
    )
    reputacion = models.CharField(
        max_length=5,
        choices=[('5', '5/5'), ('4', '4/5'), ('3', '3/5'), ('2', '2/5')],
        verbose_name="Reputación del Seller"
    )
    valor = models.IntegerField(
        verbose_name="Valor de la Tarifa (en CLP)"
    )

    class Meta:
        verbose_name = "Tarifa Falabella Colecta"
        verbose_name_plural = "Tarifas Falabella Colecta"
        ordering = ['clase_logistica', 'tramo_limite', 'reputacion']
        unique_together = [['clase_logistica', 'tramo_limite', 'reputacion']]

    def __str__(self):
        return f"{self.nombre} (Clase {self.clase_logistica}) | {self.tramo_limite} | Rep {self.reputacion}/5 → ${self.valor}"
    
# Marcas
class Marcas(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Marca")
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    


class PuertoSalida(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=255, unique=True, verbose_name="Nombre del Puerto")

    class Meta:
        verbose_name = "Puerto de Salida"
        verbose_name_plural = "Puertos de Salida"

    def __str__(self):
        return self.nombre
# Proveedor y Puerto de Salida
class Proveedor(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=255, unique=True, verbose_name="Nombre del Proveedor")
    condiciones_pago = models.TextField(null=True, blank=True, verbose_name="Condiciones de Pago")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre

# --- Tablas de Medidas ---

class MedidasCajaMaster(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    alto = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    ancho = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    largo = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    volumen = models.DecimalField(max_digits=14, decimal_places=8, null=True, blank=True) # m³ quizás?
    peso_neto = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True) # kg?
    peso_bruto = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True) # kg?
    unidades_por_caja = models.IntegerField(null=True, blank=True)
    
    producto = models.ForeignKey(
        'Producto', # Apunta al modelo Producto
        on_delete=models.CASCADE, # Si se borra el producto, se borran sus cajas master asociadas. ¡Es lo lógico!
        related_name='medidas_cajas_master', # MUY IMPORTANTE: Nos permitirá hacer `producto.medidas_cajas_master.all()`
        verbose_name="Producto Asociado",
        null=True, blank=True # Puede ser útil si se crean medidas antes de asociarlas
    )

    class Meta:
        verbose_name = "Medida Caja Master" # Singular
        verbose_name_plural = "Medidas Cajas Master"

    def __str__(self):
        if self.producto:
            return f"Caja Master para SKU: {self.producto.sku} (Bulto {self.unidades_por_bulto or 'N/A'})"
        return f"Caja Master ID: {self.id}"

class MedidasCajaProducto(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    alto_hight_cm = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Alto (cm)")
    ancho_wide_cm = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Ancho (cm)")
    largo_length_cm = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Largo (cm)")
    volumen_m3 = models.DecimalField(max_digits=40, decimal_places=24, null=True, blank=True, verbose_name="Volumen (m³)")
    peso_neto_net_weight = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Peso Neto (kg)")
    peso_bruto_gross_weight = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Peso Bruto (kg)")
    unidades_por_bulto = models.IntegerField(null=True, blank=True)

    # NUEVOS CAMPOS CALCULADOS
    h_w_l_4000 = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Alto*Ancho*Largo/4000")
    peso_volumetrico_volumetric_weight = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Peso Volumétrico (kg)")
    max_l = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="Dimensión Máxima (cm)")
    
    t_falabella = models.CharField(max_length=100, null=True, blank=True, verbose_name="Clasificación Tarifa Falabella")
    t_falabella_cl = models.CharField(max_length=100, null=True, blank=True, verbose_name="Clasificación Tarifa Falabella Full")
    t_paris = models.CharField(max_length=100, null=True, blank=True, verbose_name="Clasificación Tarifa Paris")
    t_mercadolibre = models.CharField(max_length=100, null=True, blank=True, verbose_name="Clasificación Tarifa MercadoLibre")
    t_ripley = models.CharField(max_length=100, null=True, blank=True, verbose_name="Clasificación Tarifa Ripley")
    t_walmart = models.CharField(max_length=100, null=True, blank=True, verbose_name="Clasificación Tarifa Walmart")

    class Meta:
        verbose_name = "Medidas Caja Producto"
        verbose_name_plural = "Medidas Cajas Producto"

    def __str__(self):
        # Intenta obtener el SKU del producto asociado para un __str__ más informativo
        # Usamos try-except porque 'productos_caja' podría no estar poblado o el producto borrado.
        try:
            # El related_name es 'productos_caja' en el modelo Producto
            producto_asociado = self.productos_caja.first() 
            if producto_asociado:
                return f"Medidas Caja para SKU: {producto_asociado.sku}"
        except AttributeError: # Si 'productos_caja' no existe (ej. antes de guardar relación)
            pass
        return f"Medidas Caja Producto ID: {self.id}"

class MedidasProductoArmado(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    alto = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    ancho = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    largo = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    volumen = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    peso_neto = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    peso_bruto = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

    class Meta:
        verbose_name = "Medidas Producto Armado"
        verbose_name_plural = "Medidas Productos Armados"

    def __str__(self):
        return f"Producto Armado ID: {self.id}"

# --- Tabla Principal de Productos ---

class Producto(models.Model):
    sku = models.CharField(max_length=100, primary_key=True, verbose_name="SKU")
    categoria_principal = models.CharField(max_length=100, null=True, blank=True, verbose_name="Categoría Principal")
    subcategoria = models.CharField(max_length=100, null=True, blank=True, verbose_name="Subcategoría")
    tipo_producto = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tipo de Producto")
    proveedor_nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nombre Proveedor (Texto)")
    ean_nuevo = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    ean_antiguo = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    desc_corta = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción Corta")
    garantia = models.CharField(max_length=255, null=True, blank=True)
    validacion_jordi = models.CharField(max_length=50, null=True, blank=True)
    invoice = models.CharField(max_length=100, null=True, blank=True)
    fecha_medicion = models.DateField(null=True, blank=True, verbose_name="Fecha Medición")
    moq = models.IntegerField(null=True, blank=True, verbose_name="Minima Cantidad para la Orden de Compra (MOQ)")
    tipo = models.CharField(max_length=50, null=True, blank=True)
    tiempo_fabricacion = models.IntegerField(null=True, blank=True, verbose_name="Tiempo de Fabricación (días)")
    hecho_en = models.CharField(max_length=100, null=True, blank=True)
    incluye = models.TextField(null=True, blank=True)
    req_armado = models.CharField(max_length=50, null=True, blank=True, verbose_name="Requiere Armado")
    req_montaje = models.BooleanField(default=False, verbose_name="Requiere Montaje")
    producto_electrico = models.BooleanField(default=False, verbose_name="Producto Eléctrico")
    foto = models.URLField(max_length=500, null=True, blank=True)   
    color = models.CharField(max_length=50, null=True, blank=True)
    material = models.CharField(max_length=100, null=True, blank=True)
    usa_pilas = models.CharField(max_length=50, null=True, blank=True)
    rango_edad = models.CharField(max_length=50, null=True, blank=True)
    manual_espanol = models.CharField(max_length=50, null=True, blank=True, verbose_name="Manual en Español")
    estacionalidad = models.CharField(max_length=50, null=True, blank=True)
    multibulto_prop = models.BooleanField(default=False, verbose_name="¿Es Multibulto?")
    bigbulto_prop = models.BooleanField(default=False, verbose_name="¿Es BigBulto?")
    qty_multibulto = models.IntegerField(null=True, blank=True, verbose_name="Cantidad de Bultos")
    
    # Meses como IntegerField, pueden ser null.
    mes_inicio = models.IntegerField(null=True, blank=True, verbose_name="Mes Inicio")
    mes_final = models.IntegerField(null=True, blank=True, verbose_name="Mes Final")
    mes_compra = models.IntegerField(null=True, blank=True, verbose_name="Mes Compra")
    
    observacion = models.TextField(null=True, blank=True, verbose_name="Observación")

    comentario_mv = models.TextField(null=True, blank=True, verbose_name="Comentario")

    # Foreign Keys
    marca = models.ForeignKey(
        'Marcas',
        on_delete=models.SET_NULL, # O la política que prefieras
        null=True,
        blank=True,
        verbose_name="Marca (FK)"
    )
    caja_producto = models.ForeignKey(
        MedidasCajaProducto, 
        on_delete=models.SET_NULL, # Si se borran las medidas, el producto no se borra, pero el campo queda null.
                                     # Considera models.PROTECT si no quieres que se borren medidas si un producto las usa.
                                     # O models.CASCADE si al borrar producto se borran sus medidas (si no son compartidas).
                                     # SET_NULL parece razonable aquí.
        null=True, blank=True, 
        related_name='productos_caja', # Permite acceder desde MedidasCajaProducto.productos_caja.all()
        verbose_name="Medidas Caja Producto"
    )
    producto_armado = models.ForeignKey(
        MedidasProductoArmado, 
        on_delete=models.SET_NULL, 
        null=True, blank=True, 
        related_name='productos_armado', 
        verbose_name="Medidas Producto Armado"
    )
    proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.PROTECT, # Evita borrar proveedor si tiene productos asociados
        null=True, blank=True, 
        related_name='productos', 
        verbose_name="Proveedor (FK)"
    )
    puerto_salida = models.ForeignKey(
        PuertoSalida, 
        on_delete=models.SET_NULL, 
        null=True, blank=True, 
        related_name='productos', 
        verbose_name="Puerto de Salida"
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['sku']

    def __str__(self):
        return f"{self.sku} - {self.desc_corta or self.marca or 'Producto sin descripción/marca'}"
    
class ComentarioSku(models.Model):
    sku = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='comentarios_mv',
        db_column='sku',
        to_field='sku',
    )
    texto = models.TextField(verbose_name='Comentario')
    usuario = models.CharField(max_length=150, verbose_name='Usuario')
    fecha = models.DateTimeField(default=timezone.now, verbose_name='Fecha')

    class Meta:
        db_table = 'dcic_operations_comentariosku'
        ordering = ['-fecha']
        verbose_name = 'Comentario SKU'

class ForecastSku(models.Model):
    sku = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='forecasts',
        db_column='sku',
        to_field='sku',
    )
    mes = models.IntegerField(verbose_name='Mes')        # 1–12
    anio = models.IntegerField(verbose_name='Año')
    cantidad = models.IntegerField(default=0, verbose_name='Forecast Cantidad')
    usuario = models.CharField(max_length=150, verbose_name='Modificado por')
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dcic_operations_forecastsku'
        unique_together = [('sku', 'mes', 'anio')]
        verbose_name = 'Forecast SKU'

class PrecioSku(models.Model):
    sku = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='precios',
        db_column='sku',
        to_field='sku',
    )
    canal = models.CharField(max_length=100, verbose_name='Canal')  # 'falabella' | 'mercadolibre' | 'shopify'
    precio = models.IntegerField(default=0, verbose_name='Precio CLP')
    usuario = models.CharField(max_length=150, verbose_name='Modificado por')
    fecha_modificacion = models.DateTimeField(auto_now=True)

    # Historial — cada cambio genera una fila acá
    class Meta:
        db_table = 'dcic_operations_preciosku'
        unique_together = [('sku', 'canal')]  # ← esto genera el constraint
        ordering = ['-fecha_modificacion']

class PrecioSkuHistorial(models.Model):
    sku = models.CharField(max_length=100)
    canal = models.CharField(max_length=100)
    precio_anterior = models.IntegerField()
    precio_nuevo = models.IntegerField()
    usuario = models.CharField(max_length=150)
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'dcic_operations_preciosku_historial'
        ordering = ['-fecha']
        verbose_name = 'Historial Precio SKU'

class Bodega(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Bodega")

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Stock(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    producto = models.ForeignKey(
        Producto,
        to_field='sku',
        on_delete=models.CASCADE, # Si se borra el producto, se borra su stock.
        related_name='stock_items', # Permite acceder desde un producto: producto.stock_items.all()
        verbose_name="Producto (SKU)"
    )
    stock_disponible = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)], # Evita que el stock sea negativo a nivel de BD.
        verbose_name="Stock Disponible"
    )
    costo_unitario_neto = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True, # Puede que no se conozca el costo al inicio.
        blank=True,
        verbose_name="Costo Unitario Neto"
    )
    bodega = models.ForeignKey(
        Bodega,
        on_delete=models.PROTECT, # No permite borrar una bodega si tiene stock asociado.
        related_name='stock_items', # Permite acceder desde una bodega: bodega.stock_items.all()
        verbose_name="Bodega"
    )
    fecha_eta = models.DateField(null=True, blank=True, verbose_name="Fecha Estimada de Llegada (ETA)")
    
    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stock"
        # Esta restricción asegura que solo haya una entrada de stock
        # para una combinación única de producto y bodega.
        unique_together = ('producto', 'bodega')
        ordering = ['producto__sku', 'bodega__nombre']

    def __str__(self):
        return f"{self.producto.sku} en {self.bodega.nombre}: {self.stock_disponible} unidades"

class ProformaLote(models.Model):
    producto = models.ForeignKey(
        Producto,
        to_field='sku',
        on_delete=models.CASCADE,
        related_name='proforma_lotes',
        verbose_name="Producto (SKU)"
    )
    cantidad = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Cantidad"
    )
    fecha_eta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha Estimada de Llegada (ETA)"
    )

    class Meta:
        verbose_name = "Lote Proforma"
        verbose_name_plural = "Lotes Proforma"
        ordering = ['fecha_eta', 'producto__sku']
        db_table = 'dcic_operations_proforma_lote'

    def __str__(self):
        fecha = self.fecha_eta.strftime('%d/%m/%Y') if self.fecha_eta else 'Sin ETA'
        return f"{self.producto.sku} — {self.cantidad} uds — {fecha}"
# --- Sistema de Canales (Venta y Envío) ---

class Canal(models.Model): # Representará a un Usuario de Bsale como Canal de Venta
    id = models.IntegerField(primary_key=True, verbose_name="ID Usuario Bsale") # ID de Bsale es la PK
    nombre = models.CharField(max_length=255, verbose_name="Nombre Completo (Vendedor Bsale)") # firstName + lastName

    class Meta:
        verbose_name = "Canal de Venta"
        verbose_name_plural = "Canales de Venta"
        ordering = ['nombre'] # Opcional, para ordenar por nombre

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"
    
class Tienda(models.Model): # Representará a una tienda física o virtual
    id = models.IntegerField(primary_key=True, verbose_name="ID Tienda") # ID de Bsale es la PK
    nombre = models.CharField(max_length=255, verbose_name="Nombre Tienda") # Nombre de la tienda
    
    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"
    
class TipoDocumento(models.Model): # Representará los tipos de documentos (Factura, Boleta, etc.)
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Tipo de Documento") # Ej: "Factura", "Boleta"
    
    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documentos"
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre
    

class CanalEnvio(models.Model): # Canal de ENVÍO (Transportista/Método)
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre Canal Envío")
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Canal de Envío"
        verbose_name_plural = "Canales de Envío"

    def __str__(self):
        return self.nombre

# --- Tablas para Cálculo de Costo de Envío ---

class TamanoEnvio(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    canal_envio = models.ForeignKey(CanalEnvio, on_delete=models.CASCADE, related_name='tamanos_envio', verbose_name="Canal de Envío")
    codigo = models.CharField(max_length=20, verbose_name="Código Tamaño") # Ej: XS, S, M
    desde_kg = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    hasta_kg = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = "Tamaño de Envío"
        verbose_name_plural = "Tamaños de Envío"
        # Asegura que no haya códigos duplicados para el mismo canal
        unique_together = ('canal_envio', 'codigo')
        ordering = ['canal_envio', 'desde_kg']

    def __str__(self):
        return f"{self.canal_envio.nombre} - {self.codigo} ({self.desde_kg}kg - {self.hasta_kg}kg)"

class RangoPrecio(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    canal_envio = models.ForeignKey(CanalEnvio, on_delete=models.CASCADE, related_name='rangos_precio', verbose_name="Canal de Envío")
    desde_precio = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Precio Producto Desde")
    hasta_precio = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Precio Producto Hasta")
    descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Rango de Precio (para Tarifa Envío)"
        verbose_name_plural = "Rangos de Precios (para Tarifas Envío)"
        ordering = ['canal_envio', 'desde_precio']

    def __str__(self):
        return f"{self.canal_envio.nombre} - Precio: ${self.desde_precio} - ${self.hasta_precio}"

class TarifaEnvio(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    canal_envio = models.ForeignKey(CanalEnvio, on_delete=models.CASCADE, related_name='tarifas', verbose_name="Canal de Envío")
    tamano = models.ForeignKey(TamanoEnvio, on_delete=models.CASCADE, related_name='tarifas', verbose_name="Tamaño")
    # El rango de precio puede ser opcional si algunas tarifas solo dependen del tamaño/peso
    rango_precio = models.ForeignKey(RangoPrecio, on_delete=models.CASCADE, null=True, blank=True, related_name='tarifas', verbose_name="Rango de Precio Producto")
    costo = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Costo Envío")

    class Meta:
        verbose_name = "Tarifa de Envío"
        verbose_name_plural = "Tarifas de Envío"
        # Evita duplicados exactos de tarifas
        unique_together = ('canal_envio', 'tamano', 'rango_precio')
        ordering = ['canal_envio', 'tamano', 'rango_precio']

    def __str__(self):
        rango_str = f" - Rango: {self.rango_precio.id}" if self.rango_precio else ""
        return f"Tarifa {self.canal_envio.nombre} - Tam: {self.tamano.codigo}{rango_str} = ${self.costo}"

# --- Tabla de Ventas ---

# Modelo placeholder para Cliente si no lo tienes definido
class Cliente(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    rut = models.CharField(max_length=20, unique=True, db_index=True, verbose_name="RUT Cliente") # Nuevo campo para el RUT
    nombre_completo = models.CharField(max_length=255, verbose_name="Nombre Completo") # Para nombre + apellido
    email = models.EmailField(null=True, blank=True)
    # Otros campos que podrías querer de Bsale en el futuro:
    # bsale_client_id = models.IntegerField(null=True, blank=True, unique=True, help_text="ID del cliente en Bsale")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre_completo} ({self.rut})"

# Modelo placeholder para TipoDespacho si no lo tienes definido
class TipoDespacho(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
# --- Modelo de Ventas Bsale ---
class GlosaBsale(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    codigo = models.CharField(max_length=100, unique=True, verbose_name="Glosa")
    monto_neto_servicio_contratado = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Monto Total")
    desc_corta = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción Corta")

    class Meta:
        verbose_name = "Glosa Bsale"
        verbose_name_plural = "Glosas Bsale"

    def __str__(self):
        return self.codigo if self.codigo else f"Glosa ID: {self.id}"


class VentaBsale(models.Model):
    # Campos de nivel de Documento
    tipo_doc = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Documento")
    codesii = models.CharField(max_length=50, null=True, blank=True, verbose_name="Código SII")
    filtro = models.CharField(max_length=100, null=True, blank=True)
    origen = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(db_index=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cliente")
    canal = models.ForeignKey(
        Canal, 
        on_delete=models.PROTECT, 
        related_name='ventas_bsale_directas', # <-- CAMBIO AQUÍ: Nombre único para la relación inversa
        verbose_name="Usuario Bsale (Vendedor)"
    )
    n_pedido = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name="Nº Pedido/Documento")
    n_orden = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Orden")
    
    # --- Estructura de Línea de Venta ---
    TIPO_LINEA_CHOICES = [
        ('PRODUCTO', 'Producto'),
        ('SERVICIO', 'Servicio/Glosa'),
    ]
    tipo_linea = models.CharField(max_length=20, choices=TIPO_LINEA_CHOICES, default='PRODUCTO', verbose_name="Tipo de Línea")

    sku = models.ForeignKey(
        Producto,
        to_field='sku',
        on_delete=models.PROTECT,
        related_name='ventasBsale', # <-- CAMBIO AQUÍ: Nombre único
        verbose_name="Producto (SKU)",
        null=True,
        blank=True
    )
    
    glosa_codigo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Código de Servicio/Glosa")
    glosa_descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción de Servicio/Glosa")

    # Campos de valores de la línea
    cantidad = models.IntegerField(default=1)
    venta_total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_neto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Neto Unitario")
    total_neto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Total Neto de Línea")
    
    # Campos a nivel de documento o línea
    estado_orden = models.CharField(max_length=100, null=True, blank=True)
    tipo_despacho = models.ForeignKey(TipoDespacho, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Despacho")
    costo_envio = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Envío (Obsoleto, usar línea de servicio)")
    canales_envio = models.ForeignKey(
        CanalEnvio, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        related_name='ventas_enviadas', # <-- CAMBIO AQUÍ: Nombre único
        verbose_name="Canal de Envío Utilizado"
    )

    # Campos de costos y rentabilidad (solo para PRODUCTOS)
    costo_bsale = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    c_costo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Total Calculado")
    porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="% Comisión Calculado")
    c_comision_clp_neta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Comisión CLP Neta Calculada")
    c_valor_cobrado = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Cobrado Calculado")
    c_margen_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen CLP Calculado")
    c_margen_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen % Calculado")
    
    # Campos de fecha
    n_semana = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Semana")
    mes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mes")
    año = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Línea de Venta Bsale"
        verbose_name_plural = "Líneas de Venta Bsale"
        ordering = ['-fecha', '-id']

    def __str__(self):
        item_id = self.sku.sku if self.sku else self.glosa_codigo or "N/A"
        return f"Línea Venta: {self.n_pedido} - Ítem: {item_id}"

    def clean(self):
        if self.tipo_linea == 'PRODUCTO' and not self.sku:
            raise ValidationError('Una línea de tipo "Producto" debe tener un SKU asociado.')
        if self.tipo_linea == 'SERVICIO' and self.sku:
            raise ValidationError('Una línea de tipo "Servicio" no debe tener un SKU asociado.')
        if self.tipo_linea == 'SERVICIO' and not self.glosa_codigo:
            raise ValidationError('Una línea de tipo "Servicio" debe tener un "Código de Servicio/Glosa".')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
class VentaBsaleTESTING(models.Model):
    # Campos de nivel de Documento
    tipo_doc = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Documento")
    codesii = models.CharField(max_length=50, null=True, blank=True, verbose_name="Código SII")
    filtro = models.CharField(max_length=100, null=True, blank=True)
    origen = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(db_index=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cliente")
    canal = models.ForeignKey(Canal, on_delete=models.PROTECT, related_name='ventas_bsale_directas_testing', verbose_name="Usuario Bsale (Vendedor)")
    n_pedido = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name="Nº Pedido/Documento")
    n_orden = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Orden")
    
    # --- INICIO DE CAMBIOS IMPORTANTES ---

    # 1. Campo para diferenciar el tipo de línea
    TIPO_LINEA_CHOICES = [
        ('PRODUCTO', 'Producto'),
        ('SERVICIO', 'Servicio/Glosa'),
    ]
    tipo_linea = models.CharField(max_length=20, choices=TIPO_LINEA_CHOICES, default='PRODUCTO', verbose_name="Tipo de Línea")

    # 2. SKU ahora es opcional (puede ser nulo si es un servicio)
    sku = models.ForeignKey(
        Producto,
        to_field='sku',
        on_delete=models.PROTECT,
        related_name='ventasBsale_testing',
        verbose_name="Producto (SKU)",
        null=True,  # PERMITIR NULOS
        blank=True  # PERMITIR EN BLANCO
    )
    
    # 3. Campos para almacenar la info de la glosa directamente
    glosa_codigo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Código de Servicio/Glosa")
    glosa_descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción de Servicio/Glosa")


    # Campos de valores de la línea (comunes a productos y servicios)
    cantidad = models.IntegerField(default=1)
    venta_total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True) # Este parece ser el total con IVA
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True) # ¿Este es neto o con IVA?
    valor_neto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Neto Unitario") # Del JSON 'netUnitValue'
    total_neto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Total Neto de Línea") # Del JSON 'netAmount'
    
    # Campos que pueden aplicar a nivel de documento o línea
    estado_orden = models.CharField(max_length=100, null=True, blank=True)
    tipo_despacho = models.ForeignKey(TipoDespacho, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Despacho")
    costo_envio = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Envío (Obsoleto, usar línea de servicio)")
    canales_envio = models.ForeignKey(CanalEnvio, on_delete=models.PROTECT, null=True, blank=True, related_name='ventas_enviadas_testing', verbose_name="Canal de Envío Utilizado")

    # Campos de costos y rentabilidad (solo para PRODUCTOS)
    costo_bsale = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True) # Costo de Bsale si lo informa
    c_costo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Total Calculado")
    porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="% Comisión Calculado")
    c_comision_clp_neta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Comisión CLP Neta Calculada")
    c_valor_cobrado = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Cobrado Calculado")
    c_margen_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen CLP Calculado")
    c_margen_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen % Calculado")
    
    # Campos de fecha
    n_semana = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Semana")
    mes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mes")
    año = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Línea de Venta Bsale (Testing)"
        verbose_name_plural = "Líneas de Venta Bsale (Testing)"
        ordering = ['-fecha', '-id']
        # unique_together fue eliminado para mayor flexibilidad inicial. 
        # Se puede agregar luego: unique_together = ('n_pedido', 'sku', 'glosa_codigo')

    def __str__(self):
        item_id = self.sku.sku if self.sku else self.glosa_codigo or "N/A"
        return f"Línea Venta (T): {self.n_pedido} - Ítem: {item_id}"

    def clean(self):
        # Validación para asegurar la consistencia de los datos
        if self.tipo_linea == 'PRODUCTO' and not self.sku:
            raise ValidationError('Una línea de tipo "Producto" debe tener un SKU asociado.')
        if self.tipo_linea == 'SERVICIO' and self.sku:
            raise ValidationError('Una línea de tipo "Servicio" no debe tener un SKU asociado.')
        if self.tipo_linea == 'SERVICIO' and not self.glosa_codigo:
            raise ValidationError('Una línea de tipo "Servicio" debe tener un "Código de Servicio/Glosa".')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
# --- NUEVO MODELO PARA VENTAS DE MARKETPLACE ---
class VentaBsaleMKTP(models.Model):
    # Campos de nivel de Documento
    tipo_doc = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Documento")
    codesii = models.CharField(max_length=50, null=True, blank=True, verbose_name="Código SII")
    filtro = models.CharField(max_length=100, null=True, blank=True)
    origen = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(db_index=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cliente")
    canal = models.ForeignKey(
        Canal, 
        on_delete=models.PROTECT, 
        related_name='ventas_bsale_mktp', # <-- CAMBIO AQUÍ: Nombre único
        verbose_name="Usuario Bsale (Vendedor MKTP)"
    )
    n_pedido = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name="Nº Pedido/Documento")
    n_orden = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Orden")
    
    # --- Estructura de Línea de Venta ---
    TIPO_LINEA_CHOICES = [('PRODUCTO', 'Producto'), ('SERVICIO', 'Servicio/Glosa')]
    tipo_linea = models.CharField(max_length=20, choices=TIPO_LINEA_CHOICES, default='PRODUCTO', verbose_name="Tipo de Línea")

    sku = models.ForeignKey(
        Producto, 
        to_field='sku', 
        on_delete=models.PROTECT, 
        related_name='ventasBsaleMKTP', # <-- CAMBIO AQUÍ: Nombre único
        verbose_name="Producto (SKU)", 
        null=True, 
        blank=True
    )
    
    glosa_codigo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Código de Servicio/Glosa")
    glosa_descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción de Servicio/Glosa")

    # Campos de valores de la línea
    cantidad = models.IntegerField(default=1)
    venta_total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_neto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Neto Unitario")
    total_neto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Total Neto de Línea")
    
    # Otros campos
    costo_bsale = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    costo_envio = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Envío (Obsoleto, usar línea de servicio)")
    costo_fijo_ml = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Fijo Mercado Libre")
    estado_orden = models.CharField(max_length=100, null=True, blank=True)
    tipo_despacho = models.ForeignKey(TipoDespacho, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Despacho")
    canales_envio = models.ForeignKey(
        CanalEnvio, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        related_name='ventas_enviadas_bsale_mktp', # <-- CAMBIO AQUÍ: Nombre único
        verbose_name="Canal de Envío Utilizado"
    )

    # Campos de costos y rentabilidad (solo para PRODUCTOS)
    c_costo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Total Calculado")
    porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="% Comisión Calculado")
    c_comision_clp_neta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Comisión CLP Neta Calculada")
    c_valor_cobrado = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Cobrado Calculado")
    c_margen_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen CLP Calculado")
    c_margen_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen % Calculado")
    
    # Campos de fecha
    n_semana = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Semana")
    mes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mes")
    año = models.IntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Línea de Venta Bsale MKTP"
        verbose_name_plural = "Líneas de Venta Bsale MKTP"
        ordering = ['-fecha', '-id']

    def __str__(self):
        item_id = self.sku.sku if self.sku else self.glosa_codigo or "N/A"
        return f"Línea Venta MKTP: {self.n_pedido} - Ítem: {item_id}"
    
    def clean(self):
        if self.tipo_linea == 'PRODUCTO' and not self.sku:
            raise ValidationError('Una línea de tipo "Producto" debe tener un SKU asociado.')
        if self.tipo_linea == 'SERVICIO' and self.sku:
            raise ValidationError('Una línea de tipo "Servicio" no debe tener un SKU asociado.')
        if self.tipo_linea == 'SERVICIO' and not self.glosa_codigo:
            raise ValidationError('Una línea de tipo "Servicio" debe tener un "Código de Servicio/Glosa".')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
class VentaBsaleMKTPTESTING(models.Model):
    # Campos de nivel de Documento
    tipo_doc = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Documento")
    codesii = models.CharField(max_length=50, null=True, blank=True, verbose_name="Código SII")
    filtro = models.CharField(max_length=100, null=True, blank=True)
    origen = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(db_index=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cliente")
    canal = models.ForeignKey(Canal, on_delete=models.PROTECT, related_name='ventas_bsale_mktp_testing', verbose_name="Usuario Bsale (Vendedor MKTP)")
    n_pedido = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name="Nº Pedido/Documento")
    n_orden = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Orden")
    
    # --- INICIO DE CAMBIOS IMPORTANTES ---
    TIPO_LINEA_CHOICES = [('PRODUCTO', 'Producto'), ('SERVICIO', 'Servicio/Glosa')]
    tipo_linea = models.CharField(max_length=20, choices=TIPO_LINEA_CHOICES, default='PRODUCTO', verbose_name="Tipo de Línea")

    sku = models.ForeignKey(Producto, to_field='sku', on_delete=models.PROTECT, related_name='ventasBsaleMKTP_testing', verbose_name="Producto (SKU)", null=True, blank=True)
    
    glosa_codigo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Código de Servicio/Glosa")
    glosa_descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción de Servicio/Glosa")
    # --- FIN DE CAMBIOS IMPORTANTES ---

    # Campos de valores de la línea
    cantidad = models.IntegerField(default=1)
    venta_total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_neto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Neto Unitario")
    total_neto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Total Neto de Línea")
    
    # Otros campos
    costo_bsale = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    costo_envio = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Envío (Obsoleto, usar línea de servicio)")
    costo_fijo_ml = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Fijo Mercado Libre")
    estado_orden = models.CharField(max_length=100, null=True, blank=True)
    tipo_despacho = models.ForeignKey(TipoDespacho, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Despacho")
    canales_envio = models.ForeignKey(CanalEnvio, on_delete=models.PROTECT, null=True, blank=True, related_name='ventas_enviadas_bsale_mktp_testing', verbose_name="Canal de Envío Utilizado")

    # Campos de costos y rentabilidad (solo para PRODUCTOS)
    c_costo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Total Calculado")
    porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="% Comisión Calculado")
    c_comision_clp_neta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Comisión CLP Neta Calculada")
    c_valor_cobrado = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Cobrado Calculado")
    c_margen_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen CLP Calculado")
    c_margen_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen % Calculado")
    
    # Campos de fecha
    n_semana = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Semana")
    mes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mes")
    año = models.IntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Línea de Venta Bsale MKTP (Testing)"
        verbose_name_plural = "Líneas de Venta Bsale MKTP (Testing)"
        ordering = ['-fecha', '-id']

    def __str__(self):
        item_id = self.sku.sku if self.sku else self.glosa_codigo or "N/A"
        return f"Línea Venta MKTP (T): {self.n_pedido} - Ítem: {item_id}"
    
    def clean(self):
        if self.tipo_linea == 'PRODUCTO' and not self.sku:
            raise ValidationError('Una línea de tipo "Producto" debe tener un SKU asociado.')
        if self.tipo_linea == 'SERVICIO' and self.sku:
            raise ValidationError('Una línea de tipo "Servicio" no debe tener un SKU asociado.')
        if self.tipo_linea == 'SERVICIO' and not self.glosa_codigo:
            raise ValidationError('Una línea de tipo "Servicio" debe tener un "Código de Servicio/Glosa".')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    

class NotasCredito(models.Model):
    bsale_detail_id = models.BigIntegerField(unique=True, verbose_name="ID Detalle Ítem Bsale NC") # Este es details.items[n].id
    
    # Campos que describen la Nota de Crédito a la que pertenece este ítem
    bsale_nc_document_id = models.BigIntegerField(null=True, blank=True, db_index=True, verbose_name="ID Documento NC Bsale") # Este es items[0].id
    n_nota_credito = models.CharField(max_length=100, db_index=True, verbose_name="Número de Nota de Crédito") # Este es items[0].number

    # Campos del ítem específico
    doc_referencia = models.CharField(max_length=100, verbose_name="Documento al que hace referencia")
    sku = models.ForeignKey(Producto, to_field='sku', null=True, blank=True, on_delete=models.PROTECT, related_name='notas_credito_items', verbose_name="SKU Producto")
    glosa = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción Glosa")
    cantidad = models.IntegerField(default=1, verbose_name="Cantidad")
    fecha_emision = models.DateField(verbose_name="Fecha de Emisión NC") # Fecha de la NC general
    monto_neto_unitario = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto Neto Unitario Ítem")
    monto_neto_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto Neto Total Ítem")
    monto_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto Total Ítem con IVA")
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Documento Referenciado")
    año = models.IntegerField(null=True, blank=True, verbose_name="Año de Emisión")
    mes = models.CharField(max_length=20, null=True, blank=True, verbose_name="Mes de Emisión") # Ej: "Enero", "Febrero", etc.
    n_semana = models.CharField(max_length=20, null=True, blank=True, verbose_name="Número de Semana") # Ej: 23-25
    tipo = models.CharField(max_length=50, null=True, blank=True, verbose_name="Tipo de Nota de Crédito") # Ej: "NC"
    class Meta:
        verbose_name = "Nota de Crédito"
        verbose_name_plural = "Notas de Crédito"
        ordering = ['-fecha_emision', '-n_nota_credito', 'bsale_detail_id']

    def __str__(self):
        item_desc = self.sku.sku if self.sku else self.glosa if self.glosa else f"Detalle Bsale {self.bsale_detail_id}"
        return f"Ítem NC {self.n_nota_credito} (BsaleDetID {self.bsale_detail_id}) - {item_desc} - Ref: {self.doc_referencia}"
    
    
class NotasCreditoCyber(models.Model):
    bsale_detail_id = models.BigIntegerField(unique=True, verbose_name="ID Detalle Ítem Bsale NC") # Este es details.items[n].id
    
    # Campos que describen la Nota de Crédito a la que pertenece este ítem
    bsale_nc_document_id = models.BigIntegerField(null=True, blank=True, db_index=True, verbose_name="ID Documento NC Bsale") # Este es items[0].id
    n_nota_credito = models.CharField(max_length=100, db_index=True, verbose_name="Número de Nota de Crédito") # Este es items[0].number

    # Campos del ítem específico
    doc_referencia = models.CharField(max_length=100, verbose_name="Documento al que hace referencia")
    sku = models.ForeignKey(Producto, to_field='sku', null=True, blank=True, on_delete=models.PROTECT, related_name='notas_credito_cyber_items', verbose_name="SKU Producto")
    glosa = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción Glosa")
    cantidad = models.IntegerField(default=1, verbose_name="Cantidad")
    fecha_emision = models.DateField(verbose_name="Fecha de Emisión NC") # Fecha de la NC general
    monto_neto_unitario = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto Neto Unitario Ítem")
    monto_neto_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto Neto Total Ítem")
    monto_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto Total Ítem con IVA")
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Documento Referenciado", related_name='notas_credito_cyber_tipo_documento')
    año = models.IntegerField(null=True, blank=True, verbose_name="Año de Emisión")
    mes = models.CharField(max_length=20, null=True, blank=True, verbose_name="Mes de Emisión") # Ej: "Enero", "Febrero", etc.
    n_semana = models.CharField(max_length=20, null=True, blank=True, verbose_name="Número de Semana") # Ej: 23-25
    tipo = models.CharField(max_length=50, null=True, blank=True, verbose_name="Tipo de Nota de Crédito") # Ej: "NC"
    class Meta:
        verbose_name = "Nota de Crédito Cyber"
        verbose_name_plural = "Notas de Crédito Cyber"
        ordering = ['-fecha_emision', '-n_nota_credito', 'bsale_detail_id']

    def __str__(self):
        item_desc = self.sku.sku if self.sku else self.glosa if self.glosa else f"Detalle Bsale {self.bsale_detail_id}"
        return f"Ítem NC Cyber {self.n_nota_credito} (BsaleDetID {self.bsale_detail_id}) - {item_desc} - Ref: {self.doc_referencia}"
class NotasDebito(models.Model):
    bsale_detail_id = models.BigIntegerField(unique=True, verbose_name="ID Detalle Ítem Bsale ND") # Este es details.items[n].id
    
    # Campos que describen la Nota de Débito a la que pertenece este ítem
    bsale_nd_document_id = models.BigIntegerField(null=True, blank=True, db_index=True, verbose_name="ID Documento ND Bsale") # Este es items[0].id
    n_nota_debito = models.CharField(max_length=100, db_index=True, verbose_name="Número de Nota de Débito") # Este es items[0].number

    # Campos del ítem específico
    doc_referencia = models.CharField(max_length=100, verbose_name="Documento al que hace referencia")
    sku = models.ForeignKey(Producto, to_field='sku', null=True, blank=True, on_delete=models.PROTECT, related_name='notas_debito_items', verbose_name="SKU Producto")
    glosa = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción Glosa")
    cantidad = models.IntegerField(default=1, verbose_name="Cantidad")
    fecha_emision = models.DateField(verbose_name="Fecha de Emisión ND") # Fecha de la ND general
    monto_neto_unitario = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto Neto Unitario Ítem")
    monto_neto_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto Neto Total Ítem")
    monto_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto Total Ítem con IVA")
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Documento Referenciado")
    año = models.IntegerField(null=True, blank=True, verbose_name="Año de Emisión")
    mes = models.CharField(max_length=20, null=True, blank=True, verbose_name="Mes de Emisión") # Ej: "Enero", "Febrero", etc.
    n_semana = models.CharField(max_length=20, null=True, blank=True, verbose_name="Número de Semana") # Ej: 23-25
    tipo = models.CharField(max_length=50, null=True, blank=True, verbose_name="Tipo de Nota de Débito") # Ej: "ND"
    class Meta:
        verbose_name = "Nota de Débito"
        verbose_name_plural = "Notas de Débito"
        ordering = ['-fecha_emision', '-n_nota_debito', 'bsale_detail_id']

    def __str__(self):
        item_desc = self.sku.sku if self.sku else self.glosa if self.glosa else f"Detalle Bsale {self.bsale_detail_id}"
        return f"Ítem ND {self.n_nota_debito} (BsaleDetID {self.bsale_detail_id}) - {item_desc} - Ref: {self.doc_referencia}"

    
    
class EstadoPago(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre del Estado de Pago")

    class Meta:
        verbose_name = "Estado de Pago (Wivo)"
        verbose_name_plural = "Estados de Pago (Wivo)"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class EstadoDespacho(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Estado de Despacho")

    class Meta:
        verbose_name = "Estado de Despacho (Wivo)"
        verbose_name_plural = "Estados de Despacho (Wivo)"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
class EstadoOrden(models.Model):
    # id = models.AutoField(primary_key=True) # Django lo añade automáticamente
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Estado de Orden")

    class Meta:
        verbose_name = "Estado de Orden (Wivo)"
        verbose_name_plural = "Estados de Orden (Wivo)"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# --- TABLA PRINCIPAL PARA DATOS DE WIVO (Marketplaces procesados) ---

class VentaWivo(models.Model):
    #------------------------------------------------------
    # CAMPOS FIJOS, PROVIENEN DIRECTAMENTE DEL JSON DE WIVO
    #------------------------------------------------------
    # "SKU Producto"
    sku = models.ForeignKey(Producto, to_field='sku', on_delete=models.PROTECT, related_name='ventas_wivo', verbose_name="SKU Producto")
    # "SKU Marketplace"
    sku_marketplace = models.CharField(max_length=100, null=True, blank=True, verbose_name="SKU Marketplace")
    # "Canal"
    canal = models.ForeignKey(Canal, on_delete=models.PROTECT, related_name='ventas_wivo', verbose_name="Canal de Venta (Marketplace)")
    # "Estado de Orden"
    estado_orden = models.ForeignKey(EstadoOrden, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas_wivo', verbose_name="Estado de Orden (FK)")
    # "Estado de Pago"
    estado_pago = models.ForeignKey(EstadoPago, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas_wivo', verbose_name="Estado de Pago (FK)")
    # "Fecha de Pago"
    fecha_pago = models.DateField(null=True, blank=True, verbose_name="Fecha de Pago")
    # "N° de Liquidación"
    n_liquidacion = models.CharField(max_length=100, null=True, blank=True, verbose_name="N° de Liquidación")
    # "Estado de Despacho"
    estado_despacho = models.ForeignKey(EstadoDespacho, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas_wivo', verbose_name="Estado de Despacho (FK)")
    # "Tipo de Despacho"
    tipo_despacho = models.ForeignKey(TipoDespacho, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas_wivo', verbose_name="Tipo de Despacho (FK)")
    # "Tipo de Despacho del Marketplace"
    tipo_despacho_marketplace = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tipo de Despacho del Marketplace")
    # "Nro. suborden"
    n_suborden = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nro. Sub Orden")
    # "Nro. Orden"
    n_orden = models.CharField(max_length=100, db_index=True, verbose_name="Nro. Orden")
    # "Fecha de compra"
    fecha_compra = models.DateField(verbose_name="Fecha de compra", db_index=True)
    
    # INGRESOS
    # "Ventas"
    ventas = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ventas")
    # "Ingreso por Envío Flex"
    ingreso_envio_flex = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingreso por Envío Flex")
    # "Ingreso de Compensación por Daños"
    ingreso_compensacion_danos = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingreso de Compensación por Daños")
    # "Ingreso Total"
    ingreso_total = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingreso Total")
    # "Despacho pagado por comprador"
    despacho_pagado_comprador = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Despacho pagado por comprador")
    # "Ingreso por promoción"
    ingreso_promocion = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingreso por promoción")
    # "Ingresos sin categorizar"
    ingresos_sin_categorizar = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingresos sin categorizar")
    # "Unidades"
    unidades = models.IntegerField(null=True, blank=True, verbose_name="Unidades")
    # "Costo de Comisiones"
    costo_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo de Comisiones")
    # "% Costo de Comisiones"
    porcentaje_costo_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo de Comisiones") # Formato XX.YY
    # "Costos por publicidad"
    costos_publicidad = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costos por publicidad")
    # "Costo Envío"
    costo_envio = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Envío")
    # "Rentabilidad Marketplace"
    rentabilidad_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Rentabilidad Marketplace")
    # "% Rentabilidad Marketplace"
    porcentaje_rentabilidad_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Rentabilidad Marketplace") # Formato XX.YY
    # "Costo Total" (del marketplace, según la columna del Excel)
    costo_total = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Total (del Marketplace)")
    # "Venta Cancelada" (valor)
    venta_cancelada = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Valor Venta Cancelada")
    # "Costo de Marketplace"
    costo_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo de Marketplace")
    # "% Costo de Marketplace"
    porcentaje_costo_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo de Marketplace") # Formato XX.YY

    # COBROS ESPECÍFICOS
    # "Cobro de Comisiones"
    cobro_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Comisiones")
    # "% Cobro de Comisiones"
    porcentaje_cobro_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Cobro de Comisiones") # Formato XX.YY
    # "% Costo de Publicidad"
    porcentaje_costo_publicidad = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo de Publicidad") # Formato XX.YY
    # "% Costo Envío"
    porcentaje_costo_envio = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo Envío") # Formato XX.YY
    # "Cobro por Costo Logístico"
    cobro_costo_logistico = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por Costo Logístico")
    # "Cobro de Penalizacion por Cancelación"
    cobro_penalizacion_cancelacion = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Penalizacion por Cancelación")
    # "Cobro Logística Inversa"
    cobro_logistica_inversa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro Logística Inversa")
    # "Cobro Envío Flex"
    cobro_envio_flex = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro Envío Flex")
    # "Cobro de Penalización por Daños"
    cobro_penalizacion_danos = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Penalización por Daños")
    # "Cobro Total"
    cobro_total = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro Total")
    # "Cobro de Ajuste sobre la Comisión"
    cobro_ajuste_sobre_comision = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Ajuste sobre la Comisión")
    # "% Costo Producto"
    porcentaje_costo_producto = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo Producto") # Formato XX.YY
    # "Cobro de Envío"
    cobro_envio = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Envío")
    # "Cobro por publicidad"
    cobro_publicidad = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por publicidad")
    # "Cobro por Servicio Almacenamiento"
    cobro_servicio_almacenamiento = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por Servicio Almacenamiento")
    # "Cobro por Almacenamiento Prolongado"
    cobro_almacenamiento_prolongado = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por Almacenamiento Prolongado")
    # "Cobro por Descarte de Stock"
    cobro_descarte_stock = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por Descarte de Stock")
    # "% Costo Total" (del marketplace)
    porcentaje_costo_total_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo Total (Marketplace)") # Formato XX.YY
    # "Cobros sin categorizar"
    cobros_sin_categorizar = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobros sin categorizar")

    # REEMBOLSOS
    # "Reembolso de Costo Logístico"
    reembolso_costo_logistico = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de Costo Logístico")
    # "Devolución de Penalización por Cancelación"
    devolucion_penalizacion_cancelacion = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Devolución de Penalización por Cancelación")
    # "Reembolso Logística Inversa"
    reembolso_logistica_inversa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso Logística Inversa")
    # "Reembolso de Ajuste sobre Venta"
    reembolso_ajuste_sobre_venta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de Ajuste sobre Venta")
    # "Reembolso de Comisiones"
    reembolso_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de Comisiones")
    # "Reembolso de envío"
    reembolso_envio = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de envío")
    # "Reembolso Total"
    reembolso_total = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso Total")
    # "Reembolso de Ajuste sobre la Comisión"
    reembolso_ajuste_sobre_comision = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de Ajuste sobre la Comisión")
    # "Reembolso por publicidad"
    reembolso_publicidad = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso por publicidad")
    # "Reembolsos sin categorizar"
    reembolsos_sin_categorizar = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolsos sin categorizar")
    # "Reembolso por servicio almacenamiento"
    reembolso_servicio_almacenamiento = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso por servicio almacenamiento")
    # "Reembolso por descarte de stock"
    reembolso_descarte_stock = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso por descarte de stock")
    # "Reembolso por almacenamiento prolongado"
    reembolso_almacenamiento_prolongado = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso por almacenamiento prolongado")
    
    #-------------------------------------------------------
    # VALORES CALCULADOS, QUE NO VIENEN DIRECTAMENTE DE WIVO
    #-------------------------------------------------------
    
    # campos derivados de la fecha_compra
    # n_semana ej: 23, 45, etc...
    n_semana = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Semana")
    # mes ej: 1, 2, 3, ..., 12
    mes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mes")
    # 2023, 2024, 2025, etc...
    año = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Año")
    
    # ventas / unidades
    cc_v_venta_bruta_uni = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Unitario Bruto")
    # cc_v_venta_bruta_uni / 1.19
    cc_v_venta_neta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Venta Neta Calculada")
    # cc_v_venta_neta * unidades
    cc_t_venta_neta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Total Venta Neta Calculada")
    
    # Otros Costos que se componen de: costos_publicidad
    cc_otros_costos = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Otros Costos")
    
    # Otros Ingresos que se componen de: ingreso_envio_flex + ingreso_compensacion_danos + ingreso_promocion + ingresos_sin_categorizar
    cc_otros_ingresos = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Otros Ingresos")
    
    # Costo Bsale calculado gracias a las tablas VentaBsaleTESTING y VentaBsaleMKTPTESTING por año, donde buscamos el costo bsale por el sku de la venta,
    # y sumamos todos aquellos que sean: 
    # 1) que sean el mismo SKU.
    # 2) que sean del mismo año de la fecha_compra
    # 3) mayor a 0.
    cc_costo_bsale = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Bsale")
    
    # para establecer origen del costo_bsale
    COSTO_ORIGEN_CHOICES = [
        ('BSALE_API', 'Costo API Bsale (Congelado)'),
        ('PROMEDIO_BSALE', 'Promedio de Ventas Bsale/MKTP'),
        ('COSTO_STOCK', 'Costo Unitario de Stock'),
        ('MANUAL', 'Ingresado Manualmente'),
        ('NO_CALCULADO', 'No Calculado (Nulo)'),
    ]
    costo_bsale_origen = models.CharField(max_length=20,choices=COSTO_ORIGEN_CHOICES,default='NO_CALCULADO',null=True,blank=True,verbose_name="Origen del Costo Bsale")
    
    #para determinar si los los campos de envio y comisiones fueron calculados o se extrayeron de wivo simplemente
    TIPO_CC_CHOICES = [
        ('WIVO', 'Dato por Wivo'),
        ('CALC_ENVIO', 'Calculado: Envio'),
        ('CALC_COMISION', 'Calculado: Comision'),
        ('CALC_ENVIO_COMISION', 'Calculado: Envio/Comision'),
        ('ERROR_ENVIO', 'Error: Sin Datos para Envío'),
        ('NO_DEFINIDO', 'No Definido'),
    ]
    tipo_cc = models.CharField(
        max_length=20,
        choices=TIPO_CC_CHOICES,
        default='NO_DEFINIDO',
        null=True,
        blank=True,
        verbose_name="Origen del Cálculo (Envío/Comisión)"
    )
    
    # costo bsale * unidades
    cc_costo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Total Calculado")

    # costo fijo de mercado libre, solo se aplica si el canal es mercado libre canal id 5, y corresponda a estos rangos:
    # 1) si el cc_v_venta_bruta_uni < 9990, se aplica un costo fijo de 700
    # 2) si el cc_v_venta_bruta_uni >= 9990 y < 19990, se aplica un costo fijo de 1000
    # 3) si el cc_v_venta_bruta_uni >= 19990, se aplica un costo fijo de 0
    # y ese costo fijo ml se multiplica por las unidades.
    cc_costo_fijo_ml = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Fijo Calculado")
    
    # se iguala al costo_envio + costo_cobro_logistico, pero si no esta, aplicar la siguiente logica:
    # si costo_envio es 0 y cobro_por_costo_logistico es 0:
    # si el canal es Mercado Libre, y es menor a 19990, esta okay, no se hace nada.
    # si es cualquier otro canal, se iguala al cc_costo_envio_mktp
    cc_costo_envio = models.DecimalField(max_digits=15, decimal_places=2,null=True, blank=True, verbose_name="Costo Envío Calculado")
    # costo_comisiones/1.19 y restamos el cc_costo_fijo_ml, pero, si el costo_comisiones es 0, aplicar la siguiente logica:
    # obtenemos el PromedioComisiones del producto y por su canal, donde obtener un porcentaje que se lo aplicaremos al cc_t_venta_neta,
    # o sea cc_costo_comisiones = (cc_t_venta_neta / ((Porcetaje Comisiones Obtenido de la tabla PromedioComisiones) + 1)) - cc_costo_fijo_ml
    # el "+1" es para que el porcentaje, quede por ejmplo, si es 0.15, quede en 1.15, conviertiendo por ejemplo 3670 a 3191.30
    cc_costo_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Comisiones Calculado")
    
    
    # costo_envio + costo_comisiones
    cc_costo_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Marketplace Calculado")
    
    # porcentaje de comision respecto "cc_costo_comisiones" frente a "cc_t_venta_neta" SIN * 100, HAY QUE GUARDAR EL PORCENTAJE EN ESTE FORMATO 0,15 etc.
    cc_porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="% Comisión Calculado")
    
    # total_neto * cc_porcentaje_comision
    cc_comision_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Comisión CLP Neta Calculada")
    
    # Costo Envío por Marketplace usando tarifario (dificil), antes ""valor cobrado""
    cc_costo_envio_mktp_bruto = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Envío por Marketplace Teorico")
    
    # Costo Envío por Marketplace usando tarifario (dificil), antes ""valor cobrado""
    cc_costo_envio_mktp_neto = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Envío por Marketplace Teorico c/ IVA")
    
    # DELTA = (costo_envio o costo_logistico) - c_costo_envio_por_mktp)
    cc_delta_costo_envios = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Delta Costo Envíos")
    
    # MARGEN CLP = total_neto - cc_costo - ((cc_costo_comisiones + cc_costo_envio) / 1.19)
    cc_margen_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen CLP Calculado")

    # MARGEN OPERACIONAL CLP = total_neto - cc_costo - ((cc_costo_comisiones + cc_costo_envio) / 1.19) - (total_neto * 0.20)
    cc_margen_operacional_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen Operacional CLP Calculado")
    
    # MARGEN EXPLOTACION CLP = total_neto - cc_costo
    cc_margen_explotacion_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen Explotacion CLP Calculado")
    
    # MARGEN % = c_margen_clp / ((total_neto - costo_base) / 1.19) SIN * 100, HAY QUE GUARDAR EL PORCENTAJE EN ESTE FORMATO 0,15 etc.
    cc_margen_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen % Calculado")

    # MARGEN % = c_margen_clp / ((total_neto - costo_base) / 1.19) SIN * 100, HAY QUE GUARDAR EL PORCENTAJE EN ESTE FORMATO 0,15 etc.
    cc_margen_operacional_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen Operacional % Calculado")

    # MARGEN % = c_margen_clp / ((total_neto - costo_base) / 1.19) SIN * 100, HAY QUE GUARDAR EL PORCENTAJE EN ESTE FORMATO 0,15 etc.
    cc_margen_explotacion_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen Explotacion % Calculado")
    
    # Timestamps
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # Error costo envio en un solo registro
    multi_orden = models.CharField(max_length=100, null=True, blank=True, verbose_name="MultiOrden Error Costo Envío")
    
    class Meta:
        verbose_name = "Venta Wivo"
        verbose_name_plural = "Ventas Wivo"
        ordering = ['-fecha_compra', '-n_orden']

    def __str__(self):
        return f"Venta Wivo: {self.n_orden}"
    
class VentaWivoCyber(models.Model):
    #------------------------------------------------------
    # CAMPOS FIJOS, PROVIENEN DIRECTAMENTE DEL JSON DE WIVO
    #------------------------------------------------------
    # "SKU Producto"
    sku = models.ForeignKey(Producto, to_field='sku', on_delete=models.PROTECT, related_name='ventas_wivo_cyber', verbose_name="SKU Producto")
    # "SKU Marketplace"
    sku_marketplace = models.CharField(max_length=100, null=True, blank=True, verbose_name="SKU Marketplace")
    # "Canal"
    canal = models.ForeignKey(Canal, on_delete=models.PROTECT, related_name='ventas_wivo_cyber', verbose_name="Canal de Venta (Marketplace)")
    # "Estado de Orden"
    estado_orden = models.ForeignKey(EstadoOrden, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas_wivo_cyber', verbose_name="Estado de Orden (FK)")
    # "Estado de Pago"
    estado_pago = models.ForeignKey(EstadoPago, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas_wivo_cyber', verbose_name="Estado de Pago (FK)")
    # "Fecha de Pago"
    fecha_pago = models.DateField(null=True, blank=True, verbose_name="Fecha de Pago")
    # "N° de Liquidación"
    n_liquidacion = models.CharField(max_length=100, null=True, blank=True, verbose_name="N° de Liquidación")
    # "Estado de Despacho"
    estado_despacho = models.ForeignKey(EstadoDespacho, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas_wivo_cyber', verbose_name="Estado de Despacho (FK)")
    # "Tipo de Despacho"
    tipo_despacho = models.ForeignKey(TipoDespacho, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas_wivo_cyber', verbose_name="Tipo de Despacho (FK)")
    # "Tipo de Despacho del Marketplace"
    tipo_despacho_marketplace = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tipo de Despacho del Marketplace")
    # "Nro. suborden"
    n_suborden = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nro. Sub Orden")
    # "Nro. Orden"
    n_orden = models.CharField(max_length=100, db_index=True, verbose_name="Nro. Orden")
    # "Fecha de compra"
    fecha_compra = models.DateField(verbose_name="Fecha de compra", db_index=True)
    
    # INGRESOS
    # "Ventas"
    ventas = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ventas")
    # "Ingreso por Envío Flex"
    ingreso_envio_flex = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingreso por Envío Flex")
    # "Ingreso de Compensación por Daños"
    ingreso_compensacion_danos = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingreso de Compensación por Daños")
    # "Ingreso Total"
    ingreso_total = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingreso Total")
    # "Despacho pagado por comprador"
    despacho_pagado_comprador = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Despacho pagado por comprador")
    # "Ingreso por promoción"
    ingreso_promocion = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingreso por promoción")
    # "Ingresos sin categorizar"
    ingresos_sin_categorizar = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ingresos sin categorizar")
    # "Unidades"
    unidades = models.IntegerField(null=True, blank=True, verbose_name="Unidades")
    # "Costo de Comisiones"
    costo_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo de Comisiones")
    # "% Costo de Comisiones"
    porcentaje_costo_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo de Comisiones") # Formato XX.YY
    # "Costos por publicidad"
    costos_publicidad = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costos por publicidad")
    # "Costo Envío"
    costo_envio = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Envío")
    # "Rentabilidad Marketplace"
    rentabilidad_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Rentabilidad Marketplace")
    # "% Rentabilidad Marketplace"
    porcentaje_rentabilidad_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Rentabilidad Marketplace") # Formato XX.YY
    # "Costo Total" (del marketplace, según la columna del Excel)
    costo_total = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Total (del Marketplace)")
    # "Venta Cancelada" (valor)
    venta_cancelada = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Valor Venta Cancelada")
    # "Costo de Marketplace"
    costo_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo de Marketplace")
    # "% Costo de Marketplace"
    porcentaje_costo_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo de Marketplace") # Formato XX.YY

    # COBROS ESPECÍFICOS
    # "Cobro de Comisiones"
    cobro_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Comisiones")
    # "% Cobro de Comisiones"
    porcentaje_cobro_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Cobro de Comisiones") # Formato XX.YY
    # "% Costo de Publicidad"
    porcentaje_costo_publicidad = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo de Publicidad") # Formato XX.YY
    # "% Costo Envío"
    porcentaje_costo_envio = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo Envío") # Formato XX.YY
    # "Cobro por Costo Logístico"
    cobro_costo_logistico = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por Costo Logístico")
    # "Cobro de Penalizacion por Cancelación"
    cobro_penalizacion_cancelacion = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Penalizacion por Cancelación")
    # "Cobro Logística Inversa"
    cobro_logistica_inversa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro Logística Inversa")
    # "Cobro Envío Flex"
    cobro_envio_flex = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro Envío Flex")
    # "Cobro de Penalización por Daños"
    cobro_penalizacion_danos = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Penalización por Daños")
    # "Cobro Total"
    cobro_total = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro Total")
    # "Cobro de Ajuste sobre la Comisión"
    cobro_ajuste_sobre_comision = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Ajuste sobre la Comisión")
    # "% Costo Producto"
    porcentaje_costo_producto = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo Producto") # Formato XX.YY
    # "Cobro de Envío"
    cobro_envio = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro de Envío")
    # "Cobro por publicidad"
    cobro_publicidad = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por publicidad")
    # "Cobro por Servicio Almacenamiento"
    cobro_servicio_almacenamiento = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por Servicio Almacenamiento")
    # "Cobro por Almacenamiento Prolongado"
    cobro_almacenamiento_prolongado = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por Almacenamiento Prolongado")
    # "Cobro por Descarte de Stock"
    cobro_descarte_stock = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobro por Descarte de Stock")
    # "% Costo Total" (del marketplace)
    porcentaje_costo_total_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="% Costo Total (Marketplace)") # Formato XX.YY
    # "Cobros sin categorizar"
    cobros_sin_categorizar = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Cobros sin categorizar")

    # REEMBOLSOS
    # "Reembolso de Costo Logístico"
    reembolso_costo_logistico = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de Costo Logístico")
    # "Devolución de Penalización por Cancelación"
    devolucion_penalizacion_cancelacion = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Devolución de Penalización por Cancelación")
    # "Reembolso Logística Inversa"
    reembolso_logistica_inversa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso Logística Inversa")
    # "Reembolso de Ajuste sobre Venta"
    reembolso_ajuste_sobre_venta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de Ajuste sobre Venta")
    # "Reembolso de Comisiones"
    reembolso_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de Comisiones")
    # "Reembolso de envío"
    reembolso_envio = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de envío")
    # "Reembolso Total"
    reembolso_total = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso Total")
    # "Reembolso de Ajuste sobre la Comisión"
    reembolso_ajuste_sobre_comision = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso de Ajuste sobre la Comisión")
    # "Reembolso por publicidad"
    reembolso_publicidad = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso por publicidad")
    # "Reembolsos sin categorizar"
    reembolsos_sin_categorizar = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolsos sin categorizar")
    # "Reembolso por servicio almacenamiento"
    reembolso_servicio_almacenamiento = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso por servicio almacenamiento")
    # "Reembolso por descarte de stock"
    reembolso_descarte_stock = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso por descarte de stock")
    # "Reembolso por almacenamiento prolongado"
    reembolso_almacenamiento_prolongado = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Reembolso por almacenamiento prolongado")
    
    #-------------------------------------------------------
    # VALORES CALCULADOS, QUE NO VIENEN DIRECTAMENTE DE WIVO
    #-------------------------------------------------------
    
    # campos derivados de la fecha_compra
    # n_semana ej: 23, 45, etc...
    n_semana = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Semana")
    # mes ej: 1, 2, 3, ..., 12
    mes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mes")
    # 2023, 2024, 2025, etc...
    año = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Año")
    
    # ventas / unidades
    cc_v_venta_bruta_uni = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Unitario Bruto")
    # cc_v_venta_bruta_uni / 1.19
    cc_v_venta_neta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Valor Venta Neta Calculada")
    # cc_v_venta_neta * unidades
    cc_t_venta_neta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Total Venta Neta Calculada")
    
    # Otros Costos que se componen de: costos_publicidad
    cc_otros_costos = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Otros Costos")
    
    # Otros Ingresos que se componen de: ingreso_envio_flex + ingreso_compensacion_danos + ingreso_promocion + ingresos_sin_categorizar
    cc_otros_ingresos = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Otros Ingresos")
    
    # Costo Bsale calculado gracias a las tablas VentaBsaleTESTING y VentaBsaleMKTPTESTING por año, donde buscamos el costo bsale por el sku de la venta,
    # y sumamos todos aquellos que sean: 
    # 1) que sean el mismo SKU.
    # 2) que sean del mismo año de la fecha_compra
    # 3) mayor a 0.
    cc_costo_bsale = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Bsale")
    
    # para establecer origen del costo_bsale
    COSTO_ORIGEN_CHOICES = [
        ('BSALE_API', 'Costo API Bsale (Congelado)'),
        ('PROMEDIO_BSALE', 'Promedio de Ventas Bsale/MKTP'),
        ('COSTO_STOCK', 'Costo Unitario de Stock'),
        ('MANUAL', 'Ingresado Manualmente'),
        ('NO_CALCULADO', 'No Calculado (Nulo)'),
    ]
    costo_bsale_origen = models.CharField(max_length=20,choices=COSTO_ORIGEN_CHOICES,default='NO_CALCULADO',null=True,blank=True,verbose_name="Origen del Costo Bsale")
    
    #para determinar si los los campos de envio y comisiones fueron calculados o se extrayeron de wivo simplemente
    TIPO_CC_CHOICES = [
        ('WIVO', 'Dato por Wivo'),
        ('CALC_ENVIO', 'Calculado: Envio'),
        ('CALC_COMISION', 'Calculado: Comision'),
        ('CALC_ENVIO_COMISION', 'Calculado: Envio/Comision'),
        ('NO_DEFINIDO', 'No Definido'),
    ]
    tipo_cc = models.CharField(
        max_length=20,
        choices=TIPO_CC_CHOICES,
        default='NO_DEFINIDO',
        null=True,
        blank=True,
        verbose_name="Origen del Cálculo (Envío/Comisión)"
    )
    
    # costo bsale * unidades
    cc_costo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Costo Total Calculado")

    # costo fijo de mercado libre, solo se aplica si el canal es mercado libre canal id 5, y corresponda a estos rangos:
    # 1) si el cc_v_venta_bruta_uni < 9990, se aplica un costo fijo de 700
    # 2) si el cc_v_venta_bruta_uni >= 9990 y < 19990, se aplica un costo fijo de 1000
    # 3) si el cc_v_venta_bruta_uni >= 19990, se aplica un costo fijo de 0
    # y ese costo fijo ml se multiplica por las unidades.
    cc_costo_fijo_ml = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Fijo Calculado")
    
    # se iguala al costo_envio + costo_cobro_logistico, pero si no esta, aplicar la siguiente logica:
    # si costo_envio es 0 y cobro_por_costo_logistico es 0:
    # si el canal es Mercado Libre, y es menor a 19990, esta okay, no se hace nada.
    # si es cualquier otro canal, se iguala al cc_costo_envio_mktp
    cc_costo_envio = models.DecimalField(max_digits=15, decimal_places=2,null=True, blank=True, verbose_name="Costo Envío Calculado")
    # costo_comisiones/1.19 y restamos el cc_costo_fijo_ml, pero, si el costo_comisiones es 0, aplicar la siguiente logica:
    # obtenemos el PromedioComisiones del producto y por su canal, donde obtener un porcentaje que se lo aplicaremos al cc_t_venta_neta,
    # o sea cc_costo_comisiones = (cc_t_venta_neta / ((Porcetaje Comisiones Obtenido de la tabla PromedioComisiones) + 1)) - cc_costo_fijo_ml
    # el "+1" es para que el porcentaje, quede por ejmplo, si es 0.15, quede en 1.15, conviertiendo por ejemplo 3670 a 3191.30
    cc_costo_comisiones = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Comisiones Calculado")
    
    
    # costo_envio + costo_comisiones
    cc_costo_marketplace = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Marketplace Calculado")
    
    # porcentaje de comision respecto "cc_costo_comisiones" frente a "cc_t_venta_neta" SIN * 100, HAY QUE GUARDAR EL PORCENTAJE EN ESTE FORMATO 0,15 etc.
    cc_porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="% Comisión Calculado")
    
    # total_neto * cc_porcentaje_comision
    cc_comision_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Comisión CLP Neta Calculada")
    
    # Costo Envío por Marketplace usando tarifario (dificil), antes ""valor cobrado""
    cc_costo_envio_mktp_bruto = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Envío por Marketplace Teorico")
    
    # Costo Envío por Marketplace usando tarifario (dificil), antes ""valor cobrado""
    cc_costo_envio_mktp_neto = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Costo Envío por Marketplace Teorico c/ IVA")
    
    # DELTA = (costo_envio o costo_logistico) - c_costo_envio_por_mktp)
    cc_delta_costo_envios = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Delta Costo Envíos")
    
    # MARGEN CLP = total_neto - cc_costo - ((cc_costo_comisiones + cc_costo_envio) / 1.19)
    cc_margen_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen CLP Calculado")

    # MARGEN OPERACIONAL CLP = total_neto - cc_costo - ((cc_costo_comisiones + cc_costo_envio) / 1.19) - (total_neto * 0.20)
    cc_margen_operacional_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen Operacional CLP Calculado")

    # MARGEN EXPLOTACION CLP = total_neto - cc_costo
    cc_margen_explotacion_clp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Margen Explotacion CLP Calculado")
    
    # MARGEN % = c_margen_clp / ((total_neto - costo_base) / 1.19) SIN * 100, HAY QUE GUARDAR EL PORCENTAJE EN ESTE FORMATO 0,15 etc.
    cc_margen_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen % Calculado")

    # MARGEN OPERACIONAL % = c_margen_clp / ((total_neto - costo_base) / 1.19) SIN * 100, HAY QUE GUARDAR EL PORCENTAJE EN ESTE FORMATO 0,15 etc.
    cc_margen_operacional_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen Operacional % Calculado")

    # MARGEN EXPLOTACION % = c_margen_clp / ((total_neto - costo_base) / 1.19) SIN * 100, HAY QUE GUARDAR EL PORCENTAJE EN ESTE FORMATO 0,15 etc.
    cc_margen_explotacion_porcentaje = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True, verbose_name="Margen Explotacion % Calculado")
    
    # Timestamps
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # Error costo envio en un solo registro
    multi_orden = models.CharField(max_length=100, null=True, blank=True, verbose_name="MultiOrden Error Costo Envío")
    
    class Meta:
        verbose_name = "Venta Wivo Cyber"
        verbose_name_plural = "Ventas Wivo Cyber"
        ordering = ['-fecha_compra', '-n_orden']

    def __str__(self):
        return f"Venta Wivo Cyber: {self.n_orden}"

class PromedioComisiones(models.Model):
    sku = models.ForeignKey(Producto, to_field='sku', on_delete=models.PROTECT, related_name='promedio_comisiones', verbose_name="SKU Producto")
    año = models.IntegerField(null=True, blank=True, verbose_name="Año")
    Dafiti = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Dafiti")
    Falabella = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Falabella")
    Mercado_Libre = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Mercado Libre")
    Paris = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Paris")
    Ripley = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Ripley")
    Walmart = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name="Walmart")
    
    
    class Meta:
        verbose_name = "Promedio Comisiones"
        verbose_name_plural = "Promedios Comisiones"
        ordering = ['sku']
        unique_together = ('sku','año')
    
    def __str__(self):
        return f"Promedio Comisiones SKU: {self.sku.sku} - Dafiti: {self.Dafiti} - Falabella: {self.Falabella} - Mercado Libre: {self.Mercado_Libre} - Paris: {self.Paris} - Ripley: {self.Ripley} - Walmart: {self.Walmart}"
    

# ---- Tablas para desarrollo proyecto Manifiestos.

class Data_Manifiesto_Bsale(models.Model):
    # Campos de nivel de Documento
    tipo_doc = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Documento")
    codesii = models.CharField(max_length=50, null=True, blank=True, verbose_name="Código SII")
    fecha = models.DateField(db_index=True)
    canal = models.ForeignKey(Canal, on_delete=models.PROTECT, related_name='bsale_manifiesto', verbose_name="Usuario Bsale")
    n_pedido = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name="Nº Pedido/Documento")
    n_orden = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Orden")
    class Meta:
        verbose_name = "Línea de Venta Bsale MKTP (Testing)"
        verbose_name_plural = "Boletas y Facturas de BSALE, para poder relacionarlas al n de orden de data_manifiesto_pdf"
        ordering = ['-fecha', '-id']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
class Data_Manifiesto_PDF(models.Model):
    mktp = models.CharField(max_length=100, null=True, blank=True, verbose_name="MKTP al que corresponde el proceso")
    sub_mktp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Sub MKTP al que corresponde el proceso")
    transporte = models.CharField(max_length=100, null=True, blank=True, verbose_name="Transporte a cargo")
    sesion_despacho = models.CharField(max_length=100, null=True, blank=True, verbose_name="ID de sesion de despacho Unico")
    sesion_despacho_status = models.BooleanField(default=False, verbose_name="Estado de la sesión de despacho")
    n_manifiesto = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Manifiesto")
    fecha = models.DateField(db_index=True)
    n_orden = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Orden")
    n_seguimiento = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Seguimiento")
    cantidad = models.IntegerField(null=True, blank=True, verbose_name="Cantidad")
    validacion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Validación")
    responsable_id_finalizacion = models.ForeignKey('Responsables_Scan', on_delete=models.SET_NULL, null=True, blank=True, to_field='rut', verbose_name="Responsable de Finalización", related_name='responsable_id_finalizacion')
    responsable = models.ForeignKey('Responsables_Scan', on_delete=models.SET_NULL, null=True, blank=True, to_field='rut', verbose_name="Responsable de Escaneo", related_name='responsable')
    comentarios = models.TextField(null=True, blank=True, verbose_name="Comentarios")
    
    # Sección para Picking
    responsable_packing = models.ForeignKey('Responsables_Scan', on_delete=models.SET_NULL, null=True, blank=True, to_field='rut', related_name='responsable_packing', verbose_name="Responsable de Packing")
    fecha_packing = models.DateTimeField(null=True, blank=True, verbose_name="Fecha y Hora de Packing")
    status_packing = models.BooleanField(default=False, null=True, verbose_name="Estadon de manifiesto de Packing")
    validacion_packing = models.CharField(max_length=100, null=True, blank=True, verbose_name="Validacion por bulto de Packing")
    comentarios_packing = models.TextField(null=True, blank=True, verbose_name="Comentarios de Packing")
    cancelado = models.BooleanField(default=False, verbose_name="Orden Cancelada?")
    entregado_cliente = models.BooleanField(default=False, verbose_name="Entregado al Cliente?")

    # seccion para liberacion de etiquetas
    etiqueta = models.BooleanField(default=False, verbose_name="Liberacion de Etiquetas")
    
    comuna = models.CharField(max_length=100, null=True, blank=True, verbose_name="Comuna de Entrega")
    class Meta:
        verbose_name = "Manifiesto PDF"
        verbose_name_plural = "Manifiestos PDF"
        ordering = ['-fecha', '-id']
        
    def __str__(self):
        return self.n_manifiesto

class Data_Fulfillment(models.Model):
    fecha = models.DateField(db_index=True)
    n_id = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Seguimiento")
    responsable_check = models.ForeignKey('Responsables_Scan', on_delete=models.SET_NULL, null=True, blank=True, to_field='rut', related_name='responsable_check', verbose_name="Responsable de Checking")
    fecha_check = models.DateTimeField(null=True, blank=True, verbose_name="Fecha y Hora de Checking")
    status_check = models.BooleanField(default=False, null=True, verbose_name="Estadon de manifiesto de Checking")
    validacion_check = models.CharField(max_length=100, null=True, blank=True, verbose_name="Validacion por bulto de Checking")
    comentarios_check = models.TextField(null=True, blank=True, verbose_name="Comentarios de Checking")
    cancelado = models.BooleanField(default=False, verbose_name="Orden Cancelada?")
    sku = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, blank=True, to_field='sku', related_name='sku_id', verbose_name="SKU")

    class Meta:
        verbose_name = "Data Fulfillment"
        verbose_name_plural = "Data Fulfillment"
        ordering = ['-fecha', '-id']
    
    def __str__(self):
        return f"Data Fulfillment - ID: {self.n_id} - Fecha: {self.fecha}"

class Data_Picking(models.Model):
    fecha = models.DateField(db_index=True)
    n_seguimiento = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Seguimiento")
    responsable_picking = models.ForeignKey('Responsables_Scan', on_delete=models.SET_NULL, null=True, blank=True, to_field='rut', related_name='responsable_picking_data', verbose_name="Responsable de Picking")
    mktp = models.CharField(max_length=100, null=True, blank=True, verbose_name="MKTP al que corresponde el proceso")
    comentarios_picking = models.TextField(null=True, blank=True, verbose_name="Comentarios de Picking")
    
    class Meta:
        verbose_name = "Data Picking"
        verbose_name_plural = "Data Picking"
        ordering = ['-fecha', '-id']
    
    def __str__(self):
        return f"Data Picking - Seguimiento: {self.n_seguimiento} - Fecha: {self.fecha}"

class Responsables_Scan(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name="RUT del Responsable")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Responsable")
    clave = models.CharField(max_length=100, verbose_name="Clave del Responsable")
    is_despacho = models.BooleanField(default=False, verbose_name="¿Es Responsable de Despacho?")
    is_packing = models.BooleanField(default=False, verbose_name="¿Es Responsable de Packing?")
    is_manager = models.BooleanField(default=False, verbose_name="¿Es Manager?")
    is_kpi = models.BooleanField(default=False, verbose_name="¿Puede ver KPIs?")
    is_seller = models.BooleanField(default=False, verbose_name="¿Es Seller?")
    is_loader = models.BooleanField(default=False, verbose_name="¿Es Loader?")
    is_driver = models.BooleanField(default=False, verbose_name="¿Es Driver?")

    class Meta:
        verbose_name = "Responsable de Escaneo"
        verbose_name_plural = "Responsables de Escaneo"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class LogDescargaDocumentos(models.Model):
    """
    Registra cada vez que se genera/descarga un set de documentos (Boletas/Facturas)
    en el Rotulador para evitar duplicidad.
    """
    id = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField(default=timezone.now, db_index=True)
    
    # Identificadores del documento
    n_orden = models.CharField(max_length=100, db_index=True, verbose_name="Nº de Orden")
    n_boleta = models.CharField(max_length=100, db_index=True, verbose_name="Nº de Boleta/Factura")
    tipo_documento = models.CharField(max_length=20, verbose_name="Tipo (Boleta/Factura)") # '14' o '13'

    # Contexto del proceso
    mktp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Marketplace/Courier")
    metodo_ingreso = models.CharField(max_length=50, verbose_name="Método (Manual/Archivo)")
    sesion_id = models.CharField(max_length=100, null=True, blank=True)

    # Quién realizó la descarga
    responsable_rut = models.ForeignKey(
        'Responsables_Scan',
        to_field='rut',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='responsable_rut',
        verbose_name="Usuario que descargó"
    )

    class Meta:
        db_table = 'dcic_operations_log_descarga_documentos'
        verbose_name = "Log de Descarga de Documento"
        verbose_name_plural = "Logs de Descargas de Documentos"
        # Indexamos por n_orden para búsquedas rápidas al cargar el rotulador
        indexes = [
            models.Index(fields=['n_orden', 'n_boleta']),
        ]

    def __str__(self):
        return f"{self.n_boleta} - Orden: {self.n_orden} por {self.responsable_rut}"

# TABLAS PRINCIPALES Para el desarrollo de COMEX(PreOrdenes)

class Roles(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre del Rol")

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Usuario")
    rut = models.CharField(max_length=12, unique=False, verbose_name="RUT del Usuario", null=True)
    email = models.EmailField(unique=True, verbose_name="Email del Usuario")
    password = models.CharField(max_length=100, verbose_name="Contraseña del Usuario")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
    rol = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Rol del Usuario")
    perm_productos = models.BooleanField(default=False)
    perm_ordenes   = models.BooleanField(default=False)
    perm_ventas    = models.BooleanField(default=False)
    perm_ventas_editar = models.BooleanField(default=False)
    perm_forecast  = models.BooleanField(default=False)
    perm_usuarios  = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['nombre']

    def __str__(self):
        return self.rut
    
class PreOrdenComex(models.Model):
    # id = models.AutoField(primary_key=True) # Django añade este campo automáticamente. [10]
    aux = models.CharField(max_length=255, unique=True, verbose_name="Auxiliar (ID Único)", null=True)
    item = models.IntegerField(verbose_name="Ítem", null=True)
    n_order = models.CharField(max_length=255, verbose_name="N° de Orden")
    fecha_emision = models.DateField(verbose_name="Fecha de Emisión")
    cliente = models.CharField(max_length=255, verbose_name="Cliente", null=True, blank=True)
    fecha_sol_eta = models.DateField(verbose_name="Fecha Solicitada ETA, 90 días")
    fecha_aprobacion = models.DateField(verbose_name="Fecha de Aprobación")
    qty_original = models.IntegerField(verbose_name="Cantidad Original")
    products = models.TextField(verbose_name="Productos")
    en_bsale = models.BooleanField(default=False, verbose_name="En Bsale")
    pi_code = models.CharField(max_length=100, verbose_name="Código PI", null=True, blank=True)
    units = models.IntegerField(verbose_name="Unidades")
    qty_master = models.IntegerField(verbose_name="Cantidad Master")
    etd_commitment = models.CharField(max_length=255, verbose_name="Compromiso ETD", null=True, blank=True)
    fob_unit = models.FloatField(verbose_name="FOB Unitario", null=True, blank=True)
    total_amount = models.FloatField(verbose_name="Monto Total")
    comentarios = models.TextField(null=True, blank=True, verbose_name="Comentarios", default="Sin Comentarios")
    metro_cubico_cbm = models.CharField(max_length=50, verbose_name="Metro Cúbico (CBM)", null=True, blank=True)
    
    # Llave foránea (ForeignKey) al modelo Proveedor
    proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.CASCADE, 
        verbose_name="Proveedor"
    )
    
    sku = models.ForeignKey(
        Producto, 
        to_field='sku', 
        on_delete=models.PROTECT, 
        related_name='preordenes_comex',
        verbose_name="SKU Producto",
        null=False, 
        blank=False
    )

    class Meta:
        verbose_name = "Pre Orden Comex"
        verbose_name_plural = "Pre Órdenes Comex"

    def __str__(self):

        return self.n_order
    
#####################################################################################

class FirmasDigitales(models.Model):
    nombre_firma = models.CharField(max_length=255, verbose_name="Nombre del Documento")
    fecha_subida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Subida")
    firma_svg = models.TextField(verbose_name="Firma en Formato SVG")
    usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Usuario" # Es buena práctica añadir un verbose_name
    )
    class Meta:
        verbose_name = "Firma Digital"
        verbose_name_plural = "Firmas Digitales"
        ordering = ['-fecha_subida']

    def __str__(self):
        return self.nombre_firma
    
class PreOrden(models.Model):
    po_number = models.CharField(max_length=255, unique=True, verbose_name="Número de Pre-Orden")
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='preordenes'
    )
    puerto_salida = models.ForeignKey(
        PuertoSalida,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='preordenes'
    )
    fecha_emision = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_aprobacion = models.DateField(null=True, blank=True)
    fecha_solicitud_eta = models.DateField(null=True, blank=True)
    comment_po = models.TextField(null=True, blank=True)
    invoice = models.CharField(max_length=255, null=True, blank=True)
    pi_document_key = models.CharField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Clave del Documento PI en S3"
    )
    total_cbm = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    total_contenedores = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    estado = models.CharField(max_length=50, default='CREADA')
    firma = models.ForeignKey(
        FirmasDigitales,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='preordenes_firmadas'
    )
    firmado_por = models.ForeignKey(
        Usuarios,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='preordenes_firmadas'
    )
    fecha_firma = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'dcic_operations_preorden'
        verbose_name = "Pre-Orden"
        verbose_name_plural = "Pre-Órdenes"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.po_number


class PreOrdenItem(models.Model):
    item = models.IntegerField(verbose_name="# Ítem por PO", default=1)
    preorden = models.ForeignKey(
        PreOrden,
        on_delete=models.CASCADE,
        related_name='items'
    )
    sku = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        to_field='sku',
        db_column='sku'
    )
    qty_original = models.PositiveIntegerField()
    units = models.PositiveIntegerField()
    qty_ctn = models.PositiveIntegerField()
    fob_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(null=True, blank=True)
    cbm = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)

    class Meta:
        db_table = 'dcic_operations_preorden_item'
        verbose_name = "Item de Pre-Orden"
        verbose_name_plural = "Items de Pre-Órdenes"

    def __str__(self):
        return f"{self.sku} ({self.preorden.po_number})"
    
    
    
class PreOrdenFirma(models.Model):
    ROL_CHOICES = [
        ('GERENTE_COMERCIAL', 'Gerente Comercial'),
        ('GERENTE_FINANZAS',  'Gerente Finanzas'),
        ('MARCAS',            'Marcas & Nuevos Negocios'),
    ]

    preorden = models.ForeignKey(
        PreOrden,
        on_delete=models.CASCADE,
        related_name='firmas_registradas',
        verbose_name='Pre-Orden'
    )
    firma = models.ForeignKey(
        FirmasDigitales,
        on_delete=models.RESTRICT,  # No permitir borrar una firma que ya está en una PO
        related_name='usos_en_preordenes',
        verbose_name='Firma Digital'
    )
    firmado_por = models.ForeignKey(
        Usuarios,
        on_delete=models.RESTRICT,
        related_name='firmas_en_preordenes',
        verbose_name='Firmante'
    )
    rol_firma = models.CharField(
        max_length=50,
        choices=ROL_CHOICES,
        verbose_name='Rol del Firmante'
    )
    fecha_firma = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Firma'
    )

    class Meta:
        db_table = 'dcic_operations_preorden_firma'
        verbose_name = 'Firma de Pre-Orden'
        verbose_name_plural = 'Firmas de Pre-Órdenes'
        # Un usuario solo puede firmar una vez por pre-orden
        constraints = [
            models.UniqueConstraint(
                fields=['preorden', 'firmado_por'],
                name='uq_preorden_usuario_firma'
            )
        ]
        ordering = ['fecha_firma']

    def __str__(self):
        return f"{self.preorden.po_number} — {self.rol_firma} ({self.firmado_por.nombre})"
###########################################################################
    
    
class AnalisisProyeccion(models.Model):
    """
    Tabla Maestra que almacena el resultado consolidado de un análisis 
    de proyección para un producto específico en un momento dado.
    """
    class TipoAnalisis(models.TextChoices):
        NO_ESTACIONAL = 'NO_ESTACIONAL', 'No Estacional'
        ESTACIONAL = 'ESTACIONAL', 'Estacional'

    # --- Relaciones y Contexto ---
    producto = models.ForeignKey(
        'Producto', 
        on_delete=models.CASCADE, 
        related_name='analisis_proyecciones',
        verbose_name="Producto (SKU)"
    )
    fecha_analisis = models.DateTimeField(
        default=timezone.now,
        verbose_name="Fecha y Hora del Análisis"
    )
    tipo_analisis = models.CharField(
        max_length=20,
        choices=TipoAnalisis.choices,
        verbose_name="Tipo de Análisis Realizado"
    )

    # --- Parámetros Usados (para reproducibilidad) ---
    # Usamos JSONField para guardar de forma flexible los parámetros de entrada.
    # Ej: {'start_date': '2023-01-01', 'end_date': '2023-12-31', 'peso_reciente': 0.6}
    parametros_usados = models.JSONField(
        null=True, blank=True,
        verbose_name="Parámetros de Entrada del Análisis"
    )
    
    # --- Resultados del Análisis ---
    diagnostico = models.CharField(
        max_length=255, 
        verbose_name="Diagnóstico General"
    )
    recomendacion_texto = models.TextField(
        verbose_name="Recomendación Detallada"
    )
    cantidad_sugerida = models.PositiveIntegerField(
        default=0,
        verbose_name="Cantidad de Compra Sugerida"
    )
    stock_al_analizar = models.IntegerField(
        verbose_name="Stock Registrado en el Análisis"
    )
    fecha_limite_compra = models.DateField(
        null=True, blank=True,
        verbose_name="Fecha Límite de Compra (Estacionales)"
    )
    dias_plazo_al_analizar = models.IntegerField(
        null=True, blank=True,
        verbose_name="Días de Plazo Restantes (Estacionales)"
    )

    class Meta:
        verbose_name = "Análisis de Proyección"
        verbose_name_plural = "Análisis de Proyecciones"
        ordering = ['-fecha_analisis', 'producto__sku']

    def __str__(self):
        return f"Análisis para {self.producto.sku} el {self.fecha_analisis.strftime('%Y-%m-%d %H:%M')}"


class DetalleProyeccion(models.Model):
    """
    Tabla de Detalle. Almacena cada línea de la proyección, ya sea semanal 
    (no estacional) o por temporada (estacional).
    Está vinculada a un análisis maestro.
    """
    analisis = models.ForeignKey(
        AnalisisProyeccion, 
        on_delete=models.CASCADE, 
        related_name='detalles',
        verbose_name="Análisis Padre"
    )
    
    # --- Campos para Proyección NO ESTACIONAL ---
    semana_numero = models.PositiveIntegerField(null=True, blank=True, verbose_name="Número de Semana")
    fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha Inicio Semana")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha Fin Semana")
    venta_anterior = models.IntegerField(null=True, blank=True, verbose_name="Venta Histórica/Anterior")
    venta_proyectada = models.IntegerField(null=True, blank=True, verbose_name="Venta Proyectada")

    # --- Campos para Proyección ESTACIONAL ---
    temporada_nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nombre de la Temporada")
    # El diagnóstico y sugerencia de la temporada estacional se pueden almacenar aquí,
    # aunque también están en el análisis maestro. Depende de si quieres guardarlos a nivel de detalle.
    # Por simplicidad, los datos de la proyección estacional se pueden poner aquí:
    # Ej: "Temporada": season_name, "Diagnóstico": diagnostico, "Sugerencia": f"Comprar {cantidad_sugerida} uds"
    # Vamos a usar un campo JSON para máxima flexibilidad, ya que la estructura varía.
    
    datos_proyeccion = models.JSONField(
        verbose_name="Datos Detallados de la Proyección (JSON)"
    )

    class Meta:
        verbose_name = "Detalle de Proyección"
        verbose_name_plural = "Detalles de Proyecciones"
        ordering = ['analisis', 'semana_numero', 'fecha_inicio']

    def __str__(self):
        if self.semana_numero:
            return f"Detalle Semana {self.semana_numero} para {self.analisis.producto.sku}"
        else:
            return f"Detalle Temporada para {self.analisis.producto.sku}"
        
        
        
        
####################################################################
#######               DCIC NC MANAGER               ################
####################################################################

class EstadoSKU(models.Model):
    nombre_estado = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Estado del Producto")

    class Meta:
        verbose_name = "Estado del Producto SKU"
        verbose_name_plural = "Estados de los Productos SKU"
        ordering = ['nombre_estado']

    def __str__(self):
        return self.nombre_estado

class ManagerNC(models.Model):
    # id = models.AutoField(primary_key=True) # Django añade este campo automáticamente.
    recepcion_id = models.IntegerField(verbose_name="ID de Recepción en Bsale", auto_created=True, null=True, blank=True)
    n_orden = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Orden")
    is_fulfillment = models.BooleanField(default=False, verbose_name="¿Es Fulfillment?")
    n_documento = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Documento (boleta o factura)")
    n_nc = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Nota de Crédito (NC)")
    sku_doc = models.ForeignKey(Producto, to_field='sku', on_delete=models.PROTECT, related_name='manager_nc', verbose_name="SKU Producto")
    sku_real = models.ForeignKey(Producto, to_field='sku', on_delete=models.PROTECT, related_name='manager_nc_sku_real', verbose_name="SKU Real Producto", null=True, blank=True)
    cantidad_doc = models.IntegerField(null=True, blank=True, verbose_name="Cantidad según Documento")
    cantidad_real = models.IntegerField(null=True, blank=True, verbose_name="Cantidad Real en Bodega")
    evaluacion = models.ForeignKey(EstadoSKU, on_delete=models.PROTECT, related_name='manager_nc', null=True, blank=True, verbose_name="Clasificación del SKU")
    estado_producto = models.CharField(max_length=255, null=True, blank=True, verbose_name="Estado del Producto")
    condicion_empaque = models.CharField(max_length=255, null=True, blank=True, verbose_name="Condición del Empaque")
    estado_transporte = models.BooleanField(default=False, verbose_name="Estado del Transporte")
    n_glosa = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nº Glosa")
    canal = models.ForeignKey(Canal, on_delete=models.PROTECT, related_name='manager_nc', verbose_name="Canal de Venta")
    comentarios = models.TextField(null=True, blank=True, verbose_name="Comentarios Adicionales")
    fecha_recepcion = models.DateField(null=True, blank=True, verbose_name="Fecha de Recepción")
    fecha_asignacion_nc = models.DateField(null=True, blank=True, verbose_name="Fecha de Asignación de NC")
    responsable_recepcion = models.ForeignKey(Usuarios, on_delete=models.SET_NULL,null=True, blank=True,related_name='responsable_recepcion_nc', verbose_name="Responsable de Recepción")
    responsable_asignacion_nc = models.ForeignKey(Usuarios, on_delete=models.SET_NULL,null=True, blank=True,related_name='responsable_asignacion_nc', verbose_name="Responsable de Asignación de NC")
    foto_urls = models.JSONField(default=list, blank=True, verbose_name="URLs de Fotos")

    class Meta:
        verbose_name = "Manager de Notas de Crédito"
        verbose_name_plural = "Managers de Notas de Crédito"
        ordering = ['-fecha_recepcion', '-n_orden']
        
    def __str__(self):
        return f"Manager NC - Orden: {self.n_orden} - Documento: {self.n_documento} - NC: {self.n_nc}"
    
    
class LogAuditoriaManifiestos(models.Model):
    """
    Tabla dedicada a registrar CADA movimiento que se hace en el cargador.
    No afecta la lógica de negocio, solo observa y anota.
    """

    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    # ¿Quién lo hizo?
    responsable_rut = models.ForeignKey(
        'Responsables_Scan',
        to_field='rut',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='responsable_rut'
    )

    # ¿Qué hizo? (Ej: 'CARGA_NUEVA', 'CARGA_ADICIONAL', 'ELIMINACION', 'DUPLICADO_REEMPLAZO')
    accion = models.CharField(max_length=50)

    # Contexto de la sesión
    sesion_id = models.CharField(max_length=100, null=True, blank=True)

    # Inputs Crudos (JSON String)
    detalles_input = models.TextField(null=True, blank=True)

    # Resultados (JSON String)
    resultado_proceso = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'dcic_operations_log_auditoria_manifiestos'

    def __str__(self):
        return f"LogAuditoria(id={self.id}, accion={self.accion}, user={self.responsable_rut})"


class StockComparison(models.Model):
    sku = models.CharField(max_length=100, db_index=True)
    producto = models.CharField(max_length=255, null=True, blank=True)
    stock_bsale = models.FloatField(default=0)
    stock_check = models.FloatField(default=0)
    stock_principal = models.FloatField(default=0)
    stock_externa = models.FloatField(default=0)
    stock_h = models.FloatField(default=0)
    diferencia = models.FloatField(default=0)
    estado = models.CharField(max_length=50)
    fecha_sincronizacion = models.DateTimeField(auto_now_add=True)
    costo_bsale = models.FloatField(default=0)

    class Meta:
        verbose_name = "Comparación de Stock"
        verbose_name_plural = "Comparaciones de Stock"
        # El nombre de la tabla en la DB será 'app_stockcomparison' 
        # (Depende del nombre de tu app de Django)
        ordering = ['-fecha_sincronizacion', 'sku']

    def __str__(self):
        return f"{self.sku} - Diff: {self.diferencia}"



class ShopifyStore(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nombre de la Tienda")
    shop_url = models.CharField(max_length=255, unique=True, verbose_name="URL de la Tienda")
    access_token = models.CharField(max_length=255, verbose_name="Token de Acceso")
    installed_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Instalación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Tienda Shopify"
        verbose_name_plural = "Tiendas Shopify"
        ordering = ['-created_at']

    def __str__(self):
        return self.shop_url

class ShopifyOrder(models.Model):
    # Cambiado 'index' por 'db_index'
    # Nota: como tiene unique=True, el índice se crea solo, pero lo dejamos corregido
    shopify_order_id = models.CharField(max_length=255, unique=True, db_index=True) 
    
    # Relación con la tienda
    store = models.ForeignKey(ShopifyStore, on_delete=models.CASCADE, related_name='orders')
    
    order_number = models.CharField(max_length=255)
    total_price = models.FloatField()
    currency = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    financial_status = models.CharField(max_length=255)
    fulfillment_status = models.CharField(max_length=255, null=True, blank=True)
    created_at_shopify = models.DateTimeField()
    created_at_db = models.DateTimeField(auto_now_add=True)
    order_name_normalized = models.CharField(max_length=255, null=True, blank=True)
    
    # Asegúrate de que tu versión de Django soporte JSONField (3.0+)
    raw_data = models.JSONField() 

    class Meta:
        db_table = "dcic_operations_shopifyorders"
        verbose_name = "Orden Shopify"
        verbose_name_plural = "Ordenes Shopify"
        ordering = ['-created_at_db']

    def __str__(self):
        return self.shopify_order_id


class ShopifyTransporteComunas(models.Model):
    comuna = models.CharField(max_length=255, unique=True, verbose_name="Comuna")  # ← unique=True
    transportista = models.CharField(max_length=255, verbose_name="Transportista")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Transporte Comunas"
        verbose_name_plural = "Transporte Comunas"
        ordering = ['-updated_at']
        db_table = "dcic_operations_shopifytransportecomunas"  # ← opcional pero recomendado

    def __str__(self):
        return self.comuna


# Control operaciones tools
class SolicitudCambioManifiesto(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    CAMPO_CHOICES = [
        ('n_orden', 'N° Orden'),
        ('fecha', 'Fecha'),
        ('transporte', 'Transportista'),
        ('mktp', 'Marketplace'),
        ('sub_mktp', 'Sub-Marketplace'),
    ]

    # Relación al registro afectado
    manifiesto = models.ForeignKey(
        'Data_Manifiesto_PDF',
        on_delete=models.SET_NULL,
        null=True,
        related_name='solicitudes_cambio',
        verbose_name="Manifiesto Afectado"
    )

    # Quién solicita
    solicitante_rut = models.CharField(
        max_length=12,
        verbose_name="RUT del Solicitante"
    )
    solicitante_nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre del Solicitante"
    )

    # Qué campo se quiere cambiar
    campo = models.CharField(
        max_length=50,
        choices=CAMPO_CHOICES,
        verbose_name="Campo a Modificar"
    )
    valor_anterior = models.CharField(
        max_length=255,
        verbose_name="Valor Anterior"
    )
    valor_nuevo = models.CharField(
        max_length=255,
        verbose_name="Valor Nuevo Propuesto"
    )

    # Motivo / contexto
    motivo = models.TextField(
        null=True,
        blank=True,
        verbose_name="Motivo del Cambio"
    )

    # Estado del flujo
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente',
        verbose_name="Estado"
    )

    # Auditoría de resolución
    resuelto_por_rut = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        verbose_name="RUT del Admin que Resolvió"
    )
    resuelto_por_nombre = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Nombre del Admin que Resolvió"
    )
    comentario_resolucion = models.TextField(
        null=True,
        blank=True,
        verbose_name="Comentario de Resolución"
    )
    fecha_resolucion = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha de Resolución"
    )

    # Timestamps
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Solicitud"
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última Actualización"
    )

    class Meta:
        verbose_name = "Solicitud de Cambio"
        verbose_name_plural = "Solicitudes de Cambio"
        ordering = ['-fecha_creacion']
        indexes = [
            models.Index(fields=['estado']),
            models.Index(fields=['solicitante_rut']),
            models.Index(fields=['manifiesto', 'estado']),
        ]

    def __str__(self):
        return f"Solicitud #{self.id} - {self.campo} por {self.solicitante_rut} [{self.estado}]"

class LogAuditoriaBuilder(models.Model):
    """
    Registra cada vez que se guarda un manifiesto desde el ManifestBuilder.
    Diferente a LogAuditoriaManifiestos que es para carga de PDFs.
    """
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    # Quién lo hizo
    responsable_rut = models.ForeignKey(
        'Responsables_Scan',
        to_field='rut',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='responsable_rut'
    )

    # Identificadores del manifiesto creado
    sesion_id = models.CharField(max_length=120)
    n_manifiesto = models.CharField(max_length=50)

    # Opciones usadas
    transportista = models.CharField(max_length=50)
    mktp = models.CharField(max_length=50)
    sub_mktp = models.CharField(max_length=50)
    fecha_manifiesto = models.DateField()

    # Tipo de operación: 'NUEVO' o 'ADICIONAL'
    tipo_sesion = models.CharField(max_length=20, default='NUEVO')

    # Resumen numérico
    total_bultos = models.IntegerField(default=0)
    total_envios = models.IntegerField(default=0)  # órdenes únicas

    # Detalle completo en JSON (lista de items guardados)
    detalle_items = models.TextField(null=True, blank=True)  # JSON string

    class Meta:
        db_table = 'dcic_operations_log_auditoria_builder'

    def __str__(self):
        return f"LogBuilder(id={self.id}, man={self.n_manifiesto}, user={self.responsable_rut})"

class ReporteMonitorVentas(models.Model):
    """
    Guarda la configuración de un reporte personalizado del Monitor de Ventas.
    columnas_config es un JSON que describe qué columnas mostrar y en qué orden.
    """
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Reporte")
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
    
    # JSON con la configuración: lista de column_ids ordenados
    # Ej: ["sku", "desc_corta", "stock_bsale", "venta_q_2026", "semana_16-26", ...]
    columnas_config = models.JSONField(verbose_name="Configuración de Columnas")
    
    # Filtros guardados junto al reporte (opcional pero muy útil)
    filtros_config = models.JSONField(null=True, blank=True, verbose_name="Filtros guardados")
    
    # Metadatos
    creado_por = models.CharField(max_length=100, null=True, blank=True, verbose_name="Creado por")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    es_publico = models.BooleanField(default=True, verbose_name="¿Visible para todos?")

    class Meta:
        verbose_name = "Reporte Monitor de Ventas"
        verbose_name_plural = "Reportes Monitor de Ventas"
        ordering = ['-fecha_actualizacion']

    def __str__(self):
        return self.nombre

class GrupoMonitorVentas(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Grupo")

    class Meta:
        verbose_name = "Grupo Monitor de Ventas"
        verbose_name_plural = "Grupos Monitor de Ventas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
class GrupoSKUMonitorVentas(models.Model):
    grupo = models.ForeignKey(GrupoMonitorVentas, on_delete=models.CASCADE, 
                              verbose_name="Grupo", db_column='group_id')
    sku = models.CharField(max_length=100, verbose_name="SKU")

    class Meta:
        verbose_name = "Grupo SKU Monitor de Ventas"
        verbose_name_plural = "Grupos SKU Monitor de Ventas"
        ordering = ['grupo', 'sku']

    def __str__(self):
        return f"{self.group.nombre} - {self.sku}"
    
class EventoVenta(models.Model):
    nombre = models.TextField(verbose_name="Nombre del Evento")

    class Meta:
        db_table = 'dcic_operations_eventoventa'
        verbose_name = "Evento de Venta"
        verbose_name_plural = "Eventos de Venta"

    def __str__(self):
        return self.nombre


class EventoVentaRango(models.Model):
    

    event = models.ForeignKey(
        EventoVenta,
        on_delete=models.CASCADE,
        related_name='rangos',
        verbose_name="Evento"
    )
    year = models.IntegerField(verbose_name="Año")
    start_date = models.DateField(verbose_name="Fecha Inicio")
    end_date = models.DateField(verbose_name="Fecha Fin")

    class Meta:
        db_table = 'dcic_operations_eventoventa_rango'
        verbose_name = "Rango de Evento de Venta"
        verbose_name_plural = "Rangos de Eventos de Venta"

    def __str__(self):
        return f"{self.event.nombre} - {self.year}"