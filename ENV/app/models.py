from app import db

class student(db.Model):
	id = db.Column('sutent_id',db.Integer, primary_key=True)
	codigo = db.Column(db.String(20), primary_key=True)
	name = db.Column(db.String(100), index=True, unique=True)
	resp = db.Column(db.String(100), index=True, unique=True)
	parent = db.Column(db.String(20), index=True, unique=True)
	ender = db.Column(db.String(120), index=True, unique=True)
	city = db.Column(db.String(30), index=True, unique=True)
	telef = db.Column(db.String(30), index=True, unique=True)
	teleff = db.Column(db.String(30), index=True, unique=True)
	email = db.Column(db.String(50), index=True, unique=True)

	def __repr__(self, codigo, name, resp, parent, ender, city, telef, teleff, email):
		self.codigo = codigo
		self.name = name
		self.resp = resp
		self.parent = parent
		self.ender = ender
		self.city = city
		self.telef = telef
		self.teleff = teleff
		self.email = email


class estoque(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	quant = db.Column(db.String(20), index=True, unique=True)
	materi = db.Column(db.String(20), index=True, unique=True)
	price = db.Column(db.String(30), index=True, unique=True)
	categ = db.Column(db.String(30), index=True, unique=True)
	visto = db.Column(db.String(50), index=True, unique=True)
	obser = db.Column(db.String(300), index=True, unique=True)

	def __repr__(self, quant, materi, price, categ, visto, obser):
		self.quant = quant
		self.materi = materi
		self.price = price
		self.categ = categ
		self.visto = visto
		self.obser = obser