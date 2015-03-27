# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#    Proyecto:   Testing
#    Fecha:      07/02/2015
#    Autor:      Felipe Ferreira
#    Compañia:   Datamatic - www.datamatic.com.uy
##############################################################################

from datetime import timedelta
from openerp import models, fields, api, exceptions

class reporte_lmo(models.Model):
    _name = 'reporte.lmo'

    #Cabezal
    empleador_id = fields.Many2one('res.partner', string="Nombre empleador")
    empleado_id = fields.Many2one('hr.employee', string="Nombre empleado")
    c_i =  fields.Char(string="C.I.:", required=True)
    categoria = fields.Selection([
    ('sd', "Servicio Domestico"),
    ('o', "Otros"),
    ])
    fecha_ingerso = fields.Date(string="Ingreso")
    fecha = fields.Date(string="Fecha", default=fields.Date.today)
    turno =  fields.Char(string="Turno", required=True)
    liquidacion =  fields.Char(string="Liquidacion", required=True)

    #Columnas
    codigo = fields.Char(string="Codigo")
    descripcion = fields.Char(string="Descripcion")
    cantidad = fields.Float(string="Cantidad")
    haberes = fields.Char(string="Haberes")
    retenciones = fields.Char(string="Retenciones")
    totales = fields.Float(string="Totales") #aca tengo que sumar los haberes y las retenciones
    liquido = fields.Float(string="Liquido") #aca tengo que sumar solo los haberes