"""
Lógica de generación del Reporte de Ventas Consolidadas.

Extrae datos de Bsale, Wivo, Notas de Crédito y Notas de Débito desde la base
de datos y los consolida en un DataFrame con exactamente las mismas columnas y
cálculos que el backend original (comando `extract_db_to_excel`).
"""
import os

import pandas as pd
from django.db.models import F, Value, CharField, Case, When, DecimalField
from django.db.models.functions import Coalesce, Cast, Concat

from dcic_operations.models import (
    VentaWivo,
    VentaBsaleTESTING,
    NotasCredito,
    NotasDebito,
    VentaWivoCyber,
    VentaBsale,
    NotasCreditoCyber,
)

# ==============================================================================
# CONSTANTES Y CONFIGURACIÓN
# ==============================================================================
HOJA_VENTAS_CONSOLIDADAS = "Ventas Consolidadas"

# IDs de canales activos
CANAL_IDS_ACTIVOS = {103, 68, 73, 74, 72, 30, 28, 29, 31, 32, 35, 34, 33, 3, 5}

FINAL_COLUMNS = [
    'Origen',
    'Fecha',
    'Canal',
    'Canal Activo',
    'SKU Producto',
    'Cant.',
    'Venta Total',
    'Valor Unitario',
    'Valor Neto',
    'Total Neto',
    'Costo Calc.',
    'Estado de Orden',
    'Tipo de Despacho',
    'Costo de Marketplace',
    'Costo de Comisiones',
    '% Costo de Comisiones',
    'Costo Envío',
    'Costo Cobro Logístico',
    'Ingreso por Envío Flex',
    'Ingreso Total',
    'Ingreso por Reembolso',
    'Despacho pagado por comprador',
    'Ingreso por promoción',
    'Costo Total',
    'N° Sub-Orden',
    'N° Pedido',
    'Estado de Despacho',
    'Otros Costos',
    'Otros Ingresos',
    'Costo Fijo ML',
    'Costo Envio Calc. Neto',
    'Costo Comision Calc. Neto',
    '% Cobro de Comisiones',
    '% Comisión Nuevo',
    'Comisión CLP Neta',
    'Costo Envío Teórico Bruto',
    'Costo Envío Teórico Neto',
    '∆',
    'Margen Explotación CLP',
    'Margen Explotación %',
    'Margen CLP',
    'Margen %',
    'Margen Operacional CLP',
    'Margen Operacional %',
    'Tipo Cálculo',
    'MultiOrden',
    'Marca',
    'Categoria Principal',
    'Subcategoria',
    'Tipo Producto',
    'Descripción',
    'Num. Semana',
    'Mes',
    'Año',
    'Tipo Registro'
]

NUMERIC_COLS = [
    'Cant.',
    'Venta Total',
    'Valor Unitario',
    'Valor Neto',
    'Total Neto',
    'Costo Calc.',
    'Costo de Marketplace',
    'Costo de Comisiones',
    '% Costo de Comisiones',
    'Costo Envío',
    'Costo Cobro Logístico',
    'Ingreso por Envío Flex',
    'Ingreso Total',
    'Ingreso por Reembolso',
    'Despacho pagado por comprador',
    'Ingreso por promoción',
    'Costo Total',
    'Otros Costos',
    'Otros Ingresos',
    'Costo Fijo ML',
    'Costo Envio Calc. Neto',
    'Costo Comision Calc. Neto',
    '% Cobro de Comisiones',
    '% Comisión Nuevo',
    'Comisión CLP Neta',
    'Costo Envío Teórico Bruto',
    'Costo Envío Teórico Neto',
    '∆',
    'Margen CLP',
    'Margen %',
    'Margen Explotación CLP',
    'Margen Explotación %',
    'Margen Operacional CLP',
    'Margen Operacional %'
]


def _get_bsale_data(start_date, end_date, data_source, log=print):
    if data_source == 'Cyber':
        VentaBsaleModel = VentaBsale
        log("     -> Usando modelo: VentaBsale (Cyber)")
    else:
        VentaBsaleModel = VentaBsaleTESTING
        log("     -> Usando modelo: VentaBsaleTESTING (Testing)")

    ventas_bsale = VentaBsaleModel.objects.filter(
        fecha__range=(start_date, end_date)
    ).select_related(
        'canal', 'sku', 'tipo_despacho', 'sku__proveedor', 'sku__marca'
    ).annotate(
        Origen_alias=Value('Bsale', output_field=CharField()),
        Fecha_alias=F('fecha'),
        Canal_alias=F('canal__nombre'),
        Canal_Id_alias=F('canal_id'),
        SKU_Producto_alias=Case(
            When(tipo_linea__in=['GLOSA', 'SERVICIO'], then=F('glosa_codigo')),
            default=F('sku__sku'),
            output_field=CharField()
        ),
        Cant_alias=F('cantidad'),
        Venta_Total_alias=F('venta_total'),
        Valor_Unitario_alias=F('valor_unitario'),
        Valor_Neto_alias=F('valor_neto'),
        Total_Neto_alias=F('total_neto'),
        Costo_Calc_alias=F('c_costo'),
        Estado_de_Orden_alias=F('estado_orden'),
        Tipo_de_Despacho_alias=F('tipo_despacho__nombre'),
        Costo_de_Marketplace_alias=Value(None, output_field=DecimalField()),
        Costo_de_Comisiones_alias=Case(
            When(tipo_linea__in=['GLOSA', 'SERVICIO'], then=Value(0, output_field=DecimalField())),
            default=Coalesce(F('venta_total') * 0.1, Value(0), output_field=DecimalField()),
            output_field=DecimalField()
        ),
        Porcentaje_Costo_Comisiones_alias=F('porcentaje_comision'),
        Costo_Envio_alias=F('costo_envio'),
        Costo_Envio_Calc_Neto_alias=F('c_valor_cobrado'),
        Costo_Comision_Calc_Neto_alias=F('c_comision_clp_neta'),
        Num_Sub_Orden_alias=Case(
            When(canal_id=5, then=Concat(Value('#'), F('n_orden'))),
            default=F('n_orden'),
            output_field=CharField()
        ),
        Num_Pedido_alias=F('n_pedido'),
        Estado_de_Despacho_alias=Value('Sin Información', output_field=CharField()),
        Porcentaje_Cobro_Comisiones_alias=F('porcentaje_comision'),
        Porcentaje_Comision_Nuevo_alias=F('porcentaje_comision'),
        Comision_CLP_Neta_alias=F('c_comision_clp_neta'),
        Costo_Envio_Teorico_Bruto_alias=F('costo_envio'),
        Costo_Envio_Teorico_Neto_alias=F('c_valor_cobrado'),
        Delta_alias=Value(0, output_field=DecimalField()),
        Margen_Operacional_CLP_alias=F('c_margen_clp'),
        Margen_Operacional_Porcentaje_alias=F('c_margen_porcentaje'),
        Marca_alias=F('sku__marca__nombre'),
        Subcategoria_alias=Case(
            When(tipo_linea='GLOSA', then=Value('Glosa')),
            default=F('sku__subcategoria'),
            output_field=CharField()
        ),
        Categoria_Principal_alias=Case(
            When(tipo_linea__in=['GLOSA', 'SERVICIO'], then=Value('')),
            default=F('sku__categoria_principal'),
            output_field=CharField()
        ),
        Tipo_Producto_alias=Case(
            When(tipo_linea__in=['GLOSA', 'SERVICIO'], then=Value('')),
            default=F('sku__tipo_producto'),
            output_field=CharField()
        ),
        Descripcion_alias=Case(
            When(tipo_linea='GLOSA', then=Value('Glosa')),
            default=F('sku__desc_corta'),
            output_field=CharField()
        ),
        Num_Semana_alias=F('n_semana'),
        Mes_alias=F('mes'),
        Ano_alias=F('año'),
        Tipo_Registro_alias=F('tipo_linea')
    ).values(
        'Origen_alias', 'Fecha_alias', 'Canal_alias', 'Canal_Id_alias',
        'SKU_Producto_alias', 'Cant_alias', 'Venta_Total_alias',
        'Valor_Unitario_alias', 'Valor_Neto_alias', 'Total_Neto_alias',
        'Costo_Calc_alias', 'Estado_de_Orden_alias', 'Tipo_de_Despacho_alias',
        'Costo_de_Marketplace_alias', 'Costo_de_Comisiones_alias',
        'Porcentaje_Costo_Comisiones_alias', 'Costo_Envio_alias',
        'Costo_Envio_Calc_Neto_alias', 'Costo_Comision_Calc_Neto_alias',
        'Num_Sub_Orden_alias', 'Num_Pedido_alias', 'Estado_de_Despacho_alias',
        'Porcentaje_Cobro_Comisiones_alias', 'Porcentaje_Comision_Nuevo_alias',
        'Comision_CLP_Neta_alias', 'Costo_Envio_Teorico_Bruto_alias',
        'Costo_Envio_Teorico_Neto_alias', 'Delta_alias',
        'Margen_Operacional_CLP_alias', 'Margen_Operacional_Porcentaje_alias',
        'Marca_alias', 'Subcategoria_alias', 'Categoria_Principal_alias',
        'Tipo_Producto_alias', 'Descripcion_alias',
        'Num_Semana_alias', 'Mes_alias', 'Ano_alias', 'Tipo_Registro_alias'
    )

    df = pd.DataFrame(list(ventas_bsale))

    if not df.empty and 'Mes_alias' in df.columns:
        df['Mes_alias'] = df['Mes_alias'].astype(str)
    if 'Tipo_Registro_alias' in df.columns:
        df['Tipo_Registro_alias'] = df['Tipo_Registro_alias'].str.capitalize()

    if not df.empty:
        # Canal Activo
        df['Canal_Activo_alias'] = df['Canal_Id_alias'].apply(
            lambda x: 'Sí' if x in CANAL_IDS_ACTIVOS else 'No'
        )
        # Ingreso por Reembolso — Bsale no tiene este concepto
        df['Ingreso_Reembolso_alias'] = 0

        df.rename(columns={
            'Origen_alias': 'Origen',
            'Fecha_alias': 'Fecha',
            'Canal_alias': 'Canal',
            'Canal_Activo_alias': 'Canal Activo',
            'SKU_Producto_alias': 'SKU Producto',
            'Cant_alias': 'Cant.',
            'Venta_Total_alias': 'Venta Total',
            'Valor_Unitario_alias': 'Valor Unitario',
            'Valor_Neto_alias': 'Valor Neto',
            'Total_Neto_alias': 'Total Neto',
            'Costo_Calc_alias': 'Costo Calc.',
            'Estado_de_Orden_alias': 'Estado de Orden',
            'Tipo_de_Despacho_alias': 'Tipo de Despacho',
            'Costo_de_Marketplace_alias': 'Costo de Marketplace',
            'Costo_de_Comisiones_alias': 'Costo de Comisiones',
            'Porcentaje_Costo_Comisiones_alias': '% Costo de Comisiones',
            'Costo_Envio_alias': 'Costo Envío',
            'Costo_Envio_Calc_Neto_alias': 'Costo Envio Calc. Neto',
            'Costo_Comision_Calc_Neto_alias': 'Costo Comision Calc. Neto',
            'Num_Sub_Orden_alias': 'N° Sub-Orden',
            'Num_Pedido_alias': 'N° Pedido',
            'Estado_de_Despacho_alias': 'Estado de Despacho',
            'Porcentaje_Cobro_Comisiones_alias': '% Cobro de Comisiones',
            'Porcentaje_Comision_Nuevo_alias': '% Comisión Nuevo',
            'Comision_CLP_Neta_alias': 'Comisión CLP Neta',
            'Costo_Envio_Teorico_Bruto_alias': 'Costo Envío Teórico Bruto',
            'Costo_Envio_Teorico_Neto_alias': 'Costo Envío Teórico Neto',
            'Delta_alias': '∆',
            'Margen_Operacional_CLP_alias': 'Margen Operacional CLP',
            'Margen_Operacional_Porcentaje_alias': 'Margen Operacional %',
            'Marca_alias': 'Marca',
            'Subcategoria_alias': 'Subcategoria',
            'Categoria_Principal_alias': 'Categoria Principal',
            'Tipo_Producto_alias': 'Tipo Producto',
            'Descripcion_alias': 'Descripción',
            'Num_Semana_alias': 'Num. Semana',
            'Mes_alias': 'Mes',
            'Ano_alias': 'Año',
            'Tipo_Registro_alias': 'Tipo Registro',
            'Ingreso_Reembolso_alias': 'Ingreso por Reembolso',
        }, inplace=True)

    return df


def _get_wivo_data(start_date, end_date, data_source, log=print):
    if data_source == 'Cyber':
        VentaWivoModel = VentaWivoCyber
        log("     -> Usando modelo: VentaWivoCyber (Cyber)")
    else:
        VentaWivoModel = VentaWivo
        log("     -> Usando modelo: VentaWivo (Testing)")

    ventas_wivo = VentaWivoModel.objects.filter(
        fecha_compra__range=(start_date, end_date)
    ).select_related(
        'canal', 'sku', 'estado_orden', 'tipo_despacho', 'estado_despacho', 'sku__proveedor', 'sku__marca'
    ).annotate(
        Origen_alias=Value('Wivo', output_field=CharField()),
        Fecha_alias=F('fecha_compra'),
        Canal_alias=F('canal__nombre'),
        Canal_Id_alias=F('canal_id'),
        SKU_Producto_alias=F('sku__sku'),
        Cant_alias=F('unidades'),
        Venta_Total_alias=F('ventas'),
        Valor_Unitario_alias=F('cc_v_venta_bruta_uni'),
        Valor_Neto_alias=F('cc_v_venta_neta'),
        Total_Neto_alias=F('cc_t_venta_neta'),
        Costo_Calc_alias=F('cc_costo'),
        Estado_de_Orden_alias=F('estado_orden__nombre'),
        Tipo_de_Despacho_alias=F('tipo_despacho__nombre'),
        Costo_de_Marketplace_alias=F('costo_marketplace'),
        Costo_de_Comisiones_alias=F('costo_comisiones'),
        Porcentaje_Costo_Comisiones_alias=F('porcentaje_costo_comisiones'),
        Costo_Envio_alias=F('costo_envio'),
        Costo_Cobro_Logistico_alias=F('cobro_costo_logistico'),
        Ingreso_Flex_alias=F('ingreso_envio_flex'),
        Ingreso_Total_alias=F('ingreso_total'),
        Despacho_Pagado_alias=F('despacho_pagado_comprador'),
        Ingreso_Promo_alias=F('ingreso_promocion'),
        Costo_Total_alias=F('costo_total'),
        Num_Sub_Orden_alias=Case(
            When(canal_id=5, then=Concat(Value('#'), F('n_suborden'))),
            default=F('n_suborden'),
            output_field=CharField()
        ),
        Num_Pedido_alias=Case(
            When(canal_id=5, then=Concat(Value('#'), F('n_orden'))),
            default=F('n_orden'),
            output_field=CharField()
        ),
        Estado_de_Despacho_alias=F('estado_despacho__nombre'),
        Otros_Costos_alias=F('cc_otros_costos'),
        Otros_Ingresos_alias=F('cc_otros_ingresos'),
        Costo_Fijo_ML_alias=F('cc_costo_fijo_ml'),
        Costo_Envio_Calc_Neto_alias=F('cc_costo_envio'),
        Costo_Comision_Calc_Neto_alias=F('cc_costo_comisiones'),
        Porcentaje_Cobro_Comisiones_alias=F('cc_porcentaje_comision'),
        Porcentaje_Comision_Nuevo_alias=F('cc_porcentaje_comision'),
        Comision_CLP_Neta_alias=F('cc_comision_clp'),
        Costo_Envio_Teorico_Bruto_alias=F('cc_costo_envio_mktp_bruto'),
        Costo_Envio_Teorico_Neto_alias=F('cc_costo_envio_mktp_neto'),
        Delta_alias=F('cc_delta_costo_envios'),
        Margen_Explotacion_CLP_alias=F('cc_margen_explotacion_clp'),
        Margen_Explotacion_Porcentaje_alias=F('cc_margen_explotacion_porcentaje'),
        Margen_CLP_alias=F('cc_margen_clp'),
        Margen_Porcentaje_alias=F('cc_margen_porcentaje'),
        Margen_Operacional_CLP_alias=F('cc_margen_operacional_clp'),
        Margen_Operacional_Porcentaje_alias=F('cc_margen_operacional_porcentaje'),
        Tipo_Calculo_alias=F('tipo_cc'),
        MultiOrden_alias=F('multi_orden'),
        Marca_alias=F('sku__marca__nombre'),
        Subcategoria_alias=F('sku__subcategoria'),
        Categoria_Principal_alias=F('sku__categoria_principal'),
        Tipo_Producto_alias=F('sku__tipo_producto'),
        Descripcion_alias=F('sku__desc_corta'),
        Num_Semana_alias=F('n_semana'),
        Mes_alias=F('mes'),
        Ano_alias=F('año'),
        Tipo_Registro_alias=Value('Producto', output_field=CharField()),
        # Campos para reembolso no explicado (canal 68)
        Reembolso_Total_alias=F('reembolso_total'),
        Reembolso_Envio_alias=F('reembolso_envio'),
        Reembolso_Comisiones_alias=F('reembolso_comisiones'),
        Reembolso_Ajuste_Comision_alias=F('reembolso_ajuste_sobre_comision'),
        Reembolso_Ajuste_Venta_alias=F('reembolso_ajuste_sobre_venta'),
        Reembolso_Logistica_alias=F('reembolso_logistica_inversa'),
        Reembolso_Almacenamiento_alias=F('reembolso_servicio_almacenamiento'),
        Reembolsos_Sin_Cat_alias=F('reembolsos_sin_categorizar'),
        Devolucion_Penalizacion_alias=F('devolucion_penalizacion_cancelacion'),
    ).values(
        'Origen_alias', 'Fecha_alias', 'Canal_alias', 'Canal_Id_alias',
        'SKU_Producto_alias', 'Cant_alias', 'Venta_Total_alias',
        'Valor_Unitario_alias', 'Valor_Neto_alias', 'Total_Neto_alias',
        'Costo_Calc_alias', 'Estado_de_Orden_alias', 'Tipo_de_Despacho_alias',
        'Costo_de_Marketplace_alias', 'Costo_de_Comisiones_alias',
        'Porcentaje_Costo_Comisiones_alias', 'Costo_Envio_alias',
        'Costo_Cobro_Logistico_alias', 'Ingreso_Flex_alias', 'Ingreso_Total_alias',
        'Despacho_Pagado_alias', 'Ingreso_Promo_alias', 'Costo_Total_alias',
        'Num_Sub_Orden_alias', 'Num_Pedido_alias', 'Estado_de_Despacho_alias',
        'Otros_Costos_alias', 'Otros_Ingresos_alias', 'Costo_Fijo_ML_alias',
        'Costo_Envio_Calc_Neto_alias', 'Costo_Comision_Calc_Neto_alias',
        'Porcentaje_Cobro_Comisiones_alias', 'Porcentaje_Comision_Nuevo_alias',
        'Comision_CLP_Neta_alias', 'Costo_Envio_Teorico_Bruto_alias',
        'Costo_Envio_Teorico_Neto_alias', 'Delta_alias',
        'Margen_Explotacion_CLP_alias', 'Margen_Explotacion_Porcentaje_alias',
        'Margen_CLP_alias', 'Margen_Porcentaje_alias',
        'Margen_Operacional_CLP_alias', 'Margen_Operacional_Porcentaje_alias',
        'Tipo_Calculo_alias', 'MultiOrden_alias', 'Marca_alias',
        'Subcategoria_alias', 'Categoria_Principal_alias', 'Tipo_Producto_alias',
        'Descripcion_alias', 'Num_Semana_alias',
        'Mes_alias', 'Ano_alias', 'Tipo_Registro_alias',
        'Reembolso_Total_alias', 'Reembolso_Envio_alias', 'Reembolso_Comisiones_alias',
        'Reembolso_Ajuste_Comision_alias', 'Reembolso_Ajuste_Venta_alias',
        'Reembolso_Logistica_alias', 'Reembolso_Almacenamiento_alias',
        'Reembolsos_Sin_Cat_alias', 'Devolucion_Penalizacion_alias',
    )

    df = pd.DataFrame(list(ventas_wivo))

    if not df.empty and 'Mes_alias' in df.columns:
        df['Mes_alias'] = df['Mes_alias'].astype(str)

    if not df.empty:
        # Canal Activo
        df['Canal_Activo_alias'] = df['Canal_Id_alias'].apply(
            lambda x: 'Sí' if x in CANAL_IDS_ACTIVOS else 'No'
        )

        # Ingreso por Reembolso — solo canal 68
        def calc_reembolso_no_explicado(row):
            if row['Canal_Id_alias'] != 68:
                return 0
            reembolsos_explicados = (
                (row['Reembolso_Envio_alias'] or 0) +
                (row['Reembolso_Comisiones_alias'] or 0) +
                (row['Reembolso_Ajuste_Comision_alias'] or 0) +
                (row['Reembolso_Ajuste_Venta_alias'] or 0) +
                (row['Reembolso_Logistica_alias'] or 0) +
                (row['Reembolso_Almacenamiento_alias'] or 0) +
                (row['Reembolsos_Sin_Cat_alias'] or 0) +
                (row['Devolucion_Penalizacion_alias'] or 0)
            )
            reembolso_total = row['Reembolso_Total_alias'] or 0
            residuo = reembolso_total - reembolsos_explicados
            # Convertimos residuo a float para evitar el TypeError con el float 1.19
            return round(max(float(residuo) / 1.19, 0), 2)

        df['Ingreso_Reembolso_alias'] = df.apply(calc_reembolso_no_explicado, axis=1)

        # Eliminar columnas auxiliares de reembolso
        df.drop(columns=[
            'Reembolso_Total_alias', 'Reembolso_Envio_alias', 'Reembolso_Comisiones_alias',
            'Reembolso_Ajuste_Comision_alias', 'Reembolso_Ajuste_Venta_alias',
            'Reembolso_Logistica_alias', 'Reembolso_Almacenamiento_alias',
            'Reembolsos_Sin_Cat_alias', 'Devolucion_Penalizacion_alias',
        ], inplace=True)

        df.rename(columns={
            'Origen_alias': 'Origen',
            'Fecha_alias': 'Fecha',
            'Canal_alias': 'Canal',
            'Canal_Activo_alias': 'Canal Activo',
            'SKU_Producto_alias': 'SKU Producto',
            'Cant_alias': 'Cant.',
            'Venta_Total_alias': 'Venta Total',
            'Valor_Unitario_alias': 'Valor Unitario',
            'Valor_Neto_alias': 'Valor Neto',
            'Total_Neto_alias': 'Total Neto',
            'Costo_Calc_alias': 'Costo Calc.',
            'Estado_de_Orden_alias': 'Estado de Orden',
            'Tipo_de_Despacho_alias': 'Tipo de Despacho',
            'Costo_de_Marketplace_alias': 'Costo de Marketplace',
            'Costo_de_Comisiones_alias': 'Costo de Comisiones',
            'Porcentaje_Costo_Comisiones_alias': '% Costo de Comisiones',
            'Costo_Envio_alias': 'Costo Envío',
            'Costo_Cobro_Logistico_alias': 'Costo Cobro Logístico',
            'Ingreso_Flex_alias': 'Ingreso por Envío Flex',
            'Ingreso_Total_alias': 'Ingreso Total',
            'Ingreso_Reembolso_alias': 'Ingreso por Reembolso',
            'Despacho_Pagado_alias': 'Despacho pagado por comprador',
            'Ingreso_Promo_alias': 'Ingreso por promoción',
            'Costo_Total_alias': 'Costo Total',
            'Num_Sub_Orden_alias': 'N° Sub-Orden',
            'Num_Pedido_alias': 'N° Pedido',
            'Estado_de_Despacho_alias': 'Estado de Despacho',
            'Otros_Costos_alias': 'Otros Costos',
            'Otros_Ingresos_alias': 'Otros Ingresos',
            'Costo_Fijo_ML_alias': 'Costo Fijo ML',
            'Costo_Envio_Calc_Neto_alias': 'Costo Envio Calc. Neto',
            'Costo_Comision_Calc_Neto_alias': 'Costo Comision Calc. Neto',
            'Porcentaje_Cobro_Comisiones_alias': '% Cobro de Comisiones',
            'Porcentaje_Comision_Nuevo_alias': '% Comisión Nuevo',
            'Comision_CLP_Neta_alias': 'Comisión CLP Neta',
            'Costo_Envio_Teorico_Bruto_alias': 'Costo Envío Teórico Bruto',
            'Costo_Envio_Teorico_Neto_alias': 'Costo Envío Teórico Neto',
            'Delta_alias': '∆',
            'Margen_Explotacion_CLP_alias': 'Margen Explotación CLP',
            'Margen_Explotacion_Porcentaje_alias': 'Margen Explotación %',
            'Margen_CLP_alias': 'Margen CLP',
            'Margen_Porcentaje_alias': 'Margen %',
            'Margen_Operacional_CLP_alias': 'Margen Operacional CLP',
            'Margen_Operacional_Porcentaje_alias': 'Margen Operacional %',
            'Tipo_Calculo_alias': 'Tipo Cálculo',
            'MultiOrden_alias': 'MultiOrden',
            'Marca_alias': 'Marca',
            'Subcategoria_alias': 'Subcategoria',
            'Categoria_Principal_alias': 'Categoria Principal',
            'Tipo_Producto_alias': 'Tipo Producto',
            'Descripcion_alias': 'Descripción',
            'Num_Semana_alias': 'Num. Semana',
            'Mes_alias': 'Mes',
            'Ano_alias': 'Año',
            'Tipo_Registro_alias': 'Tipo Registro',
        }, inplace=True)

    return df


def _get_nc_data(start_date, end_date, data_source, log=print):
    if data_source == 'Cyber':
        NotasCreditoModel = NotasCreditoCyber
        log("     -> Usando modelo: NotasCreditoCyber (Cyber)")
    else:
        NotasCreditoModel = NotasCredito
        log("     -> Usando modelo: NotasCredito (Testing)")

    ncs = NotasCreditoModel.objects.filter(
        fecha_emision__range=(start_date, end_date)
    ).select_related('sku', 'sku__proveedor', 'sku__marca').annotate(
        Origen_alias=Value('Bsale', output_field=CharField()),
        Fecha_alias=F('fecha_emision'),
        Canal_alias=Value('NC', output_field=CharField()),
        Estado_de_Orden_alias=Value('NC', output_field=CharField()),
        Tipo_de_Despacho_alias=Value('NC', output_field=CharField()),
        SKU_Producto_alias=F('sku__sku'),
        Cant_alias=F('cantidad'),
        Venta_Total_alias=F('monto_total'),
        Valor_Unitario_alias=Cast(F('monto_neto_unitario') * 1.19, DecimalField(max_digits=15, decimal_places=2)),
        Valor_Neto_alias=F('monto_neto_unitario'),
        Total_Neto_alias=F('monto_neto_total'),
        Num_Sub_Orden_alias=F('doc_referencia'),
        Num_Pedido_alias=F('n_nota_credito'),
        Marca_alias=F('sku__marca__nombre'),
        Subcategoria_alias=F('sku__subcategoria'),
        Categoria_Principal_alias=F('sku__categoria_principal'),
        Tipo_Producto_alias=F('sku__tipo_producto'),
        Descripcion_alias=F('sku__desc_corta'),
        Num_Semana_alias=F('n_semana'),
        Mes_alias=F('mes'),
        Ano_alias=F('año'),
        Tipo_Registro_alias=F('tipo'),
    ).values(
        'Origen_alias', 'Fecha_alias', 'Canal_alias', 'Estado_de_Orden_alias',
        'Tipo_de_Despacho_alias', 'SKU_Producto_alias', 'Cant_alias',
        'Venta_Total_alias', 'Valor_Unitario_alias', 'Valor_Neto_alias',
        'Total_Neto_alias', 'Num_Sub_Orden_alias', 'Num_Pedido_alias',
        'Marca_alias', 'Subcategoria_alias', 'Categoria_Principal_alias',
        'Tipo_Producto_alias', 'Descripcion_alias',
        'Num_Semana_alias', 'Mes_alias', 'Ano_alias', 'Tipo_Registro_alias'
    )

    df = pd.DataFrame(list(ncs))

    if not df.empty and 'Mes_alias' in df.columns:
        df['Mes_alias'] = df['Mes_alias'].astype(str)
    if 'Tipo_Registro_alias' in df.columns:
        df['Tipo_Registro_alias'] = df['Tipo_Registro_alias'].str.capitalize()

    if not df.empty:
        df['Canal_Activo_alias'] = 'No'
        df['Ingreso_Reembolso_alias'] = 0
        df.rename(columns={
            'Origen_alias': 'Origen', 'Fecha_alias': 'Fecha',
            'Canal_alias': 'Canal', 'Canal_Activo_alias': 'Canal Activo',
            'Estado_de_Orden_alias': 'Estado de Orden',
            'Tipo_de_Despacho_alias': 'Tipo de Despacho',
            'SKU_Producto_alias': 'SKU Producto', 'Cant_alias': 'Cant.',
            'Venta_Total_alias': 'Venta Total', 'Valor_Unitario_alias': 'Valor Unitario',
            'Valor_Neto_alias': 'Valor Neto', 'Total_Neto_alias': 'Total Neto',
            'Num_Sub_Orden_alias': 'N° Sub-Orden', 'Num_Pedido_alias': 'N° Pedido',
            'Marca_alias': 'Marca', 'Subcategoria_alias': 'Subcategoria',
            'Categoria_Principal_alias': 'Categoria Principal',
            'Tipo_Producto_alias': 'Tipo Producto',
            'Descripcion_alias': 'Descripción', 'Num_Semana_alias': 'Num. Semana',
            'Mes_alias': 'Mes', 'Ano_alias': 'Año',
            'Tipo_Registro_alias': 'Tipo Registro',
            'Ingreso_Reembolso_alias': 'Ingreso por Reembolso',
        }, inplace=True)

    return df


def _get_nd_data(start_date, end_date, log=print):
    nds = NotasDebito.objects.filter(
        fecha_emision__range=(start_date, end_date)
    ).select_related('sku', 'sku__proveedor', 'sku__marca').annotate(
        Origen_alias=Value('Bsale', output_field=CharField()),
        Fecha_alias=F('fecha_emision'),
        Canal_alias=Value('ND', output_field=CharField()),
        SKU_Producto_alias=F('sku__sku'),
        Cant_alias=F('cantidad'),
        Venta_Total_alias=F('monto_total'),
        Valor_Unitario_alias=Cast(F('monto_neto_unitario') * 1.19, DecimalField(max_digits=15, decimal_places=2)),
        Valor_Neto_alias=F('monto_neto_unitario'),
        Total_Neto_alias=F('monto_neto_total'),
        Num_Sub_Orden_alias=F('doc_referencia'),
        Num_Pedido_alias=F('n_nota_debito'),
        Marca_alias=F('sku__marca__nombre'),
        Subcategoria_alias=F('sku__subcategoria'),
        Categoria_Principal_alias=F('sku__categoria_principal'),
        Tipo_Producto_alias=F('sku__tipo_producto'),
        Descripcion_alias=F('sku__desc_corta'),
        Num_Semana_alias=F('n_semana'),
        Mes_alias=F('mes'),
        Ano_alias=F('año'),
        Tipo_Registro_alias=F('tipo'),
    ).values(
        'Origen_alias', 'Fecha_alias', 'Canal_alias', 'SKU_Producto_alias',
        'Cant_alias', 'Venta_Total_alias', 'Valor_Unitario_alias',
        'Valor_Neto_alias', 'Total_Neto_alias', 'Num_Sub_Orden_alias',
        'Num_Pedido_alias', 'Marca_alias', 'Subcategoria_alias',
        'Categoria_Principal_alias', 'Tipo_Producto_alias',
        'Descripcion_alias', 'Num_Semana_alias', 'Mes_alias',
        'Ano_alias', 'Tipo_Registro_alias'
    )

    df = pd.DataFrame(list(nds))

    if not df.empty and 'Mes_alias' in df.columns:
        df['Mes_alias'] = df['Mes_alias'].astype(str)
    if 'Tipo_Registro_alias' in df.columns:
        df['Tipo_Registro_alias'] = df['Tipo_Registro_alias'].str.capitalize()

    if not df.empty:
        df['Canal_Activo_alias'] = 'No'
        df['Ingreso_Reembolso_alias'] = 0
        df.rename(columns={
            'Origen_alias': 'Origen', 'Fecha_alias': 'Fecha',
            'Canal_alias': 'Canal', 'Canal_Activo_alias': 'Canal Activo',
            'SKU_Producto_alias': 'SKU Producto', 'Cant_alias': 'Cant.',
            'Venta_Total_alias': 'Venta Total', 'Valor_Unitario_alias': 'Valor Unitario',
            'Valor_Neto_alias': 'Valor Neto', 'Total_Neto_alias': 'Total Neto',
            'Num_Sub_Orden_alias': 'N° Sub-Orden', 'Num_Pedido_alias': 'N° Pedido',
            'Marca_alias': 'Marca', 'Subcategoria_alias': 'Subcategoria',
            'Categoria_Principal_alias': 'Categoria Principal',
            'Tipo_Producto_alias': 'Tipo Producto',
            'Descripcion_alias': 'Descripción', 'Num_Semana_alias': 'Num. Semana',
            'Mes_alias': 'Mes', 'Ano_alias': 'Año',
            'Tipo_Registro_alias': 'Tipo Registro',
            'Ingreso_Reembolso_alias': 'Ingreso por Reembolso',
        }, inplace=True)

    return df


def generar_reporte(start_date, end_date, output_dir, data_source='Testing',
                    selected_columns=None, log=print):
    """
    Genera el archivo Excel del reporte consolidado y devuelve la ruta final.

    - start_date, end_date: objetos date/datetime.
    - output_dir: carpeta de salida.
    - data_source: 'Testing' o 'Cyber'.
    - selected_columns: lista de columnas a exportar (por defecto, todas).
    """
    if selected_columns is None:
        selected_columns = list(FINAL_COLUMNS)

    log(f"Fechas seleccionadas: {start_date.strftime('%Y-%m-%d')} a {end_date.strftime('%Y-%m-%d')}")
    log(f"Fuente de datos seleccionada: {data_source}")

    log("1/5 - Obteniendo datos de Bsale...")
    df_bsale = _get_bsale_data(start_date, end_date, data_source, log)
    log(f"     Se encontraron {len(df_bsale)} registros de Bsale.")

    log("2/5 - Obteniendo datos de Wivo...")
    df_wivo = _get_wivo_data(start_date, end_date, data_source, log)
    log(f"     Se encontraron {len(df_wivo)} registros de Wivo.")

    log("3/5 - Obteniendo datos de Notas de Crédito...")
    df_nc = _get_nc_data(start_date, end_date, data_source, log)
    log(f"     Se encontraron {len(df_nc)} registros de NC.")

    log("4/5 - Obteniendo datos de Notas de Débito...")
    df_nd = _get_nd_data(start_date, end_date, log)
    log(f"     Se encontraron {len(df_nd)} registros de ND.")

    log("5/5 - Consolidando y generando el archivo Excel...")
    df_final = pd.concat([df_bsale, df_wivo, df_nc, df_nd], ignore_index=True)

    # Ajuste cantidades negativas
    log("     Ajustando cantidades negativas para NC y devoluciones...")
    if 'Cant.' not in df_final.columns:
        df_final['Cant.'] = 0
    else:
        df_final['Cant.'] = pd.to_numeric(df_final['Cant.'], errors='coerce').fillna(0)

    if 'Canal' not in df_final.columns:
        df_final['Canal'] = ''
    else:
        df_final['Canal'] = df_final['Canal'].fillna('')

    if 'Estado de Orden' not in df_final.columns:
        df_final['Estado de Orden'] = ''
    else:
        df_final['Estado de Orden'] = df_final['Estado de Orden'].fillna('')

    df_final.loc[df_final['Canal'] == 'NC', 'Cant.'] = -df_final.loc[df_final['Canal'] == 'NC', 'Cant.'].abs()
    estados_negativos = ['Cancelada', 'Devuelta']
    df_final.loc[df_final['Estado de Orden'].isin(estados_negativos), 'Cant.'] = -df_final.loc[df_final['Estado de Orden'].isin(estados_negativos), 'Cant.'].abs()

    # Reindexar con todas las columnas posibles
    df_final = df_final.reindex(columns=FINAL_COLUMNS)

    # Tipos numéricos
    for col in NUMERIC_COLS:
        if col in df_final.columns:
            df_final[col] = pd.to_numeric(df_final[col], errors='coerce').fillna(0)

    # Tipos texto
    object_cols = [col for col in df_final.columns if col not in NUMERIC_COLS]
    for col in object_cols:
        if col in df_final.columns:
            df_final[col] = df_final[col].fillna('')

    # Filtrar solo columnas seleccionadas por el usuario
    cols_a_exportar = [c for c in FINAL_COLUMNS if c in selected_columns]
    df_export = df_final[cols_a_exportar]

    # Nombre de archivo con rango de fechas
    fecha_inicio_str = start_date.strftime('%d-%m-%Y')
    fecha_fin_str = end_date.strftime('%d-%m-%Y')
    filename = f"Ventas-{fecha_inicio_str}_al_{fecha_fin_str}.xlsx"
    output_path = os.path.join(output_dir, filename)

    log("Creando archivo Excel...")
    with pd.ExcelWriter(
        output_path,
        engine='xlsxwriter',
        engine_kwargs={'options': {'decimal_point': ','}}
    ) as writer:
        df_export.to_excel(writer, index=False, sheet_name=HOJA_VENTAS_CONSOLIDADAS)

    log(f"¡Éxito! El archivo ha sido guardado en: {output_path}")
    return output_path
