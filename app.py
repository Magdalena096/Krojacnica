from flask import Flask, Response, jsonify, request, flash, render_template, current_app, redirect
from baza import Krojaci , Posalji
import sqlite3
import secrets
import os

db = sqlite3.connect("baza.sqlite", check_same_thread=False)

app = Flask(__name__)

cur = db.cursor()

@app.route('/')
def pocetna():
	return render_template('pocetna.html')

@app.route('/krojacnica', methods=['GET', 'POST'])
def krojacnica():
	if request.method == 'POST':
		vlasnik = request.form.get('vlasnik')
		materijal = request.form.get('materijal')
		kroj = request.form.get('kroj')
		ime = request.form.get('ime')
		datum1 = request.form.get('datum1')
		datum2 = request.form.get('datum2')
		db.execute("INSERT INTO Krojaci(vlasnik,materijal,kroj,ime, datum1, datum2) VALUES (:vlasnik,:materijal,:kroj,:ime, :datum1, :datum2)", {"vlasnik":vlasnik, "materijal":materijal,"kroj":kroj,"ime":ime, "datum1":datum1, "datum2":datum2})
		db.commit()
		return render_template('krojacnica.html')
	return render_template('krojacnica.html')

@app.route('/prikaz', methods=['GET', 'POST'])
def prikaz():
	if request.method == 'POST':
		print("radi")
		oznaka = request.form.get('oznaka')
		
		print(oznaka)
		if oznaka != None:
			db.execute("DELETE FROM Krojaci WHERE id="+oznaka+"")
			db.commit()
		
	cur.execute("select * from Krojaci")
	data = cur.fetchall()
	return render_template('prikaz.html', value=data)

@app.route('/posalji', methods=['GET', 'POST'])
def posalji():
	if request.method == 'POST':
		
		print("radi")
		oznaka1 = request.form.get('oznaka1')
		
		print(oznaka1)
		if oznaka1 != None:
			db.execute("DELETE FROM Krojaci WHERE id="+oznaka1+"")
			db.commit()
		
	cur.execute("select * from Posalji")
	data1 = cur.fetchall()
	return render_template('posalji.html', value=data1)

@app.route('/unosD', methods=['GET', 'POST'])
def unosD():
	if request.method == 'POST':
		adresa = request.form.get('adresa')
		broj = request.form.get('broj')
		cijena = request.form.get('cijena')
		dostava = request.form.get('dostava')
		db.execute("INSERT INTO Posalji(adresa,broj,cijena,dostava) VALUES (:adresa,:broj,:cijena,:dostava)", {"adresa":adresa, "broj":broj,"cijena":cijena,"dostava":dostava})
		db.commit()
		return render_template('unosD.html')
	return render_template('unosD.html')
if __name__ == "__main__":
	app.run(debug=True)