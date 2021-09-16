# -*- coding: utf-8 -*-


from odoo import models, fields, api
# pyTelegramBotAPI
import telebot # Importamos las librería

TOKEN = '1998721499:AAEANtp7-E7JwRk0D3esngYflc_n-tu1qWk' # Ponemos nuestro Token generado con el @BotFather
tb = telebot.TeleBot(TOKEN)

# tb.send_message('-533761534', 'HOLA DESDE PAYTHON') # Ejemplo tb.send_message('109556849', 'Hola mundo!')
# tb.send_message('-533761534', 'HOLA DESDE PAYTHON') # Ejemplo tb.send_message('109556849', 'Hola mundo!')


# class my_telegram(models.Model):
#     _name = 'my_telegram.my_telegram'
#     _description = 'my_telegram.my_telegram'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class LeadExtend(models.Model):
    _name  =  "crm.lead"
    _inherit = "crm.lead"
    # @api.depends('create_date')
    # @api.onchange('create_date')
    # @api.model
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('website'):
                vals['website'] = self.env['res.partner']._clean_website(vals['website'])
        leads = super(LeadExtend, self).create(vals_list)

        for lead, values in zip(leads, vals_list):
            if any(field in ['active', 'stage_id'] for field in values):
                lead._handle_won_lost(values)
        SMS = "**Nuevo LEAD**\n"
        SMS = SMS +  "Nombre: " + lead.name + "\n"
        SMS = SMS +  "Contacto: " + lead.contact_name + "\n"
        SMS = SMS +  "Descripción: " + lead.description + "\n"
        SMS = SMS +  "Email: " + lead.email_from + "\n"
        SMS = SMS +  "Esperado: " + str(lead.expected_revenue) + "\n"
        SMS = SMS +  "Probabilidad: " + str(lead.automated_probability) + "%\n"
        SMS = SMS +  "Teléfono: " + lead.phone + "\n"


 

        tb.send_message('-533761534', SMS) # Ejemplo tb.send_message('109556849', 'Hola mundo!')

        return leads