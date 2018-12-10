#include <stdio.h>
#include "file.h"
#ifndef COUNT_H
#define COUNT_H

Data Add(char *argv, Data data);
Data getCounts(FILE *f, Data data);
Data fillStruct(int w, int l, int c, Data data);
void doStdin(int argc, Data data);


int wordCount(char *argv, FILE *f);
int lineCount(FILE *f);
int charCount(FILE *f);
int wAdditions(char *argv);
int lAdditions(char *argv);
int cAdditions(char *argv);
void additions(int argc, char *argv[], FILE *f);

#endif
