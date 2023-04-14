# -*- coding: utf-8 -*-
from odoo import models, fields, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    weighted_weight = fields.Float('Manual Weight', help="Manually weighted weight of a package.", default=0)

    def _pre_put_in_pack_hook(self, move_line_ids):
        res = super(StockPicking, self)._pre_put_in_pack_hook(move_line_ids)
        if not res:
            if self.weighted_weight == 0:
                return self._set_weighted_weight_dialog()
            else:
                return res
        else:
            return res

    def _set_weighted_weight_dialog(self):
        self.ensure_one()
        view_id = self.env.ref('weight_check.weight_check_manual_view_form').id
        context = dict(
            self.env.context,
            default_picking_id=self.id
        )
        return {
            'name': 'Weigh package',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'weight.check.manual',
            'view_id': view_id,
            'views': [(view_id, 'form')],
            'target': 'new',
            'context': context,
        }

    def _pre_action_done_hook(self):
        if self.weighted_weight == 0:
            return self._set_weighted_weight_dialog()

        return True
