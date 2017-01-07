from openerp import fields,api,models

class Ins(models.Model):
    _name='mod.inscription'
    nom=fields.Char('Nom')
    prenom=fields.Char('Prenom')
    sexe=fields.Selection((('f','Feminin'), ('m','Masculin')),'sexe')
    ddn=fields.Date('Date de Naissance')
    image1=fields.Binary("image")

    @api.one
    def call_wizz(self):
       # id=self.env['wizard.ins']#create({'nom':self.nom,'ddn':self.ddn,'sexe':self.sexe})
        
        return self.env['wizard.ins'].fun()  
        

