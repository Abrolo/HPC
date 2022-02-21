// Write file and readinput have been added to the blas_example.c code provided in DD2358 course
#include <stdio.h>
#include <stdlib.h>
#include <cblas.h>

int main() {

	int i, j;
	int m; // square matrix, number of rows and columns int i,j;
	printf("Enter the size of the matrix: ");
        scanf("%d", &m);
	double *A, *B, *C;

	FILE *ofile;  
	char filename[] = "reference.txt";
	int num;
	
	double alpha = 1.0; 	
	double beta = 0.0;
	
	
	
	A = (double *) malloc(m*m*sizeof(double)); 
	B = (double *) malloc(m*m*sizeof(double)); 
	C = (double *) malloc(m*m*sizeof(double));
	// initialize the matrices
	for (i=0;i<m;i++) { 
		for (j=0;j<m;j++) {
			A[j + m*i] = j + m*i; // arbitrarily initialized B[j + m*i] = 3.14*(j + m*i);
			B[j + m*i] = 3.14*(j + m*i);
			C[j + m*i] = 0.0;
		} 
	}
	cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, m, m, m, alpha, A, m, B, m, beta, C, m);
	
	// Print the results
	//for (i=0;i<m;i++) { 
	//	for (j=0;j<m;j++) {
	//		printf(" C[%d][%d]=%g ",i,j,C[j+m*i]);
	//	}
	//	printf("\n");
	//}
	// Write the results
	ofile = fopen(filename, "w"); 

	for (i=0;i<m;i++) {
	  for (j=0;j<m;j++) {
	    fprintf(ofile, "%lf ", C[j+m*i]); 
	  }
	  fprintf(ofile, "\n");
        }
	fclose(ofile);
	// free the arrays
 	free(A); free(B); free(C); 

 	return 0;
} 
