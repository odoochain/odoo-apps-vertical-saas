from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class product_template(models.Model):
    _inherit = "product.template"

    license_type_id = fields.Many2one('license.type')
    license_ok = fields.Boolean(
        'Can be licensed',
        help='If set, confirming a sale order with this product will create a license.')
    license_policy = fields.Selection(
        [('quantity', 'License per quantity'),
         ('product', 'License per product')],
         default='order',
        help='License per quantity: Generate a license for each ordered quantity.\n'
             'License per product: Generate a single license for a product order.')