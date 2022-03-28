from odoo.tests import common
from odoo.exceptions import ValidationError

class TestHelpdeskTest(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.ticket = self.env['helpdesk.ticket'].create({
            'name' : 'Test ticket'
        })
        self.user_id = self.ref('base.user_admin')

    def test_01_ticket(self):
        self.assertEqual(self.ticket.name, 'Test ticket')
        
    def test_02_ticket(self):
        self.assertFalse(self.ticket.name =='Teswefft ticket')
        
    def test_03_ticket(self):
        self.assertEqual(self.ticket.user_id, self.env['res.users']) # ESTE NO FUNCIONA, CREO QUE PQ NO INSTALE EN UN PRINCIPIO CON DATOS DEMOS
        self.ticket.user_id = self.user_id
        self.assertEqual(self.ticket.user_id.id, self.user_id)
        
    def test_04_ticket(self):
        self.ticket.time = 2
        self.assertEqual(self.ticket.time, 2)
        self.ticket.time = 0
        self.assertEqual(self.ticket.time, 0)
        with self.assertRaises(ValidationError), self.cr.savepoint():
            self.ticket.time = -5
