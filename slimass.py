# -*- coding: utf-8 -*-

from src.SlimService import slims
import sys
import os
import time
from termcolor import colored
import colorama 
from colorama import init, Fore
def param_check():
    try:
        a = sys.argv[1]
    except IndexError:
        return False
    return True

def file_check(file_path):
    try:
        open(file_path)
    except IOError:
        return False
    return True

from termcolor import colored

def print_rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for char, color in zip(text, colors * (len(text) // len(colors) + 1)):
        print(colored(char, color)),
        sys.stdout.flush()
        time.sleep(0.1)  # Adjust the delay for animation speed
    print('')

def colored_spider():
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    spider_parts = [
        '    / _ \\ ',
        '  \\_\\(_)/_/',
        '   _//"\\\\_',
        '    /   \\  '
    ]

    for part in spider_parts:
        colored_part = [colored(char, random.choice(colors)) for char in part]
        print(''.join(colored_part))

def about():
    os.system("clear")
    colored_spider()
    print_rainbow_text("TrknMass by TRHACKNON\n")

import time
import sys

import random

def twinkling_text(text, twinkling_duration=2):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    start_time = time.time()

    while time.time() - start_time < twinkling_duration:
        colored_text = [colored(char, random.choice(colors)) for char in text]
        sys.stdout.write(''.join(colored_text) + "\r")
        sys.stdout.flush()
        time.sleep(0.1)

    print('')

def fun_prompt():
    print(colored("Bienvenue dans l'outil interactif de ", 'blue'))
    twinkling_text("TrknMass par TRHACKNON", twinkling_duration=4)
    print(colored("Veuillez entrer le chemin du ", 'yellow') + colored("fichier .txt", 'blue') +
          colored(" que vous souhaitez utiliser.", 'yellow'))
    print(colored("Si vous ne l'avez pas, vous pouvez créer un nouveau fichier.", 'cyan'))

fun_prompt()



if __name__ == "__main__":
    try:
        about()

        if not param_check():
            fun_prompt()
            file_path = raw_input("Entrez le chemin du fichier .txt : ")
            while not file_check(file_path):
                print(colored("Le fichier spécifié n'existe pas. Veuillez réessayer.", 'red'))
                file_path = raw_input("Entrez le chemin du fichier .txt : ")
        else:
            file_path = sys.argv[1]
            if not file_check(file_path):
                print(colored("Le fichier spécifié n'existe pas. Veuillez réessayer.", 'red'))
                sys.exit()

        while True:
            target = raw_input("[ GRT ]> ")
            if not target:
                break
            a = slims(target, file_path)
    except Exception as e:
        print(colored("Une erreur s'est produite: {}".format(e), 'red'))