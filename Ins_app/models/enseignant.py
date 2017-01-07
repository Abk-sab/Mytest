from openerp import fields,api,models

class Ens(models.Model):
	_name='mod.enseignant'
	
	nom=fields.Char('Nom')
	prenom=fields.Char('Prenom')
	cours_ens=fields.Many2one('mod.cours','Cours')
	grade=fields.Selection((('mca','Maitre Assisstant'), ('Dr','Docteur')),'Grade')
	image2=fields.Binary("image")
	