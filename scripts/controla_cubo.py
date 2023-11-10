#!/usr/bin python3

import rospy
from std_msgs.msg import String, Bool
import random

# Lista de mensagens possíveis
mensagens = ['U', 'D', 'L', 'R', 'F', 'B']

# Função para verificar se o tópico /cubo/trabalhando está enviando False
def callback(data):
    global trabalhando
    trabalhando = data.data

# Inicializa o nó
rospy.init_node('enviar_comandos')

# Cria os publicadores e o subscritor
pub = rospy.Publisher('/cubo/comando', String, queue_size=10)
sub = rospy.Subscriber('/cubo/trabalhando', Bool, callback)

# Inicializa a variável de trabalho
trabalhando = False

# Taxa de loop
rate = rospy.Rate(100) # 1hz

while not rospy.is_shutdown():
    # Se o tópico /cubo/trabalhando está enviando False
    if not trabalhando:
        # Sorteia 20 sequências aleatórias das 9 possíveis mensagens
        seq = random.choices(mensagens, k=20)
        for msg in seq:
            # Publica a mensagem
            pub.publish(msg)
            # Espera até que o tópico /cubo/trabalhando volte a enviar False
            while trabalhando:
                pass
    rate.sleep()
