# -*- encoding: utf-8 -*-
#!/usr/bin/env python
# Copyleft (C) 2015 Diego Accorinti - diegoacco@gmail.com

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301

# Importamos la libreira de PySerial
import serial


# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
sys.path.insert(0, "..")

import pilasengine
pilas = pilasengine.iniciar(ancho=438, alto=360, titulo='Control ROBOT T-2')

# Abrimos el puerto del arduino a 9600
PuertoSerie = serial.Serial('/dev/ttyACM0', 9600)


# Cargo el fondo
fondo = pilas.fondos.Fondo('mifondo.png')

class ecu(pilasengine.actores.Actor):

	def iniciar(self):
		animacion = pilas.imagenes.cargar_animacion('grilla_ecualizador.png', 7)

		animacion.definir_animacion('andando', [1,2,3,4,5,6], 10)
		animacion.definir_animacion('parado', [0], 0)

		self.imagen = animacion #vinculo la animación
		self.imagen.cargar_animacion('parado')
		self.y=-123

	def actualizar(self):
		self.imagen.avanzar()

pilas.actores.vincular(ecu)
ecualizador = pilas.actores.ecu()


def cuando_pulsa_tecla(evento):
    print ("texto", evento.texto, "codigo", evento.codigo)

    if evento.codigo == 2:
        print "Pulso la tecla derecha"
        PuertoSerie.write("4")

    if evento.codigo == 1:
        print "Pulso la tecla izquierda"
        PuertoSerie.write("5")

    if evento.codigo == 3:
        print "Pulso la tecla arriba"
        PuertoSerie.write("2")

    if evento.codigo == 4:
        print "Pulso la tecla abajo"
        PuertoSerie.write("3")

#SAMPLER
    if evento.codigo == 49:
        print "Reproduzco sample 1"
        sample1 = pilas.sonidos.cargar('sonidos/hasta-la-vista-baby.ogg')
        sample1.reproducir();
        ecualizador.imagen.cargar_animacion('andando')

    if evento.codigo == 50:
        print "Reproduzco sample 2"
        sample1 = pilas.sonidos.cargar('sonidos/metalicotrasero.ogg')
        sample1.reproducir();
        ecualizador.imagen.cargar_animacion('andando')

    if evento.codigo == 51:
        print "Reproduzco sample 3"
        sample1 = pilas.sonidos.cargar('sonidos/r2d2_01.ogg')
        sample1.reproducir();
        ecualizador.imagen.cargar_animacion('andando')

    if evento.codigo == 52:
        print "Reproduzco sample 4"
        sample1 = pilas.sonidos.cargar('sonidos/r2d2_02.ogg')
        sample1.reproducir();
        ecualizador.imagen.cargar_animacion('andando')

def cuando_suelta_tecla(evento):
        PuertoSerie.write("0")
        ecualizador.imagen.cargar_animacion('parado')

pilas.eventos.pulsa_tecla.conectar(cuando_pulsa_tecla)
pilas.eventos.suelta_tecla.conectar(cuando_suelta_tecla)

pilas.ejecutar()
