from openerp import fields,api,models

class Cours(models.Model):
	_name='mod.cours'
	nom=fields.Char('Nom')
	description=fields.Char('Description')
	nb_s=fields.Integer('Nombre de seance')
        enseignant=fields.One2many('mod.enseignant','cours_ens')
	
