#!/usr/bin/env python2
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# main.py
# Copyright (C) 2017 krock <krock@krock-MS-7917>
# 
# hexapode_ihm is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# hexapode_ihm is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys, time, math
from client import Client
from point import Point

import paramiko

#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/hexapode_ihm.ui"
#UI_FILE = "/usr/local/share/hexapode_ihm/ui/hexapode_ihm.ui"


class GUI:
	def __init__(self):

		self.liste_pos = []
		
		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')

		self.b1s0 = self.builder.get_object('b1s0')
		self.b1s1 = self.builder.get_object('b1s1')
		self.b1s2 = self.builder.get_object('b1s2')
		self.b2s3 = self.builder.get_object('b2s3')
		self.b2s4 = self.builder.get_object('b2s4')
		self.b2s5 = self.builder.get_object('b2s5')
		self.b3s6 = self.builder.get_object('b3s6')
		self.b3s7 = self.builder.get_object('b3s7')
		self.b3s8 = self.builder.get_object('b3s8')
		self.b4s0 = self.builder.get_object('b4s0')
		self.b4s1 = self.builder.get_object('b4s1')
		self.b4s2 = self.builder.get_object('b4s2')
		self.b5s3 = self.builder.get_object('b5s3')
		self.b5s4 = self.builder.get_object('b5s4')
		self.b5s5 = self.builder.get_object('b5s5')
		self.b6s6 = self.builder.get_object('b6s6')
		self.b6s7 = self.builder.get_object('b6s7')
		self.b6s8 = self.builder.get_object('b6s8')
		self.slider_ik_vert = self.builder.get_object('slider_ik_verticale')
		self.slider_ik_hori = self.builder.get_object('slider_ik_horizontal')

		self.label_status_conn = self.builder.get_object('label_statut_conn')
		
		window.show_all()

		self.active_slider = True #active l envoi de donnees au serveur lors d'un mouvement des sliders

	def on_window_destroy(self, window):
		Gtk.main_quit()

	def on_b1s0_value_changed(self, window):
		if self.active_slider == True:
			print self.b1s0.get_value()
			self.client.envoir_msg ("code2#b1s0#" + str(self.b1s0.get_value()))

	def on_b1s1_value_changed(self, window):
		if self.active_slider == True:
			print self.b1s1.get_value()
			self.client.envoir_msg ("code2#b1s1#" + str(self.b1s1.get_value()))
				
	def on_b1s2_value_changed(self, window):
		if self.active_slider == True:
			print self.b1s2.get_value()
			self.client.envoir_msg ("code2#b1s2#" + str(self.b1s2.get_value()))
		
	def on_b2s3_value_changed(self, window):
		if self.active_slider == True:
			print self.b2s3.get_value()
			self.client.envoir_msg ("code2#b2s3#" + str(self.b2s3.get_value()))
		
	def on_b2s4_value_changed(self, window):
		if self.active_slider == True:
			print self.b2s4.get_value()
			self.client.envoir_msg ("code2#b2s4#" + str(self.b2s4.get_value()))

	def on_b2s5_value_changed(self, window):
		if self.active_slider == True:
			print self.b2s5.get_value()
			self.client.envoir_msg ("code2#b2s5#" + str(self.b2s5.get_value()))

	def on_b3s6_value_changed(self, window):
		if self.active_slider == True:
			print self.b3s6.get_value()
			self.client.envoir_msg ("code2#b3s6#" + str(self.b3s6.get_value()))

	def on_b3s7_value_changed(self, window):
		if self.active_slider == True:
			print self.b3s7.get_value()	
			self.client.envoir_msg ("code2#b3s7#" + str(self.b3s7.get_value()))

	def on_b3s8_value_changed(self, window):
		if self.active_slider == True:
			print self.b3s8.get_value()
			self.client.envoir_msg ("code2#b3s8#" + str(self.b3s8.get_value()))

	def on_b4s0_value_changed(self, window):
		if self.active_slider == True:
			print self.b4s0.get_value()
			self.client.envoir_msg ("code2#b4s0#" + str(self.b4s0.get_value()))

	def on_b4s1_value_changed(self, window):
		if self.active_slider == True:
			print self.b4s1.get_value()
			self.client.envoir_msg ("code2#b4s1#" + str(self.b4s1.get_value()))

	def on_b4s2_value_changed(self, window):
		if self.active_slider == True:
			print self.b4s2.get_value()
			self.client.envoir_msg ("code2#b4s2#" + str(self.b4s2.get_value()))

	def on_b5s3_value_changed(self, window):
		if self.active_slider == True:
			print self.b5s3.get_value()
			self.client.envoir_msg ("code2#b5s3#" + str(self.b5s3.get_value()))

	def on_b5s4_value_changed(self, window):
		if self.active_slider == True:
			print self.b5s4.get_value()
			self.client.envoir_msg ("code2#b5s4#" + str(self.b5s4.get_value()))

	def on_b5s5_value_changed(self, window):
		if self.active_slider == True:
			print self.b5s5.get_value()
			self.client.envoir_msg ("code2#b5s5#" + str(self.b5s5.get_value()))

	def on_b6s6_value_changed(self, window):
		if self.active_slider == True:
			print self.b6s6.get_value()	
			self.client.envoir_msg ("code2#b6s6#" + str(self.b6s6.get_value()))

	def on_b6s7_value_changed(self, window):
		if self.active_slider == True:
			print self.b6s7.get_value()
			self.client.envoir_msg ("code2#b6s7#" + str(self.b6s7.get_value()))

	def on_b6s8_value_changed(self, window):
		if self.active_slider == True:
			print self.b6s8.get_value()	
			self.client.envoir_msg ("code2#b6s8#" + str(self.b6s8.get_value()))

	def on_button_set_middle_server_clicked(self, window):
		self.client.envoir_msg ("init")
		self.update_pos_servos ();
		
	def on_button_set_middle_clicked(self, window):
		print "TOUT LES SERVOS A 90"

		trame = "code1#90#90#90#90#90#90#90#90#90#90#90#90#90#90#90#90#90#90"
		self.client.envoir_msg (trame)

		self.init_sliders()

	def init_sliders(self):
		
		self.active_slider = False
		self.b1s0.set_value(90)
		self.b1s1.set_value(90)
		self.b1s2.set_value(90)
		self.b2s3.set_value(90)
		self.b2s4.set_value(90)
		self.b2s5.set_value(90)
		self.b3s6.set_value(90)
		self.b3s7.set_value(90)
		self.b3s8.set_value(90)
		self.b4s0.set_value(90)
		self.b4s1.set_value(90)
		self.b4s2.set_value(90)
		self.b5s3.set_value(90)
		self.b5s4.set_value(90)
		self.b5s5.set_value(90)
		self.b6s6.set_value(90)
		self.b6s7.set_value(90)
		self.b6s8.set_value(90)
		self.active_slider = True

	def sshCommand(self, hostname, port, username, password, command):
		sshClient = paramiko.SSHClient()
		sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		sshClient.load_system_host_keys()
		sshClient.connect(hostname, port, username, password)
		stdin, stdout, stderr = sshClient.exec_command(command)
		print(stdout.read())
		
	def on_button_connect_clicked(self, window):
		'''
		print "CREATION CONNECTION SSH"
		self.sshCommand('192.168.1.21', 22, 'pi', 'juju', 'python hexapode_pi/server.py')

		time.sleep (5)
		'''
		print "CONNECT"
		self.client = Client()
		self.label_status_conn.set_text("non connecté")
		
		if self.client.connection() == True :
			self.label_status_conn.set_text("connecté")
			self.update_pos_servos()
		elif self.client.connection() == False :
			self.label_status_conn.set_text("erreur")
		
	def on_button_save_pos_clicked(self, window):
		print "apprentissage"
		self.liste_pos.append(Point(
		self.b1s0.get_value(),
		self.b1s1.get_value(),
		self.b1s2.get_value(),
		self.b2s3.get_value(),
		self.b2s4.get_value(),
		self.b2s5.get_value(),
		self.b3s6.get_value(),
		self.b3s7.get_value(),
		self.b3s8.get_value(),
		self.b4s0.get_value(),
		self.b4s1.get_value(),
		self.b4s2.get_value(),
		self.b5s3.get_value(),
		self.b5s4.get_value(),
		self.b5s5.get_value(),
		self.b6s6.get_value(),
		self.b6s7.get_value(),
		self.b6s8.get_value()))

		

	def on_button_raz_prog_clicked(self, window):
		print "raz prog"
		del(self.liste_pos[:])
		self.client.envoir_msg("code5")
		
	def on_button_upload_clicked(self, window):
		print "upload"
		
		for Pt in self.liste_pos:

			tmp_trame = str(Pt.b1s0) + "@" + str(Pt.b1s1) + "@" + str(Pt.b1s2) + "@" +	str(Pt.b2s3) + "@" +	str(Pt.b2s4) + "@" +	str(Pt.b2s5) + "@" +	str(Pt.b3s6) + "@" +	str(Pt.b3s7) + "@" +	str(Pt.b3s8) + "@" +	str(Pt.b4s0) + "@" +	str(Pt.b4s1) + "@" +	str(Pt.b4s2) + "@" +	str(Pt.b5s3) + "@" +	str(Pt.b5s4) + "@" +	str(Pt.b5s5) + "@" +	str(Pt.b6s6) + "@" +	str(Pt.b6s7) + "@" +	str(Pt.b6s8)

			self.client.envoir_msg("code3" + "#" + tmp_trame)
			time.sleep(0.3)			
			
		print "upload complete"
	
			
	def on_button_execute_clicked(self, window):
		print "execution"
		self.client.envoir_msg ("code4")

	def on_button_debug_serveur_clicked(self, window):
		self.client.envoir_msg ("debug")
		
	def on_button_update_clicked(self, window):
		self.update_pos_servos()

	def on_button_sauver_prog_clicked(self, window):
		print "SAUVEGARDE DU PROGRAMME"

	def on_button_charger_prog_clicked(self, window):
		print "CHARGEMENT PROGRAMME"
		
	def update_pos_servos(self):
		print "UPDATE"
		self.client.envoir_msg ("dmdepose")
		trame = self.client.recevoir()
		print "---------------------------------------"
		print "TRAME RECUE : " + trame
		print "---------------------------------------"

		tmp = trame.split('#')
		self.active_slider = False
		self.b1s0.set_value(float(tmp[1]))
		self.b1s1.set_value(float(tmp[2]))
		self.b1s2.set_value(float(tmp[3]))
		self.b2s3.set_value(float(tmp[4]))
		self.b2s4.set_value(float(tmp[5]))
		self.b2s5.set_value(float(tmp[6]))
		self.b3s6.set_value(float(tmp[7]))
		self.b3s7.set_value(float(tmp[8]))
		self.b3s8.set_value(float(tmp[9]))
		self.b4s0.set_value(float(tmp[10]))
		self.b4s1.set_value(float(tmp[11]))
		self.b4s2.set_value(float(tmp[12]))
		self.b5s3.set_value(float(tmp[13]))
		self.b5s4.set_value(float(tmp[14]))
		self.b5s5.set_value(float(tmp[15]))
		self.b6s6.set_value(float(tmp[16]))
		self.b6s7.set_value(float(tmp[17]))
		self.b6s8.set_value(float(tmp[18]))
		self.active_slider = True
		
	def on_button_disconnect_clicked(self, window):
		print "DECONNECT"
		self.client.deconnect ()

	def on_button_mvt_haut_clicked(self, window):
		print "MOUVEMENT HAUT"

		pt_milieu_A = 111
		pt_milieu_B = 94
		
		A, B = self.calc_ik_2D(0, 0)
		self.client.envoir_msg ("code2#b4s1#" + str(pt_milieu_A - A))
		self.client.envoir_msg ("code2#b4s2#" + str((pt_milieu_B * B) / 90))
		time.sleep(5)

		A, B = self.calc_ik_2D(-2, 0)
		self.client.envoir_msg ("code2#b4s1#" + str(pt_milieu_A - A))
		self.client.envoir_msg ("code2#b4s2#" + str((pt_milieu_B * B) / 90))
		time.sleep(5)

		A, B = self.calc_ik_2D(-4, 0)
		self.client.envoir_msg ("code2#b4s1#" + str(pt_milieu_A - A))
		self.client.envoir_msg ("code2#b4s2#" + str((pt_milieu_B * B) / 90))
		time.sleep(5)

		A, B = self.calc_ik_2D(4, 0)
		self.client.envoir_msg ("code2#b4s1#" + str(pt_milieu_A - A))
		self.client.envoir_msg ("code2#b4s2#" + str((pt_milieu_B * B) / 90))
		time.sleep(5)

		print str(A)
		print str(B)

	def on_slider_ik_verticale_value_changed(self, window):
		self.bouge_IK(self.slider_ik_vert.get_value(), self.slider_ik_hori.get_value())

	def on_slider_ik_horizontal_value_changed(self, window):

		self.bouge_IK(self.slider_ik_vert.get_value(), self.slider_ik_hori.get_value())

	def bouge_IK(self, value_v, value_h):
		pt_milieu_0 = 90
		pt_milieu_1 = 103
		pt_milieu_2 = 91
		pt_milieu_3 = 90
		pt_milieu_4 = 112
		pt_milieu_5 = 101
		pt_milieu_6 = 90
		pt_milieu_7 = 111
		pt_milieu_8 = 109
		pt_milieu_9 = 90
		pt_milieu_10 = 111
		pt_milieu_11 = 94
		pt_milieu_12 = 90
		pt_milieu_13 = 112
		pt_milieu_14 = 119
		pt_milieu_15 = 90
		pt_milieu_16 = 109
		pt_milieu_17 = 120
		
		A, B = self.calc_ik_2D(value_v, value_h)

		trame = "code1"
		
		trame += "#90" + "#" + str(pt_milieu_1 + A) + "#" + str(15 + (2*pt_milieu_2 - ((pt_milieu_2 * B) / 90)))
		trame += "#90" + "#" + str(pt_milieu_4 + A) + "#" + str(15 + (2*pt_milieu_5 - ((pt_milieu_5 * B) / 90)))
		trame += "#90" + "#" + str(pt_milieu_7 + A) + "#" + str(15 + (2*pt_milieu_8 - ((pt_milieu_8 * B) / 90)))
		
		trame += "#90" + "#" + str(pt_milieu_10 - A) + "#" + str(-15 + ((pt_milieu_11 * B) / 90))
		trame += "#90" + "#" + str(pt_milieu_13 - A) + "#" + str(-15 + ((pt_milieu_14 * B) / 90))
		trame += "#90" + "#" + str(pt_milieu_16 - A) + "#" + str(-15 + ((pt_milieu_17 * B) / 90))



		
		self.client.envoir_msg (trame)
		
	def calc_ik_2D(self, cmdeH, cmdeL):
		coxa = 4.2
		femur = 6.1
		tibia = 8.2
		B1 = 180
	
		EmpatementParDefaut = (femur + tibia) / 2
		GardeAuSol = femur + cmdeH
		EmpatementD = EmpatementParDefaut - cmdeL
		VecteurD = math.sqrt(self.carre(GardeAuSol) + self.carre(EmpatementD))
		A2 = math.acos((self.carre(EmpatementD) + self.carre(VecteurD) - self.carre(GardeAuSol)) / (2 * EmpatementD * VecteurD))
		A1 = math.acos((self.carre(VecteurD) + self.carre(femur) - self.carre(tibia)) / (2 * VecteurD * femur))
		A = A1 - A2
		B = (math.acos((self.carre(femur) + self.carre(tibia) - self.carre(VecteurD)) / (2 * femur * tibia)))

		return math.degrees(A), math.degrees(B)

	def carre(self, a):
		return a * a
		
def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
	sys.exit(main())

