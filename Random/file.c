#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include "file.h"
#include "count.h"

Data flagCheck(int argc, char *argv[], Data data){
   data = flagHelper(argc, argv, data);
   if (data.numFlags == 0){
      data.lFlag = 1;
      data.wFlag = 1;
      data.cFlag = 1;
   }
   return data;
}

Data flagHelper(int argc, char *argv[], Data data){
   int i, flags = 0;
   for (i = 1; i < argc; i++){
      if ((strcmp(argv[i], "-l")) == 0){
         flags ++;
         data.lFlag = 1;
      }
      if ((strcmp(argv[i], "-w")) == 0){
         flags ++;
         data.wFlag = 1;
      }
      if ((strcmp(argv[i], "-c")) ==0){
         flags ++;
         data.cFlag = 1;
      }
   }
   data.numFlags = flags;
   return data;
}

FILE* fileOpen(const char *fname){
   FILE *fp;
   fp = fopen(fname, "r");
   if (fp == NULL){
      fprintf(stderr, "swc: ");
      perror(fname);
   }
   return fp;
}

int notFlag(char *c){
   if ((strcmp(c,"-c") !=0) && (strcmp(c,"-l") !=0) && (strcmp(c,"-w") !=0)){
      return 1;
   }
   return 0;
}

void printInfo(Data data){
   int l, w = 0;
   if (data.lFlag == 1){
      l = 1;
      printCount(data.lCount);
   }
   if (data.wFlag == 1){
      if (l == 1){
         printf(" ");
      }
      w = 1;
      printCount(data.wCount);
   }
   if (data.cFlag == 1){
      if (w == 1){
         printf(" ");
      }
      printCount(data.cCount);
   }
}

void printTotal(Data data){
   if (data.lFlag == 1){
      printf("%10u", data.lTot);
   }
   if (data.wFlag == 1){
      printf(" %10u", data.wTot);
   }
   if (data.cFlag == 1){
      printf(" %10u", data.cTot);
   }
   printf(" total\n");
}

void printFileInfo(Data data, char *arg){
   printInfo(data);
   printfname(arg);
}
   
void printfname(char *fname){
   printf(" %s\n", fname);
}

void printCount(int wCount){
   printf("%10u", wCount);
}

