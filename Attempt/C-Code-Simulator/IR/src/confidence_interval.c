/*
Copyright (c) 2022 Peter Jamieson (jamieson.peter@gmail.com)
and Bryan Van Scoy

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
*/
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string.h>
#include "confidence_interval.h"

/* globals */
// Number of sample
const int iteration = 10;


/*-------------------------------------------------------------------------
* (function: )
*-----------------------------------------------------------------------*/


double sum_2Darray(double arr[][state_dist_size], int row, int column)
{
	double sum = 0;
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < column; j++) {
			sum += arr[i][j];
		}
	}
	return(sum);
}

void normalize_2Darray(double arr[][state_dist_size], int row, int column) {
	double sum = sum_2Darray(arr, row, column);
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < column; j++) {
			arr[i][j] = arr[i][j] / sum;
		}
	}
}

double (*make_prediction(double reading, int restart ))[state_dist_size] {
	// Variable to notify reading and 
	static int sampleCount = 0;
	static int init = 1;
	/* Storing finite number of state */
	int state_dist[] = { 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21 };
	int state_angle[] = { 0, 10, 20, 30, 40, 50, 60, 70, 80, 90 };
	/* ===== Start Predicting ======== */
	double mean_k1 = 14001.60930435;
	double mean_a = -1.05352284;
	double mean_b = 0.00120735;

	double std_k1 = 3.78093567;
	double std_k2 = 0.15687919;

	/* Array to store prediction probability */
	double en = 1.0 / (double)(state_dist_size*state_angle_size);
	static double prob_arr[state_angle_size][state_dist_size];

	if ((init == 1) || (sampleCount >= iteration) || (restart == 1)) {
		sampleCount = 0;
		init = 0;
		for (int i = 0; i < state_angle_size; i++) {
			for (int j = 0; j < state_dist_size; j++) {
				prob_arr[i][j] = en;
			}
		}
	}

	for (int i = 0; i < state_angle_size; i++) {
		for (int j = 0; j < state_dist_size; j++) {
			int eachDist = state_dist[j];
			int eachAngle = state_angle[i];
			double mean = mean_k1 * (pow(eachDist, (mean_a + mean_b * eachAngle)));
			double std = std_k1 * pow(M_E, (std_k2*eachDist));
			double variance = pow((std), 2.0);
			double prob = ((1.0 / (std * sqrt(2.0 * M_PI))) * (pow(M_E, -1.0 * ((pow((reading - mean), 2.0)) / (variance * 2.0)))));
			prob_arr[i][j] = prob * prob_arr[i][j];
		}
	}
	normalize_2Darray(prob_arr, state_angle_size, state_dist_size);
	sampleCount++;

	return prob_arr;
}

double randnorm(double mu, double sigma)
{
	double U1, U2, W, mult;
	static double X1, X2;
	static int call = 0;

	if (call == 1)
	{
		call = !call;
		return (mu + sigma * (double)X2);
	}

	do
	{
		U1 = -1 + ((double)rand() / RAND_MAX) * 2;
		U2 = -1 + ((double)rand() / RAND_MAX) * 2;
		W = pow(U1, 2) + pow(U2, 2);
	} while (W >= 1 || W == 0);

	mult = sqrt((-2 * log(W)) / W);
	X1 = U1 * mult;
	X2 = U2 * mult;

	call = !call;

	return (mu + sigma * (double)X1);
}

double generate_data(double distance, double angle) {
	// Constant to calculate to mean and standard deviation from the given distance
	double mean_k1 = 14001.60930435;
	double mean_a = -1.05352284;
	double mean_b = 0.00120735;

	double std_k1 = 3.78093567;
	double std_k2 = 0.15687919;

	// Calculate the mean and std for the Gausian Distribution
	double mean = mean_k1 * (pow(distance, (mean_a + mean_b * angle)));
	double std = std_k1 * pow(M_E, (std_k2*distance));

	// Generate a random number that follows the Gausian Distribution
	return randnorm(mean, std);
}

/*Geneate a set of data that follows a distribution with mean and standard deviation calculated from the distance*/
double* generate_data_set(double distance, double angle, int numberSample) {
	// Constant to calculate to mean and standard deviation from the given distance
	double mean_k1 = 14001.60930435;
	double mean_a = -1.05352284;
	double mean_b = 0.00120735;

	double std_k1 = 3.78093567;
	double std_k2 = 0.15687919;

	// Calculate the mean and std for the Gausian Distribution
	double mean = mean_k1 * (pow(distance, (mean_a + mean_b * angle)));
	double std = std_k1 * pow(M_E, (std_k2*distance));

	// Generate the random numbers that follows the Gausian Distribution
	double *returnArr = malloc(sizeof(double) * numberSample);
	for (int i = 0; i < numberSample; i++) {
		returnArr[i] = randnorm(mean, std);
	}

	return returnArr;
}

void print2DArr(double arr[][state_dist_size], int row, int column) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < column; j++) {
			printf("%.7f ", arr[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

//int main() {
//	double(*prob)[state_dist_size];
//	for (int i = 0; i < iteration; i++) {
//		double reading = generate_data(6, 0);
//		prob = make_prediction(reading, 0);
//		printf("=============================\n");
//		printf("Sensor Value: %.2f\n", reading);
//		print2DArr(prob, state_angle_size, state_dist_size);
//		printf("\n");
//	}
//	return 0;
//}
