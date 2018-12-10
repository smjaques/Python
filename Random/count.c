#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>
#include "count.h"
#include "file.h"

#define IN 1
#define OUT 0

Data Add(char *argv, Data data){
   FILE *fp;
   fp = fileOpen(argv);
   data.bad = 0;
   if (fp == NULL){
      data.bad = 1;
      return data;
   }
   data = getCounts(fp, data);
   close(*argv);
   return data;
}

Data getCounts(FILE *f, Data data){
   unsigned int c;
   int state;
   int lc, wc, cc = 0;
   lc = 0;
   wc = 0;
   while ((c = fgetc(f)) != EOF){
      cc++;
      if (c == '\n'){
         lc++;
      }
      if (isspace(c) != 0){
         state = OUT;
      }
      else if ((isprint(c) != 0) && (state == OUT)){
         wc++;
         state = IN;
      }
   }
   data = fillStruct(wc, lc, cc, data);
   return data;
}

Data fillStruct(int w, int l, int c, Data data){
   data.wCount = w;
   data.cCount = c;
   data.lCount = l;
   data.wTot += w;
   data.cTot += c;
   data.lTot += l;
   return data;
} 

Data forStdin(Data data){
   data = getCounts(stdin, data);
   printInfo(data);
   printf("\n");
   return data;
}

