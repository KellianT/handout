import sys, os
import datetime
import argparse
import logging


logging.basicConfig(level=logging.DEBUG)


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(dest='path', type=str, help='chemin vers fichier .log')
args = parser.parse_args()

def read_file(path_to_myfile):

    """ This function allows to read the specified file """


    logging.info("entrée dans fonction open_log_file")
    loglist = []
    with open(path_to_myfile, "r") as logfile:
        logging.warning("Ouverture du fichier")
        for line in logfile.readlines():
            logging.info("Lecture du contenu du fichier")
            if line != "\n":
                logging.info("Ajout des lignes recevables")
                loglist += [line.strip()]
    return loglist


def min_delay(line):

    """ This function calculate the delay between two tasks in the scheduler """


    date_time1 = datetime.datetime.strptime(line[0:5], '%H:%M')
    date_time2 = datetime.datetime.strptime(line[6:11], '%H:%M')
    timedelta= date_time2-date_time1
    return int(timedelta.total_seconds()/60)


def create_delay_list(log):

    """ This function create a list from previous min_delay function """
        # Piqué à Emilie, à mieux comprendre

    delai = min_delay(log)
    activity = log.strip().split(" ", 1)[1]
    return [delai, activity]




# print(read_file(planning.log))



# print(main("planning.log"))
# main("planning.log")