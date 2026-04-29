# -*- coding: utf-8 -*-
{
    'name': 'MRG SCV Nominas',
    'version': '16.0.1.0.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Modificaciones al reporte SCV de nómina',
    'description': """
        Módulo para heredar y modificar el reporte SCV emitido desde la nómina.
    """,
    'author': 'Antigravity / Mario Gomez',
    'depends': [
        'hr_payroll',
        'treming_sv_payroll',
    ],
    'data': [
        'views/hr_planilla_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
