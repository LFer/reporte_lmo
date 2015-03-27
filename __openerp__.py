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
#    Proyecto:   Reporte de liquidacion de sueldos
#    Fecha:      27/03/2015
#    Autor:      Felipe Ferreira
#    Compañia:   Datamatic - www.datamatic.com.uy
#    Adecuacion: Reporte
##############################################################################

{
    'name': 'Reporte LMO',
    'version': '1.0',
    'author': 'Felipe Ferreira',
    'website': 'www.datamatic.com.uy',
    'category': 'Reportes',
    'images': [],
    'depends': ['hr'],
    'description': """
Genera Recibo de sueldo
""",
    'demo': [],
    'test': [],
    'data': [
        'reporte_lmo_view.xml',
        'views/report_reporte_lmo.xml'
            ],
    'installable': True,
    'auto_install': False,
}