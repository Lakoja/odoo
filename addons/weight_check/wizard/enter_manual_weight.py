# -*- coding: utf-8 -*-

from odoo import fields, models


class CheckManualWeight(models.TransientModel):
    _name = 'weight.check.manual'
    _description = 'Check for manual weight'

    picking_id = fields.Many2one('stock.picking', required=True, ondelete="cascade")
    manual_weight = fields.Float('Weighted Weight', store=True, readonly=False)

    def button_confirm(self):
        if self.manual_weight > 0:
            self.picking_id.weighted_weight = self.manual_weight
