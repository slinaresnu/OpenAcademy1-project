from openerp import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course' #model odoo name
    name = fields.Char(string='Title', required=True) #field reserved to identified name rec
    description = fields.Text(string='Description')
