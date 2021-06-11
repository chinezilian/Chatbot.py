# ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import PySimpleGUI as sg

class DecidaPorMim:

    def __init__(self):
        self.conversa = ['Oi',
                    'Olá',
                    'Tudo bem?',
                    'Tudo ótimo',
                    'Que bom',
                    'Você gosta de programar?',
                    'Sim, eu programo em Python']

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input(size=(50,10),key='Pergunta')],
            [sg.Output(size=(50,10))],
            [sg.Button('Enviar')]
        ]
        # criar a janela
        self.janela = sg.Window('Decida por Mim!',layout=layout)
        bot = ChatBot('Chat Bot')
        bot = ChatBot(
            'Chat Bot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3'

        )
        bot = ChatBot(
            'Chat Bot',
            logic_adapters=[
                'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'],
        )
        conversa = ChatterBotCorpusTrainer(bot)
        conversa.train('chatterbot.corpus.portuguese')
        conversa.train('chatterbot.corpus.english')
        conversa.train('chatterbot.corpus.spanish')
        conversa.train('chatterbot.corpus.german')
        conversa = ListTrainer(bot)
        conversa.train(self.conversa)

        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            self.pergunta = self.valores['Pergunta']
            # Fazer algo com os valores
            if self.eventos == 'Decida por mim':
                pergunta = self.pergunta
                resposta = bot.get_response(pergunta)
                if float(resposta.confidence) > 0.2:
                    print('Bot: ', resposta)
                else:
                    print('Bot: Ainda não sei responder esta pergunta')


decida = DecidaPorMim()
decida.Iniciar()
