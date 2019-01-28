from odoo import models, fields, api

class Modelo(models.Model):
    _name = 'calculo2.modelo'
    nombre = fields.Char('Articulo', required=True)
    precio = fields.Integer('Precio', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    total = fields.Float(string='Total', compute='_total')

    @api.one
    @api.depends('precio', 'cantidad')
    def _total(self):
        self.total = self.precio * self.cantidad

