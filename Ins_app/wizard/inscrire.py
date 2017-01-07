from openerp import api,fields,models

class  Wiz(models.TransientModel):
	_name='wizard.ins'
	#nom=fields.Char('Nom')
	#ddn=fields.Date('Date De Naissance')
	#cours=fields.One2many('mod.cours')
	#sexe=fields.Selection((('f','Feminin'), ('m','Masculin')),'sexe')
	#ens_par=fields.One2many('mod.enseignant')
	state=fields.Selection([('draft','Draft'),('save','Save'),('download','Download')],required='true' , default='draft',track_visibility='onchange')

	@api.multi
	def fun(self):
            print 'beforeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
	    start_view=self.env.ref('Ins_app.wiz_view')
            print 'hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
            print start_view
            print 'hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
	    return {
             'name': 'Inscription',
             'view_mode': 'form',
             'view_id': 'view_form_ins_wiz',
             'views': [('view_form_ins_wiz', 'form')],
             'view_type': 'form',
             'res_model': 'wizard.ins',
             'type': 'ir.actions.act_window',

             'target': 'new',
             'res_id': self.id,
                      }
        @api.one
        def act_save(self):
	    self.state='save'


        @api.one
        def act_download(self):
          self.state='download'



		
