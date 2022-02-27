#include <stdio.h>

void gauss_seidel(double *x, int n){
  int i,j;
  for (i=1; i<n-1; i++){
    for(j=1; j<n-1; j++){
      x[i*n+j] = 0.25*(x[i*n+(j+1)]+x[i*n+(j-1)]+x[(i+1)*n+j]+x[(i-1)*n+j]);
    }
  }
}
