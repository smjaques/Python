#include <stdio.h>
#ifndef FILE_H
#define FILE_H

typedef struct{
   char *fname;
   int cCount;
   int lCount;
   int wCount;
   int cTot;
   int lTot;
   int wTot;
   int lFlag;
   int wFlag;
   int cFlag;
   int numFlags;
   int bad;
}Data;

Data flagCheck(int arg, char *argv[], Data data);
Data flagHelper(int c, char *argv[], Data data);
int notFlag(char *c);
void printInfo(Data data);
void printTotal(Data data);
Data clearData(Data data);
void printFileInfo(Data data, char *arg);


FILE *fileOpen(const char *fname);
int hasFile(int argc);
int isFile(const char *fname);
int numFlags(int argc, char *argv[]);
int hasCFlag(int argc, char *argv[]);
int hasWFlag(int argc, char *argv[]);
int hasLFlag(int argc, char *argv[]);
void filesTotal(int files, int w, int l, int c);
int forEachFile(int argc, char *argv[]);
void printwCount(int w);
void printCount(int l);
void printcCount(int c);
void printTotals(int wTot, int lTot, int cTot);
void printWhat(int argc, char *argv[], int w, int l, int c);
void printfname(char *fname);
void fileTotal(int files, int w, int l, int c);
int checkArg(char *v);
int isFlag(char *v);

#endif
