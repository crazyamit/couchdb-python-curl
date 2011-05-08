#!/usr/bin/env python

import sys
import os
import logging
import multiprocessing

class Pinger(multiprocessing.Process):
    def __init__(self, verbosity, db_key, view_name, func_name):
        multiprocessing.Process.__init__(self)

        self.verbosity = verbosity
        self.db_key = db_key
        self.view_name = view_name
        self.func_name = func_name
        
    def run(self):
        db = django_couch.db(self.db_key)
        if self.verbosity >= 2:
            print 'quering view %s/%s' % (self.view_name, self.func_name)
        db.view('%s/%s' % (self.view_name, self.func_name), limit = 0).rows
                

def main():
    pass


if __name__ == '__main__':
    main()


