# -*- coding: utf-8 -*-
from odoo import api, fields, models
import base64

class HrPlanilla(models.Model):
    _inherit = 'hr.planilla'

    def action_generate_scv_csv(self):
        if not self:
            return True
        content = ""
        for record in self:
            for line in record.planilla_lines:
                # Cuenta (solo números)
                acc_number = line.employee_id.bank_account_id.acc_number or ""
                acc_number_clean = "".join(filter(str.isdigit, acc_number))
                
                # Monto (Regla Líquido - LIQUIDTR)
                # Buscamos en reglas_ids de la línea de planilla
                liq_rule = line.reglas_ids.filtered(lambda r: r.salary_rule_id.code == 'LIQUIDTR')
                amount = sum(liq_rule.mapped('total'))
                
                # Nombres (Primer nombre y primer apellido) en MAYÚSCULAS y separados por espacio
                first_name = (line.employee_id.nombres or "").strip().split(" ")[0].upper()
                first_surname = (line.employee_id.apellidos or "").strip().split(" ")[0].upper()
                
                full_name = f"{first_name} {first_surname}"
                
                # Formato final: Cuenta,Monto,Nombre Apellido
                content += f"{acc_number_clean},{amount:.2f},{full_name}\n"
            
        # Codificar contenido
        content_bytes = content.encode('utf-8')
        content_b64 = base64.b64encode(content_bytes)
        
        # Guardar en el campo doc_csv de todos los registros seleccionados
        self.write({'doc_csv': content_b64})
        
        # Retornar acción para descargar el archivo (usando el primer ID del conjunto)
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/?model=hr.planilla&id={self.ids[0]}&field=doc_csv&download=true&filename=planilla_scv.csv',
            'target': 'self',
        }
