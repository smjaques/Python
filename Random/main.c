#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "file.h"
#include "count.h"
#include "stdin.h"

int main(int argc, char *argv[]){
   int i, files = 0;
   Data data;

   data = flagCheck(argc, argv, data);
   for (i = 1; i < argc; i++){
      if (notFlag(argv[i]) == 1) {  /*is 0 if it is a flag */
         files ++;
         data = Add(argv[i], data);
         if (data.bad == 1){
            continue;
         }
         printFileInfo(data, argv[i]);
      }
   }
   if (files > 1){
      printTotal(data);
   }
   
   if ((argc == 1) | (data.numFlags == argc-1)){
      forStdin(data);
   }
   
   return 0;
}
