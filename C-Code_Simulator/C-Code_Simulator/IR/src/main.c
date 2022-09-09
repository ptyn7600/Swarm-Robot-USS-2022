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
#include "sensor_IR.h"

int main() {
	// File to store the probability arrays
	FILE *fpt;
	fpt = fopen("./probability.csv", "w+");

	// Change this in "sensor_IR.c" if you modify this variable
	const int iteration = 10;
	const int trials = 200;


	for (int trial = 0; trial < trials; trial++) {
		double *prob;
		for (int i = 0; i < iteration; i++) {
			double reading = generate_data(8);
			prob = make_prediction(reading, 0);
			/*printf("=============================\n");
			printf("Sensor Value: %.2f\n", reading);
			print2DArr(prob, state_angle_size, state_dist_size);
			printf("\n");*/
		}
		// Write to file the probability array as 1D array
		for (int i = 0; i < state_size; i++) {
			fprintf(fpt, "%.7f", prob[i]);
			if (i != (state_size - 1)) {
				fprintf(fpt, ",");
			}
		}
		fprintf(fpt, "\n");
	}
	return 0;
}
